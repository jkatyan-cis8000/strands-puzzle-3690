import json
import os
import random
from typing import Optional

from .board import Board
from .word_finder import WordFinder
from .game import Game
from .hint_system import HintSystem
from .ui import UI


def load_puzzles() -> list[dict]:
    """Load puzzles from data/puzzles.json."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    puzzles_path = os.path.join(script_dir, "data", "puzzles.json")
    
    with open(puzzles_path, "r") as f:
        data = json.load(f)
    
    return data.get("puzzles", [])


def select_puzzle(puzzles: list[dict], theme_name: Optional[str] = None) -> dict:
    """Select a puzzle, optionally by theme name."""
    if theme_name:
        for puzzle in puzzles:
            if puzzle["theme"].upper() == theme_name.upper():
                return puzzle
    
    return random.choice(puzzles)


def initialize_game(puzzle: dict) -> tuple[Board, Game, HintSystem]:
    """Initialize game with puzzle data."""
    theme = puzzle["theme"]
    spangram = puzzle["spangram"]
    words = puzzle["words"]
    
    board = Board()
    game = Game(words, spangram)
    hint_system = HintSystem()
    
    return board, game, hint_system


def handle_input(ui: UI, board: Board, game: Game, hint_system: HintSystem, word: str) -> tuple[bool, bool]:
    """Process user input. Returns (game_continues, word_was_valid)."""
    if word is None:
        return True, False
    
    found, message = game.find_word(word)
    
    if found:
        ui.display_message(message)
        return True, True
    else:
        ui.display_message(message)
        return True, False


def run_game_loop(ui: UI, board: Board, game: Game, hint_system: HintSystem, theme: str) -> None:
    """Run the main game loop."""
    while True:
        ui.clear_screen()
        ui.display_theme(theme)
        ui.display_board(board)
        ui.display_game_status(game, hint_system)
        
        if game.is_solved(board.is_full()):
            ui.display_win()
            break
        
        user_input = ui.get_user_input()
        word = ui.parse_input(user_input)
        
        if word is None:
            continue
        
        if word == "QUIT":
            break
        
        if word == "HINT" and hint_system.is_hint_available():
            hint_system.use_hint()
            ui.display_message("Hint used!")
            continue
        
        _, _ = handle_input(ui, board, game, hint_system, word)


def main() -> None:
    """Main entry point."""
    puzzles = load_puzzles()
    puzzle = select_puzzle(puzzles)
    
    theme = puzzle["theme"]
    spangram = puzzle["spangram"]
    words = puzzle["words"]
    
    board = Board()
    game = Game(words, spangram)
    hint_system = HintSystem()
    
    ui = UI()
    run_game_loop(ui, board, game, hint_system, theme)


if __name__ == "__main__":
    main()
