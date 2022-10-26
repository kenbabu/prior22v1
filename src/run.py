
from lib import *
from commands import *

import utility as ut
import semantic
import vectorsim
import prior
import loaddata
import ontologyprocess as op
import rank 




# print(f"'GO:0120132', 'GO:0097190': {sim2}")


def main():
    """Run PrIOR """
    score = ut.naive_score(0.4,0.6)
    sim = op.general_universal('GO:0120132', 'GO:0097190', GOParentsLevels, GOTopos)
    print(f'Score: {score}\nSemantic similarity {sim}')


    cli()

if __name__ =="__main__":
    main()