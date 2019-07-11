import caloric_balance, sys

# activity_chart = {
#    'j' = .074,
#    'r' = .087,
#    's' = .009,
#    'w' = .036
# }

def formatMenu():
    return [
    'What would you like to do?', 
    '[f] Record Food Consumption',
    '[a] Record Physical Activity',
    '[q] Quit']

def formatMenuPrompt():
    return 'Enter an option: '

def formatActivityMenu():
    return[
    'Choose an activity to record',
    '[j] Jump rope',
    '[r] Running',
    '[s] Sitting',
    '[w] Walking']

def getUserString(prompt):
    response = ''
    while response == '':
        response = input(prompt)
        response =  response.strip()
    return response

def getUserFloat(prompt):
    while True:
        try:
            UserFloat = float(input(prompt))
            if UserFloat > 0.0:
                return UserFloat
            else:
                print('Error, please enter a float > 0.0')
        except:
            print('Error, please enter a float > 0.0')

def createCaloricBalance():
    gender = getUserString('Are you Male or Female? ')
    age = getUserFloat('How old are you? ')
    height = getUserFloat('How tall are you in inches? ')
    weight = getUserFloat('How much do you weight? ')
    CB = caloric_balance.CaloricBalance(gender, age, height, weight)
    return CB

def recordActivityAction(CaloricBalance):
    CB = CaloricBalance
    for option in formatActivityMenu():
        print(option)

    UserIn = getUserString("Enter an option: ")

    if UserIn == 'j':
        minutes = getUserFloat('for how many minutes did you perform this activity? ')
        CB.recordActivity(.074 ,minutes)
        print('Awesome, you caloric balance is now ', str(CB.getBalance() ) )

    elif UserIn == 'r':
        minutes = getUserFloat('for how many minutes did you perform this activity? ')
        CB.recordActivity(.087 ,minutes)
        print('Awesome, you caloric balance is now ', str(CB.getBalance() ) ) 

    elif UserIn == 's':
        minutes = getUserFloat('for how many minutes did you perform this activity? ')
        CB.recordActivity(.009 ,minutes)
        print('Awesome, you caloric balance is now ', str(CB.getBalance() ) ) 

    elif UserIn == 'w':
        minutes = getUserFloat('for how many minutes did you perform this activity? ')
        CB.recordActivity(.036 ,minutes)
        print('Awesome, you caloric balance is now ', str(CB.getBalance() ) )
        
    else:
        print('you need to enter a valid option')

def eatFoodAction(caloric_balance):
    CB = caloric_balance
    calories = getUserFloat('How many calories did you just eat? ')
    CB.eatFood(calories)
    print('Sweet, your caloric balance is now ', str(CB.getBalance()))

def quitAction(caloric_balance):
    print('Leaving? You should do this again tomorrow. Stay healthy!')
    sys.exit( 0 )

def applyAction(caloric_balance, choice):
    if choice == 'f':
        eatFoodAction(caloric_balance)
    
    elif choice == 'a':
        recordActivityAction(caloric_balance)

    elif choice == 'q':
        quitAction(caloric_balance)

    else:
        print('Sorry, that option is invalid.')

def Welcome():
    print('''Hi! This program will calculate your caloric balance for the day! 
Before we can start, I need some information about you. Be honest! :)''' + '\n')

def main():
    Welcome()
    x = createCaloricBalance()
    print('Your caloric balance for the day is: ', x.balance)
    menu = formatMenu()
    UserIn = formatMenuPrompt()
    while True:
        print(menu)
        l = input(UserIn)
        applyAction(x, l)


if __name__ == '__main__':
    main()
