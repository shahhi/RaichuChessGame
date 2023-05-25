#
# raichu.py : Play the game of Raichu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
# Himani Shah - shahhi, Riya Shetty - rishett, Vanita Lalwani -vlalwan
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import time
from copy import deepcopy


def board_to_string(board, N):
    s = '\n'
    for row in board:
        s = s + ''.join(row)
    return s

# The oneDtotwoD matrix reference has been taken fromvarious sources over the internet
def oneDtotwoD(board, N):
    j = 0
    s = []
    for row in range(N):
        inner_list = []
        for col in range(N):
            inner_list.append(board[j])
            j += 1
            # print(j)
        s.append(inner_list)
        # print(j)
    return s

# Finds all the possible moves for Raichu in Upward direction of its current position
def moveNorth(player, board2d, row, col):
    moves = []
    kill_moves = []
    if player == 'w':
        playerPieces = 'wW@'
        opponentpieces = 'bB$'
    else:
        playerPieces = 'bB$'
        opponentpieces = 'wW@'
    move = deepcopy(board2d)
    # Move till position above is empty
    while row >= 1 and move[row - 1][col] == '.':
        # move the piece if place is empty

        move[row - 1][col] = move[row][col]
        move[row][col] = '.'
        row -= 1
        moves.append(deepcopy(move))

    # If there is opponent piece ahead, then we jump over it
    if row >= 2 and move[row - 1][col] in opponentpieces and move[row - 2][col] == '.':
        # check if we can kill the piece
        move[row - 2][col] = move[row][col]
        move[row][col] = '.'
        move[row-1][col] = '.'
        row -= 2
        kill_moves.append(deepcopy(move))
        # Once killed we can only move till there are blank positions
        while row >= 1 and move[row - 1][col] == '.':
            move[row - 1][col] = move[row][col]
            move[row][col] = '.'
            row -= 1
            kill_moves.append(deepcopy(move))
    return (moves,kill_moves)

def moveSouth(player, board2d, row, col):
    moves = []
    kill_moves = []
    N = len(board2d)
    if player == 'w':
        playerPieces = 'wW@'
        opponentpieces = 'bB$'
    else:
        playerPieces = 'bB$'
        opponentpieces = 'wW@'
    move = deepcopy(board2d)
    # Move till position above is empty
    while row <= N-2 and move[row + 1][col] == '.':
        # move the piece if place is empty
        move[row + 1][col] = move[row][col]
        move[row][col] = '.'
        row += 1
        moves.append(deepcopy(move))

    # If there is opponent piece ahead, then we jump over it
    if row < N-2 and move[row + 1][col] in opponentpieces and move[row + 2][col] == '.':
        # check if we can kill the piece
        move[row + 2][col] = move[row][col]
        move[row][col] = '.'
        move[row+1][col] = '.'
        row += 2
        kill_moves.append(deepcopy(move))
        # Once killed we can only move till there are blank positions
        while row <= N - 2 and move[row + 1][col] == '.':
            move[row + 1][col] = move[row][col]
            move[row][col] = '.'
            row += 1
            kill_moves.append(deepcopy(move))
    return (moves,kill_moves)

def moveWest(player, board2d, row, col):
    moves = []
    kill_moves = []
    if player == 'w':
        playerPieces = 'wW@'
        opponentpieces = 'bB$'
    else:
        playerPieces = 'bB$'
        opponentpieces = 'wW@'
    move = deepcopy(board2d)
    # Move till position above is empty
    while col >= 1 and move[row][col - 1] == '.':
        # move the piece if place is empty
        move[row][col - 1] = move[row][col]
        move[row][col] = '.'
        col -= 1
        moves.append(deepcopy(move))

    # If there is opponent piece ahead, then we jump over it
    if col >= 2 and move[row][col - 1] in opponentpieces and move[row][col - 2] == '.':
        # check if we can kill the piece
        move[row][col - 2] = move[row][col]
        move[row][col] = '.'
        move[row][col-1] = '.'
        col -= 2
        kill_moves.append(deepcopy(move))
        # Once killed we can only move till there are blank positions
        while col >= 1 and move[row][col - 1] == '.':
            move[row][col - 1] = move[row][col]
            move[row][col] = '.'
            col -= 1
            kill_moves.append(deepcopy(move))
    return (moves,kill_moves)

