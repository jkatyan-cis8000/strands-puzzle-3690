# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

```
src/
├── __init__.py
├── board.py          # 6x8 grid state, letter placement, cell state management
├── word_finder.py    # Path finding, word validation, adjacent cell logic
├── game.py           # Core game logic: theme words, spangram, hints, win condition
├── hint_system.py    # Non-theme word tracking and hint unlocking logic
├── ui.py             # Terminal rendering, user input parsing, display formatting
└── data/
    ├── words.json    # Theme words, spangrams, and non-theme words for puzzles
    └── puzzles.json  # Pre-defined puzzle configurations
```

## Interfaces

### board.py
- `Board`: Class managing 6x8 grid
  - `__init__()`: Initialize empty grid
  - `place_letter(row, col, letter)`: Place a letter at position
  - `get_letter(row, col) -> str`: Get letter at position
  - `is_valid_cell(row, col) -> bool`: Check if cell is within bounds
  - `mark_cell_active(row, col)`: Mark cell as selected
  - `mark_cell_revealed(row, col)`: Mark cell as revealed by word
  - `is_revealed(row, col) -> bool`: Check if cell is revealed
  - `clear_selection()`: Clear active selection
  - `is_full() -> bool`: Check if all cells have letters

### word_finder.py
- `WordFinder`: Path finding and word validation
  - `find_words(board) -> list[Path]`: Find all possible paths of length 3+
  - `get_adjacent_cells(row, col) -> list[tuple[int, int]]`: Get neighboring cells
  - `validate_path(path) -> bool`: Check path doesn't revisit cells
  - `path_to_word(path, board) -> str`: Convert path to string

### game.py
- `Game`: Core game state and logic
  - `__init__(theme_words: list[str], spangram: str)`: Initialize game
  - `find_word(word: str) -> tuple[bool, str]`: Try to find word in grid
  - `is_spangram(word: str) -> bool`: Check if word is the spangram
  - `is_theme_word(word: str) -> bool`: Check if word is a theme word
  - `is_solved() -> bool`: Check if all theme words found and board full
  - `get_revealed_cells() -> set[tuple[int, int]]`: Get all revealed cell positions

### hint_system.py
- `HintSystem`: Hint tracking and unlocking
  - `__init__()`: Initialize counter
  - `add_non_theme_word() -> int`: Increment counter, return current count
  - `is_hint_available() -> bool`: Check if 3 non-theme words found
  - `use_hint() -> bool`: Mark hint as used, return success

### ui.py
- `UI`: Terminal interface
  - `display_board(board)`: Render the grid to terminal
  - `display_game_status(game)`: Show score, hints, remaining words
  - `parse_input(input_str) -> str | None`: Parse user input, return word or None
  - `display_message(msg)`: Show feedback message
  - `display_theme(theme: str)`: Show the theme category

### data/words.json
- Contains sample words grouped by themes
- Each theme has: theme name, list of theme words, spangram

### data/puzzles.json
- Contains complete puzzle definitions
- Each puzzle: theme, 5-8 theme words, one spangram

## Shared Data Structures

```python
# Cell state
CellState = {
    "empty": "",
    "active": "selected by player",
    "revealed": "part of found word",
    "locked": "fixed letter from puzzle"
}

# Path representation
Path = list[tuple[int, int]]  # List of (row, col) coordinates

# Found word result
FoundWord = {
    "word": str,
    "path": Path,
    "type": "theme" | "spangram" | "non-theme",
    "score": int
}

# Game state summary
GameState = {
    "board": list[list[str]],  # Current grid letters
    "found_words": list[FoundWord],
    "revealed_cells": set[tuple[int, int]],
    "hints_available": int,
    "puzzle_complete": bool
}
```

## External Dependencies

- **Python standard library only**: No external dependencies required
  - `json` for data files
  - `os` for path handling
  - `random` for shuffling words
  - `typing` for type hints

## Word Finding Rules

1. Words can be formed by connecting adjacent letters in any direction
2. Adjacent includes: up, down, left, right, and all 4 diagonals (8 directions)
3. Words can change direction mid-word
4. Cannot revisit the same cell in a single word
5. Minimum word length: 3 letters
6. The spangram must touch two opposite sides of the board

## Scoring

- Theme words: 10 points each
- Spangram: 50 points (bonus for finding the special word)
- Non-theme words: 5 points each (also unlocks hints)
