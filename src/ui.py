import os
from typing import Optional


class UI:
    """Terminal interface for the Strands puzzle."""
    
    COLORS = {
        "blue": "\033[34m",
        "yellow": "\033[33m",
        "reset": "\033[0m",
        "bold": "\033[1m"
    }
    
    def __init__(self):
        """Initialize UI."""
        self._last_message = ""
    
    def clear_screen(self) -> None:
        """Clear terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_board(self, board) -> None:
        """Render the 6x8 grid to terminal with color-coded highlighting."""
        grid = board.get_grid()
        state = board.get_state()
        
        print("\n┌───┬───┬───┬───┬───┬───┬───┬───┐")
        
        for row in range(6):
            print("│", end="")
            for col in range(8):
                letter = grid[row][col] if grid[row][col] else " "
                cell_state = state[row][col]
                
                if cell_state == "revealed":
                    print(f" {self.COLORS['blue']}{letter}{self.COLORS['reset']}\033[39m │", end="")
                elif cell_state == "active":
                    print(f" {self.COLORS['bold']}{letter}{self.COLORS['reset']}\033[39m │", end="")
                else:
                    print(f" {letter} │", end="")
            
            if row < 5:
                print("\n├───┼───┼───┼───┼───┼───┼───┼───┤")
            else:
                print("\n└───┴───┴───┴───┴───┴───┴───┴───┘")
    
    def display_theme(self, theme: str) -> None:
        """Display the theme category."""
        print(f"\n{self.COLORS['bold']}STRANDS{self.COLORS['reset']}")
        print(f"Theme: {theme}")
        print("-" * 40)
    
    def display_game_status(self, game, hint_system) -> None:
        """Display game status: found words, hints available."""
        print("\n[Found Words]")
        
        found = game.get_found_words()
        theme_words = game.get_theme_words()
        
        if found:
            for word in found:
                if word == game.get_spangram():
                    print(f"  {self.COLORS['yellow']}{word}{self.COLORS['reset']} (Spangram!)")
                elif word in theme_words:
                    print(f"  {self.COLORS['blue']}{word}{self.COLORS['reset']}")
                else:
                    print(f"  {word}")
        else:
            print("  (none yet)")
        
        print(f"\n[Hints]")
        non_theme_count = hint_system.get_non_theme_count()
        print(f"  Non-theme words found: {non_theme_count}/3")
        
        if hint_system.is_hint_available():
            print(f"  {self.COLORS['yellow']}HINT AVAILABLE!{self.COLORS['reset']}")
        else:
            print("  (need 3 non-theme words for hint)")
    
    def parse_input(self, input_str: str) -> Optional[str]:
        """Parse user input, return word or None."""
        if not input_str:
            return None
        
        word = input_str.strip().upper()
        
        if not word:
            return None
        
        return word
    
    def display_message(self, msg: str) -> None:
        """Display feedback message."""
        print(f"\n{msg}")
        self._last_message = msg
    
    def get_user_input(self, prompt: str = "> ") -> str:
        """Get input from user."""
        return input(prompt)
    
    def display_win(self) -> None:
        """Display win message."""
        print(f"\n{self.COLORS['yellow']}{self.COLORS['bold']}🎉 PUZZLE SOLVED! 🎉{self.COLORS['reset']}")
        print(f"{self.COLORS['bold']}You found all theme words and the spangram!{self.COLORS['reset']}")
