import sys

def milesPerGallon( miles, gallons ):
    if gallons == 0:
        return 0
    else:
        return miles/ gallons

def createNotebook():
    return []


def recordTrip( notebook, date, miles, gallons ):
    newTrip = {'date': date, 'miles': miles, 'gallons': gallons}
    notebook.append(newTrip)


def listTrips( notebook ):
    list = []
    for item in notebook:
        trip = 'On {0}: {1} miles traveled using {2} gallons. Gas mileage: {3} MPG'\
            .format(item['date'], item['miles'], item['gallons'], milesPerGallon(item['miles'], item['gallons']))
        list.append(trip)
    return list


def calculateMPG( notebook ):
    if len(notebook) < 1:
        return 0.0
    else:
        miles = 0
        gallons = 0
        for item in notebook:
            miles += item['miles']
            gallons += item['gallons']
    return milesPerGallon(miles, gallons)


def formatMenu():
    return ['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[c]Calculate Gas', '[q] Quit']


def formatMenuPrompt():
    return 'Enter an option: '


def getUserString( prompt ):
    response = ''
    while response == '':
        response = input(prompt)
        response = response.strip()
    return response



def getUserFloat(prompt):
    keepLooking = True
    while keepLooking:
        numIn = input(prompt)
        #if len(numIn) > 0:
        try:
            x = float(numIn)
            if x > 0:
                keepLooking = False
        except ValueError:
            continue
    return x


def getDate():
    return getUserString('date: ')


def getMiles():
    return getUserFloat('miles: ')


def getGallons():
    return getUserFloat('gallons: ')


def recordTripAction(notebook):
    date = getDate()
    miles = getMiles()
    gallons = getGallons()
    recordTrip(notebook, date, miles, gallons)
    print('You have successfully uploaded a trip')


def listTripsAction(notebook):
    trips = listTrips(notebook)
    if len(trips) < 1:
        print('No trips have been recorded')
    else:
        for trip in trips:
            print(trip)


def calculateMPGAction(notebook):
    MPG = calculateMPG(notebook)
    if MPG == 0:
        print('No trips have been recorded')
    else:
        print(f'average gas mileage: {MPG} MPG')


def quitAction(notebook):
    print('Thank you for using the gas mileage program')
    sys.exit(0)


def applyAction(notebook, action):
    if action == 'r':
        recordTripAction(notebook)
    elif action == 'l':
        listTripsAction(notebook)
    elif action == 'c':
        calculateMPGAction(notebook)
    elif action == 'q':
        quitAction(notebook)
    else:
        print('You need to enter a valid option')


def main():
    book = createNotebook()
    userOption = 'select'
    while userOption != 'q':
        menu = formatMenu()
        for option in menu:
            print(option)
        userOption = input(formatMenuPrompt())
        applyAction(book, userOption)
        print()

if __name__ == '__main__':
    main()
