import click 
import utility as ut
import ontologyprocess as op
from semantic import best_match_avg2
import loaddata

from  loaddata import (
    load_test_data_dict,
    load_disgenet_to_uniprot_data_dict,
    load_diabetes_test_genes,
    load_diabetes_proteins
) 

from rank import (
    rank_train_test,
    rank_genes_disease
)

from prior import lsprot_gohpo_universal


DictProtUniversalData = load_test_data_dict()
DisgenetData =  load_disgenet_to_uniprot_data_dict()
DIABETES_GENES_2016 = load_diabetes_test_genes()
DIABETES_PROTEINS_2016 = load_diabetes_proteins()


# DictTopologyData = loaddata.load_topology_data()
DictTopologyData = loaddata.load_test_data_dict()
GOTopos = DictTopologyData['go_topologies']
HPOTopos = DictTopologyData['hpo_topologies']

GOParentsLevels = DictTopologyData['go_parents']
HPOParentsLevels = DictTopologyData['hpo_parents']

def load_diabetes_test_genes():
    try:
        with open('Data/TestData/DiabetesData/t2dgenes2016.txt', 'r') as handle:
            ls_diabetes_genes = list()
            for line in handle:
                ls_diabetes_genes.append(line.rstrip())
        return ls_diabetes_genes
    except FileNotFoundError as fe:
        return None

DICT_ONTOLOGY = {'go':1, 'hpo':2, 'all':3}

# ctx.obj = {
#     'dict_ontology': DICT_ONTOLOGY
# }


@click.group()
def cli():
    pass
@cli.command(name='semsim')
@click.argument('term1')
@click.argument('term2')
@click.argument('ontology')
# @click.argument('--ontology', default='GO', help='Ontology to use for prioritization')
def semantic_similarity(term1, term2, ontology='GO'):
    """ Semantic similarity between ontology terms """
    sim =0.0
    if ontology.upper() =='HPO':
        print("HPO")
        sim = op.general_universal(term1, term2, HPOParentsLevels, HPOTopos)
    elif ontology.upper() == 'GO':
        print('GO')
        sim = op.general_universal(term1, term2, GOParentsLevels, GOTopos)
    else:
        print(f'The specified ontology {ontology} is not valid!')
    print(f"Semantic similarity between {term1} and {term2} = {sim}")


@cli.command(name='rank')
@click.argument('proteins', nargs=-1)
@click.argument('disease', nargs=1)
def prior_rank(proteins, disease):
    """Prioritize proteins"""
    ls_prots =[prot for prot in proteins ]
    print(f"Proteins: {ls_prots}\nDisease: {disease}")
    return ls_prots

@cli.command(name='prior')
@click.argument('target', nargs=-1)
@click.argument('source', nargs=1)
def prioritize(target, source):
    """Prioritize source and target proteins"""
    ls_source, ls_target =  ['KCNJ11', 'HNF4A' ], ['INS', 'GCK','TCF7L2', 'HHEX','IGF2BP2']
    sim = lsprot_gohpo_universal(ls_source, ls_target,2, DictTopologyData)
    return sim 
    # pass

@cli.command(name='rankdisease')
# @click.argument('proteins', nargs=-1)
@click.pass_context
@click.option('-o', '--ontology', type=click.Choice(['GO', 'HPO', 'ALL'], case_sensitive=False), help="Ontology choice")
@click.option('-pf', '--proteinfile', type=click.Path(exists=True), help='Path to the file that contains proteins that are to be ranked')
@click.option('-rf', '--resultfile',type=click.Path(), default='Results/ResultFile.txt', help="Path to output file")
@click.argument('disease', nargs=1, metavar='DISEASE_ID')
def prioritize_proteins_disease(ctx, proteinfile, disease, ontology, resultfile):
    """Rank proteins against a disease"""
    ls_source, ls_target =  ['KCNJ11', 'HNF4A' ], ['INS', 'GCK','TCF7L2', 'HHEX','IGF2BP2']
    DICT_ONTOLOGY
    with open(proteinfile, 'r') as handle:
        ls_test_proteins = list()
        for line in handle:
            ls_test_proteins.append(line.rstrip())
    ranks = rank_genes_disease(ls_test_proteins, disease, DICT_ONTOLOGY[ontology.lower()])
    with click.progressbar(ranks.items()) as data:
        with open(resultfile, 'w') as handle:
            for key, val in data:
                handle.write(f'{key}\t{val}\n')
    
    # for k, v in ranks.items():
    #     print(f"{k}\t{v}")
    


def main():
    data = DictTopologyData
    # print(data.keys())
    # print(f'DictTopologyData: {DictTopologyData.keys()}')

if __name__ == '__main__':
    main()


    