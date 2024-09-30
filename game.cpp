
#include <iostream>
#include <vector>

// Function to draw the Tic Tac Toe board
void drawBoard(const std::vector<char>& board) {
    std::cout << " " << board[0] << " | " << board[1] << " | " << board[2] << "\n";
    std::cout << "-----------\n";
    std::cout << " " << board[3] << " | " << board[4] << " | " << board[5] << "\n";
    std::cout << "-----------\n";
    std::cout << " " << board[6] << " | " << board[7] << " | " << board[8] << "\n";
}

// Function to check if a player has won
bool checkWin(const std::vector<char>& board, char player) {
    // Check rows
    for (int i = 0; i < 9; i += 3) {
        if (board[i] == player && board[i + 1] == player && board[i + 2] == player) {
            return true;
        }
    }

    // Check columns
    for (int i = 0; i < 3; i++) {
        if (board[i] == player && board[i + 3] == player && board[i + 6] == player) {
            return true;
        }
    }

    // Check diagonals
    if ((board[0] == player && board[4] == player && board[8] == player) ||
        (board[2] == player && board[4] == player && board[6] == player)) {
        return true;
    }

    return false;
}

// Function to check if the game is a draw
bool checkDraw(const std::vector<char>& board) {
    for (char cell : board) {
        if (cell == '-') {
            return false;
        }
    }
    return true;
}

// Function to handle player move
void playerMove(std::vector<char>& board, char player) {
    int move;
    std::cout << "Player " << player << ", enter your move (1-9): ";
    std::cin >> move;

    // Validate move
    if (move < 1 || move > 9) {
        std::cout << "Invalid move. Please try again.\n";
        playerMove(board, player);
        return;
    }

    // Check if cell is occupied
    if (board[move - 1] != '-') {
        std::cout << "Cell already occupied. Please try again.\n";
        playerMove(board, player);
        return;
    }

    board[move - 1] = player;
}

int main() {
    std::vector<char> board(9, '-');
    char currentPlayer = 'X';

    while (true) {
        drawBoard(board);
        playerMove(board, currentPlayer);

        // Check win condition
        if (checkWin(board, currentPlayer)) {
            drawBoard(board);
            std::cout << "Player " << currentPlayer << " wins!\n";
            break;
        }

        // Check draw condition
        if (checkDraw(board)) {
            drawBoard(board);
            std::cout << "It's a draw!\n";
            break;
        }

        // Switch player
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    return 0;
}

