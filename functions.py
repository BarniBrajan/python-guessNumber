def getDataFromUser():
    while True:  
        userValue = input("Podaj liczbę: ")
        try:
            value = int(userValue)
            return int(value)
            exit()
        except ValueError:
            print("Wprowadzona wartośc nie jest liczbą!")