def moveEast(player, board2d, row, col):
    moves = []
    kill_moves = []
    N = len(board2d)
    if player == 'w':
        playerPieces = 'wW@'
        opponentpieces = 'bB$'
    else:
        playerPieces = 'bB$'
        opponentpieces = 'wW@'
    move = deepcopy(board2d)
    # Move till position above is empty
    while col <= N-2 and move[row][col + 1] == '.':
        # move the piece if place is empty
        move[row][col + 1] = move[row][col]
        move[row][col] = '.'
        col += 1
        moves.append(deepcopy(move))

    # If there is opponent piece ahead, then we jump over it
    if col < N-2 and move[row][col + 1] in opponentpieces and move[row][col + 2] == '.':
        # check if we can kill the piece
        move[row][col + 2] = move[row][col]
        move[row][col] = '.'
        move[row][col + 1] = '.'
        col += 2
        kill_moves.append(deepcopy(move))
        # Once killed we can only move till there are blank positions
        while col <= N - 2 and move[row][col + 1] == '.':
            move[row][col + 1] = move[row][col]
            move[row][col] = '.'
            col += 1
            kill_moves.append(deepcopy(move))
    return (moves,kill_moves)

def moveNorthWest(player, board2d, row, col):
    moves=[]
    kill_moves = []
    N = len(board2d)
    if player == 'w':
        playerPieces = 'wW@'
        opponentpieces = 'bB$'
    else:
        playerPieces = 'bB$'
        opponentpieces = 'wW@'
    move = deepcopy(board2d)
    # Move till position above is empty
    while row>=1 and col>=1 and move[row - 1][col - 1] == '.':
        # move the piece if place is empty
        move[row - 1][col - 1] = move[row][col]
        move[row][col] = '.'
        col -= 1
        row -= 1
        moves.append(deepcopy(move))
    # If there is opponent piece ahead, then we jump over it
    if col >= 2 and row >=2 and move[row - 1][col - 1] in opponentpieces and move[row - 2][col - 2] == '.':
        # check if we can kill the piece
        move[row - 2][col - 2] = move[row][col]
        move[row][col] = '.'
        move[row - 1][col - 1] = '.'
        col -= 2
        row -= 2
        kill_moves.append(deepcopy(move))
        # Once killed we can only move till there are blank positions
        while col >= 1 and row >=1 and move[row - 1][col - 1] == '.':
            move[row - 1][col - 1] = move[row][col]
            move[row][col] = '.'
            col -= 1
            row -= 1
            kill_moves.append(deepcopy(move))
    return (moves, kill_moves)

def moveSouthWest(player, board2d, row, col):
    moves=[]
    kill_moves = []
    N = len(board2d)
    if player == 'w':
        playerPieces = 'wW@'
        opponentpieces = 'bB$'
    else:
        playerPieces = 'bB$'
        opponentpieces = 'wW@'
    move = deepcopy(board2d)
    # Move till position above is empty
    while row <= N-2 and col>=1 and move[row + 1][col - 1] == '.':
        # move the piece if place is empty
        move[row + 1][col - 1] = move[row][col]
        move[row][col] = '.'
        col -= 1
        row += 1
        moves.append(deepcopy(move))
    # If there is opponent piece ahead, then we jump over it
    if col >= 2 and row <N-2 and move[row + 1][col - 1] in opponentpieces and move[row + 2][col - 2] == '.':
        # check if we can kill the piece
        move[row + 2][col - 2] = move[row][col]
        move[row][col] = '.'
        move[row + 1][col - 1] = '.'
        col -= 2
        row += 2
        kill_moves.append(deepcopy(move))
        # Once killed we can only move till there are blank positions
        while row <= N-2 and col>=1 and move[row + 1][col - 1] == '.':
            move[row + 1][col - 1] = move[row][col]
            move[row][col] = '.'
            col -= 1
            row += 1
            kill_moves.append(deepcopy(move))
    return (moves, kill_moves)

