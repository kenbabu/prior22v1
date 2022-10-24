def average(ls1, ls2, ont, dict_levels):
    av = [sim_universal(a, b, ont, dict_levels) for a in ls2 for b in ls1]
    sim = round(sum(av)/len(av),5)
    return sim
    

def best_match_avg(ls1, ls2, ont, dict_levels, ont_sub=None):
    if ls1 == ls2:
        return 1.0
    if ont_sub:
        ls1c, ls2c = set(ls1) & set(ont_sub), set(ls2) & set(ont_sub)
    else:
        ls1c, ls2c = ls1, ls2
        
    if (ls1c == set() or ls2c == set()):
        return 0.0
        
#         print(f'{ls1c}')
    try:
        max1 = [max([sim_universal(a, b, ont, dict_levels) for a in ls2c]) for b in ls1c]
        max2 = [max([sim_universal(a, b, ont, dict_levels) for a in ls1c]) for b in ls2c]
        sim = round((np.mean(max1)+np.mean(max2))/2.0, 5)
        return sim
    except Exception as e:
        print(f'{e}')
        pass

def average_best_match(ls1, ls2, dict_parents, dict_topologies, ont_sub=None):
    if ls1 == [] or ls2 ==[]:
        return 0.0
    if ls1 == ls2:
        return 1.0
    if ont_sub:
        ls1c, ls2c = set(ls1) & set(ont_sub), set(ls2) & set(ont_sub)
    else:
        ls1c, ls2c = set(ls1), set(ls2)
        
    if (ls1c == set() or ls2c == set()):
        return 0.0
    try:
        max1 = [max([general_universal(a, b, dict_parents, dict_topologies) for a in ls2c]) for b in ls1c]
        max2 = [max([general_universal(a, b, dict_parents, dict_topologies) for a in ls1c]) for b in ls2c]
        sim = max1 + max2
        sim = round(np.mean(sim), 5)
        return sim
    except Exception as e:
        print(e)
        pass
# Best match average for aggregating  semantic similarity
def best_match_avg2(ls1, ls2, dict_parents, dict_topologies, ont_sub=None):
#     print(ls1, ls2)
    if (not ls1) or (not ls2 ):
#         print("List not defined")
        return 0.0
    if ls1 == [] or ls2 ==[]:
        return 0.0
    if ls1 == ls2:
        return 1.0
  
    ls1c = list(set(ls1) & set(dict_topologies))
    ls2c = list(set(ls2) & set(dict_topologies))
    
#     print(ls2c)

#         print(ont_sub)
    if ls1c == [] or  ls2c == []:
        return 0.0

    try:
        max1 = [max([general_universal(a, b, dict_parents, dict_topologies) for a in ls2c]) for b in ls1c]
#         print(max1)
#         print("***")
        max2 = [max([general_universal(a, b, dict_parents, dict_topologies) for a in ls1c]) for b in ls2c]
#         print(max2)
        sim = round((np.mean(max1)+np.mean(max2))/2.0, 5)
        return sim
    except Exception as e:
        print(f' Error {e}')