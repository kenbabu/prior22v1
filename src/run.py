
from lib import *
from commands import *
# from semantic import best_match_avg2

import utility as ut
import semantic
import vectorsim
import prior
import loaddata
import ontologyprocess as op
import rank 




# print(f"'GO:0120132', 'GO:0097190': {sim2}")

from prior import  DictProtUniversalData


def main():
    from semantic import best_match_avg2
    """Run PrIOR """
    score = ut.naive_score(0.4,0.6)
    # sim = op.general_universal(['P14222'], ['Q96KN2'], **DictProtUniversalData)
    sim = op.general_universal('GO:0003089', 'GO:0033377', GOParents, GOTopos)

    sim_go = prior.go_similarity_score(['P14222'], ['Q96KN2'], **DictProtUniversalData)
    print(f'Score: {score}\nSemantic similarity {sim_go}')



    cli()

if __name__ =="__main__":
    main()