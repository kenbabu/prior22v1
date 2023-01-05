from  dataclasses import dataclass
from typing import List
import pickle
import json
import pandas as pd

@dataclass
class PopulationFrequency:
    population: str
    frequency: float

@dataclass
class Gene:
    name: str 
    freqlist: List[PopulationFrequency]
def mean_pop_frequency(df):
    pass

def annotate_genes(df, lsproteins):
    dfannot = df.loc[df["Protein"].isin(lsproteins)]
    # if not dfannot:
    #     return
    return dfannot


def main():
    with open("config.json") as configfile:
        data = json.load(configfile)

    SINKDATA = data['sinkdata']
    MAMDATA = data['mamdata']

    # Dictionary mapping for genes  to proteins
    with open(data['gene2prot'], 'rb') as handle:
        DictGeneProt = pickle.load(handle)
    # Load results for frequency annotation

    with open(data['rankresult'], "r") as handle:
        RankProteins = [line.split('\t')[0].strip() for line in handle.readlines()]


    AfricanPops = [
    'AMR_AF', 'ASW_MAF',
    'Baganda_MAF', 'BantuKenya_MAF', 'BantuTswana_MAF',
    'Bapedi_MAF', 'Biaka_MAF',  'CDX_MAF', 'CEU_MAF',
    'Dinka_MAF', 'ESN_MAF', 'ETHIOPIA_MAF', 'EUR_AF', 'Esan_MAF',
    'FIN_MAF', 'GNOMAD_ALL_MAF',  'GWD_MAF', 'Gambian_MAF', 'H3A_MAF',
    'H3A_V4_MAF','KHOESAN_MAF', 'Khomani_San_MAF', 'LWK_MAF', 'Luhya_MAF',
    'Luo_MAF',  'MSL_MAF', 'MXL_MAF', 'Mandenka_MAF',
    'Masai_MAF', 'Mbuti_MAF', 'Mende_MAF', 'Mozabite_MAF',
    'SOTHO_MAF', 'Saharawi_MAF', 'Somali_MAF',
    'TSI_MAF', 'Tsonga_MAF', 'Tswana_MAF',
    'Venda_MAF', 'XHOSA_MAF', 'YRI_MAF', 'Yoruba_MAF',
    'Zulu_MAF'
    
    ]

    EuroPops = ['FIN_MAF', 'EUR_AF', 'CEU_MAF']

    AnnotationData = [
    'CHROM_x', 'POS_x','REF', 'ALT',  'GENE', 'HugoSymbol', 'Variant', 
    'RSID','CLNSIG', 'EFFECT', 'CLNDISEASE'
    ]

    SinkCols = AfricanPops+AnnotationData

    # with open(SINKDATA, 'rb') as datafile:
    dfSink = pd.read_pickle(SINKDATA)

    # Add protein mapping
    dfSink["Protein"] = dfSink.GENE.apply(lambda x: DictGeneProt.get(x))

    # Calculate mean frequencies
    dfSink["AfrMeanFreq"] = dfSink.loc[:, AfricanPops].mean(axis=1)
    dfSink["EurMeanFreq"] = dfSink.loc[:, EuroPops].mean(axis=1)

    df_freq_annot = annotate_genes(dfSink, RankProteins+["P56693","O95696"])

    print(df_freq_annot.sort_values(["AfrMeanFreq"], ascending=False).reset_index().drop(["index"], axis=1).head())

    # print(df_freq_annot.loc[:, ["GENE", "Protein", "RSID"]+AfricanPops].sort_values(["AfrMeanFreq"], ascending=False))

    print(RankProteins)

    # print(dfsink.loc[:, AnnotationData+["Protein"]+AfricanPops].head())

    # print(dfsink.tail(40))

    # print(dfsink.columns)

    yri = PopulationFrequency('YRI_MAF', 0.3)
    lwk = PopulationFrequency('LWK_MAF', 0.02)
    zulu = PopulationFrequency('ZULU_MAF', 0.1)

    gene1 = Gene("P53",[yri, lwk, zulu])
    print(gene1)

if __name__ == '__main__':
    main()