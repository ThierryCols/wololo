# -*- coding: utf-8 -*-

from placement import *

def get_serveurs_updated(serveurs_sorted_by_capacite):
    serveurs_updated = add_missing_serveur(serveurs_sorted_by_capacite, M)
    return serveurs_updated

def get_groupe_ordonnancement(serveurs, P, R, M):
    groupes = [([],[0 for i in range(R)]) for i in range(P)]
    serveurs_sorted_by_capacite = sorted(serveurs,key=lambda s:-s[2])
    for i, s in enumerate(serveurs_sorted_by_capacite):
        g = select_group(groupes,s)
        add_in_group(groupes, serveurs_sorted_by_capacite, g, s, i)
    print(capa_garantie(groupes))
    return groupes, serveurs_sorted_by_capacite


def add_in_group(groupes, serveurs, g, s, i):
    groupes[g][0].append(s[0]) # ajoute l id du serveur a la liste des serveurs du groupe
    groupes[g][1][s[3]]+=s[2] # ajoute la capacite dans la liste des caoacites par rangees
    serveurs[i] = (s[0],s[1],s[2],s[3],s[4],g) # ajoute le groupe au tuple representant le serveur

def remove_from_group(groups, serveurs, g, s, i):
    groups[g][0].remove(s[0]) # enleve l id du serveur de la liste des serveurs du groupe
    groups[g][1][s[3]]-=s[2] # enleve la capacite de la liste des capacites par rangees
    serveurs[i] = (s[0],s[1],s[2],s[3],s[4],-1) # enleve le groupe du tuple representant le serveur

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
        if s[5]<0:
            print("x")
        else:
            print(str(s[3])+" "+str(s[4])+" "+str(s[5]))

def save_results_in_file(serveurs, filename):
    with open(filename,"w") as file:
        for s in serveurs:
            if s[5]<0:
                file.write("x\n")
            else:
                file.write(str(s[3])+" "+str(s[4])+" "+str(s[5])+"\n")

def add_missing_serveur(serveurs, M):
    serveurs_with_missings = [(-1,-1,-1,-1,-1,-1) for i in range(M)]
    for s in serveurs:
        serveurs_with_missings[s[0]]=s
    return serveurs_with_missings

if __name__ == "__main__":
    P = 45
    R = 16
    M = 625
    # serveurs = [(1,1,1,2,0),(0,3,2,0,0),(0,3,3,1,0)]
    serveurs = getPlacedServers()
    groupes, serveurs_sorted_by_capacite = get_groupe_ordonnancement(serveurs, P, R, M)
    serveurs_updated = get_serveurs_updated(serveurs_sorted_by_capacite)
    # affiche_resultat(serveurs_updated)
    save_results_in_file(serveurs_updated,"resultats.txt")


