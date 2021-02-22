"""
The idea is to simply find the city that we enter with the least
amount of gas overall. There is guaranteed to be such a city,
and it is guaranteed that the gas amount will be minimal.

This will be the case if we travel there from ANY city and means we can't
reach this city if we start from other cities, therefore it must be the city
we have to start at because if we start there, we can get back there and if we get back there,
we were able to reach ALL of the other cities.
"""


def validStartingCity(distances, fuel, mpg):
    miles = min_gas = min_city = 0
# keep track of miles we have left in car when entering a city
    for city in range(1, len(distances)):
        # miles left when entering city is equal to the number of miles
        # we started w/ prior to departure, plus amount we filled before leaving,
        # less miles needed to travel
        miles += (mpg * fuel[city - 1]) - distances[city - 1]
        if miles < min_gas:
            min_gas = miles
            min_city = city
    return min_city
