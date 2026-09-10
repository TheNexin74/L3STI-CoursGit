unites ={'mg':0.001,'cg':0.01,'dg':0.1,'g':1,'dag':10,'hg':100,'kg':1000}
def conversion_masse(masse,unite_dep,unite_arr):
    if unite_dep or unite_arr not in unites:
        return "Erreur"
    masse_g=masse*unites[unite_dep]
    return masse_g/unites[unite_arr]