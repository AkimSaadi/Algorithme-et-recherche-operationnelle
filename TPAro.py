from collections import deque
class Objet :
    def __init__ (self,poids,valeur) :
        self.poids = poids;
        self.valeur = valeur

          
class Noeud :
        def __init__(self,profondeur,x,valeur,poids) :
            self.profondeur = profondeur
            self.x = x
            self.enfant_gauche = None
            self.enfant_droit = None
            self.borne_sup = self.calcul_borne_sup()
            self.valeur = valeur
            self.poids = poids
        
        def insert_gauche (self) :
            self.enfant_gauche = Noeud (self.profondeur+1,self.x,self.valeur,self.poids)
            
        def insert_droit(self) :
            new_liste = (self.x).copy()
            new_liste[self.profondeur+1]=1
            new_valeur = self.valeur+liste_objet[self.profondeur+1].valeur
            new_poids = self.poids+liste_objet[self.profondeur+1].poids
            self.enfant_droit = Noeud (self.profondeur+1,new_liste,new_valeur,new_poids)
        
        def calcul_borne_sup(self) :
            total_valeur = 0
            total_poids = 0
            temp = 0
            for i in range (nombre_objet) :
                if i < self.profondeur :
                    if temp < capacite :
                        total_valeur += liste_objet[i].valeur * self.x[i]
                        total_poids += liste_objet[i].poids * self.x[i]
                        if i < (nombre_objet-1) :
                            temp = total_poids+liste_objet[i+1].poids * self.x[i+1]
                    else :
                        fragment = capacite-total_poids
                        total_valeur += (liste_objet[i].valeur * self.x[i] /liste_objet[i].poids )*(fragment)
                        total_poids += fragment
                        temp = total_poids
                else :
                    if temp < capacite :
                        total_valeur += liste_objet[i].valeur
                        total_poids += liste_objet[i].poids
                        if i < (nombre_objet-1) :
                            temp = total_poids+liste_objet[i+1].poids
                    else :
                        fragment = capacite-total_poids
                        total_valeur += (liste_objet[i].valeur   /liste_objet[i].poids )*(fragment)
                        total_poids += fragment
                        temp = total_poids
            return total_valeur
        def print(self) :
            print('Profondeur = {}\nListe = {}\nEnfant de gauche = {}\nEnfant de droite = {}\nBorne_sup = {}\nValeur = {}\nPoids = {}\n'.format(self.profondeur,self.x,self.enfant_gauche,self.enfant_droit,self.borne_sup,self.valeur,self.poids))
        
        
print("Quel sac voulez-vous ? 0, 1, 2, 3 ou 4 ?")
numero_sac = int(input())

if numero_sac > 4 :
    numero_sac = 0


fichier = open('sac'+str(numero_sac)+'.txt', "r")
liste = fichier.read().split('\n')
fichier.close()
liste_objet = list()


for element in liste :
    if element != liste[0] and element != '':
        element = element.strip("\n\r").split(' ')
        liste_objet.append(Objet((int)(element[0]),(int)(element[1])))
    elif element == liste[0]:
        capacite = (int)(liste[0])
nombre_objet = len(liste_objet)       
liste_objet.sort(key=lambda objet : objet.valeur/objet.poids,reverse=True)     

def init_prendre_objet (prendre_objet) :
    for i in range (nombre_objet) :
        prendre_objet.append(0)

def decision ():
    max_profit = 0
    queue = deque()
    prendre_objet = list()
    init_prendre_objet (prendre_objet)
    racine = Noeud(-1,prendre_objet,0,0)
    queue.append(racine)
    while(len(queue)) :
        noeud_courant = queue.pop()
        if (noeud_courant.profondeur != nombre_objet-1) :
            noeud_courant.insert_gauche()
            noeud_courant.insert_droit()
            if ((noeud_courant.enfant_droit.poids<=capacite) and (noeud_courant.enfant_droit.valeur > max_profit)) :
                max_profit = noeud_courant.enfant_droit.valeur
                noeud_solution = noeud_courant.enfant_droit
            if noeud_courant.enfant_droit.borne_sup >= max_profit:
                queue.append(noeud_courant.enfant_droit)
            if noeud_courant.enfant_gauche.borne_sup >= max_profit :
                queue.append(noeud_courant.enfant_gauche)
    return noeud_solution

solution = decision()
print('La solution au problème pour le sac {} est de prendre les objets {}\npour un poids de {} inférieur à {} et une valeur de {}.'.format(numero_sac,solution.x,solution.poids,capacite,solution.valeur))