def moveSouthEast(player, board2d, row, col):
    moves=[]
    kill_moves = []
    N = len(board2d)
    if player == 'w':
        playerPieces = 'wW@'
        opponentpieces = 'bB$'
    else:
        playerPieces = 'bB$'
        opponentpieces = 'wW@'
    move = deepcopy(board2d)
    # Move till position above is empty
    while row <= N-2 and col <= N-2 and move[row + 1][col + 1] == '.':
        # move the piece if place is empty
        move[row + 1][col + 1] = move[row][col]
        move[row][col] = '.'
        col += 1
        row += 1
        moves.append(deepcopy(move))
    # If there is opponent piece ahead, then we jump over it
    if col < N-2 and row < N-2 and move[row + 1][col + 1] in opponentpieces and move[row + 2][col + 2] == '.':
        # check if we can kill the piece
        move[row + 2][col + 2] = move[row][col]
        move[row][col] = '.'
        move[row + 1][col + 1] = '.'
        col += 2
        row += 2
        kill_moves.append(deepcopy(move))
        # Once killed we can only move till there are blank positions
        while row <= N-2 and col <= N-2 and move[row + 1][col + 1] == '.':
            move[row + 1][col + 1] = move[row][col]
            move[row][col] = '.'
            col += 1
            row += 1
            kill_moves.append(deepcopy(move))
    return (moves, kill_moves)

def moveNorthEast( player, board2d, row, col):
    moves = []
    kill_moves = []
    N = len(board2d)
    if player == 'w':
        playerPieces = 'wW@'
        opponentpieces = 'bB$'
    else:
        playerPieces = 'bB$'
        opponentpieces = 'wW@'
    move = deepcopy(board2d)
    # Move till position above is empty
    while row >= 1 and col <= N-2 and move[row - 1][col + 1] == '.':
        # move the piece if place is empty
        move[row - 1][col + 1] = move[row][col]
        move[row][col] = '.'
        col += 1
        row -= 1
        moves.append(deepcopy(move))
    # If there is opponent piece ahead, then we jump over it
    if row >= 2 and col < N-2 and move[row - 1][col + 1] in opponentpieces and move[row - 2][col + 2] == '.':
        # check if we can kill the piece
        move[row - 2][col + 2] = move[row][col]
        move[row][col] = '.'
        move[row - 1][col + 1] = '.'
        col += 2
        row -= 2
        kill_moves.append(deepcopy(move))
        # Once killed we can only move till there are blank positions
        while row >= 1 and col <= N-2 and move[row - 1][col + 1] == '.':
            move[row - 1][col + 1] = move[row][col]
            move[row][col] = '.'
            col += 1
            row -= 1
            kill_moves.append(deepcopy(move))
    return (moves, kill_moves)

def getMovesForPichu(player, board2d, row, col):
    N = len(board2d)
    moves = []
    if player == 'b' and board2d[row][col] == 'b':
        # move north east
        if row >= 1 and col <= N - 2 and board2d[row - 1][col + 1] == '.':
            board = deepcopy(board2d)
            if row - 1 == 0:
                board[row - 1][col + 1] = '$'
            else:
                board[row - 1][col + 1] = 'b'
            board[row][col] = '.'
            moves.append(board)
        elif row >= 2 and col <= N - 3 and board2d[row - 1][col + 1] in 'w' and board2d[row - 2][col + 2] == '.':
            board = deepcopy(board2d)
            board[row][col] = '.'
            board[row - 1][col + 1] = '.'
            if row - 2 == 0:
                board[row - 2][col + 2] = '$'
            else:
                board[row - 2][col + 2] = 'b'
            moves.append(board)

        # move North West
        if row >= 1 and col >= 1 and board2d[row - 1][col - 1] == '.':
            board = deepcopy(board2d)
            if row - 1 == 0:
                board[row - 1][col - 1] = '$'
            else:
                board[row - 1][col - 1] = 'b'
            board[row][col] = '.'
            moves.append(board)
        elif row >= 2 and col >= 2 and board2d[row - 1][col - 1] in 'w' and board2d[row - 2][col - 2] == '.':
            board = deepcopy(board2d)
            board[row - 1][col - 1] = '.'
            board[row][col] = '.'
            if row - 2 == 0:
                board[row - 2][col - 2] = '$'
            else:
                board[row - 2][col - 2] = 'b'
            moves.append(board)
    elif player == 'w' and board2d[row][col] == 'w':
        # move south east
        if row <= N - 2 and col <= N - 2 and board2d[row + 1][col + 1] == '.':
            board = deepcopy(board2d)
            if row + 1 == N - 1:
                board[row + 1][col + 1] = '@'
            else:
                board[row + 1][col + 1] = 'w'
            board[row][col] = '.'
            moves.append(board)
        elif row <= N - 3 and col <= N - 3 and board2d[row + 1][col + 1] in 'b' and board2d[row - 2][col + 2] == '.':
            board = deepcopy(board2d)
            board[row][col] = '.'
            board[row + 1][col + 1] = '.'
            if row + 2 == N - 1:
                board[row + 2][col + 2] = '@'
            else:
                board[row + 2][col + 2] = 'w'
            moves.append(board)

        # move south West
        if row <= N - 2 and col >= 1 and board2d[row + 1][col - 1] == '.':
            board = deepcopy(board2d)
            if row + 1 == N - 1:
                board[row + 1][col - 1] = '@'
            else:
                board[row + 1][col - 1] = 'w'
            board[row][col] = '.'
            moves.append(board)
        elif row <= N - 3 and col >= 2 and board2d[row + 1][col - 1] in 'b' and board2d[row + 2][col - 2] == '.':
            board = deepcopy(board2d)
            board[row + 1][col - 1] = '.'
            board[row][col] = '.'
            if row + 2 == N - 1:
                board[row + 2][col - 2] = '@'
            else:
                board[row + 2][col - 2] = 'w'
            moves.append(board)

    return moves

