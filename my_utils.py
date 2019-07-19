def count_unk(path, UNK_TAG = '<unk>'):
    """
    path: Path to a space-separated file
    for [NT-OTH-1]
    """
    unk, total = 0, 0
    with open(path,'r',encoding='utf8') as f:
        tokens = [token for line in f.readlines() for token in line.split()]
        total = len(tokens)
        unk = sum([1 for token in tokens if UNK_TAG in token])
    return unk,total

if __name__ == '__main__':
    org_unk, org_ttl = count_unk('segs/seg-otherTrain-100-55-5-far-NER-no_test.txt')
    new_unk, new_ttl = count_unk('segs/seg-otherTrain-100-55-5-far-NER-no_test-unk.txt')
    print(org_unk,org_ttl,org_unk/org_ttl)
    print(new_unk,new_ttl,new_unk/new_ttl)