import random
import functions


userValue = 0
counter = 0
value = int(random.randint(1,100))

while userValue != value:
    counter += 1
    userValue = functions.getDataFromUser()
    if userValue == value:
        print("Gratulacje wygrales! Potrzebowałeś do tego: ", counter)
        exit()
    elif userValue < value:
        print("Twoja wartość jest mniejsza niż wylosowana")
    elif userValue > value:
        print("Twoja wartość jest większa niż wylosowana")
    


