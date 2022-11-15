# Developer notes

## Instruction to developers

## Data
Data that was used to buid the algorithm is stored in various files as outlined below. Please
note that the path to the individual files is provided relative to the project directory.
### Ontologies
Ontologies that are integrated into the algorithm. As at version_1 of PrIOR, two ontologies
have been integrated. Future version may include more ontologies. Relative paths of the 
ontology files are as outlined below.
#### Gene ontology ([GO](https://go-online.org))
    - Data/Ontologies/GO/go_basic.obo
#### Human phenotype ontology ([HPO](https://hpo.jax.org))
    - Data/Ontologies/HPO/hp.obo
### Mapping dictionaries
These are files that provide a mapping between genes and proteins
#### Mapping from genes to proteins
    - Data/MappingDictionaries/dict_gene_uniprot.pk

#### Mapping from proteins to genes 
    - Data/MappingDictionaries/dict_uniprot_gene.pk
### Pre-calculated ontology related data 
#### Annotation files
- GO Annotation
    - Data/Annotations/dict_prots_go_all.pk
- HPO Annotation
    - Data/Annotations/dict_prots_hpo.pk
### Ontology topology graph data
Data that is used to calculate semantic similarity between ontology term.
#### Term parents at each level
    - GO Data/ProcessedOntology/GO/GOParentsLevelMarch2022.pk
    - HPO Data/ProcessedOntology/HPO/HPOParentsLevelMarch2022.pk
#### Term topology
    - GO  Data/ProcessedOntology/GO/GOToposMarch2022.pk
    - HPO Data/ProcessedOntology/HPO/HPOToposMarch2022.pk
### Disease-to-protein maps
A file that associates diseases in [DisGeNET](https://disgenet.org) to their associated proteins.

- Data/Disease/disgenet_to_uniprot.pk

### Test files