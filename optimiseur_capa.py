# -*- coding: utf-8 -*-

from capacite_garantie import *


def order_groupes_by_capa(groupes):
    min_capa = 10000
    gpe_min = -1
    max_capa = 0
    gpe_max = -1
    for groupe_id, groupe in enumerate(groupes):
        m = capa(groupe)
        if m > max_capa:
            max_capa = m
            gpe_max = groupe_id
        elif m < min_capa:
            min_capa = m
            gpe_min = groupe_id

    return(gpe_min, gpe_max)

if __name__ == "__main__":
    P = 45
    R = 16
    M = 625
    # serveurs = [(1,1,1,2,0),(0,3,2,0,0),(0,3,3,1,0)]
    serveurs = getPlacedServers()
    groupes, serveurs_sorted_by_capacite = get_groupe_ordonnancement(serveurs, P, R, M)

    for i in range(10):
        groupe_min_id, groupe_max_id = order_groupes_by_capa(groupes)

        serveur_to_add = groupe_max[0][-1]
        remove_from_groupe(groupes, serveurs, groupe_max_id, serveur)



