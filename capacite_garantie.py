# -*- coding: utf-8 -*-

def add_in_group(groupes, serveurs, g, s, i):
    groupes[g][0].append(s[0]) # ajoute l id du serveur a la liste des serveurs du groupe
    groupes[g][1][s[3]]+=s[2] # ajoute la capacite dans la liste des caoacites par rangees
    serveurs[i] = (s[0],s[1],s[2],s[3],s[4],g) # ajoute le groupe au tuple representant le serveur

def select_group(groupes,s):
    return capa_garantie(groupes)[0]


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

def affiche_resultat(serveurs):
    for s in serveurs:
        print(str(s[3])+" "+str(s[4])+" "+str(s[5]))

if __name__ == "__main__":
    P = 2
    R = 5
    serveurs = [(1,1,1,2,0),(0,3,2,0,0),(0,3,3,1,0)]
    groupes = [([],[0 for i in range(R)]) for i in range(P)]
    serveurs_sorted_by_capacite = sorted(serveurs,key=lambda s:-s[2])

    for i, s in enumerate(serveurs_sorted_by_capacite):
        g = select_group(groupes,s)
        add_in_group(groupes, serveurs_sorted_by_capacite, g, s, i)
    serveurs = sorted(serveurs_sorted_by_capacite,key=lambda s:s[0])
    affiche_resultat(serveurs)


