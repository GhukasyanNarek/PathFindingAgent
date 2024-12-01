import pygame
from game import Game
from algorithms import Strategy
from openpyxl import Workbook, load_workbook

# Constants
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Agent")



def save_metrics_to_xlsx(metrics, filename="data.xlsx"):
    """
    Saves the pathfinding metrics to an Excel (.xlsx) file.

    Args:
        metrics (dict): The dictionary of metrics to save.
        filename (str): The name of the Excel file.
    """
    try:
        # Load the workbook if it exists; otherwise, create a new one
        try:
            workbook = load_workbook(filename)
            sheet = workbook.active
        except FileNotFoundError:
            workbook = Workbook()
            sheet = workbook.active
            # Add header row
            sheet.append(["Path", "Execution Time (s)", "Steps", "Manhattan Distance", "Expanded Nodes"])

        # Append the metrics to the worksheet
        sheet.append([
            str(metrics["path"]),  # Path as a string
            metrics["time"],  # Execution time in seconds
            metrics["steps"],  # Number of steps in the path
            metrics["manhattan_distance"],  # Manhattan distance
            metrics["expanded_nodes"],  # Number of expanded nodes
            metrics["algorithm"]  # Algorithm type
        ])

        # Save the workbook
        workbook.save(filename)
        print(f"Metrics saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving to {filename}: {e}")


# Main function without collecting data
# def main(win, width, algorithm=Strategy.a_star):
#     """
#     Main function to run the pathfinding visualization.
#
#     Args:
#         win (pygame.Surface): The pygame window surface to draw the grid and pathfinding.
#         width (int): The width of the grid in pixels.
#         algorithm (function): The pathfinding algorithm to use. Defaults to A* (Strategy.a_star).
#
#     Features:
#         - Left mouse button: Place the start, end, or barrier nodes.
#         - Right mouse button: Remove nodes.
#         - Spacebar: Start the pathfinding algorithm.
#         - 'C' key: Clear the grid.
#     """
#     ROWS = 50  # Number of rows and columns in the grid
#     grid = Game.make_grid(ROWS, width)
#
#     # Initialize variables
#     start = None  # Starting node
#     end = None  # Ending node
#     run = True  # Control the game loop
#
#     while run:
#         Game.draw(win, grid, ROWS, width)  # Draw the grid
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:  # Handle quit event
#                 run = False
#
#             if pygame.mouse.get_pressed()[0]:  # Left mouse button
#                 pos = pygame.mouse.get_pos()
#                 row, col = Game.get_clicked_pos(pos, ROWS, width)
#                 spot = grid[row][col]
#                 if not start and spot != end:  # Place start node
#                     start = spot
#                     start.make_start()
#                 elif not end and spot != start:  # Place end node
#                     end = spot
#                     end.make_end()
#                 elif spot != end and spot != start:  # Place barrier
#                     spot.make_barrier()
#
#             elif pygame.mouse.get_pressed()[2]:  # Right mouse button
#                 pos = pygame.mouse.get_pos()
#                 row, col = Game.get_clicked_pos(pos, ROWS, width)
#                 spot = grid[row][col]
#                 spot.reset()  # Reset the spot
#                 if spot == start:
#                     start = None
#                 elif spot == end:
#                     end = None
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE and start and end:
#                     # Update neighbors for all spots
#                     for row in grid:
#                         for spot in row:
#                             spot.update_neighbors(grid)
#
#                     # Run the selected pathfinding algorithm
#                     algorithm(lambda: Game.draw(win, grid, ROWS, width), grid, start, end)
#
#                 if event.key == pygame.K_c:  # Clear the grid
#                     start = None
#                     end = None
#                     grid = Game.make_grid(ROWS, width)
#
#     pygame.quit()

def main(win, width, algorithm=Strategy.a_star):
    ROWS = 50
    grid = Game.make_grid(ROWS, width)

    start = None
    end = None
    run = True
    while run:
        Game.draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                pos = pygame.mouse.get_pos()
                row, col = Game.get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:  # Place start node
                    start = spot
                    start.make_start()
                elif not end and spot != start:  # Place end node
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:  # Place barrier
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # Right mouse button
                pos = pygame.mouse.get_pos()
                row, col = Game.get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()  # Reset the spot
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    # Update neighbors for all spots
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    # Run the algorithm and get metrics
                    metrics = algorithm(lambda: Game.draw(win, grid, ROWS, width), grid, start, end)

                    if metrics:  # If a valid path is found
                        print("Pathfinding Metrics:")
                        print(metrics)
                        save_metrics_to_xlsx(metrics, "data.xlsx")
                    else:
                        print("No path found!")

                if event.key == pygame.K_c:  # Clear the grid
                    start = None
                    end = None
                    grid = Game.make_grid(ROWS, width)

    pygame.quit()


if __name__ == "__main__":
    main(WIN, WIDTH, Strategy.a_star)
