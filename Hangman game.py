import random
def choose():
    print("**************************")
    print("Choose any 1 category to play the game ")
    print("1.Fruits")
    print("2.Animals")
    print("3.Colours")
    print("4.Vegetables")
    print("5.Country")
    ch=input("Please enter the category number : ")
    if ch=='1':
        word=random.choice(["apple","apricot","avocado","banana","cherry","coconut","dates","grapefruit","jackfruit","grapes","guava","kiwi","lemon","mango","orange","olive","papaya","peach","pear","pineapple","pomegranate","strawberry","watermelon"])
    if ch=='2':
        word=random.choice(["dog","turtle","rabbit","cat","kitten","mouse","hamster","cow","pig","goat","deer","sheep","fish","chicken","horse","fish","fox","tiger","lion","snake","kangaroo","camel","chimpanzee","crocodile","deer","elephant","giraffe","frog","lizard","squirrel","sheep"])
    if ch=='3':
        word=random.choice(["red","blue","pink","yellow","brown","purple","black","white","green","orange","gray","azure","maroon","lime","golden","salmon","chocolate","bronze","turquoise","aqua","crimson","silver","navy","orchid","mustard","indigo","teal"])
    if ch=='4':
        word=random.choice(["cabbage","onion","spinach","potato","celery","raddish","broccoli","tomato","cucumber","carrot","pumpkin","pea","mushroom","onion","corn","cauliflower","chili","leek","garlic","eggplant","zucchini","asparagus","beetroot"])
    if ch=='5':
        word=random.choice(["aghanistan","albania","algeria","argentina","australia","bangladesh","belgium","bhutan","brazil","bulgaria","canada","chile","china","colombia","denmark","egypt","france","germany","greece","iceland","india","iran","iraq","indonesia","israel","italy","japan","liberia","malaysia","mexico","mongolia","nepal","oman","pakistan","philippines","russia","spain","sweden","thailand","ukraine"])
    
    return word

def hangman():
    wordc = choose() 
    turns = 10
    guessmade = ''
    validLetters='abcdefghijklmnopqrstuvwxyz'
    print("***************************\n")
    print("You have 10 attempts to guess the word ")
    print("\n***************************\n")

    while len(wordc) > 0:
        main = ""
        missed = 0

        for letter in wordc:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == wordc:
            print(main)
            print("\n***************************\n")
            print("Congratulations, You won!")
            print("\n***************************\n")
            break

        print("Guess the word : " , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter the letters in small letter only ")
            guess = input()

        if guess not in wordc:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turn left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("*********************\n YOU LOOSE !")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                print("**********************\n")
                print(" THE WORD IS : ",wordc)
                print("\n**********************\n")
                break


name = input("Enter your name : ")
print("**********************\n")
print("Welcome" , name.capitalize() ," !" )
hangman()
print()
