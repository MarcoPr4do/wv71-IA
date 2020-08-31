import data

#   g(n): coste del camino desde el nodo inicio a n
#   h(n): coste estimado del camino mas barato desde n al objetivo
#   f(n): coste mas barato estimado de la solucion através de n
#   f(n) = g(n) + h(n)


def printTravel(init):
    wayTraveled = 0
    cityNow = init
    optionsUsed = []
    print(data.names[init])
    while cityNow != data.BUCHAREST:

        citySelected, distanceToTravel = getBestWay(
            cityNow, wayTraveled, optionsUsed)

        cityNow = citySelected
        wayTraveled = wayTraveled + distanceToTravel

        optionsUsed.append(citySelected)
        print(data.names[citySelected])


def isIntoArray(value, array):
    result = False
    for x in array:
        if x == value:
            result = True
    return result


def getBestWay(city, wayTraveled, optionsUsed):
    options = data.connects[city]
    min = 1000000
    citySelected = -1
    distanceToTravel = 0
    for optionCity, distanceToCity in options:
        if (isIntoArray(optionCity, optionsUsed) == False):
            g = distanceToCity + wayTraveled
            h = data.distanceToBucharest[optionCity]
            f = g + h
            if (min >= f):
                min = f
                citySelected = optionCity
                distanceToTravel = distanceToCity

    return {
        citySelected: citySelected,
        distanceToTravel: distanceToTravel
    }


printTravel(data.ZERIND)
