def createIndex():
    return{}

def recordBook(index, isbn, title):
    index[isbn] = title

def findBook(index, isbn):
    try:
        return index[isbn]
    except:
        return ""

def listBooks(index):
    strings = []
    i = 0
    for key in index:
        i += 1
        strings.append(str(i) + ") " + key + ": " + index[key])
    return strings

def formatMenu():
    return ['What would you like to do?', '[r] Record a Book', '[f] Find a Book', '[l] List a Book', '[q] Quit']

def formatMenuPrompt():
        return "Enter an option: "

def getUserChoice(prompt):
    text = input(prompt)
    while text.strip() == "":
        text = input(prompt)
    return text.strip()

def getISBN():
    isbn = getUserChoice("Enter a ISBN: ")
    return isbn

def getTitle():
    title = getUserChoice("Enter a title: ")
    return title

def recordBookAction(index):
    isbn = getISBN()
    title = getTitle()
    recordBook(index, isbn, title)

def findBookAction(index):
    isbn = getISBN()
    foundbook = findBook(index, isbn)
    if foundbook != "":
        print("Book found: " + foundbook)
    else:
        print("Book not found")

def listBooksAction(index):
    books = listBooks(index)
    if len(books) > 0:
        for book in books:
            print(book)
    else:
        print("No books listed")


def quitAction(index):
    import sys
    print("Goodbye")
    sys.exit(0)

def applyAction(index, choice):
    if choice == "r":
        recordBookAction(index)
    elif choice == "f":
        findBookAction(index)
    elif choice == "l":
        listBooksAction(index)
    elif choice == "q":
        quitAction(index)
    else:
        print("Invalid input")

def main():
    index = createIndex()

    while True:
        menu = formatMenu()
        for item in menu:
            print(item)
        choice = getUserChoice(formatMenuPrompt())
        print()
        applyAction(index, choice)
        print()


if __name__ == '__main__':
    main()

