# -*- coding: utf-8 -*-


def select_groupe(groupes):
    return capa_garantie(groupes)[1]


def capa_garantie(groupes):
    capa_garantie = 100000
    groupe_choisi = - 1
    for groupe_id, groupe in enumerate(groupes):
        capa_min_groupe = capa(groupe)
        if capa_min_groupe < capa_garantie:
            capa_garantie = capa_min_groupe
            groupe_choisi = groupe_id
    return groupe_choisi, capa_garantie


def capa(groupe):
    rangees_capacites = groupe[1]
    rangee_max = max(rangees_capacites)
    capa_min_groupe = sum(rangees_capacites) - rangee_max
    return capa_min_groupe

