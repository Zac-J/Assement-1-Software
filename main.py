def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#-------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("\033[32mCORRECT!:)\033[0m")#绿色代码
        return 1
    else:
        print("\033[31mWRONG!:)\033[0m")#红色代码
        return 0

#-------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("\033[34mRESULTS\033[0m")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

#------------------------
def play_again():
    response = input("\033[32m----Type 'yes' to play again----\033[0m")

    if response == "yes":
        return True
    else:
        print("\033[32mByeeeeee!\033[0m")
#------------------------


questions = {#question store
 "1.Who is more at risk of coronavirus?": "A",
 "2.What's the largest bone in the human boday?": "B",
 "3.Which muscle is responsible for the movement of the shoulder joint?": "B",
 "4.It is a common scalp condition marked by flaking and itching": "A",
 "5.What is the normal heart rate per minute?": "D",
 "6.Access to health care and education is...?":"A",
 "7.I am food-borne & water-borne":"C",
 "8.What part of the skeleton supports the weight of the body and protects the spinal cord?":"B",
 "9.What property of water allows it to regulate temperature effectively?":"B",
 "10.This reaction may cause sneezing, watery eyes, and cough in response to a foreign substance":"D",
}

options = [['A)Older People', 'B)The Youth', 'C)Babies'],
          ["A)Humerus", "B)Femur", "C)Tibia", "D)Pelvis"],
          ["A)Trapezius", "B)Deltold", "C)Pectoralis Major", "D)Latissimus Dorsi"],
          ["A)Dandruff","B)Blisters"],
          ["A)59","B)58","C)121","D)75"],
          ["A)an objective factor","B)a subjective factor"],
          ["A)TB","B)HIVS/AIDS","C)Cholera","D)Malaria"],
          ["A)Rib cage","B)Spine","C)Skull","D)Pelvis"],
          ["A)Cohesion","B)High specific heat","C)Low boiling point","D)Solubility"],
          ["A)interferon response","B)immune response","C)None of the responses are correct","D)allergic response"],
          ["A)","B)","C)","D)"],
          ]

print("-"*30)
print("-*-*-Welcome To Our Quiz Game-*-*-")
print("------What's your [Name]?-----")
print("-------✌ ( ◕ ‿ - )✌-------")
name = input("\033[34m------[Type here]: \033[0m")
print("-"*30)
print("\033[36mWhat type would you like to choose?\033[0m")
print("-"*30)
print("1)Basic Medical Sciences")
print("2)Public Health and Preventive Medicine")
print("3)Nursing")
print("-"*30)
input("\033[36m[Enter the medical subject you want to complete]\033[0m")
print("-"*30)
print("\033[32mReady for the quiz {},they're coming.\033[0m".format(name))#test
print("-"*30)
input("\033[32m<#Press any button to continue#>\033[0m")
new_game()

while play_again() == True:
    new_game()
