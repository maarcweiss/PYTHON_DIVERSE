count = 0

# options for the game
first_option = [
    "a  = Constant Penus Upgrade",
    "b = Carrot Pumpkin Ultragood",
    "c = Central Processing Unit",
]

second_option = [
    "a = Marc Weiss",
    "b = You, the player",
    "c = Please follow me on Github!",
]

third_option = ["a = Oslo", "b = Finnland", "c= Sweden"]

# all the code that contains the game
def play():
    global count
    # question one
    while True:
        print(
            "*********************************************************************************"
        )
        print(
            "First question: !!!!!ONLY ANSWER WITH THE LETTER, OTHERWISE IT WON'T WORK!!!!!!!"
        )
        print(
            "------------------------------------------------------------------------------------"
        )
        print("1-. What stands for CPU?")
        answer1 = input(first_option)
        if answer1 == ("a").lower():
            print("Incorrect!")
            print("You currently have {} guesses".format(count))
            break
        elif answer1 == ("b").lower():
            print("Incorrect!")
            print("You currently have {} guesses".format(count))
            break
        elif answer1 == ("c").lower():
            print("Correct!")
            count += 1
            print("You currently have {} guesses".format(count))
            break
        else:
            print(
                "*********************************************************************************"
            )
            print("Select an option that does exist")
            continue
        # question two
    while True:
        print(
            "------------------------------------------------------------------------------------"
        )
        print(
            "Second question: !!!!!ONLY ANSWER WITH THE LETTER, OTHERWISE IT WON'T WORK!!!!!!!"
        )
        print(
            "------------------------------------------------------------------------------------"
        )
        print("2-. Who is the best programmer in the world")
        answer2 = input(second_option)
        if answer2 == ("a").lower():
            print("Incorrect!")
            print("You currently have {} guesses".format(count))
            break
        elif answer2 == ("b").lower():
            print("Incorrect!")
            print("You currently have {} guesses".format(count))
            break
        elif answer2 == ("c").lower():
            print("Correct, hope you followed me!")
            count += 1
            print("You currently have {} guesses".format(count))
            break
        else:
            print(
                "*********************************************************************************"
            )
            print("Select an option that does exist")
            continue

    # question three
    while True:
        print(
            "------------------------------------------------------------------------------------"
        )
        print(
            "Third question: !!!!!ONLY ANSWER WITH THE LETTER, OTHERWISE IT WON'T WORK!!!!!!!"
        )
        print(
            "------------------------------------------------------------------------------------"
        )
        print("3-. Whats the capital of Norway\n")
        answer3 = input(third_option)
        if answer3 == ("a").lower():
            print("Correct, you know basic Geography!")
            count += 1
            print("You finally have {} guesses".format(count))
            break
        elif answer3 == ("b").lower():
            print("Incorrect!")
            print("You finally have {} guesses".format(count))
            break
        elif answer3 == ("c").lower():
            print("Correct, hope you followed me!")
            print("Incorrect!")
            print("You finally have {} guesses".format(count))
            break
        else:
            print(
                "*********************************************************************************"
            )
            print("Select an option that does exist")
            continue

    print(
        "------------------------------------------------------------------------------------"
    )
    print("You have ended the quiz, I hope you have enjoyed the game")
    quit()


print("Wellcome to Marc's quiz game")

while True:
    playing = input("Do you want to play? ")
    if playing == "YES".lower():
        print("Perfect, let's start then!")
        play()

    elif playing == ("No").lower():
        print("Ok, next time then!")
        break

    else:
        print("You should type yes or no, idiot")
        print(
            "------------------------------------------------------------------------------------"
        )
        continue
