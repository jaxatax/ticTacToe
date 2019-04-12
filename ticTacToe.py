from random import *
import time
import pyttsx3
engine = pyttsx3.init()
#uncomment the next line to mute it
#engine.setProperty("volume",0)

a1Occupied = False
a2Occupied = False
a3Occupied = False
b1Occupied = False
b2Occupied = False
b3Occupied = False
c1Occupied = False
c2Occupied = False
c3Occupied = False

squares = ["_","_","_","_","_","_","_","_","_"]

def choose():
    global computerChoice
    computerChoice = randint(0,8)

print('''  1 2 3
a _|_|_
b _|_|_
c  | | ''')

engine.say("Do you want easy or hard difficulty?")
engine.runAndWait()
difficulty = input("Do you want easy or hard difficulty? ")

#easy difficulty

if difficulty == "easy":
    while True:
        engine.say("Where do you want to go?")
        engine.runAndWait()
        p = input("Where do you want to go? ").lower()
        
        if p == "a1":
            if a1Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[0] = "X"
                a1Occupied = True
        elif p == "a2":
            if a2Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[1] = "X"
                a2Occupied = True
        elif p == "a3":
            if a3Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[2] = "X"
                a3Occupied = True
        elif p == "b1":
            if b1Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[3] = "X"
                b1Occupied = True
        elif p == "b2":
            if b2Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[4] = "X"
                b2Occupied = True
        elif p == "b3":
            if b3Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[5] = "X"
                b3Occupied = True
        elif p == "c1":
            if c1Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[6] = "X"
                c1Occupied = True
        elif p == "c2":
            if c2Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[7] = "X"
                c2Occupied = True
        elif p == "c3":
            if c3Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[8] = "X"
                c3Occupied = True
        else:
            print("Do you really not understand how to play Tic Tac Toe? You lose your turn")
            engine.say("Do you really not understand how to play Tic Tac Toe? You lose your turn")
            engine.runAndWait()
            
        print(squares[0] + "|" + squares[1] + "|" + squares[2])
        print(squares[3] + "|" + squares[4] + "|" + squares[5])
        print(squares[6] + "|" + squares[7] + "|" + squares[8])

        if squares[0] == squares[1] and squares[1] == squares[2] and squares[0] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        if squares[3] == squares[4] and squares[4] == squares[5] and squares[3] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        if squares[6] == squares[7] and squares[7] == squares[8] and squares[6] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        if squares[0] == squares[3] and squares[3] == squares[6] and squares[0] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        if squares[1] == squares[4] and squares[4] == squares[7] and squares[1] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        if squares[2] == squares[5] and squares[5] == squares[8] and squares[2] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        if squares[0] == squares[4] and squares[4] == squares[8] and squares[0] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        if squares[2] == squares[4] and squares[4] == squares[6] and squares[2] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break

        if squares[0] != "_" and squares[1] != "_" and squares[2] != "_" and squares[3] != "_" and squares[4] != "_" and squares[5] != "_" and squares[6] != "_" and squares[7] != "_" and squares[8] != "_":
            print("Cat!")
            engine.say("Cat!")
            engine.runAndWait()
            break
        
        #computer chooses
        print("Computer is thinking...")
        engine.say("Computer is thinking.")
        engine.runAndWait()
        
        choose()
        while squares[computerChoice] == "X" or squares[computerChoice] == "O":
            choose()

        if computerChoice == 0:
            squares[0] = "O"
            a1Occupied = True
        elif computerChoice == 1:
            squares[1] = "O"
            a2Occupied = True
        elif computerChoice == 2:
            squares[2] = "O"
            a3Occupied = True
        elif computerChoice == 3:
            squares[3] = "O"
            b1Occupied = True
        elif computerChoice == 4:
            squares[4] = "O"
            b2Occupied = True
        elif computerChoice == 5:
            squares[5] = "O"
            b3Occupied = True
        elif computerChoice == 6:
            squares[6] = "O"
            c1Occupied = True
        elif computerChoice == 7:
            squares[7] = "O"
            c2Occupied = True
        elif computerChoice == 8:
            squares[8] = "O"
            c3Occupied = True

        print(squares[0] + "|" + squares[1] + "|" + squares[2])
        print(squares[3] + "|" + squares[4] + "|" + squares[5])
        print(squares[6] + "|" + squares[7] + "|" + squares[8])

        if squares[0] == squares[1] and squares[1] == squares[2] and squares[0] != "_":
            print("Get rekt, the computer won.")
            engine.say("Get rekt, the computer won.")
            engine.runAndWait()
            break
        if squares[3] == squares[4] and squares[4] == squares[5] and squares[3] != "_":
            print("Get rekt, the computer won.")
            engine.say("Get rekt, the computer won.")
            engine.runAndWait()
            break
        if squares[6] == squares[7] and squares[7] == squares[8] and squares[6] != "_":
            print("Get rekt, the computer won.")
            engine.say("Get rekt, the computer won.")
            engine.runAndWait()
            break
        if squares[0] == squares[3] and squares[3] == squares[6] and squares[0] != "_":
            print("Get rekt, the computer won.")
            engine.say("Get rekt, the computer won.")
            engine.runAndWait()
            break
        if squares[1] == squares[4] and squares[4] == squares[7] and squares[1] != "_":
            print("Get rekt, the computer won.")
            engine.say("Get rekt, the computer won.")
            engine.runAndWait()
            break
        if squares[2] == squares[5] and squares[5] == squares[8] and squares[2] != "_":
            print("Get rekt, the computer won.")
            engine.say("Get rekt, the computer won.")
            engine.runAndWait()
            break
        if squares[0] == squares[4] and squares[4] == squares[8] and squares[0] != "_":
            print("Get rekt, the computer won.")
            engine.say("Get rekt, the computer won.")
            engine.runAndWait()
            break
        if squares[2] == squares[4] and squares[4] == squares[6] and squares[2] != "_":
            print("Get rekt, the computer won.")
            engine.say("Get rekt, the computer won.")
            engine.runAndWait()
            break
        
        if squares[0] != "_" and squares[1] != "_" and squares[2] != "_" and squares[3] != "_" and squares[4] != "_" and squares[5] != "_" and squares[6] != "_" and squares[7] != "_" and squares[8] != "_":
            print("Cat!")
            engine.say("Cat!")
            engine.runAndWait()
            break

