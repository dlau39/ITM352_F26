celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd", "Keanu Reeves", "Angelina Jolie")
ages = (36, 38, 36, 61, 50)

celebList = []
for celeb in celebs:
    celebList.append(celeb)

agesList = [age for age in ages]

celebsDict = {"celebs": celebList, "ages": agesList}
print(celebsDict)