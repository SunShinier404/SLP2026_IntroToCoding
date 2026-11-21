def main():
    while True:
        print("QUIZ TIME! (type 'quit' to exit)")
        
        print("QUESTION 1: What is the first letter of the alphabet? ")
        print("A) A")
        print("B) B")
        print("C) C")
        print("D) D")

        user_input = input("Your answer: ")
        
        if user_input.lower() == "quit":
            print("Exiting quiz...")
            break
        elif user_input.lower() == "a":
            print("Correct! The first letter of the alphabet is A.")
            break
        else:
            print("Incorrect. Try again or type 'quit' to exit.")

if __name__ == "__main__":
    main()