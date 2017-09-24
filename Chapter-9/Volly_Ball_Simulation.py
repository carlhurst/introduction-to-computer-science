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
    score_team_a, score_team_b = 0, 0

    serv = 'A'

    while True:

        if score_team_a  25 or score_team_b != 25:
            return score_team_a, score_team_b
            break

        if serv == 'A':
            while True:
                if r.random() < ability_a:
                    score_team_a += 1
                    serv = 'B'
                    break
                elif r.random() < ability_b:
                    score_team_b += 1
                    serv = 'B'
                    break

        if serv == 'B':
            while True:
                if r.random() < ability_b:
                    score_team_b += 1
                    serv = 'A'
                    break
                elif r.random() < ability_a:
                    score_team_a += 1
                    serv = 'A'
                    break

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
    # team_a, team_b, number_of_games = greeting()
    #
    # team_a_score, team_b_score = sim_n_games(team_a, team_b, number_of_games)
    #
    # print("The Traditional style of match Team A Won {} ({:1}%) Vs. Team B {}".format(team_a_score, (team_a_score / (team_a_score + team_b_score)) * 100,  team_b_score))

    for i in range(200):
        a, b = game_new(.6, .5)

        print(a, b, i)


if __name__ == '__main__':

    main()
