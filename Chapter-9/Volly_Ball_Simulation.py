import random as R

"""
This programme is designed to simulate a game of volly ball.
"""

def Greeting():

    print("This programme is designed to compare the different types of Volly ball")

    team_a = eval(input("\n Please input the level of ability of both the teams in the following format (0.1): "))

    team_b = eval(input("\n Please input the level of ability of both the teams in the following format (0.1): "))

    Number_of_Games = eval(input("\n Please enter the number of the amount of games you wish to simulate."))

    return team_a, team_b,  Number_of_Games


def GameTraditional(ability_a, ability_b):

    serv = 'A'

    scoreA = 0

    scoreB = 0

    if (serv == 'A') and (R.random <= ability_a):

        scoreA += 1

    else:
        serv = 'B'

    if (serv == 'B') and (R.random <= ability_b):

        scoreB += 1
    else:
        serv = 'A'

    if scoreA == 15:

        return 'A'

    elif scoreB == 15:

        return 'B'



def SimNGames(ability_a, ability_b, n):


def main():
    print("hello")


if __name__ == '__main__':
    main()
