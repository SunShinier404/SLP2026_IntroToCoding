class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):

        return self.word+'('+self.meaning+')'

flash = []
print("Welcome to your study set!")

while(True):
    word = input("Word: ")
    meaning = input("Definition: ")
    
    flash.append(flashcard(word, meaning))
    print("Flashcard added!")
    option = int(input("Do you want to add another flashcard? (0 for yes, 1 for no): "))
   
    if(option):
        break

print("\nYour flashcards:")
for i in flash:
    print(">",i)