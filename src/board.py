from typing import Optional


CellState = {
    "empty": "",
    "active": "selected by player",
    "revealed": "part of found word",
    "locked": "fixed letter from puzzle"
}


class Board:
    """6x8 grid for the Strands puzzle."""
    
    def __init__(self):
        """Initialize empty 6x8 grid."""
        self._grid: list[list[str]] = [[ "" for _ in range(8) ] for _ in range(6)]
        self._cell_state: list[list[str]] = [[ "empty" for _ in range(8) ] for _ in range(6)]
        self._active_cells: list[tuple[int, int]] = []
    
    def place_letter(self, row: int, col: int, letter: str) -> None:
        """Place a letter at position."""
        if self.is_valid_cell(row, col):
            self._grid[row][col] = letter
            self._cell_state[row][col] = "locked"
    
    def get_letter(self, row: int, col: int) -> str:
        """Get letter at position."""
        if self.is_valid_cell(row, col):
            return self._grid[row][col]
        return ""
    
    def is_valid_cell(self, row: int, col: int) -> bool:
        """Check if cell is within bounds."""
        return 0 <= row < 6 and 0 <= col < 8
    
    def mark_cell_active(self, row: int, col: int) -> None:
        """Mark cell as selected."""
        if self.is_valid_cell(row, col):
            self._cell_state[row][col] = "active"
            self._active_cells.append((row, col))
    
    def mark_cell_revealed(self, row: int, col: int) -> None:
        """Mark cell as revealed by word."""
        if self.is_valid_cell(row, col):
            self._cell_state[row][col] = "revealed"
    
    def is_revealed(self, row: int, col: int) -> bool:
        """Check if cell is revealed."""
        if self.is_valid_cell(row, col):
            return self._cell_state[row][col] == "revealed"
        return False
    
    def clear_selection(self) -> None:
        """Clear active selection."""
        for row, col in self._active_cells:
            if self.is_valid_cell(row, col):
                self._cell_state[row][col] = "empty"
        self._active_cells = []
    
    def is_full(self) -> bool:
        """Check if all cells have letters."""
        for row in range(6):
            for col in range(8):
                if not self._grid[row][col]:
                    return False
        return True
    
    def get_grid(self) -> list[list[str]]:
        """Get the current grid state."""
        return [row[:] for row in self._grid]
    
    def get_state(self) -> list[list[str]]:
        """Get the current cell state."""
        return [row[:] for row in self._cell_state]
