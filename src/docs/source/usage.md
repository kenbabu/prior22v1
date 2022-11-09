# Usage

## Installation

To install PrIOR

```console
(env) $ pip install prior

```

## Run PrIOR

### Get UMLS_CUI ID for a disease
- Search this url (https://www.disgenet.org/search)[DisGeNET]

### Rank a list of proteins

```console
(env) $ python run.py rankdisease -o all -pf <path/to/protein/file> UMLS_Disease_ID

# Example to rank breast cancer proteins against alzheimer's disease

(env) $ python run.py rankdisease -o go -pf Data/TestData/BreastCancer/brca_proteins.txt C0001080
```
#### Description of inputs
*-o or --ontology*   Ontology upon which the ranking is based.

*-pf or --protein_file*   A file containing UniProt protein IDs for proteins to be ranked.
                          A single ID per line.

*-rf or --resultfile*   A file onto which the result of the ranking is written.\nIf a file path
                        is not provided ther results will be stored in Results/ResultFile.txt