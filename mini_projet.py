dic = {
    'Marseille': {
    'Nîmes' : 122,
    'Ajaccio' : 521,
    'Paris' : 773,
    'Perpignan' : 317,
    'Annecy' : 421,
    'Besançon' : 564,
    'Toulouse' : 403,
    'Toulon' : 122
    },

    'Nîmes':{
    'Ajaccio' : 605,
    'Paris' : 711,
    'Perpignan' : 203, 
    'Annecy' : 359,
    'Besançon' : 502, 
    'Toulouse' : 290,
    'Toulon' : 190
    },

    'Ajaccio':{
    'Paris' : 1253,
    'Perpignan' : 797, 
    'Annecy' : 901,
    'Besançon' : 1044,
    'Toulouse' : 883,
    'Toulon' : 471
    },

    'Paris': {
    'Perpignan' : 846,
    'Annecy' : 538,
    'Besançon' : 412,
    'Toulouse' : 676,
    'Toulon' : 838
    },

    'Perpignan': {
    'Annecy' :560,
    'Besançon' : 703,
    'Toulouse' : 207,
    'Toulon' : 383 
    },

    'Annecy': {
    'Besançon' : 215,
    'Toulouse' : 646,
    'Toulon' : 487 
    },

    'Besançon': {
    'Toulouse' : 707,
    'Toulon' :627
    },

    'Toulouse': {
    'Toulon' : 468
    }
}

def theGODfunction(vroomvroom):
    def accel(temps_distance_fait):
        temps = temps_distance_fait[0]
        distance_fait = temps_distance_fait[1]
        vitesse = 0
        while vitesse < 90:
            temps += 1
            vitesse += 10
            tempsheure = 1 / 60
            distance_fait += (tempsheure * vitesse)
        temps_distance_fait[0] = temps
        temps_distance_fait[1] = distance_fait
        return temps_distance_fait


    def frein(temps_distance_fait):
        temps = temps_distance_fait[0]
        distance_fait = temps_distance_fait[1]
        vitesse = 90
        while vitesse > 0:
            temps += 1
            tempsheure = 1 / 60
            distance_fait += (tempsheure * vitesse)
            vitesse -= 10
        temps_distance_fait[0] = temps
        temps_distance_fait[1] = distance_fait
        return temps_distance_fait


    def pause(temps_distance_fait):
        frein(temps_distance_fait)
        temps_distance_fait[0] += 15 #le temps de prendre un petit café
        accel(temps_distance_fait)
        return temps_distance_fait

    def roulerposer(temps_distance_fait):
        temps = temps_distance_fait[0]
        distance_fait = temps_distance_fait[1]
        temps += (1/10)
        tempsheure = ((1 / 60) / 10)
        distance_fait += (tempsheure * 90)
        temps_distance_fait[0] = temps
        temps_distance_fait[1] = distance_fait
        return temps_distance_fait

    vitesse = 0
    temps = 0
    distance_fait = 0
    distance = vroomvroom
    temps_avant_pause = 0
    temps_distance_fait = [0,0]
    arret = [0,0]
    arret = frein(arret)


    while True:

        if vitesse == 0:
            accel(temps_distance_fait)
            vitesse = 90
        if temps_avant_pause >= 111:
            pause(temps_distance_fait)
            vitesse = 90
            temps_avant_pause = 0
        if distance - temps_distance_fait[1] <= arret[1]:
            frein(temps_distance_fait)
            break
        
        temps_avant_pause += (1/10)
        roulerposer(temps_distance_fait)
    
    return temps_distance_fait


nbvilles = input('Combien de livraison ton camion doit-il faire ? Une, deux ou trois ? (Marque ton chiffre sous le format numérique): ')


if nbvilles == '1':
    ville1 = input('Ville de départ: ')
    ville2 = input('Ville d\'arriver: ')
    try:
        nbkil = dic[ville2][ville1]
    except KeyError:
        nbkil = dic[ville1][ville2]

    result = theGODfunction(nbkil)
    print('Vôtre ville de départ est ' + ville1)
    print('Vôtre ville de d\'arriver est ' + ville2)
    print('Vous avez parcouru la distance de ' + str(result[1]) + ' Km')
    print('Ce trajet vous à pris ' + str(result[0]) + ' Minutes')

elif nbvilles == '2':
    ville1 = input('Ville de départ: ')
    ville2 = input('Ville pour la première livraison: ')
    ville3 = input('Ville pour la denière livraison: ')

    try:
        nbkil = dic[ville2][ville1]
    except KeyError:
        nbkil = dic[ville1][ville2]
    try:
        nbkil = dic[ville2][ville3]
    except KeyError:
        nbkil = dic[ville3][ville2]
    
elif nbvilles == '3':
    ville1 = input('Ville de départ: ')
    ville2 = input('Ville pour la première livraison: ')
    ville3 = input('Ville pour la seconde livraison: ')
    ville4 = input('Ville pour la dernière livraison: ')

    try:
        nbkil = dic[ville2][ville1]
    except KeyError:
        nbkil = dic[ville1][ville2]
    result = theGODfunction(nbkil)
    print('Vous avez parcouru la distance de ' + str(result[1]) + ' Km')

    try:
        nbkil = dic[ville2][ville3]
    except KeyError:
        nbkil = dic[ville3][ville2]
    result = theGODfunction(nbkil)
    print('Vous avez parcouru la distance de ' + str(result[1]) + ' Km')


    try:
        nbkil = dic[ville4][ville3]
    except KeyError:
        nbkil = dic[ville3][ville4]
    result = theGODfunction(nbkil)
    print('Vous avez parcouru la distance de ' + str(result[1]) + ' Km')


else:
    print('Tu tes trompé dans tes valeurs !')
  



    




 



