import random 
def printCar(cars):
    randomCar = random.choice(cars)
    print(randomCar)
def printYear(years):
    randomYear = random.choice(years)
    print(randomYear)
        

carList = ["Ford", "Nissan", "Toyota"]
yearList = [2005,2023,2021]
printCar(carList)
printYear(yearList)
