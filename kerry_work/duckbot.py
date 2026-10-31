from datetime import datetime
import random

def main():
    other_replies = ["quack quack (interesting)", "quack quack quack (i'm just a duck...)", 
                     "quackity quack (tell me more)", "\N{bread}?", "\N{skull}", 
                     "quuuuuuuuuuuuuuaaaaack", "quack (i see)", "quack (hmmm)"]

    
    print("\N{duck}: quack \n (hello i am a duck, type \'quit\' to exit)")

    while True:
        print("You: ", end="")
        user_input = input().lower()
        
        if user_input in ["quit", "exit", "bye"]:
            print("\N{duck}: quack quack (goodbye)")
            break
        elif any(msg in user_input for msg in ["hello", "hi", "hey"]):
            print("\N{duck}: quack (hello)")
        #elif user_input in ["how are you", "how's it going", "what's up", "how do you do"]:
        elif any(msg in user_input for msg in ["how are you", "how's it going", "what's up", "how do you do"]):
            print("\N{duck}: quack quack (all my ducks are in a row)")
        elif "help" in user_input:
            print("\N{duck}: quack quack (i'll do my best, i'm a good listener)")
        elif any(msg in user_input for msg in ["sad", ":(", "unhappy"]):
            print("\N{duck}: quack quuuack (i'm sorry to hear that)")
        elif any(msg in user_input for msg in ["happy", ":)", "glad", "excited", "!"]):
            print("\N{duck}: quack quack (happy for you)")
        elif "thank" in user_input:
            print("\N{duck}: quack quack (you're welcome)")
        elif "time" in user_input:
            current_time = datetime.now().strftime("%H:%M")
            print(f"\N{duck}: quack (the current time is {current_time})")
        else:
            print(f"\N{duck}: {random.choice(other_replies)}")



        #print("\N{duck}: quack")

if __name__ == "__main__":
    main()
