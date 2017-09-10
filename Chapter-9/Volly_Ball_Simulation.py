import random as r

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

    while True:

        if (r.random() <= ability_a) and (serv == 'A'):

            scoreA += 1

        else:
            serv = 'B'

        if (r.random() <= ability_b) and (serv == 'B'):

            scoreB += 1
        else:
            serv = 'A'

        if scoreA == 15:

            return 'A'

        elif scoreB == 15:

            return 'B'


def GameNew(Ability_a, Ability_b):
    scoreA = 0

    scoreB = 0

    Serv = 'A'

    while True:

        if Serv == 'A':

            if r.random() <= Ability_a:

                scoreA += 1

                Serv = 'B'

            elif r.random() <= Ability_b:

                scoreB += 1
                Serv = 'B'

        if Serv == 'B':

            if r.random() <= Ability_b:

                scoreA += 1
                Serv = 'A'

            elif r.random() <= Ability_a:

                scoreB += 1
                Serv = 'A'

        if scoreA == 15:
            return 'A'
        elif scoreB == 15:
            return 'B'



def SimNGames(ability_a, ability_b, n):
    Traditional_A_Team_Score = 0

    Traditional_B_Team_Score = 0

    New_A_Team_Score = 0

    New_B_Team_Score = 0



    for i in range(n):

        a = GameTraditional(ability_a, ability_b)

        # print(i)

        if a == 'A':
            Traditional_A_Team_Score += 1
            # print("Team A Win")

        elif a == 'B':
            Traditional_B_Team_Score += 1
            # print("Team B Win")

        b = GameNew(ability_a, ability_b)

        # print(i)

        if b == 'A':
            New_A_Team_Score += 1

        elif b == 'B':
            New_B_Team_Score += 1

    return Traditional_A_Team_Score, Traditional_B_Team_Score, New_A_Team_Score, New_B_Team_Score


def main():
    Team_A, Team_B, Number_of_Games = Greeting()

    Team_A_Score, Team_B_score, New_A_Score, New_B_Score = SimNGames(Team_A, Team_B, Number_of_Games)

    print("The Traditional style of match Team A Won \t {} \t Vs. \t Team B {}".format(Team_A_Score, Team_B_score))

    print("\nThe new style of match Team A Won \t {} \t Vs. \t Team B {}".format(New_A_Score, New_B_Score))

if __name__ == '__main__':
    main()
