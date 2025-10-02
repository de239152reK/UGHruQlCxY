# 代码生成时间: 2025-10-02 17:23:59
import numpy as np

"""
ThemeSwitcher class for switching themes based on user preference.
This class demonstrates the use of Numpy for handling color values and
provides a basic structure for theme management.
"""

class ThemeData:
    """
    A class to hold theme data.
    """
    def __init__(self, name, background_color, text_color):
        """
        Initialize ThemeData with a name and color values.
        :param name: The name of the theme.
        :param background_color: The background color in RGB format.
        :param text_color: The text color in RGB format.
        """
        self.name = name
        self.background_color = np.array(background_color, dtype=np.uint8)
        self.text_color = np.array(text_color, dtype=np.uint8)

    def __str__(self):
        """
        String representation of the theme data.
        """
        return f"{self.name}: Background - {self.background_color}, Text - {self.text_color}"

class ThemeSwitcher:
    """
    A class to manage themes and switch between them.
    """
    def __init__(self):
        """
        Initialize the ThemeSwitcher with a dictionary of themes.
        """
        self.themes = {}

    def add_theme(self, theme_name, background_color, text_color):
        """
        Add a new theme to the switcher.
        :param theme_name: The name of the theme.
        :param background_color: The background color in RGB format.
        :param text_color: The text color in RGB format.
        """
        if theme_name in self.themes:
            raise ValueError(f"Theme '{theme_name}' already exists.")
        self.themes[theme_name] = ThemeData(theme_name, background_color, text_color)

    def get_theme(self, theme_name):
        """
        Get a theme by its name.
        :param theme_name: The name of the theme to retrieve.
        :return: The ThemeData object associated with theme_name.
        """
        if theme_name not in self.themes:
            raise ValueError(f"Theme '{theme_name}' does not exist.")
        return self.themes[theme_name]

    def switch_theme(self, theme_name):
        """
        Switch to the specified theme.
        :param theme_name: The name of the theme to switch to.
        """
        try:
            current_theme = self.get_theme(theme_name)
            print(f"Switched to theme: {current_theme}")
        except ValueError as e:
            print(e)

# Example usage
if __name__ == '__main__':
    theme_switcher = ThemeSwitcher()
    theme_switcher.add_theme('Dark', [0, 0, 0], [255, 255, 255])
    theme_switcher.add_theme('Light', [255, 255, 255], [0, 0, 0])
    theme_switcher.switch_theme('Dark')
    theme_switcher.switch_theme('Light')
