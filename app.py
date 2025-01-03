

def trivia_quiz():
    largeStateChoice = input("Which state has the largest population?").lower()
    correctCount = 0

    if largeStateChoice in {"california", "cali", "ca"}:
        print("Correct!")
        correctCount += 1
    else:
        print("Incorrect")

    smallStateChoice = input("Which state has the smallest population?").lower()

    if smallStateChoice in {"wyoming", "wy"}:
        print("Correct!")
        correctCount += 1
    else:
        print("Incorrect")

    southStateChoice = input("Which state is the furthest south?").lower()
    if southStateChoice in {"hawaii", "hi"}:
        print("Correct!")
        correctCount += 1
    else:
        print("Incorrect")

    result = correctCount / 3 * 100

    print("Score: " + str(result) + "%")

    print("1. Yes")
    print("2. Exit")
    returnChoice = input("Return to main menu?")

    if returnChoice == 1:
        main_menu()
    elif returnChoice == 2:
        print("Goodbye!")
        exit()
    else:
        print("Invalid entry. Please try again")


def personality_quiz():
    print("Personality quiz building in process. Please try again later.")
    main_menu()


def main_menu():
    while True:
        print("\nQuiz App")
        print("1. State Trivia Quiz")
        print("2. Personality Quiz")
        print("3. Exit")
        choice = input("Select a quiz!")

        if choice == '1':
            trivia_quiz()
        elif choice == '2':
            personality_quiz()
        elif choice == '3':
            print("Goodbye!")
            exit()


def main():
    main_menu()


if __name__ == "__main__":
    main()