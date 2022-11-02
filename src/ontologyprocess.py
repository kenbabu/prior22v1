ONTOLOGY_ROOTS = ['GO:0008150', 'HP:0000001']

def topology(term, ont, dict_levels):
    try:
        lsrparents = list(ont[term].superclasses(with_self=False).to_set().ids) 
    #     lsrparents = [i.id for i in ont[term].rparents() if ont[i.id].rparents() != []]

        dict_num = {d:[dict_levels[d],ont[d].subclasses(with_self=False,
                                                        distance=1).to_set().__len__()] for d in lsrparents }
        ls_num_children  = [v[1] for k,v in dict_num.items()]
#         print(f'ls_num_children: {ls_num_children}')
#         ls_num_children = list(filter(lambda x: x>0, ls_num_children))
        if ls_num_children != []:
            topo = np.reciprocal(float(reduce(lambda x, y: x*y, ls_num_children)))

            return round(-1*math.log(topo), 5)
        return 0.0
    except KeyError as ke:
        return 0.0


        # Generate topology
def generate_topologies(lsterms,ont,ont_root, dict_levels):
    dict_topos = {}
    dict_topos[ont_root] = 0.0
    for term in lsterms:
        dict_topos[term] = topology(term, ont, dict_levels)
    return dict_topos

def gen_level_dict(ont, root):
    descendants = ont[root].subclasses(with_self=False)
    level_dict = {}
    level_dict[root]=0
    for desc in descendants:
        oid = desc.id
        level_dict[oid] = len(ont[oid].superclasses(with_self=False).to_set().ids)
    return level_dict

# 
def generate_parents_level(lsterms, ont, ont_root):
#     ontology dictionary
    dict_parents ={}
    dict_parents[ont_root] = {}
    for term in lsterms:
#         dict_parents[term] = ont[term].rparents().id
        dict_parents[term] = set(ont[term].superclasses(with_self=False).to_set().ids)

    return dict_parents

def general_universal(term1, term2, dict_parents, dict_topologies, DictTermSim={}):
    #     Roots hard corded
#     DictTermSim.clear()
    if (term1 in ONTOLOGY_ROOTS) | (term2 in ONTOLOGY_ROOTS):
        return 0.0
    if term1 == term2:
        return 1.0
    if (term1, term2) in DictTermSim:
        return DictTermSim[(term1, term2)]
    ancs = dict_parents[term1].intersection(dict_parents[term2])
#     print(f"ancestors of {term1} and {term2}: {ancs}")
    mica = max(dict_topologies[t] for t in ancs)
    
    sim = round(mica/max(dict_topologies[term1],dict_topologies[term2]), 5)
    
    DictTermSim[(term1, term2)] =  DictTermSim[(term2, term1)] = sim
    return sim

if __name__ == '__main__':
    pass