import pygame

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 244, 208)
PURPLE = (128, 0, 128)


class Spot:
    """
    Represents a single grid cell (spot) in the pathfinding visualization.

    Attributes:
        row (int): Row index of the spot in the grid.
        col (int): Column index of the spot in the grid.
        width (int): Width of the spot.
        total_rows (int): Total number of rows in the grid.
        x (int): Pixel x-coordinate of the spot's top-left corner.
        y (int): Pixel y-coordinate of the spot's top-left corner.
        color (tuple): Current color of the spot (default is WHITE).
        neighbors (list): List of neighboring spots.
    """

    def __init__(self, row, col, width, total_rows):
        """
        Initializes a Spot object.

        Args:
            row (int): Row index of the spot.
            col (int): Column index of the spot.
            width (int): Width of the spot.
            total_rows (int): Total number of rows in the grid.
        """
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []

    def get_pos(self):
        """
        Gets the position of the spot in the grid.

        Returns:
            tuple: A tuple (row, col) representing the spot's position.
        """
        return self.row, self.col

    def is_closed(self):
        """
        Checks if the spot is in the closed set.

        Returns:
            bool: True if the spot is closed (RED), False otherwise.
        """
        return self.color == RED

    def is_open(self):
        """
        Checks if the spot is in the open set.

        Returns:
            bool: True if the spot is open (GREEN), False otherwise.
        """
        return self.color == GREEN

    def is_barrier(self):
        """
        Checks if the spot is a barrier.

        Returns:
            bool: True if the spot is a barrier (BLACK), False otherwise.
        """
        return self.color == BLACK

    def is_start(self):
        """
        Checks if the spot is the starting point.

        Returns:
            bool: True if the spot is the start (ORANGE), False otherwise.
        """
        return self.color == ORANGE

    def is_end(self):
        """
        Checks if the spot is the end point.

        Returns:
            bool: True if the spot is the end (TURQUOISE), False otherwise.
        """
        return self.color == TURQUOISE

    def reset(self):
        """
        Resets the spot's color to its default state (WHITE).
        """
        self.color = WHITE

    def make_closed(self):
        """
        Marks the spot as closed (RED).
        """
        self.color = RED

    def make_open(self):
        """
        Marks the spot as open (GREEN).
        """
        self.color = GREEN

    def make_barrier(self):
        """
        Marks the spot as a barrier (BLACK).
        """
        self.color = BLACK

    def make_end(self):
        """
        Marks the spot as the end point (TURQUOISE).
        """
        self.color = TURQUOISE

    def make_path(self):
        """
        Marks the spot as part of the final path (PURPLE).
        """
        self.color = PURPLE

    def make_start(self):
        """
        Marks the spot as the starting point (ORANGE).
        """
        self.color = ORANGE

    def draw(self, win):
        """
        Draws the spot on the screen.

        Args:
            win (pygame.Surface): The pygame window surface where the spot is drawn.
        """
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        """
        Updates the spot's neighbors by checking adjacent spots.

        Args:
            grid (list): The grid containing all the spots.
        """
        self.neighbors = []
        # Check below
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        # Check above
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        # Check right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        # Check left
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        """
        Less-than comparison operator for the Spot class.

        Args:
            other (Spot): Another Spot object.

        Returns:
            bool: Always False, as Spots are not directly comparable.
        """
        return False
