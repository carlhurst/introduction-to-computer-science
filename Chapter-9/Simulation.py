import random as r
"""The aim of this programme is to simulate games of racket ball and work out if a person of a given ability is loosing more than
would be expected given the players ability

A game consists of 15 points and each point can only me won when a player wins during his serve if he looses on his serve then serve passes to the other people."""

def Intro():
    print("This programme is designed to simulate racket ball games and determine whether the person is loosing " +
          "more than expected given their level of ability.")

def Input():
    playerA = eval(input("Please input player A ability level based in a percentage form (.0): "))
    playerB = eval(input("Please input player B ability level based in a percentage form (.0): "))
    N = eval(input("How many games would you like to simulate: "))

    return playerA, playerB, N

def simngames(n, probA, ProbB):
    # Scores counter for the for loop

    A_Score = 0

    B_Score = 0

    # for loop for the amount of games which is to be run
    for i in range(n):
        Winner = simgame(probA, ProbB)
        print("Cycle: " + str(i))
        if Winner == 'A':
            A_Score += 1
        else:
            B_Score += 1

    return A_Score, B_Score



def simgame(prob_a, prob_b):
    serv = 'A'

    score_a = 0
    score_b = 0

    while (True):
        # Serv A
        if r.random() < prob_a and serv == 'A':
            score_a += 1
            # print("Serve A win")
        else:
            serv = 'B'
            # print("A Lost Serve")
        # Serv B
        if r.random() < prob_b and serv == 'B':
            score_b +=1
            # print("Serve B win")
        else:
            serv = "A"
            # print("B Lost Serve")

        if score_a == 15 or score_b ==15:
            if score_a == 15:
                return 'A'
            else:
                return 'B'
            break


def GameOver():
    print("End of Simulation")


def main():
    Intro()

    playA, playB, N = Input()

    A, B = simngames(N, playA, playB)

    print(A)
    print(B)


if __name__ == '__main__':
    main()
