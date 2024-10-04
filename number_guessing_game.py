import random

print("WELCOME TO MY NUMBER GUESSING GAME!")
while True:
    game = input("Do you want to play this game?\n").lower()

    if game == "no":
        print("🌸 Thanks for playing")
        print(f"🎉 Your score is {score}")
        quit()
    
    else:
        score = 0
        number = random.randint(1, 1000)
        while True:
            user = int(input("Guess the number between 1 and 1000: \n"))
            if user in range(1 ,1000):
        
                if user == number:
                    print("✅ Correct!")
                    score += 1
                    break
                elif number > user:
                    print(f"\n ❌ The number is greater than {user}\n")
                elif number < user:
                    print(f"\n ❌ The number is less than {user}\n")
            else:
                print("🛑 Enter number between 1 and 1000")
