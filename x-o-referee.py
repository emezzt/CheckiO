##------------------------------------------------------------------------------
# CheckiO: Xs and Ox Referee
# http://www.checkio.org/mission/x-o-referee/
##------------------------------------------------------------------------------

def checkio(game_result):
    # Constants for each possible way to win in a Tic-Tac-Toe board
    row1 = game_result[0]
    row2 = game_result[1]
    row3 = game_result[2]
    col1 = row1[0] + row2[0] + row3[0]
    col2 = row1[1] + row2[1] + row3[1]
    col3 = row1[2] + row2[2] + row3[2]
    diag1 = row1[0] + row2[1] + row3[2]
    diag2 = row1[2] + row2[1] + row3[0]
    combos = [row1, row2, row3, col1, col2, col3, diag1, diag2]
    # for loop to produce winner, "X", "O", or "D"
    winner = ""
    for c in combos:
        if len(filter(lambda b: b == "X", c)) == 3 or\
           len(filter(lambda b: b == "O", c)) == 3:
            winner = c[0]
    if winner == "":
        winner = "D"
    return winner


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"