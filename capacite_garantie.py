# -*- coding: utf-8 -*-

P = 45
R = 16

serveurs = [(1,1,1,2,0),(0,3,2,0,0)]
groupes = [([],[0 for i in range(R)]) for i in range(P)]

serveurs_sorted_by_capacite = sorted(serveurs,key=lambda s:-s[2])

def add_in_group(groupes, g, s):
    groupes[g][0].append(s[0]) # ajoute l id du serveur a la liste des serveurs du groupe
    groupes[g][1][s[3]]+=s[2] # ajoute la capacite dans la liste des caoacites par rangees

def select_groupe(groupes,s):
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

if __name__ == "__main__":
    for s in serveurs_sorted_by_capacite:
        g = select_group(groupes,s)
        add_in_group(groupes, g, s)

