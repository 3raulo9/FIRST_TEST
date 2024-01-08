
def myzip(it1, it2):
    return [(it1[i], it2[i]) for i in range(min(len(it1), len(it2)))]
