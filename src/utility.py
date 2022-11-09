from functools import reduce, wraps
import time

# Decorator for timining functions
def timer_func(myfunc):
    @wraps(myfunc)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = myfunc(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        print(f"Ran {myfunc.__name__!r} in {run_time:.2f} seconds")
        return result
    return wrapper


def naive_score(*args):
    scores = []
    for arg in args:
        scores.append(1.0-arg)
#     print(scores)
    return round(1-reduce(lambda x, y: (x*y), scores ),5)

# 

def create_non_redundant(lsterms,ont, ont_sub=None):
    try:
        ls_parents = list(filter(None,[ ont[t].rparents().id for t in lsterms]))
        ls_parents=list(chain(*ls_parents))+lsterms
#         return ls_parents
        if ont_sub:
            lsfiltered = list(set(ls_parents) & set(ont_sub))
            return lsfiltered
        else:
            return list(set(ls_parents))
    except KeyError as ke:
        pass
    
def get_prot_annot(prot, annot_dict):
    try:
        ls_prot = annot_dict.get(prot)
        return ls_prot
    except Exception as e:
        print(f"{e}")