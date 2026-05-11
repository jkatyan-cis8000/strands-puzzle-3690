# Strands Puzzle

A terminal-based word puzzle game inspired by the New York Times Strands.

## Game Rules

Strands is a word-finding puzzle where you must find all the theme words and the special "spangram" in a 6x8 grid of letters.

### How to Play

1. **Find Theme Words**: Connect adjacent letters to form words related to the current theme.
2. **Find the Spangram**: There's one special word (the spangram) that must be found. It's indicated by a yellow color when revealed.
3. **Theme words** are shown in blue when revealed.

### Word Rules

- Words can be formed by connecting adjacent letters in any direction (horizontal, vertical, or diagonal)
- Letters can change direction mid-word
- Cannot revisit the same cell in a single word
- Minimum word length: 3 letters
- The spangram must touch two opposite sides of the board

### Scoring

- Theme words: 10 points each
- Spangram: 50 points (bonus)
- Non-theme words: 5 points each (also unlocks hints)

### Hints

- Finding 3 non-theme words unlocks a hint
- Use the hint by typing `HINT` during gameplay

## Installation

```bash
git clone <repository-url>
cd strands-puzzle
```

## Usage

Run the game:

```bash
python -m src.main
```

### Controls

- Type words to submit them
- Type `HINT` to use an available hint
- Type `QUIT` to exit the game

### Game States

- **Blue letters**: Part of a found theme word
- **Yellow letters**: Part of the spangram
- **Normal letters**: Not yet revealed

## Puzzle Themes

The game includes multiple pre-defined puzzles:

- **SOLAR SYSTEM**: Space-related words
- **OCEAN LIFE**: Marine biology words  
- **BIRDS**: Avian-themed words

## File Structure

```
src/
├── __init__.py
├── main.py          # Entry point
├── board.py         # 6x8 grid state
├── word_finder.py   # Path finding and validation
├── game.py          # Core game logic
├── hint_system.py   # Hint tracking
├── ui.py            # Terminal interface
└── data/
    ├── words.json   # Theme words and spangrams
    └── puzzles.json # Puzzle configurations
```

## Development

The project uses only Python standard library - no external dependencies required.

## Author

Built as part of the Strands puzzle implementation project.
