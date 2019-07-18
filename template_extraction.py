import re
from collections import defaultdict

import torch

import labeled_data

seg_patt = re.compile('([^\|]+)\|(\d+)') # detects segments

####
# for other_mwp statistics only
total_data_len = 1556
####

def group_by_template(fi, startlineno):
    """
    returns a label-tup -> [(phrase-list, lineno), ...] map
    """
    labes2sents = defaultdict(list)
    lineno = startlineno
    with open(fi) as f:
        for line in f:
            if '|' not in line:
                continue
            seq = seg_patt.findall(line.strip()) # list of 2-tuples
            #print(seq)
            wordseq, labeseq = zip(*seq) # 2 tuples
            wordseq = [phrs.strip() for phrs in wordseq]
            labeseq = tuple(int(labe) for labe in labeseq)
            labes2sents[labeseq].append((wordseq, lineno))
            #print(f"D group_by_template labeseq={labeseq}\t wordseq={wordseq}\t lineno={lineno}")
            lineno += 1
    return labes2sents

def remap_eos_states(top_temps, temps2sents):
    """
    allocates a new state for any state that is also used for an <eos>
    """
    used_states = set()
    [used_states.update(temp) for temp in top_temps]    #: to avoid set("abc") = {'a','b','c'} rather than {"abc"}
    final_states = set()
    for temp in top_temps:
        final_state = temp[-1]
        assert any(sent[-1] == "<eos>" for sent, lineno in temps2sents[temp])
        final_states.add(final_state)

    # make new states
    remap = {}
    for i, temp in enumerate(top_temps):
        nutemp = []
        changed = False
        for j, t in enumerate(temp):
            if j < len(temp)-1 and t in final_states:
                changed = True
                if t not in remap:
                    remap[t] = max(used_states) + len(remap) + 1
            nutemp.append(remap[t] if t in remap else t)
        if changed:
            nutuple = tuple(nutemp)
            top_temps[i] = nutuple
            temps2sents[nutuple] = temps2sents[temp]
            del temps2sents[temp]

def just_state2phrases(temps, temps2sents):
    state2phrases = defaultdict(lambda: defaultdict(int)) # defaultdict of defaultdict
    for temp in temps:
        for sent, lineno in temps2sents[temp]:
            for i, state in enumerate(temp):
                #state2phrases[state].add(sent[i])
                state2phrases[state][sent[i]] += 1

    nustate2phrases = {}
    for k, v in state2phrases.items():
        phrases = list(v)
        counts = torch.Tensor([state2phrases[k][phrs] for phrs in phrases])
        counts.div_(counts.sum())
        nustate2phrases[k] = (phrases, counts)
    state2phrases = nustate2phrases
    return state2phrases


def extract_from_tagged_data(datadir, bsz, thresh, tagged_fi, ntemplates):
    corpus = labeled_data.SentenceCorpus(datadir, bsz, thresh=thresh, add_bos=False,
                                         add_eos=False, test=False)
    """
    returns the most common templates, and mappings from these 
    templates to sentences, and from states to phrases.
    """    
    nskips = 0
    for i in range(len(corpus.train)):
        if corpus.train[i][0].size(0) <= 4:
            nskips += corpus.train[i][0].size(1)
    print("assuming we start on line", nskips, "of train")
    temps2sents = group_by_template(tagged_fi, nskips)
    #top_temps = sorted(temps2sents.keys(), key=lambda x: -len(temps2sents[x]))[:ntemplates]    #original code
    top_temps = sorted(list(temps2sents.keys()), key=lambda x: -len(temps2sents[x]))[:ntemplates]

    from collections import Counter
    for i in range(5):  # Print top 5 tamplates
        print(f"Top-{i+1} template:{top_temps[i]}")

        ## HackMD table format
        line_0, line_1 = '| ', '| '
        for state in top_temps[i]:
            line_0 = line_0 + f"{state} | "
            line_1 = line_1 + "-"*8 + " | "
        print(line_0 + "count | portion |")
        print(line_1 + ("-"*8 + " | ") *2 )

        sents = temps2sents[top_temps[i]]
        duplicated = Counter()#set()     # Counter for duplicated templates
        #j = 0
        #while j < len(sents) and len(printed_line) < 10:    # 10 examples for each template
        #    line = ' | '.join(sents[j][0])
            #if line not in printed_line:
            #    print(line)
            #    printed_line.add(line)
            #j = j + 1
        for sent in sents:
            templt = ' | '.join(sent[0])
            duplicated[templt] += 1

        duplicated = sorted([(c,t) for (t,c) in duplicated.items()], reverse=True)
        sum_duplicated = sum([c for (c,t) in duplicated])
        for count,templt in duplicated:
            print(templt, f' | {count} | {count/total_data_len:.3f} |')
        
        print(f'In total: {sum_duplicated} problems using this templates')

    #remap_eos_states(top_temps, temps2sents)
    state2phrases = just_state2phrases(top_temps, temps2sents)


    return top_temps, temps2sents, state2phrases


def topk_phrases(pobj, k):
    phrases, probs = pobj
    thing = sorted(zip(phrases, list(probs)), key=lambda x: -x[1])
    sphrases, sprobs = zip(*thing)
    return sphrases[:k]


def align_cntr(cntr, thresh=0.4):
    tote = float(sum(list(cntr.values())))
    nug = {k : v/tote for k, v in cntr.items()}
    best, bestp = None, 0
    for k, v in nug.items():
        if v > bestp:
            best, bestp = k, v
    if bestp >= thresh:
        return best
    else:
        return None