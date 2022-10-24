import click 
import utility as ut
import ontologyprocess as op
import loaddata


DictTopologyData = loaddata.load_topology_data()
GOTopos = DictTopologyData['GOTopos']
HPOTopos = DictTopologyData['HPOTopos']

GOParentsLevels = DictTopologyData['GOParentsLevels']
HPOParentsLevels = DictTopologyData['HPOParentsLevels']


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
    