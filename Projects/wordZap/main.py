from player import Player

def getInputInt(string):
    while True:
        try:
            number = int(input(string))
            if number > 1:
                return number

            print("Please enter a value that is greater than zero.")

        except:
            print("Please enter a number.")

def main():
    players = []

    playerCount = getInputInt("How many players are going to be playing? ")
    for i in range(playerCount):
        players.append(
            Player(
                input("Enter the name of player #" + str(i+1) + " ")
            )
        )
    
    print("\nGreat! Now we can play!\n")
    
    while True:
        for player in players:
            print(player.getName() + ", it is your turn!")
            print("Your letters are: " + player.printLetters())

            word = input("Enter a word to play (or press enter to pass) ")
            if len(word) == 0:
                print(
                    "You get another letter, \"" +
                    player.drawLetter() +
                    "\"!"
                )

            else:
                player.checkWord(word)

            print("Great job!\n")

            if len(player.getLetters()) == 0:
                print(player.getName() + " wins!!")
                return

if __name__ == "__main__":
    main()