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


def rally(ability_a, ability_b, serv):
    if serv == 'A':
        while True:
            if r.random() <= ability_a:
                return 'B'
            elif r.random() <= ability_b:
                return 'A'
    if serv == 'B':
        while True:
            if r.random() <= ability_b:
                return 'A'
            elif r.random() <= ability_a:
                return 'B'


def game_new(ability_a, ability_b):

    score_team_a, score_team_b = 0, 0

    serv = 'A'

    while True:

        a = rally(ability_a, ability_b, serv)

        if a == 'B':
            score_team_b += 1
        elif a == 'A':
            score_team_a += 1

        if serv == 'A':
            serv = 'B'
        elif serv == 'B':
            serv = 'A'

        if score_team_a == 25:
            return 'A'
        elif score_team_b == 25:
            return 'B'


def sim_n_games(ability_a, ability_b, n):

    traditional_score_a, traditional_score_b = 0, 0

    score_a, score_b = 0, 0

    for i in range(n):
        result = game_traditional(ability_a, ability_b)

        n_result = game_new(ability_a, ability_b)

        if result == 'A':
            traditional_score_a += 1

        elif result == 'B':
            traditional_score_b += 1

        if n_result == 'A':
            score_a += 1
        elif n_result == 'B':
            score_b += 1

    return traditional_score_a, traditional_score_b, score_a, score_b


def main():
    team_a, team_b, number_of_games = greeting()

    trad_a_score, trad_b_score, new_a_score, new_b_score = sim_n_games(team_a, team_b, number_of_games)

    print("Traditional A score is: {} \t Traditional B Score is: {}".format(trad_a_score, trad_b_score))
    print("New A score is: {} \t New B score is: {}".format(new_a_score, new_b_score))


if __name__ == '__main__':
    main()

