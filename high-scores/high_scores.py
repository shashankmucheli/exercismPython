"""
Manage a game player's High Score list.

Your task is to build a high-score component of the classic Frogger game, one of the highest selling and addictive
games of all time, and a classic of the arcade era. Your task is to write methods that return the highest score from
the list, the last added score and the three highest scores. """


# latest method returns the latest score that was added to the list
def latest(scores):
    if len(scores) > 0:
        return scores[len(scores) - 1]
    else:
        raise Exception("Length of the list is less than 1")


# personal_best is a method that would find the best score in the list of scores
def personal_best(scores):
    if len(scores) > 0:
        return max(scores)
    else:
        raise Exception("length of the list is less than 1")


# personal top three is a method to list the top three scores of a user given a list of scores
def personal_top_three(scores):
    if len(scores) < 1:
        raise Exception("List is empty")
    # to reduce iterating over the entire list, we sort the list in reverse order i.e., Descending order and pick the
    # top three items
    scores.sort(reverse=True)
    if len(scores) < 3:
        return scores
    else:
        return scores[0:3]
