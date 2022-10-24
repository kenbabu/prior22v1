# Generate ranks from similarity scores 
def generate_rank(sorted_dict):
    ranks = {}
    cur_score = None
    cur_count = 0
    for ix, (name, score) in enumerate(sorted_dict.items()):
        if score == cur_score:
            cur_count += 1
        else: 
            #Different scores
            cur_score = score
            cur_count = 0
        ranks[name] = ix - cur_count + 1
    return ranks

# Given  a list of training and test proteins generate a list of ranks of the list of test based on their 
# semantic similarity to the training proteins.
def rank_train_test(lstrain, lstest, tag=1):
    DictRanks = {}
    for prot in lstest:
        sim = lsprot_gohpo_universal(lstrain, [prot], tag, **DictProtUniversalData)
        DictRanks[prot] = sim
    dict_ordered_sim = OrderedDict(
            sorted(DictRanks.items(), key=itemgetter(1), reverse=True))
    ranks = generate_rank(dict_ordered_sim)
    
    del DictRanks
    return ranks# go_pred = t2d2016_go
def subset_by_rank(d, rank):
    try:
        subdict = {k:v for k, v in d.items() if int(v)<rank }
        return subdict
    except Exception as e:
        print(e)


# Subset
# go_pred = t2d2016_go
def subset_by_rank(d, rank):
    try:
        subdict = {k:v for k, v in d.items() if int(v)<rank }
        return subdict
    except Exception as e:
        print(e)
