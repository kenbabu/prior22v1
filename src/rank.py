# Generate ranks from similarity scores 
from prior import (
    lsprot_gohpo_universal,
    go_similarity_score
)
from  loaddata import (
    load_test_data_dict,
    load_disgenet_to_uniprot_data_dict,
    load_diabetes_test_genes,
    load_diabetes_proteins
) 
from collections import OrderedDict
from operator import itemgetter
from itertools import  chain
from utility import (
    naive_score, 
    timer_func
)

DictProtUniversalData = load_test_data_dict()
DisgenetData =  load_disgenet_to_uniprot_data_dict()
DIABETES_GENES_2016 = load_diabetes_test_genes()
DIABETES_PROTEINS_2016 = load_diabetes_proteins()

# del DictProtUniversalData['agg_func']

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
        # go_sim = go_similarity_score(lstrain, [prot],  **DictProtUniversalData )
        DictRanks[prot] = sim
    dict_ordered_sim = OrderedDict(
            sorted(DictRanks.items(), key=itemgetter(1), reverse=True))
    ranks = generate_rank(dict_ordered_sim)
    
    # print(DictRanks)
    del DictRanks
    return ranks
@timer_func
def rank_genes_disease(ls_test_prots, disease, tag):
    ls_disease_prots = DisgenetData.get(disease)
    ranks = {}
    if not ls_disease_prots:
        return ranks
    try:
        ranks = rank_train_test(ls_disease_prots, ls_test_prots, tag)
        return ranks
    except Exception:
        print(f"Unknown error: {e}")
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
# ['FOOBAR','INS', 'GCK','TCF7L2', 'HHEX','IGF2BP2', 'ACE', 'APOE', 'ANO4', 'MAPT', 'PLAU', 'MPO']

def main():
    rank = rank_train_test(['KCNJ11', 'HNF4A' ], ['INS', 'GCK','TCF7L2', 'HHEX','IGF2BP2'])

    rank_diabetes = rank_train_test(DIABETES_PROTEINS_2016[:4], DIABETES_PROTEINS_2016)

    rank_disease = rank_genes_disease(DIABETES_PROTEINS_2016 , 'C0011854', 3)
    diabetes_proteins = DisgenetData.get('C0011854')
    num_prots = len(diabetes_proteins)
    num_set_prots = len(set(diabetes_proteins))
    print(f"Ranking diabetes proteins: {rank_diabetes}")
    print(f"Ranking disease genes: {rank}")

    print(f"Ranking disease genes: {rank_disease}")
    # print(f"Diabetes proteins: {diabetes_proteins}\n{num_prots}\n{num_set_prots}")

if __name__ == '__main__':
    main()