def getMovesForPikachu(player, board2d, row, col):
    N = len(board2d)
    moves = []
    kill_moves = []
    if player == 'w':
        opponentPiece = 'bB'
    else:
        opponentPiece = 'wW'
    # Move one step west
    if col >= 1 and board2d[row][col - 1] == '.':
        board = deepcopy(board2d)
        board[row][col - 1] = board[row][col]
        board[row][col] = '.'
        moves.append(board)

    elif col >= 2 and board2d[row][col - 1] in opponentPiece and board2d[row][col - 2] == '.':
        board = deepcopy(board2d)
        board[row][col - 1] = '.'
        board[row][col - 2] = board[row][col]
        board[row][col] = '.'
        kill_moves.append(board)

    # move 2 steps west
    if col >= 2 and board2d[row][col - 1] == '.' and board2d[row][col - 2] == '.':
        board = deepcopy(board2d)
        board[row][col - 2] = board[row][col]
        board[row][col] = '.'
        moves.append(board)
    if col >= 3 and board2d[row][col - 3] == '.' and ((board2d[row][col - 1] in opponentPiece and board2d[row][col - 2] == '.') or (board2d[row][col - 1] == '.' and board2d[row][col - 2] in opponentPiece)):
        board = deepcopy(board2d)
        board[row][col - 3] = board[row][col]
        board[row][col] = '.'
        board[row][col - 1] = '.'
        board[row][col - 2] = '.'
        kill_moves.append(board)

    # Move one step east
    if col <= N-2 and board2d[row][col + 1] == '.':
        board = deepcopy(board2d)
        board[row][col + 1] = board[row][col]
        board[row][col] = '.'
        moves.append(board)
    elif col <= N-3 and board2d[row][col + 1] in opponentPiece and board2d[row][col + 2] == '.':
        board = deepcopy(board2d)
        board[row][col + 1] = '.'
        board[row][col + 2] = board[row][col]
        board[row][col] = '.'
        kill_moves.append(board)

    # move 2 steps east
    if col <= N-3 and board2d[row][col + 1] == '.' and board2d[row][col + 2] == '.':
        board = deepcopy(board2d)
        board[row][col + 2] = board[row][col]
        board[row][col] = '.'
        moves.append(board)
    if col <= N-4 and board2d[row][col + 3] == '.' and ((board2d[row][col + 1] in opponentPiece and board2d[row][col + 2] == '.') or (board2d[row][col + 1] == '.' and board2d[row][col + 2] in opponentPiece)):
        board = deepcopy(board2d)
        board[row][col + 3] = board[row][col]
        board[row][col] = '.'
        board[row][col + 1] = '.'
        board[row][col + 2] = '.'
        kill_moves.append(board)
    # Move North
    if player == 'b' and board2d[row][col] == 'B':
        # One step
        if row >= 1 and board2d[row - 1][col] == '.':
            board = deepcopy(board2d)
            if row - 1 == 0:
                board[row - 1][col] = '$'
            else:
                board[row - 1][col] = 'B'
            board[row][col] = '.'
            moves.append(board)
        elif row >= 2 and board2d[row - 1][col] in opponentPiece and board2d[row - 2][col] == '.':
            board = deepcopy(board2d)
            if row - 2 == 0:
                board[row - 2][col] = '$'
            else:
                board[row - 2][col] = 'B'
            board[row][col] = '.'
            board[row - 1][col] = '.'
            kill_moves.append(board)
        # two step
        if row >= 2 and board2d[row - 1][col] == '.' and board2d[row - 2][col] == '.':
            board = deepcopy(board2d)
            if row - 2 == 0:
                board[row - 2][col] = '$'
            else:
                board[row - 2][col] = 'B'
            board[row][col] = '.'
            moves.append(board)
        if row >= 3 and board2d[row - 3][col] == '.' and (
                (board2d[row - 1][col] in opponentPiece and board2d[row - 2][col] == '.') or (
                board2d[row - 1][col] == '.' and board2d[row - 2][col] in opponentPiece)):
            board = deepcopy(board2d)
            if row -3 == 0:
                board[row - 3][col] = '$'
            else:
                board[row - 3][col] = 'B'
            board[row][col] = '.'
            board[row - 1][col] = '.'
            board[row - 2][col] = '.'
            kill_moves.append(board)

    # Move south
    if player == 'w' and board2d[row][col] == 'W':
        # One step
        if row <= N-2 and board2d[row + 1][col] == '.':
            board = deepcopy(board2d)
            if row + 1 == N-1:
                board[row + 1][col] = '@'
            else:
                board[row + 1][col] = 'W'
            board[row][col] = '.'
            moves.append(board)
        elif row <= N-3 and board2d[row + 1][col] in opponentPiece and board2d[row + 2][col] == '.':
            board = deepcopy(board2d)
            if row + 2 == N-1:
                board[row + 2][col] = '@'
            else:
                board[row + 2][col] = 'W'
            board[row][col] = '.'
            board[row + 1][col] = '.'
            kill_moves.append(board)
        # two step
        if row <= N-3 and board2d[row + 1][col] == '.' and board2d[row + 2][col] == '.':
            board = deepcopy(board2d)
            if row + 2 == N-1:
                board[row + 2][col] = '@'
            else:
                board[row + 2][col] = 'W'
            board[row][col] = '.'
            moves.append(board)
        if row <= N-4 and board2d[row + 3][col] == '.' and (
                (board2d[row + 1][col] in opponentPiece and board2d[row + 2][col] == '.') or (
                board2d[row + 1][col] == '.' and board2d[row + 2][col] in opponentPiece)):
            board = deepcopy(board2d)
            if row + 3 == N-1:
                board[row + 3][col] = '@'
            else:
                board[row + 3][col] = 'W'
            board[row][col] = '.'
            board[row + 1][col] = '.'
            board[row + 2][col] = '.'
            kill_moves.append(board)
    return (moves,kill_moves)


