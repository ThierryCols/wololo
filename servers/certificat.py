
from capacite_garantie import capacite_garantie


forbiddenPlaces = [(10,23),(0,40),(4,40),(3,57),(11,78),(10,82),(14,27),(1,39),(6,75),(0,47),(3,49),(8,8),(0,42),(3,18),(10,39),(8,71),(3,52),(9,42),(12,95),(0,10),(12,89),(11,17),(5,44),(2,48),(15,31),(5,38),(1,48),(1,54),(13,55),(9,65),(12,91),(11,67),(8,57),(15,56),(6,5),(8,83),(13,27),(9,89),(13,78),(9,23),(11,27),(0,73),(3,64),(4,63),(1,27),(3,72),(1,61),(4,44),(10,17),(5,83),(5,92),(3,35),(4,27),(14,98),(10,36),(9,74),(2,73),(11,66),(2,61),(6,7),(15,83),(8,91),(10,95),(13,48),(12,41),(3,66),(0,51),(5,4),(4,28),(3,37),(15,8),(14,2),(5,3),(10,48),(6,33),(14,63),(7,34),(4,23),(3,94),(8,98)];

def verify_position(serveurs):
    forbidden = forbidden_rangee()
    for rangee in range(16):
        sum_rangee = 0
        for serveur in serveurs:
            if serveur[3] == rangee:
                sum_rangee += serveur[1]
        sum_rangee += forbidden[rangee]
        if sum_rangee > 100:
            print("rangee "+rangee+" excède 100")


def forbidden_rangee():
    forbidden = []
    for place in forbiddenPlaces:
        forbidden[place[0]] += place[1]
    return forbidden


