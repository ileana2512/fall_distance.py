# Author: Ileana Hernandez
# Date: 01/27/2021
# Description: determine the distance an object falls due to gravity

def fall_distance(time):
    """takes the time in seconds that an object falls and returns the distance"""
    return 0.5 * 9.8 * time **2

time = 3.2
print("The distance the object has fallen is", fall_distance(time))
