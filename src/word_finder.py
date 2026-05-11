from typing import List, Tuple, Set

Path = List[Tuple[int, int]]


class WordFinder:
    """Path finding and word validation."""
    
    DIRECTIONS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    def __init__(self, valid_words: Set[str]):
        """Initialize word finder with valid words list."""
        self._valid_words = valid_words
    
    def get_adjacent_cells(self, row: int, col: int, board) -> List[Tuple[int, int]]:
        """Get neighboring cells in all 8 directions."""
        adjacent = []
        for dr, dc in self.DIRECTIONS:
            new_row, new_col = row + dr, col + dc
            if board.is_valid_cell(new_row, new_col):
                adjacent.append((new_row, new_col))
        return adjacent
    
    def validate_path(self, path: Path) -> bool:
        """Check path doesn't revisit cells."""
        return len(path) == len(set(path))
    
    def path_to_word(self, path: Path, board) -> str:
        """Convert path to string."""
        word = ""
        for row, col in path:
            letter = board.get_letter(row, col)
            word += letter
        return word
    
    def find_words(self, board) -> List[Tuple[Path, str]]:
        """Find all valid words in grid."""
        found_words = []
        grid = board.get_grid()
        
        for row in range(6):
            for col in range(8):
                if grid[row][col]:
                    self._dfs_paths(row, col, [(row, col)], found_words, board)
        
        return found_words
    
    def _dfs_paths(self, row: int, col: int, current_path: Path, found_words: List[Tuple[Path, str]], board) -> None:
        """Depth-first search for all valid paths and words."""
        if len(current_path) >= 3:
            word = self.path_to_word(current_path, board)
            if word in self._valid_words:
                found_words.append((current_path[:], word))
        
        for next_row, next_col in self.get_adjacent_cells(row, col, board):
            if (next_row, next_col) not in current_path:
                current_path.append((next_row, next_col))
                self._dfs_paths(next_row, next_col, current_path, found_words, board)
                current_path.pop()
