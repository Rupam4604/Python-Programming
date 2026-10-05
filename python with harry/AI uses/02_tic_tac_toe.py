"""A simple two-player Tic-Tac-Toe game.

Build steps:
1. Open a Python environment.
2. Run this file with Python.
3. Players take turns entering numbers 1-9 to place X and O.
4. The first player to complete a row, column, or diagonal wins.
"""
def greet_players() -> None:
    """Greet the players and explain the rules."""
    print("Welcome to Tic-Tac-Toe!")
    print("Players take turns entering numbers 1-9 to place X and O.")
    print("The first player to complete a row, column, or diagonal wins.")
    print("If all positions are filled without a winner, the game is a draw.\n")

def display_board(board: list[str]) -> None:
    """Display the board using positions for empty cells."""
    cells = [value if value else str(index) for index, value in enumerate(board, 1)]
    print(f"\n {cells[0]} | {cells[1]} | {cells[2]}")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]}")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]}\n")


def check_winner(board: list[str], player: str) -> bool:
    """Return whether player occupies a complete row, column, or diagonal."""
    winning_lines = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    return any(all(board[index] == player for index in line) for line in winning_lines)


def get_move(board: list[str], player: str) -> int:
    """Read and validate a player's chosen board position."""
    while True:
        choice = input(f"Player {player}, choose a position (1-9): ").strip()
        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice) - 1
        if board[position]:
            print("That position is already occupied.")
            continue
        return position


def play_game() -> None:
    """Run one complete game."""
    greet_players()
    board = [""] * 9
    player = "X"

    for turn in range(9):
        display_board(board)
        board[get_move(board, player)] = player

        if check_winner(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            return

        if turn == 8:
            display_board(board)
            print("It's a draw!")
            return

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    play_game()