def getMovesForRaichu(player, board2d , row, col):
    m = []
    k = []
    # All possible moves in north direction
    moves, kill_moves = moveNorth(player, deepcopy(board2d), row, col)
    m.extend(deepcopy(moves))
    k.extend(deepcopy(kill_moves))

    # All possible moves in south direction
    moves, kill_moves = moveSouth(player, deepcopy(board2d), row, col)
    m.extend(deepcopy(moves))
    k.extend(deepcopy(kill_moves))

    # All possible move in west direction
    moves, kill_moves = moveWest(player, deepcopy(board2d), row, col)
    m.extend(deepcopy(moves))
    k.extend(deepcopy(kill_moves))

    # All possible move in east direction
    moves, kill_moves = moveEast(player, deepcopy(board2d), row, col)
    m.extend(deepcopy(moves))
    k.extend(deepcopy(kill_moves))

    # All possible move in North West direction
    moves, kill_moves = moveNorthWest(player, deepcopy(board2d), row, col)
    m.extend(deepcopy(moves))
    k.extend(deepcopy(kill_moves))

    # All possible move in South West direction
    moves, kill_moves = moveSouthWest(player, deepcopy(board2d), row, col)
    m.extend(deepcopy(moves))
    k.extend(deepcopy(kill_moves))

    # All possible move in North East direction
    moves, kill_moves = moveNorthEast(player, deepcopy(board2d), row, col)
    m.extend(deepcopy(moves))
    k.extend(deepcopy(kill_moves))

    # All possible move in South East direction
    moves, kill_moves = moveSouthEast(player, deepcopy(board2d), row, col)
    m.extend(deepcopy(moves))
    k.extend(deepcopy(kill_moves))

    return (m,k)

