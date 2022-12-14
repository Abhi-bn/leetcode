import itertools


def func():
    teamA = [1, 4, 2, 4]
    teamB = [3, 5]
    scoresList = [(scoreA, scoreB) for scoreA in teamA for scoreB in teamB]
    print(scoresList)

    # for scores in scoresList:
    #     if(scores(0))


func()
