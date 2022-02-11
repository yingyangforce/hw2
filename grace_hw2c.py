# +---------------------+
# | hw2c - Isaiah Grace |
# +---------------------+

# Part c - the real winners are the friends we made along the way

def hockeyWinner():
    our_score = int(input("Umaine's score: "))
    their_score = int(input("Visiting team's score: "))
    if our_score > their_score:
        print("We won!")
    elif our_score < their_score:
        print("We lost.")
    else:
        print("It's a tie.")

hockeyWinner()
hockeyWinner()
hockeyWinner()
