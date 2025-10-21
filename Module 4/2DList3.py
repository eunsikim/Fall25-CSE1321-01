def main():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    for r in board:
        for c in r:
            print(c, end="")
        print()
    
    print()

    # Player 1's move (X)
    row = int(input())
    col = int(input())
    board[row][col] = "X"

    for r in board:
        for c in r:
            print(c, end="")
        print()
    
    print()

    # Player 2's move (0)
    board[1][1] = "O"

    for r in board:
        for c in r:
            print(c, end="")
        print()
    
    print()

    # Player 1's move (X)
    board[2][0] = "X"

    for r in board:
        for c in r:
            print(c, end="")
        print()
    
    print()

    # Player 2's move (0)
    board[1][0] = "O"

    for r in board:
        for c in r:
            print(c, end="")
        print()
    
    print()



if __name__ == "__main__":
    main()