#hard difficulty

elif difficulty == "hard":
    while True:
        engine.say("Where do you want to go?")
        engine.runAndWait()
        p = input("Where do you want to go? ").lower()
        
        if p == "a1":
            if a1Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[0] = "X"
                a1Occupied = True
        elif p == "a2":
            if a2Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[1] = "X"
                a2Occupied = True
        elif p == "a3":
            if a3Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[2] = "X"
                a3Occupied = True
        elif p == "b1":
            if b1Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[3] = "X"
                b1Occupied = True
        elif p == "b2":
            if b2Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[4] = "X"
                b2Occupied = True
        elif p == "b3":
            if b3Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[5] = "X"
                b3Occupied = True
        elif p == "c1":
            if c1Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[6] = "X"
                c1Occupied = True
        elif p == "c2":
            if c2Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[7] = "X"
                c2Occupied = True
        elif p == "c3":
            if c3Occupied == True:
                print("That square is occupied. You lose your turn.")
                engine.say("That square is occupied. You lose your turn.")
                engine.runAndWait()
            else:
                squares[8] = "X"
                c3Occupied = True
        else:
            print("Do you really not understand how to play Tic Tac Toe? You lose your turn")
            engine.say("Do you really not understand how to play Tic Tac Toe? You lose your turn")
            engine.runAndWait()
            
        print(squares[0] + "|" + squares[1] + "|" + squares[2])
        print(squares[3] + "|" + squares[4] + "|" + squares[5])
        print(squares[6] + "|" + squares[7] + "|" + squares[8])

        if squares[0] == squares[1] and squares[1] == squares[2] and squares[0] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        elif squares[3] == squares[4] and squares[4] == squares[5] and squares[3] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        elif squares[6] == squares[7] and squares[7] == squares[8] and squares[6] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        elif squares[0] == squares[3] and squares[3] == squares[6] and squares[0] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        elif squares[1] == squares[4] and squares[4] == squares[7] and squares[1] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        elif squares[2] == squares[5] and squares[5] == squares[8] and squares[2] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        elif squares[0] == squares[4] and squares[4] == squares[8] and squares[0] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        elif squares[2] == squares[4] and squares[4] == squares[6] and squares[2] != "_":
            print("Good job! You win!")
            engine.say("Good job! You win!")
            engine.runAndWait()
            break
        
        if squares[0] != "_" and squares[1] != "_" and squares[2] != "_" and squares[3] != "_" and squares[4] != "_" and squares[5] != "_" and squares[6] != "_" and squares[7] != "_" and squares[8] != "_":
            print("Cat!")
            engine.say("Cat!")
            engine.runAndWait()
            break

        #computer chooses
        print("Computer is thinking...")
        engine.say("Computer is thinking.")
        engine.runAndWait()
        
        #if computer can win (ik this is a mess)
        if squares[0] == squares[1] and squares[2] == "_" and squares[0] != "_" and squares[0] == "O":
            squares[2] = "O"

        elif squares[1] == squares[2] and squares[0] == "_" and squares[1] != "_" and squares[1] == "O":
            squares[0] = "O"

        elif squares[0] == squares[2] and squares[1] == "_" and squares[0] != "_" and squares[0] == "O":
            squares[1] = "O"

        elif squares[3] == squares[4] and squares[5] == "_" and squares[3] != "_" and squares[3] == "O":
            squares[5] = "O"

        elif squares[4] == squares[5] and squares[3] == "_" and squares[4] != "_" and squares[4] == "O":
            squares[3] = "O"

        elif squares[3] == squares[5] and squares[4] == "_" and squares[3] != "_" and squares[3] == "O":
            squares[4] = "O"

        elif squares[6] == squares[7] and squares[8] == "_" and squares[6] != "_" and squares[6] == "O":
            squares[8] = "O"

        elif squares[7] == squares[8] and squares[6] == "_" and squares[7] != "_" and squares[7] == "O":
            squares[6] = "O"

        elif squares[6] == squares[8] and squares[7] == "_" and squares[6] != "_" and squares[6] == "O":
            squares[7] = "O"

        elif squares[0] == squares[3] and squares[6] == "_" and squares[0] != "_" and squares[0] == "O":
            squares[6] = "O"

        elif squares[3] == squares[6] and squares[0] == "_" and squares[3] != "_" and squares[3] == "O":
            squares[0] = "O"

        elif squares[0] == squares[6] and squares[3] == "_" and squares[0] != "_" and squares[0] == "O":
            squares[3] = "O"

        elif squares[1] == squares[4] and squares[7] == "_" and squares[1] != "_" and squares[1] == "O":
            squares[7] = "O"

        elif squares[4] == squares[7] and squares[1] == "_" and squares[4] != "_" and squares[4] == "O":
            squares[1] = "O"

        elif squares[1] == squares[7] and squares[4] == "_" and squares[1] != "_" and squares[1] == "O":
            squares[4] = "O"

        elif squares[2] == squares[5] and squares[8] == "_" and squares[2] != "_" and squares[2] == "O":
            squares[8] = "O"

        elif squares[5] == squares[8] and squares[2] == "_" and squares[5] != "_" and squares[5] == "O":
            squares[2] = "O"

        elif squares[2] == squares[8] and squares[5] == "_" and squares[2] != "_" and squares[2] == "O":
            squares[5] = "O"

        elif squares[0] == squares[4] and squares[8] == "_" and squares[0] != "_" and squares[0] == "O":
            squares[8] = "O"

        elif squares[4] == squares[8] and squares[0] == "_" and squares[4] != "_" and squares[4] == "O":
            squares[0] = "O"

        elif squares[0] == squares[8] and squares[4] == "_" and squares[0] != "_" and squares[0] == "O":
            squares[4] = "O"

        elif squares[2] == squares[4] and squares[6] == "_" and squares[2] != "_" and squares[2] == "O":
            squares[6] = "O"

        elif squares[4] == squares[6] and squares[2] == "_" and squares[4] != "_" and squares[4] == "O":
            squares[2] = "O"

        elif squares[2] == squares[6] and squares[4] == "_" and squares[2] != "_" and squares[2] == "O":
            squares[4] = "O"

        #if computer can block

        elif squares[0] == squares[1] and squares[2] == "_" and squares[0] != "_":
            squares[2] = "O"

        elif squares[1] == squares[2] and squares[0] == "_" and squares[1] != "_":
            squares[0] = "O"

        elif squares[0] == squares[2] and squares[1] == "_" and squares[0] != "_":
            squares[1] = "O"

        elif squares[3] == squares[4] and squares[5] == "_" and squares[3] != "_":
            squares[5] = "O"

        elif squares[4] == squares[5] and squares[3] == "_" and squares[4] != "_":
            squares[3] = "O"

        elif squares[3] == squares[5] and squares[4] == "_" and squares[3] != "_":
            squares[4] = "O"

        elif squares[6] == squares[7] and squares[8] == "_" and squares[6] != "_":
            squares[8] = "O"

        elif squares[7] == squares[8] and squares[6] == "_" and squares[7] != "_":
            squares[6] = "O"

        elif squares[6] == squares[8] and squares[7] == "_" and squares[6] != "_":
            squares[7] = "O"

        elif squares[0] == squares[3] and squares[6] == "_" and squares[0] != "_":
            squares[6] = "O"

        elif squares[3] == squares[6] and squares[0] == "_" and squares[3] != "_":
            squares[0] = "O"

        elif squares[0] == squares[6] and squares[3] == "_" and squares[0] != "_":
            squares[3] = "O"

        elif squares[1] == squares[4] and squares[7] == "_" and squares[1] != "_":
            squares[7] = "O"

        elif squares[4] == squares[7] and squares[1] == "_" and squares[4] != "_":
            squares[1] = "O"

        elif squares[1] == squares[7] and squares[4] == "_" and squares[1] != "_":
            squares[4] = "O"

        elif squares[2] == squares[5] and squares[8] == "_" and squares[2] != "_":
            squares[8] = "O"

        elif squares[5] == squares[8] and squares[2] == "_" and squares[5] != "_":
            squares[2] = "O"

        elif squares[2] == squares[8] and squares[5] == "_" and squares[2] != "_":
            squares[5] = "O"

        elif squares[0] == squares[4] and squares[8] == "_" and squares[0] != "_":
            squares[8] = "O"

        elif squares[4] == squares[8] and squares[0] == "_" and squares[4] != "_":
            squares[0] = "O"

        elif squares[0] == squares[8] and squares[4] == "_" and squares[0] != "_":
            squares[4] = "O"

        elif squares[2] == squares[4] and squares[6] == "_" and squares[2] != "_":
            squares[6] = "O"

        elif squares[4] == squares[6] and squares[2] == "_" and squares[4] != "_":
            squares[2] = "O"

        elif squares[2] == squares[6] and squares[4] == "_" and squares[2] != "_":
            squares[4] = "O"

        #if computer can't win or block pick a random square
        else:
            choose()
            while squares[computerChoice] == "X" or squares[computerChoice] == "O":
                choose()

            if computerChoice == 0:
                squares[0] = "O"
                a1Occupied = True
            elif computerChoice == 1:
                squares[1] = "O"
                a2Occupied = True
            elif computerChoice == 2:
                squares[2] = "O"
                a3Occupied = True
            elif computerChoice == 3:
                squares[3] = "O"
                b1Occupied = True
            elif computerChoice == 4:
                squares[4] = "O"
                b2Occupied = True
            elif computerChoice == 5:
                squares[5] = "O"
                b3Occupied = True
            elif computerChoice == 6:
                squares[6] = "O"
                c1Occupied = True
            elif computerChoice == 7:
                squares[7] = "O"
                c2Occupied = True
            elif computerChoice == 8:
                squares[8] = "O"
                c3Occupied = True

        print(squares[0] + "|" + squares[1] + "|" + squares[2])
        print(squares[3] + "|" + squares[4] + "|" + squares[5])
        print(squares[6] + "|" + squares[7] + "|" + squares[8])

        if squares[0] == "O" and squares[1] == "O" and squares[2] == "O" or squares[3] == "O" and squares[4] == "O" and squares[5] == "O" or squares[6] == "O" and squares[7] == "O" and squares[8] == "O" or squares[0] == "O" and squares[3] == "O" and squares[6] == "O" or squares[1] == "O" and squares[4] == "O" and squares[7] == "O" or squares[2] == "O" and squares[5] == "O" and squares[8] == "O" or squares[0] == "O" and squares[4] == "O" and squares[8] == "O" or squares[2] == "O" and squares[4] == "O" and squares[6] == "O":
            print("Computer won, get rekt")
            engine.say("Computer won, get rekt")
            engine.runAndWait()
            break

        if squares[0] != "_" and squares[1] != "_" and squares[2] != "_" and squares[3] != "_" and squares[4] != "_" and squares[5] != "_" and squares[6] != "_" and squares[7] != "_" and squares[8] != "_":
            print("Cat!")
            engine.say("Cat!")
            engine.runAndWait()
            break
