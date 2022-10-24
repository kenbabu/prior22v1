def jaccard_sim(ls1, ls2):
    num = set(ls1).intersection(set(ls2))
    denom = set(ls1).union(set(ls2))
    sim = round(len(num)/float(len(denom)), 5)
    return sim
# trim
def trim_id(ls1):
    
     return [i.split(":")[1] for i in ls1]
    
# Protein cosine similarity
def protein_cos_sim(ls1, ls2):
#     ls1, ls2 = annot_dict.get(prot1), annot_dict.get(prot2)
    
    doc1 = " ".join(trim_id(ls1))
    doc2 = " ".join(trim_id(ls2))
    
    docs = [doc1, doc2]
    
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(docs)
    
    doc_term_matrix = sparse_matrix.todense()
    
#     df = pd.DataFrame(doc_term_matrix, 
#                  columns=count_vectorizer.get_feature_names(),
#                  index=['doc1', 'doc2'])
#     print(df)
    return round(cosine_similarity(doc_term_matrix)[0,1],5)
    
# Protsim vector
def prot_sim_vector(prot1, prot2, ont, annot_dict, sub_ontology, sim_measure):
#     Groupwise
    lsprot1, lsprot2 = get_prot_annot(prot1, annot_dict), \
                        get_prot_annot(prot2, annot_dict) 
    ls_n_prot1, ls_n_prot2 = create_non_redundant(lsprot1, go, sub_ontology), \
                                create_non_redundant(lsprot2, go, sub_ontology)
    return sim_measure(ls_n_prot1, ls_n_prot2)

def prot_sim_ontology(prot1, prot2, ont,\
                      annot_dict, sub_ontology,\
                      dict_levels, agg_method):
#     Groupwise
    lsprot1, lsprot2 = get_prot_annot(prot1, annot_dict), \
                        get_prot_annot(prot2, annot_dict) 
#      Get only annotations that are preset in the subontology
    lsprot1, lsprot2 = list(set(lsprot1) & set(sub_ontology)), list(set(lsprot2) & set(sub_ontology))
    ls_n_prot1, ls_n_prot2 = create_non_redundant(lsprot1, ont, sub_ontology), \
                                create_non_redundant(lsprot2, ont, sub_ontology)
#     sim=agg_method(ls_n_prot1, ls_n_prot2, ont, dict_levels )
    sim=agg_method(ls_n_prot1, ls_n_prot2, ont, dict_levels )
    return sim