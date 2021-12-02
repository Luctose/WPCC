"""
Lucas Sarweh
110042658
Date: 11 Jan 2021
"""

# Checks if there is a connect 4
def connect4(board):
    # Keeps track of chains
    connects1 = 0
    connects2 = 0

    # Horizontal
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                connects1 += 1
                connects2 = 0
            elif board[row][col] == 2:
                connects2 += 1
                connects1 = 0
            elif board[row][col] == 0:
                connects1 = 0
                connects2 = 0
            if connects1 >= 4:
                return True
            elif connects2 >= 4:
                return True
    
    # Vertical
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[col][row] == 1:
                connects1 += 1
                connects2 = 0
            elif board[col][row] == 2:
                connects2 += 1
                connects1 = 0
            elif board[col][row] == 0:
                connects1 = 0
                connects2 = 0
            if connects1 >= 4:
                return True
            elif connects2 >= 4:
                return True
    
    # Left to right diagonal
    for row in range(len(board)):
        for col in range(len(board[row])):
            pass
    
    return False
                

# Main function
def main():
    pass

if __name__ == "__main__":
    main()