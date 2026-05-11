class HintSystem:
    """Track non-theme words and hint unlocking."""
    
    def __init__(self):
        """Initialize counter."""
        self._non_theme_count = 0
        self._hint_used = False
    
    def add_non_theme_word(self) -> int:
        """Increment counter, return current count."""
        self._non_theme_count += 1
        return self._non_theme_count
    
    def is_hint_available(self) -> bool:
        """Check if 3 non-theme words found."""
        return self._non_theme_count >= 3 and not self._hint_used
    
    def use_hint(self) -> bool:
        """Mark hint as used, return success."""
        if self.is_hint_available():
            self._hint_used = True
            return True
        return False
    
    def get_non_theme_count(self) -> int:
        """Get count of non-theme words found."""
        return self._non_theme_count
