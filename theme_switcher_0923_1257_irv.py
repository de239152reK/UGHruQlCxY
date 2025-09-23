# 代码生成时间: 2025-09-23 12:57:26
import numpy as np

class ThemeSwitcher:
    """
    A class to manage different themes.
    """
    def __init__(self):
        """
        Initialize the theme switcher with a default theme.
        """
        self.themes = {
            'dark': {'bg_color': '#000000', 'text_color': '#FFFFFF'},
            'light': {'bg_color': '#FFFFFF', 'text_color': '#000000'}
        }
        self.current_theme = 'light'

    def switch_theme(self, new_theme):
        """
        Switch to a new theme.
        
        Args:
        new_theme (str): The name of the theme to switch to.
        
        Raises:
        ValueError: If the new theme is not available.
        """
        if new_theme not in self.themes:
            raise ValueError(f"Theme '{new_theme}' not found. Available themes: {list(self.themes.keys())}")

        self.current_theme = new_theme
        self.apply_theme()
        print(f"Switched to {self.current_theme} theme.")

    def apply_theme(self):
        """
        Apply the current theme.
        """
        theme = self.themes[self.current_theme]
        # This is where you would apply the theme to your application,
        # such as setting background colors, text colors, etc.
        # Here we just print the theme colors for demonstration purposes.
        print(f"Background color: {theme['bg_color']}, Text color: {theme['text_color']}")

    def get_current_theme(self):
        """
        Get the current theme.
        
        Returns:
        str: The name of the current theme.
        """
        return self.current_theme

# Example usage:
if __name__ == '__main__':
    switcher = ThemeSwitcher()
    try:
        switcher.switch_theme('dark')
        switcher.switch_theme('light')
        switcher.switch_theme('unknown')  # This should raise an error
    except ValueError as e:
        print(e)
