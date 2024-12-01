import pygame
from queue import PriorityQueue
from collections import deque


def h(p1, p2):
    """
    Heuristic function for pathfinding.

    Args:
        p1 (tuple): Coordinates of the first point (x1, y1).
        p2 (tuple): Coordinates of the second point (x2, y2).

    Returns:
        int: The Manhattan distance between the two points.
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    """
    Reconstructs the path from the end node to the start node.

    Args:
        came_from (dict): A dictionary mapping nodes to their parent nodes.
        current (Spot): The current node to trace back from.
        draw (function): A function to update the drawing for visualization.

    Returns:
        None
    """
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


class Strategy:
    """
    A collection of static methods for various pathfinding algorithms.
    """

    @staticmethod
    # A* without collectiong data
    # def a_star(draw, grid, start, end):
    #     """
    #     Implements the A* pathfinding algorithm.
    #
    #     Args:
    #         draw (function): A function to update the drawing for visualization.
    #         grid (list): The grid containing all the Spot objects.
    #         start (Spot): The starting node.
    #         end (Spot): The target node.
    #
    #     Returns:
    #         bool: True if a path is found, False otherwise.
    #     """
    #     count = 0
    #     open_set = PriorityQueue()
    #     open_set.put((0, count, start))
    #     came_from = {}
    #     g_score = {spot: float("inf") for row in grid for spot in row}
    #     g_score[start] = 0
    #     f_score = {spot: float("inf") for row in grid for spot in row}
    #     f_score[start] = h(start.get_pos(), end.get_pos())
    #
    #     open_set_hash = {start}
    #
    #     while not open_set.empty():
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #
    #         current = open_set.get()[2]
    #         open_set_hash.remove(current)
    #
    #         if current == end:
    #             reconstruct_path(came_from, end, draw)
    #             end.make_end()
    #             return True
    #
    #         for neighbor in current.neighbors:
    #             temp_g_score = g_score[current] + 1
    #
    #             if temp_g_score < g_score[neighbor]:
    #                 came_from[neighbor] = current
    #                 g_score[neighbor] = temp_g_score
    #                 f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
    #                 if neighbor not in open_set_hash:
    #                     count += 1
    #                     open_set.put((f_score[neighbor], count, neighbor))
    #                     open_set_hash.add(neighbor)
    #                     neighbor.make_open()
    #
    #         draw()
    #
    #         if current != start:
    #             current.make_closed()
    #
    #     return False
    def a_star(draw, grid, start, end):
        """
        A* pathfinding algorithm with visualization.

        Args:
            draw (function): A function to update the drawing for visualization.
            grid (list): 2D list of Spot objects representing the grid.
            start (Spot): Starting node.
            end (Spot): Goal node.

        Returns:
            dict: A dictionary containing metrics, or None if no path is found.
        """
        import time

        start_time = time.time()  # Start the timer

        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, start))
        came_from = {}
        g_score = {spot: float("inf") for row in grid for spot in row}
        g_score[start] = 0
        f_score = {spot: float("inf") for row in grid for spot in row}
        f_score[start] = h(start.get_pos(), end.get_pos())

        open_set_hash = {start}
        expanded_nodes = 0  # Counter for expanded nodes

        while not open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = open_set.get()[2]
            open_set_hash.remove(current)
            expanded_nodes += 1  # Increment expanded node count

            if current == end:
                end_time = time.time()  # End the timer
                total_time = end_time - start_time

                # Reconstruct and draw the path
                reconstruct_path(came_from, end, draw)

                # Metrics
                path = []
                while current in came_from:
                    path.append(current.get_pos())
                    current = came_from[current]
                path.append(start.get_pos())
                path.reverse()

                metrics = {
                    "path": path,
                    "time": total_time,
                    "steps": len(path),
                    "manhattan_distance": h(start.get_pos(), end.get_pos()),
                    "expanded_nodes": expanded_nodes,
                    "algorithm": "A_star"
                }
                return metrics  # Return metrics instead of True

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_open()

            draw()

            if current != start:
                current.make_closed()

        return None  # Return None if no path is found

    @staticmethod
    # def bfs(draw, grid, start, end):
    #     """
    #     Implements the Breadth-First Search (BFS) algorithm.
    #
    #     Args:
    #         draw (function): A function to update the drawing for visualization.
    #         grid (list): The grid containing all the Spot objects.
    #         start (Spot): The starting node.
    #         end (Spot): The target node.
    #
    #     Returns:
    #         bool: True if a path is found, False otherwise.
    #     """
    #     queue = deque()
    #     queue.append(start)
    #     came_from = {}
    #
    #     visited = {spot: False for row in grid for spot in row}
    #     visited[start] = True
    #
    #     while queue:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #
    #         current = queue.popleft()
    #
    #         if current == end:
    #             reconstruct_path(came_from, end, draw)
    #             end.make_end()
    #             return True
    #
    #         for neighbor in current.neighbors:
    #             if not visited[neighbor]:
    #                 visited[neighbor] = True
    #                 came_from[neighbor] = current
    #                 queue.append(neighbor)
    #                 neighbor.make_open()
    #
    #         draw()
    #
    #         if current != start:
    #             current.make_closed()
    #
    #     return False
    def bfs(draw, grid, start, end):
        """
        Breadth-First Search (BFS) algorithm with visualization and metrics collection.

        Returns:
            dict: A dictionary containing metrics, or None if no path is found.
        """
        import time

        start_time = time.time()
        queue = deque([start])
        came_from = {}
        visited = {spot: False for row in grid for spot in row}
        visited[start] = True
        expanded_nodes = 0

        while queue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = queue.popleft()
            expanded_nodes += 1

            if current == end:
                end_time = time.time()
                total_time = end_time - start_time
                reconstruct_path(came_from, end, draw)

                path = []
                while current in came_from:
                    path.append(current.get_pos())
                    current = came_from[current]
                path.append(start.get_pos())
                path.reverse()

                metrics = {
                    "path": path,
                    "time": total_time,
                    "steps": len(path),
                    "manhattan_distance": h(start.get_pos(), end.get_pos()),
                    "expanded_nodes": expanded_nodes,
                    "algorithm": "BFS"
                }
                return metrics

            for neighbor in current.neighbors:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    came_from[neighbor] = current
                    queue.append(neighbor)
                    neighbor.make_open()

            draw()
            if current != start:
                current.make_closed()

        return None

    @staticmethod
    # def dfs(draw, grid, start, end):
    #     """
    #     Implements the Depth-First Search (DFS) algorithm.
    #
    #     Args:
    #         draw (function): A function to update the drawing for visualization.
    #         grid (list): The grid containing all the Spot objects.
    #         start (Spot): The starting node.
    #         end (Spot): The target node.
    #
    #     Returns:
    #         bool: True if a path is found, False otherwise.
    #     """
    #     stack = [start]
    #     came_from = {}
    #     visited = {spot: False for row in grid for spot in row}
    #     visited[start] = True
    #
    #     while stack:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #
    #         current = stack.pop()
    #
    #         if current == end:
    #             reconstruct_path(came_from, end, draw)
    #             end.make_end()
    #             return True
    #
    #         for neighbor in current.neighbors:
    #             if not visited[neighbor]:
    #                 visited[neighbor] = True
    #                 came_from[neighbor] = current
    #                 stack.append(neighbor)
    #                 neighbor.make_open()
    #
    #         draw()
    #
    #         if current != start:
    #             current.make_closed()
    #
    #     return False
    def dfs(draw, grid, start, end):
        """
        Depth-First Search (DFS) algorithm with visualization and metrics collection.

        Returns:
            dict: A dictionary containing metrics, or None if no path is found.
        """
        import time

        start_time = time.time()
        stack = [start]
        came_from = {}
        visited = {spot: False for row in grid for spot in row}
        visited[start] = True
        expanded_nodes = 0

        while stack:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = stack.pop()
            expanded_nodes += 1

            if current == end:
                end_time = time.time()
                total_time = end_time - start_time
                reconstruct_path(came_from, end, draw)

                path = []
                while current in came_from:
                    path.append(current.get_pos())
                    current = came_from[current]
                path.append(start.get_pos())
                path.reverse()

                metrics = {
                    "path": path,
                    "time": total_time,
                    "steps": len(path),
                    "manhattan_distance": h(start.get_pos(), end.get_pos()),
                    "expanded_nodes": expanded_nodes,
                    "algorithm": "DFS"
                }
                return metrics

            for neighbor in current.neighbors:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    came_from[neighbor] = current
                    stack.append(neighbor)
                    neighbor.make_open()

            draw()
            if current != start:
                current.make_closed()

        return None

    @staticmethod
    # def greedy_bfs(draw, grid, start, end):
    #     """
    #     Implements the Greedy Best-First Search algorithm.
    #
    #     Args:
    #         draw (function): A function to update the drawing for visualization.
    #         grid (list): The grid containing all the Spot objects.
    #         start (Spot): The starting node.
    #         end (Spot): The target node.
    #
    #     Returns:
    #         bool: True if a path is found, False otherwise.
    #     """
    #     open_set = PriorityQueue()
    #     open_set.put((h(start.get_pos(), end.get_pos()), start))
    #     came_from = {}
    #
    #     visited = {spot: False for row in grid for spot in row}
    #     visited[start] = True
    #
    #     while not open_set.empty():
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #
    #         current = open_set.get()[1]
    #
    #         if current == end:
    #             reconstruct_path(came_from, end, draw)
    #             end.make_end()
    #             return True
    #
    #         for neighbor in current.neighbors:
    #             if not visited[neighbor]:
    #                 visited[neighbor] = True
    #                 came_from[neighbor] = current
    #                 open_set.put((h(neighbor.get_pos(), end.get_pos()), neighbor))
    #                 neighbor.make_open()
    #
    #         draw()
    #
    #         if current != start:
    #             current.make_closed()
    #
    #     return False
    def greedy_bfs(draw, grid, start, end):
        """
        Greedy Best-First Search algorithm with visualization and metrics collection.

        Returns:
            dict: A dictionary containing metrics, or None if no path is found.
        """
        import time

        start_time = time.time()
        open_set = PriorityQueue()
        open_set.put((h(start.get_pos(), end.get_pos()), start))
        came_from = {}
        visited = {spot: False for row in grid for spot in row}
        visited[start] = True
        expanded_nodes = 0

        while not open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = open_set.get()[1]
            expanded_nodes += 1

            if current == end:
                end_time = time.time()
                total_time = end_time - start_time
                reconstruct_path(came_from, end, draw)

                path = []
                while current in came_from:
                    path.append(current.get_pos())
                    current = came_from[current]
                path.append(start.get_pos())
                path.reverse()

                metrics = {
                    "path": path,
                    "time": total_time,
                    "steps": len(path),
                    "manhattan_distance": h(start.get_pos(), end.get_pos()),
                    "expanded_nodes": expanded_nodes,
                    "algorithm": "Greedy_BFS"
                }
                return metrics

            for neighbor in current.neighbors:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    came_from[neighbor] = current
                    open_set.put((h(neighbor.get_pos(), end.get_pos()), neighbor))
                    neighbor.make_open()

            draw()
            if current != start:
                current.make_closed()

        return None
