# -*- coding: utf-8 -*-
import argparse
import pandas as pd
import print_result

def count_unk(path, UNK_TAG = '<unk>'):
    """
    path: Path to a space-separated file
    for [NT-OTH-1] in tech report
    """
    unk, total = 0, 0
    with open(path,'r',encoding='utf8') as f:
        tokens = [token for line in f.readlines() for token in line.split()]
        total = len(tokens)
        unk = sum([1 for token in tokens if UNK_TAG in token])
    return unk,total

def print_title(name, **kwargs):
    print(f"# Analysis of {name}")
    for kw,arg in kwargs.items():
        print(f"{kw}={arg}")

def parse_seg_file(seg_path):
    """
    Returns:
    -----------
        linenos: list of int. ordered by seg; corresponding to metadata
        temps2sents: dict. (states) -> [([phrases], lineno_in_seg_txt)]
            Example:
            key: (114, 201, 207, 184, 149, 252, 122, 75)
            value: [(['Each', 'banana', 'costs $ <num>', 
                '. How much', 'do <num>', 'bananas', 'cost', '? <eos>'], 0)]
        top_temps: list of temps2sents keys, sorted by frequency of samples
    """
    from template_extraction import group_by_template
    linenos = []
    with open(seg_path,'r',encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('D label_train(): corpus.train_mb2linenos='): # HACK Don't contain '|'
                linenos = [ int(strno) for strno in line.strip().split('=')[1].split()]
                break
    temps2sents = group_by_template(seg_path,0) # startlineno=0; returns a label-tup -> [(phrase-list, lineno), ...] map
    top_temps = sorted(list(temps2sents.keys()), key=lambda x: -len(temps2sents[x]))
    return linenos, temps2sents, top_temps

def re_sort_metadata(metadata_path, linenos, new_idxname):
    try:
        metadata = pd.read_csv(metadata_path, sep='\t', header=0)
    except FileNotFoundError:
        return None

    # Sort metadata by linenos s.t. the idx match: metadata and temps2sents and seg file
    # 1. Sort linenos
    #   FROM  linenos[seg_index] = corresponding index in metadata
    #   TO    linenos[metadata] = corresponding index in seg_index
    linenos = [b for a,b in sorted(zip(linenos, range(len(linenos))), key=lambda x: x[0])]
    # 2. Add metadata col
    metadata[new_idxname] = linenos
    metadata = metadata.sort_values(by=new_idxname)
    metadata = metadata.set_index(new_idxname)
    return metadata

def analyze_seg(data,metadata_path,seg_path, k, n, pure_path=''):
    """
    Give statistics according to given metadata and segmentation
    """
    print_title("segmentation", metadata_path=metadata_path,seg_path=seg_path,k=k,n=n)

    def specific_top_templates(temps2sents,metadata, attribute, metadata_colnames, 
            pure = False):
        """
        Parameters:
        -----------
            attribute:  str
                e.g. 'solution type'
            pure:  bool
                Whether print templates that is 'Addition' only (or so). Must match attribute
        """
        if metadata is None:
            return None

        # sort solution types (stype, e.g. 'Addition') by their frequencies (counts)
        from collections import Counter
        stype_counts = Counter(metadata[attribute])
        stypes = [stype for stype, count in sorted(list(stype_counts.items()), key=lambda x: -x[1])]

        # empty dictionary: stype -> { (temps) -> [sample sents] }
        stype2templates = dict(zip(stypes, [dict() for i in range(len(stypes))]))
        
        # stype -> [pure top_temps]
        pure_templates = dict()

        for temp, sents in temps2sents.items():
            for (phrases,lineno_in_seg_txt) in sents:
                stype = metadata[attribute][lineno_in_seg_txt]
                if temp not in stype2templates[stype]:
                    stype2templates[stype][temp] = []
                stype2templates[stype][temp].append((phrases,lineno_in_seg_txt))
        for stype in stypes:
            if stype_counts[stype] < 5:     # HACK to avoiding printing stypes of little samples
                continue
            print(f"## {stype} ({stype_counts[stype]} samples)")
            stype_temps2sents = stype2templates[stype]
            top_temps = sorted(list(stype_temps2sents.keys()), key=lambda x: -len(stype_temps2sents[x]))
            
            # For correct statistics, use temps2sents instead of stype_temps2sents below
            filters = {attribute:[stype]} if pure else None
            printed = print_result.top_templates_from_train(top_temps,temps2sents,metadata,
                metadata_colnames=metadata_colnames, n_toptemps=k, n_samples=n, filters=filters)
            if pure:
                pure_templates[stype] = [top_temps[p] for p in printed]
        
        if pure:
            with open(pure_path,'w') as f:
                f.writelines([f"{attribute}|{s}|||{' '.join([ ','.join([str(tt) for tt in t]) for t in pure_templates[s]])}\n" for s in stypes if s in pure_templates.keys()])

    linenos, temps2sents, top_temps = parse_seg_file(seg_path)
    metadata = re_sort_metadata(metadata_path, linenos, new_idxname='seg_linenos')
    
    # Evaluate the quality of segmentation
    print("# Overall - top templates")
    print_result.top_templates_from_train(top_temps, temps2sents, metadata, metadata_colnames=[],n_toptemps=k, n_samples=n) #'solution type','source','question'
    
    #print("# Solution type - top templates")
    #specific_top_templates(temps2sents,metadata, 'solution type', metadata_colnames=['solution type','source'], pure=False)

    #print('# Dataset - top templates')
    #specific_top_templates(temps2sents,metadata, 'source', metadata_colnames=['solution type','source'], pure=False)

    if pure_path is not '':
        print('# Pure templates: specific solution type')
        specific_top_templates(temps2sents,metadata, 'solution type', metadata_colnames=['solution type','source'], pure=True)


def analyze_gen(data, metadata_path, gen_path, startlineno=0, seg_path=''):
    """
    Give statistics according to metadata & generation file
    Adapted from group_by_template(fi, startlineno) in template_extraction.py
    1. Statistics: How many samples use which template? Compare to training data distribution?
    """

    print_title("generation", data=data, metadata_path=metadata_path, gen_path=gen_path)

    _,seg_temps2sents,_ = parse_seg_file(seg_path) if seg_path!='' else None,{},None

    import re
    from collections import defaultdict
    seg_patt = re.compile('([^\|]+)\|(\d+)') # detects segments
    temps2sents = defaultdict(list)
    lineno = startlineno

    try:
        metadata = pd.read_csv(metadata_path, sep='\t', header=0)
        conditions = ['' for i in range(metadata.shape[0])] # metadata.shape == (#rows, #cols)
    except FileNotFoundError: 
        metadata = None
    
    #metadata = None #HACK  # cuz the linenos aren't for #alltmplt gen
    
    with open(gen_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('__start'):
                state = None
                condition = []
                for token in line.split():
                    if token.startswith('__start'):
                        assert state == None
                        state = token[8:-2]
                    elif token.startswith('__end'):
                        assert state == token[6:-2]
                        if metadata is not None:
                            conditions[lineno] += f'{state}:{" ".join(condition)}  '
                        state = None
                        condition = []
                    else:
                        condition.append(token)
            elif '|||' in line:
                mwp, seqs = line.split('|||')
                seq = seg_patt.findall(seqs.strip())
                wordseq, labeseq = zip(*seq) # 2 tuples
                wordseq = [phrs.strip() for phrs in wordseq]
                labeseq = tuple(int(labe) for labe in labeseq)
                temps2sents[labeseq].append((wordseq, lineno))  #mwp, 
                lineno += 1
    
    top_temps = sorted(list(temps2sents.keys()), key=lambda x: -len(temps2sents[x]))
    if metadata is not None:
        metadata['conditions'] = conditions
        print_result.top_templates_from_train(top_temps, temps2sents, metadata, 
            metadata_colnames=['conditions'], n_toptemps=999, n_samples=99999, seg_temps2sents=seg_temps2sents, n_examples=2)
    else:
        print_result.top_templates_from_train(top_temps, temps2sents, None, 
            metadata_colnames=[], n_toptemps=999, n_samples=99999, seg_temps2sents=seg_temps2sents, n_examples=2)

#: err print
def eprint(*args, **kwargs):
    #print(*args, file=sys.stderr, **kwargs)
    pass

def get_pure_toptemps(pure_path, some_types):
    pure_temps = [] # [(attr,stype,[temps])]    e.g. ('solution type','Addition',[(0,1,2),(3,4,5)] )
    with open(pure_path) as f:
        for line in f:
            info , temps = line.split('|||')
            attr, stype = info.split('|')   # 'solution type', 'Addition'
            temps = [tuple(int(i) for i in t.split(',')) for t in temps.split(' ')]
            if stype in some_types:
                pure_temps.extend(temps)
    return pure_temps

    
parser = argparse.ArgumentParser(description='')
parser.add_argument('-data', type=str, default='', help='path to data dir')
parser.add_argument('-tagged_fi', type=str, default='', help='path to tagged file i.e. segmentation')
parser.add_argument('-gen_fi', type=str, default='', help='path to generation file')
parser.add_argument('-pure', type=str, default='', help='path to pure_temps')

parser.add_argument('-a_seg', action='store_true', help='Analysis segmentation file')
parser.add_argument('-a_gen', action='store_true', help='Analyze generation file')

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)

    #org_unk, org_ttl = count_unk('segs/seg-otherTrain-100-55-5-far-NER-no_test.txt')
    #new_unk, new_ttl = count_unk('segs/seg-otherTrain-100-55-5-far-NER-no_test-unk.txt')
    #print(org_unk,org_ttl,org_unk/org_ttl)
    #print(new_unk,new_ttl,new_unk/new_ttl)
    DATA = args.data
    SEG = args.tagged_fi
    GEN = args.gen_fi
    PURE = args.pure
    #DATA='/Users/shanglinghsu/mwp/Datasets/ai2-ilds-train-valid/ai2-ilds-train-valid-concated'
    #SEG = '/Users/shanglinghsu/mwp/ntg2/segs/seg-ai2-cmds-100-55-5-far-NER.txt'
    #GEN = '/Users/shanglinghsu/mwp/ntg2/gens/gen-ai2-ilds-100-55-5-far-NER-pure_add-sub.md'
    if args.a_seg:
        analyze_seg(data=DATA, metadata_path=DATA+'/metadata_train.tsv', seg_path=SEG, 
            k=100, n=10, pure_path=PURE)
    if args.a_gen:
        analyze_gen(data=DATA, metadata_path=DATA+'/metadata_valid.tsv', gen_path=GEN, seg_path=SEG)
    
    #PURE = 'pure_temps.txt'
    #get_pure_toptemps(PURE,'Addition')
    