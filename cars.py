import random 
def printCar(cars):
    randomCar = random.choice(cars)
    print(randomCar)
        

carList = ["Ford", "Nissan", "Toyota"]
printCar(carList)
