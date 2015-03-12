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
    print(gpe_min, min_capa, gpe_max, max_capa)
    return(gpe_min, gpe_max)


def find_serveur_pos(serveurs, s_id):
    position = 0
    for pos, s in enumerate(serveurs):
        if s[0] == s_id:
            position = pos
    return position


if __name__ == "__main__":
    P = 45
    R = 16
    M = 625
    # serveurs = [(1,1,1,2,0),(0,3,2,0,0),(0,3,3,1,0)]
    serveurs = getPlacedServers()
    groupes, serveurs_sorted_by_capacite = get_groupe_ordonnancement(serveurs, P, R, M)

    for i in range(10):
        print(capa_garantie(groupes))
        groupe_min_id, groupe_max_id = order_groupes_by_capa(groupes)

        serveur_to_add = groupes[groupe_max_id][0][-2]
        serveur_position = find_serveur_pos(serveurs, serveur_to_add)
        remove_from_group(groupes, serveurs, groupe_max_id, serveurs[serveur_position], serveur_position)
        add_in_group(groupes, serveurs, groupe_min_id, serveurs[serveur_position], serveur_position)

