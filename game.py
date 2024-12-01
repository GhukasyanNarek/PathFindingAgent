import pygame
from spot import Spot

# Define colors
WHITE = (255, 255, 255)
GREY = (128, 128, 128)


class Game:
    """
    A collection of static methods for managing the grid and game-related operations.
    """

    @staticmethod
    def make_grid(rows, width):
        """
        Creates a grid of Spot objects.

        Args:
            rows (int): The number of rows (and columns) in the grid.
            width (int): The width of the grid in pixels.

        Returns:
            list: A 2D list of Spot objects representing the grid.
        """
        grid = []
        gap = width // rows  # Width of each cell in the grid
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                spot = Spot(i, j, gap, rows)
                grid[i].append(spot)
        return grid

    @staticmethod
    def draw_grid(win, rows, width):
        """
        Draws the grid lines on the window.

        Args:
            win (pygame.Surface): The pygame window surface where the grid is drawn.
            rows (int): The number of rows (and columns) in the grid.
            width (int): The width of the grid in pixels.
        """
        gap = width // rows
        for i in range(rows):
            # Horizontal lines
            pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
            for j in range(rows):
                # Vertical lines
                pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

    @staticmethod
    def draw(win, grid, rows, width):
        """
        Draws the entire grid, including the spots and grid lines.

        Args:
            win (pygame.Surface): The pygame window surface where the grid is drawn.
            grid (list): The 2D list of Spot objects representing the grid.
            rows (int): The number of rows (and columns) in the grid.
            width (int): The width of the grid in pixels.
        """
        win.fill(WHITE)  # Clear the window with a white background
        for row in grid:
            for spot in row:
                spot.draw(win)  # Draw each spot on the grid
        Game.draw_grid(win, rows, width)  # Draw the grid lines
        pygame.display.update()  # Update the display

    @staticmethod
    def get_clicked_pos(pos, rows, width):
        """
        Converts a mouse click position to grid coordinates.

        Args:
            pos (tuple): The (x, y) position of the mouse click.
            rows (int): The number of rows (and columns) in the grid.
            width (int): The width of the grid in pixels.

        Returns:
            tuple: A tuple (row, col) representing the grid coordinates of the clicked position.
        """
        gap = width // rows  # Width of each cell in the grid
        y, x = pos
        row = y // gap
        col = x // gap
        return row, col
