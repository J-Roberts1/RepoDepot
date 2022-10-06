import random


def rps():
    user = input('Rock, Paper, or Scissors:')
    ai = random.choice(['Rock', 'Paper', 'Scissors'])

    if user == ai:
        print('computer choice: ' + ai)
        return "Mid"

    if win_func(user, ai):
        print('computer choice: ' + ai)
        return 'Common player W'
    return 'L Choice \n' 'computer choice: ' + ai

def win_func(player, opponent):
    if ((player == 'Rock' and opponent == 'Scissors') or
            (player == 'Scissors' and opponent == "Paper") or
            (player == "Paper" and opponent == 'Rock')):
        return True


print(rps())
