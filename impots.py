#Salut, ca va?
def calculer_mes_impots(mon_revenu):
    taux = 0
    if mon_revenu > 11497 and mon_revenu <= 29315:
        taux= 0.11
    elif mon_revenu > 19315 and mon_revenu <= 83823:
        taux= 0.30
    elif mon_revenu > 83823 and mon_revenu < 180294:
        taux = 0.41
    elif mon_revenu > 180294:
        taux = 0.45
    return mon_revenu*taux