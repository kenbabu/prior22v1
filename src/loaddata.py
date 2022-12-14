from ast import Try
import pickle
from semantic import best_match_avg2



def load_mapping_dicts():
    MappingDict ={}
    with open('dict_uniprot_gene.pk', 'rb') as handle:
        DictUniprotGene = pickle.load(handle)
# DictUniprotGene
    with open('dict_gene_uniprot.pk', 'rb') as handle:
        DictGeneUniprot = pickle.load(handle)
    MappingDict['DictUniprotGene'] = DictUniprotGene
    MappingDict['DictGeneUniprot'] = DictGeneUniprot
    return MappingDict


# Load test data
def load_test_genes():
    t2dfile = os.path.join(GeneDataDir,'t2diabetes_genes_omar2013.txt' )
    t2d2016file = os.path.join(GeneDataDir,'t2dgenes_soo_heon_kwak2016.txt' )
    DataDict ={}
    with open(t2dfile, 'r') as handle:
        t2dgenes = list(map(lambda x: x.strip('\n'),handle.readlines()))
#         Split multiple genes listed in one line e.g 'RBMS1/ITGB6',
        t2dgenes = list(chain.from_iterable([[a, c] for a,b,c in (x.partition('/') for x in t2dgenes )])) 
        t2dgenes = [x for x in t2dgenes if len(x)>1]
    with open(t2d2016file, 'r') as handle:
        t2d2016genes = list(map(lambda x: x.strip(',\n'),handle.readlines()))
    DataDict['t2d2013'] = t2dgenes
    DataDict['t2d2016genes'] = t2d2016genes
    return DataDict 

def load_topology_data():
    # Load levels
    DictTopologyData = dict()
    with open('Data/ProcessedOntology/GO/GOParentsLevelMarch2022.pk', 'rb') as handle:
        GOParentsLevels = pickle.load(handle)
    DictTopologyData['GOParentsLevels']= GOParentsLevels

    with open('Data/ProcessedOntology/HPO/HPOParentsLevelMarch2022.pk', 'rb') as handle:
        HPOParentsLevels = pickle.load(handle)
    DictTopologyData['HPOParentsLevels']= HPOParentsLevels

    # Load topologies

    with open('Data/ProcessedOntology/GO/GOToposMarch2022.pk', 'rb') as handle:
        GOTopos = pickle.load(handle)
    DictTopologyData['GOTopos']= GOTopos

    with open('Data/ProcessedOntology/HPO/HPOToposMarch2022.pk', 'rb') as handle:
        HPOTopos = pickle.load(handle)
    DictTopologyData['HPOTopos']= HPOTopos

    return DictTopologyData

def load_disgenet_to_uniprot_data_dict():
    # c/Data/TestData
    try:
        with open('Data/Disease/disgenet_to_uniprot.pk', 'rb') as handle:
            DisgenetData = pickle.load(handle)
        return DisgenetData
    except FileNotFoundError as fe:
        return None

def load_diabetes_test_genes():
    try:
        with open('Data/TestData/DiabetesData/t2dgenes2016.txt', 'r') as handle:
            ls_diabetes_genes = list()
            for line in handle:
                ls_diabetes_genes.append(line.rstrip())
        return ls_diabetes_genes
    except FileNotFoundError as fe:
        return None

def load_diabetes_proteins():
    try:
        with open('Data/TestData/DiabetesData/diabetes_prots_2016.txt', 'r') as handle:
            ls_diabetes_prots = list()
            for line in handle:
                ls_diabetes_prots.append(line.rstrip())
        return ls_diabetes_prots
    except FileNotFoundError as fe:
        return None
# load_diabetes_proteins

def load_test_data_dict():
    # c/Data/TestData
    try:
        with open('Data/TestData/DictProtUniversalData.pk', 'rb') as handle:
            DictTestData = pickle.load(handle)
        return DictTestData
    except FileNotFoundError as fe:
        return None

def main():
  print('Loading data...')

if __name__ == '__main__':
    main()