import random as r

"""
This programme is designed to simulate a game of volly ball.
"""


def greeting():

    print("This programme is designed to compare the different types of Volly ball")

    team_a = eval(input("\n Please input the level of ability of both the teams in the following format (0.1): "))

    team_b = eval(input("\n Please input the level of ability of both the teams in the following format (0.1): "))

    number_of_games = eval(input("\n Please enter the number of the amount of games you wish to simulate."))

    return team_a, team_b,  number_of_games


def game_traditional(ability_a, ability_b):

    serv = 'A'

    score_a = 0

    score_b = 0

    while True:

        if (r.random() <= ability_a) and (serv == 'A'):

            score_a += 1

        else:
            serv = 'B'

        if (r.random() <= ability_b) and (serv == 'B'):

            score_b += 1
        else:
            serv = 'A'

        if score_a == 15:

            return 'A'

        elif score_b == 15:

            return 'B'


def game_new(ability_a, ability_b):
    scoreA = 0

    scoreB = 0

    Serv = 'A'

    while True:

        if serv == 'A':

            if r.random() <= ability_a:

                scoreA += 1

                serv = 'B'

            elif r.random() <= ability_b:

                scoreB += 1
                serv = 'B'

        if serv == 'B':

            if r.random() <= ability_b:

                scoreA += 1
                serv = 'A'

            elif r.random() <= ability_a:

                scoreB += 1
                serv = 'A'

        if scoreA == 15:
            return 'A'
        elif scoreB == 15:
            return 'B'


def sim_n_games(ability_a, ability_b, n):

    traditional_score_a = 0

    traditional_score_b = 0

    for i in range(n):
        result = game_traditional(ability_a, ability_b)

        print(i)

        if result == 'A':
            traditional_score_a += 1

        elif result == 'B':
            traditional_score_b += 1

    return traditional_score_a, traditional_score_b


def main():
    team_a, team_b, number_of_games = greeting()

    team_a_score, team_b_score = sim_n_games(team_a, team_b, number_of_games)

    print("The Traditional style of match Team A Won {} ({:1}%) Vs. Team B {}".format(team_a_score, (team_a_score / (team_a_score + team_b_score)) * 100,  team_b_score))


if __name__ == '__main__':

    main()