def successors(player, board2d):
    N = len(board2d)
    succ = []
    for row in range(N):
        for col in range(N):
            if board2d[row][col] == '.':
                continue
            # get all possible moves for all Pichus on board
            if board2d[row][col] in 'wb':
                succ.extend(getMovesForPichu(player,deepcopy(board2d), row, col))

            # Get all possible moves for all Pikachus on Board
            if player == 'w' and board2d[row][col] == 'W':
                moves, kill_moves = getMovesForPikachu(player,deepcopy(board2d), row, col)
                succ =  deepcopy(kill_moves) + succ + deepcopy(moves)

            if player == 'b' and board2d[row][col] == 'B':
                moves, kill_moves = getMovesForPikachu(player, deepcopy(board2d), row, col)
                succ = deepcopy(kill_moves) + succ + deepcopy(moves)

            # Get all possible moves for all Raichus on board
            if player == 'w' and board2d[row][col] == '@':
                m,k = getMovesForRaichu(player, deepcopy(board2d), row, col)
                succ = deepcopy(k) + succ + deepcopy(m)


            if player == 'b' and board2d[row][col] == '$':
                m, k = getMovesForRaichu(player, deepcopy(board2d), row, col)
                succ = deepcopy(k) + succ + deepcopy(m)

    return succ

def is_win(player, move, N):
    if player == 'w':
        piece = 'wW@'
    else:
        piece = 'bB$'
    for row in range(N):
        for col in range(N):
            if move[row][col] not in piece:
                return False

    return True

def is_loose(player, move, N):
    if player == 'w':
        opponent_piece = 'bB$'
    else:
        opponent_piece = 'wW@'

    for row in range(N):
        for col in range(N):
            if move[row][col] not in opponent_piece:
                return False

    return True


def evaluateLeaf(player, move, N):
    if is_win(player, move, N):
        return 1000
    if is_loose(player, move, N):
        return -1000

    if player == 'w':
        piece = 'wW@'
        opponent_piece = 'bB$'
    else:
        piece = 'bB$'
        opponent_piece = 'wW@'
    score = 0
    for row in range(N):
        for col in range(N):
            if move[row][col] == piece[0]:
                score += 100
            elif move[row][col] == piece[1]:
                score += 200
            elif move[row][col] == piece[2]:
                score += 500
            elif move[row][col] == opponent_piece[0]:
                score -= 100
            elif move[row][col] == opponent_piece[1]:
                score -= 200
            elif move[row][col] == opponent_piece[2]:
                score -= 500
    return score

# The minmax algorithim has been referenced from https://www.javatpoint.com/mini-max-algorithm-in-ai

def minimax(player, move, depth, isMaximizingPlayer, alpha, beta):
    if depth == 0:
        return evaluateLeaf(player, move, len(move))
    if player == 'w':
        opponentPlayer = 'b'
    else:
        opponentPlayer = 'w'
    if isMaximizingPlayer:
        bestValue = -9999999999
        for move in successors(player,deepcopy(move)):
            value = minimax(opponentPlayer, deepcopy(move), depth-1, False, alpha , beta)
            bestValue = max(bestValue, value)
            alpha = max(alpha, bestValue)
            if beta <= alpha:
                break
        return bestValue
    else:
        bestValue = 9999999999
        for move in successors(player, deepcopy(move)):
            value = minimax(opponentPlayer, deepcopy(move), depth-1, True, alpha, beta)
            bestValue = min(bestValue, value)
            beta = min(alpha, bestValue)
            if beta <= alpha:
                break
        return bestValue


def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    board2d = oneDtotwoD(deepcopy(board), N)
    if player == 'w':
        opponent_player = 'b'
    else:
        opponent_player = 'w'
    print("Initial board")
    for row in board2d:
        print(row)
    best_value = -9999999999
    depth = 4
    alpha = -9999999999
    beta = 9999999999
    best_move = deepcopy(board2d)

    for move in successors(player, deepcopy(board2d)):
        value = minimax(opponent_player, deepcopy(move), depth - 1, False, alpha, beta)
        if (value > best_value):
            best_value = value
            best_move = deepcopy(move)

        alpha = max(best_value, alpha)
        if beta <= alpha:
            break
        yield board_to_string(best_move, N)
    yield board_to_string(best_move, N)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")

    (_, N, player, board, timelimit) = sys.argv
    N = int(N)
    timelimit = int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N * N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)
