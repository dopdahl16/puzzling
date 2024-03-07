def pointsAwarded(place):
    if place == 1:
        return 15
    if place == 2:
        return 12
    else:
        return 13 - place
    

for x in range (1, 13):
    print(pointsAwarded(x))