from typing import Set


class Game:
    """Core game state and logic."""
    
    def __init__(self, theme_words: list[str], spangram: str, word_finder=None):
        """Initialize game with theme words and spangram."""
        self._theme_words = set(word.upper() for word in theme_words)
        self._spangram = spangram.upper()
        self._all_valid_words = self._theme_words | {self._spangram}
        self._found_words: list[str] = []
        self._found_spangram = False
        self._word_finder = word_finder
        self._found_paths: dict[str, list[tuple[int, int]]] = {}
    
    def set_word_finder(self, word_finder) -> None:
        """Set word finder for path finding."""
        self._word_finder = word_finder
    
    def find_word(self, word: str, path: list[tuple[int, int]] = None) -> tuple[bool, str]:
        """Try to find word in grid. Returns (success, message)."""
        word_upper = word.upper()
        
        if word_upper in self._found_words or (word_upper == self._spangram and self._found_spangram):
            return False, "Already found"
        
        if word_upper == self._spangram:
            self._found_spangram = True
            self._found_words.append(word_upper)
            self._found_paths[word_upper] = path or []
            return True, "Spangram found!"
        
        if word_upper in self._theme_words:
            if word_upper not in self._found_words:
                self._found_words.append(word_upper)
                self._found_paths[word_upper] = path or []
                return True, "Theme word found!"
            return False, "Already found"
        
        if word_upper in self._all_valid_words:
            return False, "Already found"
        
        return False, "Not a valid word"
    
    def is_spangram(self, word: str) -> bool:
        """Check if word is the spangram."""
        return word.upper() == self._spangram
    
    def is_theme_word(self, word: str) -> bool:
        """Check if word is a theme word."""
        return word.upper() in self._theme_words
    
    def is_valid_word(self, word: str) -> bool:
        """Check if word is valid (theme or spangram)."""
        return word.upper() in self._all_valid_words
    
    def is_solved(self, board_full: bool) -> bool:
        """Check if all theme words found and board full."""
        return board_full and self._found_spangram and len(self._found_words) >= len(self._theme_words)
    
    def get_revealed_cells(self) -> set[tuple[int, int]]:
        """Get all revealed cell positions."""
        revealed = set()
        for path in self._found_paths.values():
            revealed.update(path)
        return revealed
    
    def get_found_words(self) -> list[str]:
        """Get list of found words."""
        return self._found_words.copy()
    
    def get_theme_words(self) -> list[str]:
        """Get list of theme words."""
        return list(self._theme_words)
    
    def get_spangram(self) -> str:
        """Get the spangram."""
        return self._spangram
    
    def is_spangram_found(self) -> bool:
        """Check if spangram has been found."""
        return self._found_spangram
    
    def add_found_word_path(self, word: str, path: list[tuple[int, int]]) -> None:
        """Record path for found word."""
        word_upper = word.upper()
        self._found_paths[word_upper] = path
        if word_upper not in self._found_words:
            self._found_words.append(word_upper)
    
    def get_found_path(self, word: str) -> list[tuple[int, int]]:
        """Get path for found word."""
        return self._found_paths.get(word.upper(), [])
