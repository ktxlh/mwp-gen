from collections import Counter

####
# for other_mwp statistics only
total_data_len = 1557
####

# TODO: > .md in gen, how about segs??

def _print_md_col_names(items):
    ## Print the first 2 lines of a .MarkDown table
    print(f"| {' | '.join([str(item) for item in items])} |")
    print(f"| {' | '.join(['-'*8 for item in items])} |")

def top_templates_from_train(top_temps, temps2sents, k=5):    

    print(f"# Top {k} templates from train")
    for i in range(k):  # Print top k tamplates
        print(f"## Top-{i+1}: {top_temps[i]}")

        _print_md_col_names([*(top_temps[i]), 'count', 'portion'])

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
            #lineno = sent[1]
            templt = ' | '.join(sent[0])
            duplicated[templt] += 1

        duplicated = sorted([(c,t) for (t,c) in duplicated.items()], reverse=True)
        sum_duplicated = sum([c for (c,t) in duplicated])
        for count,templt in duplicated:
            print(f'| {templt} | {count} | {count/total_data_len:.3f} |')
        
        print(f'In total: {sum_duplicated} problems using this templates')
    
    print()


def top_template_phrase_examples(top_temps, state2phrases, k=5, n_phrases=10):
    """
    Parameters:
        n_phrases:  print top {n_phrases} examples for each state
    """
    def _print_it(with_freq):
        for template_it in range(k):    # Top 5 templates
            print(f"### Top-{template_it+1}")

            _print_md_col_names(top_temps[template_it])

            template = top_temps[template_it]  # a tuple of states
            template_examples = [[] for i in range(n_phrases)]  #[['phr1-1','phr2-1'], ['ph1-2', 'phr2-2']]
            for i_state,state in enumerate(template):
                # [0] for phrase; [1] for frequency
                phr_frq = sorted(zip(state2phrases[state][1],state2phrases[state][0]), reverse=True)
                for i_exp in range(n_phrases):
                    example_phrase = ' '
                    if i_exp < len(phr_frq):
                        example_phrase = f"{phr_frq[i_exp][1]}"             #e.g. "How much"
                        if with_freq:
                            example_phrase += f" ({phr_frq[i_exp][0]:.2f})"  #e.g. "How much (0.03)"
                    template_examples[i_exp].append(example_phrase)
                    
            for i_exp in range(n_phrases):
                print(f"| {' | '.join(template_examples[i_exp])} |")
            print()

    print(f"# Top {k} templates consist of")
    print(f"## No frequencies")
    _print_it(False)
    print(f"## With frequencies")
    _print_it(True)
    

