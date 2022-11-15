# Usage

## Installation

To install PrIOR

```console
(env) $ pip install prior

```
## Build docker image
Build docker image of priorv22 and hand cursor back to the commandline
```console
$ docker build -t priorv22 --rm -d

```
## Run docker image
Run image of priorv22 in an interactive
```console
$ docker run -t -i priorv22 --rm

```

## Execute a PrIOR run after initalising a container
An example of prioritising a set of proteins for a disease
<!--  -->

```console
app_user@874509d8a:~$ python run.py rankdisease -o go -pf Data/TestData/BreastCancer/brca_proteins.txt C0001080

```

## Run PrIOR

```console
$ docker run -it --name priorv22_app --rm priorv22

```


### Get UMLS_CUI ID for a disease
- Search  [DisGeNET](https://www.disgenet.org/search) for mapping between disease names and corresponding UMLS IDs

## Rank a list of proteins

```
(env) $ python run.py rankdisease -o all -pf <path/to/protein/file> UMLS_Disease_ID

# Example to rank breast cancer proteins against alzheimer's disease

(env) $ python run.py rankdisease -o go -pf Data/TestData/BreastCancer/brca_proteins.txt C0001080

```

## Description of inputs

**-o or --ontology** \n 
&nbsp;&nbsp; Ontology upon which the ranking is based.

**-o or --ontology**   Ontology upon which the ranking is based.

*-pf or --protein_file*   A file containing UniProt protein IDs for proteins to be ranked.
                          A single ID per line.

*-rf or --resultfile*   A file onto which the result of the ranking is written.\nIf a file path
                        is not provided ther results will be stored in Results/ResultFile.txt