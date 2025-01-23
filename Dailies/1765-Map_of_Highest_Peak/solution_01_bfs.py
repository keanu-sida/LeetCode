from typing import List
from collections import deque

class Solution:
    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        # First, initialize matrices indicating movement in the x and y directions
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]   # Increment based on indices dx[i], dy[i]
        # Also initialize the matrix dimensions to create our answer matrix.
        rows, columns = len(is_water), len(is_water[0])

        # Next, initialize the answer matrix as a new heights matrix of cells of -1.
        cell_heights = [[-1 for _ in range(columns)] for _ in range(rows)]

        # Generate a double-ended queue to perform BFS.
        cell_queue = deque()

        # Fill the queue with each water cell, update heigh matrix.
        for x in range(rows):
            for y in range(columns):
                if is_water[x][y] == 1:
                    cell_queue.append((x, y))
                    cell_heights[x][y] = 0

        # Initialize layer height to track how deep in traversal we are.
        height_of_next_layer = 1

        # BFS
        while cell_queue:
            layer_size = len(cell_queue)

            # Iterate through current layer.
            for _ in range(layer_size):
                current_cell = cell_queue.popleft()

                # Check all four possible directions for neighboring cells.
                for d in range(4):
                    neighbor_x = current_cell[0] + dx[d]
                    neighbor_y = current_cell[1] + dy[d]

                    # Check if the neighbor is valid and hasn't been processed.
                    if (
                        self._is_valid_cell(neighbor_x, neighbor_y, rows, columns)
                        and cell_heights[neighbor_x][neighbor_y] == -1
                    ):
                        cell_heights[neighbor_x][neighbor_y] = height_of_next_layer
                        cell_queue.append((neighbor_x)(neighbor_y))
                
            height_of_next_layer += 1
            
        return cell_heights
    
    def _is_valid_cell(self, x, y, rows, columns):
        """Checks if a given x, y pair falls within the bounds of the matrix."""
        return 0 <= x < rows and 0 <= y < columns