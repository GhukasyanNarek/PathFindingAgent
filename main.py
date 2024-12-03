import random
import time
import pygame
from game import Game
from algorithms import Strategy
from openpyxl import Workbook, load_workbook

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Agent")

ROWS = 50
OBSTACLE_DENSITY = 0.3


def generate_random_points(rows):
    start = (random.randint(0, rows - 1), random.randint(0, rows - 1))
    end = (random.randint(0, rows - 1), random.randint(0, rows - 1))
    while start == end:
        end = (random.randint(0, rows - 1), random.randint(0, rows - 1))
    return start, end


def place_obstacles(grid, density):
    total_cells = ROWS * ROWS
    obstacle_count = int(total_cells * density)
    obstacles = set()
    while len(obstacles) < obstacle_count:
        row, col = random.randint(0, ROWS - 1), random.randint(0, ROWS - 1)
        if not grid[row][col].is_barrier():
            obstacles.add((row, col))
            grid[row][col].make_barrier()


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


def automated_tests(win, width, algorithm, num_tests=100):
    for run_id in range(1, num_tests + 1):
        print(f"Running test {run_id}...")

        grid = Game.make_grid(ROWS, width)
        start_pos, end_pos = generate_random_points(ROWS)

        start = grid[start_pos[0]][start_pos[1]]
        end = grid[end_pos[0]][end_pos[1]]
        start.make_start()
        end.make_end()

        place_obstacles(grid, OBSTACLE_DENSITY)

        for row in grid:
            for spot in row:
                spot.update_neighbors(grid)

        metrics = algorithm(lambda: Game.draw(win, grid, ROWS, width), grid, start, end)
        if metrics:
            metrics["run"] = run_id
            save_metrics_to_xlsx(metrics)
        else:
            print(f"Test {run_id}: No path found.")

    print("All tests completed.")


def run_all_algorithms_for_configurations(win, width, num_tests=100):
    """
    Runs all algorithms on randomly generated grid configurations for a specified number of tests.
    """
    algorithms = ["a_star", "ucs", "bfs", "dfs", "greedy_bfs"]

    for test_number in range(1, num_tests + 1):
        print(f"Running test {test_number}...")

        grid = Game.make_grid(ROWS, width)
        start_pos, end_pos = generate_random_points(ROWS)

        start = grid[start_pos[0]][start_pos[1]]
        end = grid[end_pos[0]][end_pos[1]]
        start.make_start()
        end.make_end()

        place_obstacles(grid, OBSTACLE_DENSITY)

        for row in grid:
            for spot in row:
                spot.update_neighbors(grid)

        for algo_name in algorithms:
            try:
                func = getattr(Strategy, algo_name)
                print(f"Running {algo_name} on test {test_number}...")

                start_time = time.time()
                metrics = func(lambda: Game.draw(win, grid, ROWS, width), grid, start, end)
                exec_time = time.time() - start_time

                if metrics:
                    metrics.update({
                        "run": test_number,
                        "algorithm": algo_name,
                        "time": exec_time
                    })
                    save_metrics_to_xlsx(metrics)
                else:
                    print(f"Test {test_number}, Algorithm {algo_name}: No path found.")
            except Exception as e:
                print(f"Test {test_number}, Algorithm {algo_name}: Error occurred - {e}")

    print("All tests completed.")


def main(win, width, algorithm=Strategy.a_star):
    grid = Game.make_grid(ROWS, width)
    start = None
    end = None
    run = True
    while run:
        Game.draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = Game.get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = Game.get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    metrics = algorithm(lambda: Game.draw(win, grid, ROWS, width), grid, start, end)

                    if metrics:
                        print("Pathfinding Metrics:")
                        print(metrics)
                        save_metrics_to_xlsx(metrics, "data.xlsx")
                    else:
                        print("No path found!")

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = Game.make_grid(ROWS, width)

    pygame.quit()


if __name__ == "__main__":
    choice = input("Enter '1' for manual mode or '2' for automated tests or '3' for automated tests that run on the same "
                   "grid: ").strip()
    pygame.init()
    if choice == "1":
        main(WIN, WIDTH, Strategy.greedy_bfs)  # Use manual mode
    elif choice == "2":
        automated_tests(WIN, WIDTH, Strategy.greedy_bfs, num_tests=50)  # Use automated tests
    elif choice == "3":
        run_all_algorithms_for_configurations(WIN, WIDTH, num_tests=50)
    pygame.quit()
