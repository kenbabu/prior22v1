import click 
import utility as ut
import ontologyprocess as op
from semantic import best_match_avg2
import loaddata

from prior import lsprot_gohpo_universal


# DictTopologyData = loaddata.load_topology_data()
DictTopologyData = loaddata.load_test_data_dict()
GOTopos = DictTopologyData['go_topologies']
HPOTopos = DictTopologyData['hpo_topologies']

GOParentsLevels = DictTopologyData['go_parents']
HPOParentsLevels = DictTopologyData['hpo_parents']


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

@cli.command(name='rankproteins')
@click.argument('proteins', nargs=-1)
@click.argument('disease', nargs=1)
def prioritize_protens_disease(proteins, disease):
    """Rank proteins against a disease"""
    ls_source, ls_target =  ['KCNJ11', 'HNF4A' ], ['INS', 'GCK','TCF7L2', 'HHEX','IGF2BP2']
    sim = lsprot_gohpo_universal(ls_source, ls_target,2, DictTopologyData)
    return sim 
    # pass


def main():
    data = DictTopologyData
    # print(data.keys())
    print(f'DictTopologyData: {DictTopologyData.keys()}')

if __name__ == '__main__':
    main()


    