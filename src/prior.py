# import numpy as np
from itertools import  chain
from semantic import best_match_avg2
from utility import naive_score
from loaddata import  load_test_data_dict
from ontologyprocess import (
    general_universal,
    ONTOLOGY_ROOTS
)
from itertools import  chain

DictProtUniversalData = load_test_data_dict()

# Calculate semantic similarity between a pair of protein list based on any one of the ontologies or both 
# of the ontologies by specifying a tag 1=GO, 2=HPO, 3=GO and HPO
def prot_sim(prot1, prot2):
    pass
# lsprot_gohpo_universal(ls1, ls2, tag, **kwargs)
def go_similarity_score(ls_prot1, ls_prot2, **kwargs):
    # same list
    if ls_prot1 == ls_prot2: return 1.0

    if (ls_prot1 == []) or (ls_prot2 == []): return 0.0
    
    go_sim_score = -10.0 
    annots1 = (kwargs['go_annotations'].get(prot) for prot in ls_prot1)
    annots2 = (kwargs['go_annotations'].get(prot) for prot in ls_prot2)

    ls_go_annots1 = list(set(chain(*filter(None, annots1 ))))
    ls_go_annots2 = list(set(chain(*filter(None, annots2 ))))

    go_sim_score = best_match_avg2(ls_go_annots1, ls_go_annots2,kwargs['go_parents'], kwargs['go_topologies'], kwargs['go_sub'])
    return go_sim_score


def hpo_similarity_score(ls_prot1, ls_prot2, **kwargs):
    # same list
    if ls_prot1 == ls_prot2: return 1.0

    if (ls_prot1 == []) or (ls_prot2 == []): return 0.0
    
    hpo_sim_score = -10.0 
    annots1 = (kwargs['hpo_annotations'].get(prot) for prot in ls_prot1)
    annots2 = (kwargs['hpo_annotations'].get(prot) for prot in ls_prot2)

    ls_go_annots1 = list(set(chain(*filter(None, annots1 ))))
    ls_go_annots2 = list(set(chain(*filter(None, annots2 ))))

    hpo_sim_score = best_match_avg2(ls_go_annots1, ls_go_annots2,kwargs['hpo_parents'], kwargs['hpo_topologies'], kwargs['hpo_sub'])
    return hpo_sim_score
# Combined similarity score
def combined_similarity_score(ls_prot1, ls_prot2, **kwargs):
    # same list
    if ls_prot1 == ls_prot2: return 1.0

    if (ls_prot1 == []) or (ls_prot2 == []): return 0.0
    go_sim_score, hpo_sim_score, combined_sim_score = 0.0, 0.0, 0.0
    go_sim_score = go_similarity_score(ls_prot1, ls_prot2, **kwargs)
    hpo_sim_score = hpo_similarity_score(ls_prot1, ls_prot2, **kwargs)
    combined_sim = naive_score(go_sim_score, hpo_sim_score)
    return combined_sim


def lsprot_gohpo_universal(ls1, ls2, tag, **kwargs):
    if ls1 == ls2:
        return 1.0
    if ls1 == [] or ls2 == []:
        return 0.0
    # print(f"ls1: {ls1}   ls2: {ls2}")
#     GO
    go_sim_score, hpo_sim_score, combined_sim = 0.0, 0.0, 0.0
    if tag == 1:
        annots1 = [kwargs['go_annotations'].get(prot) for prot in ls1]
        ls_go_annots1 = list(set(chain(*filter(None, annots1 ))))
        
        annots2 = [kwargs['go_annotations'].get(prot) for prot in ls2]
        ls_go_annots2 = list(set(chain(*filter(None, annots2 ))))
        go_sim_score = best_match_avg2(ls_go_annots1, ls_go_annots2,\
                                            kwargs['go_parents'], kwargs['go_topologies'], kwargs['go_sub'])
        return go_sim_score
    elif tag == 2:
        annots1 = [kwargs['hpo_annotations'].get(prot) for prot in ls1]
        ls_hpo_annots1 = list(set(chain(*filter(None, annots1 ))))
        
        annots2 = [kwargs['hpo_annotations'].get(prot) for prot in ls2]
        ls_hpo_annots2 = list(set(chain(*filter(None, annots2 ))))
        hpo_sim_score = best_match_avg2(ls_hpo_annots1, ls_hpo_annots2,\
                                            kwargs['hpo_parents'], kwargs['hpo_topologies'], kwargs['hpo_sub'])
        
        return hpo_sim_score
    elif tag == 3:
        annots_go_1 = [kwargs['go_annotations'].get(prot) for prot in ls1]
        ls_go_annots1 = list(set(chain(*filter(None, annots_go_1 ))))
        
        annots_go_2 = [kwargs['go_annotations'].get(prot) for prot in ls2]
        ls_go_annots2 = list(set(chain(*filter(None, annots_go_2 ))))
        go_sim_score = best_match_avg2(ls_go_annots1, ls_go_annots2,\
                                            kwargs['go_parents'], kwargs['go_topologies'], kwargs['go_sub'])
        
        annots_hpo_1 = [kwargs['hpo_annotations'].get(prot) for prot in ls1]
        ls_hpo_annots1 = list(set(chain(*filter(None, annots_hpo_1 ))))
        
        annots_hpo_2 = [kwargs['hpo_annotations'].get(prot) for prot in ls2]
        ls_hpo_annots2 = list(set(chain(*filter(None, annots_hpo_2 ))))
        hpo_sim_score = best_match_avg2(ls_hpo_annots1, ls_hpo_annots2,\
                                            kwargs['hpo_parents'], kwargs['hpo_topologies'], kwargs['hpo_sub'])

        
#         check if score is defined on both ontologies
        if go_sim_score and hpo_sim_score:
        
            combined_sim = naive_score(go_sim_score, hpo_sim_score)
            return combined_sim
        elif go_sim_score:
            return go_sim_score
        elif hpo_sim_score:
            return hpo_sim_score
        else:
            return -1.0      
    else:
        print("Error! Please check that the correct tag is passed.")

def main():
    sim = go_similarity_score(['P14222'], ['Q96KN2'], **DictProtUniversalData)   
    
    print(f"GO Score: {sim}")
        
if __name__ == '__main__':
    main()