P = 45
R = 16

serveurs = [(1,1,1,2,0),(0,3,2,0,0)]
groupes = [([],[0 for i in range(R)]) for i in range(P)]

serveurs_sorted_by_capacite = sorted(serveurs,key=lambda s:-s[2])

for s in serveurs_sorted_by_capacite:
	g = select_group(groupes, s)
	add_in_group(groupes, g, s)

def add_in_group(groupes, g, s):
	groupes[g][0].append(s) # ajoute le serveur a la liste des serveurs du groupe
	groupes[g][1][s[3]]+=s[2] # ajoute la capacite dans la liste des caoacites par rangees