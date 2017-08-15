import random as r
"""The aim of this programme is to simulate games of racket ball and work out if a person of a given ability is loosing more than
would be expected given the players ability

A game consists of 15 points and each point can only me won when a player wins during his serve if he looses on his serve then serve passes to the other people."""

def Intro():
    print("""This programme is designed to simulate racket ball games and determine whether the person is loosing,
     more than expected given their level of ability.""")

def Input():

    playerA = eval(input("Please input player A ability level based in a percentage form ( .0"))

def simngames(n, probA, ProbB):

    for i in range(n):
        simgame()
        if gameOver():
            break


def simgame(prob_a, prob_b):

    score_a = 0
    score_b = 0

    serv = 'A'

    while (True):
        # Serv A
        if r.random() < prob_a and serv == 'A':
            score_a += 1
        else:
            serv = 'B'
        # Serv B
        if r.random() < prob_b and serv == 'B':
            score_b +=1
        else:
            serv = "A"

        if score_a == 15 or score_b ==15:
            break




    # todo design the code to simulate the games







def gameOver():
    # todo Design the code for the game over which should stop the game when a player reached 15 points