from collections import deque
import heapq
import pygame
import time

class Algorithm:

    

    def heuristic(self, present, target):
        # Unpack the coordinates of the present and target nodes
        (x1, y1), (x2, y2) = present, target

        # Calculate the distance in each dimension
        x_distance = abs(x1 - x2)
        y_distance = abs(y1 - y2)

        # Return the sum of the distances as the heuristic value
        return x_distance + y_distance

    def find_shortest_path(self, before, present, draw):
        # Traverse the path from the end node to the start node
        while present in before:
            present = before[present]  # Update the present node to its predecessor
            present.shortest_path()  # Color the present node as YELLOW
            draw()  # Redraw the grid with the updated colors

    def BFS(self, draw, grid, start, end):
        queue = deque([start])
        visited = set()
        visited.add(start)
        prior = {}  # Store the parent nodes
        
        while queue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            node = queue.popleft()

            if node == end:
                self.find_shortest_path(prior, end, draw)
                end.end_node()
                start.start_node()
                return True
            

            for neighbour in node.neighbours:
                if neighbour not in visited:
                    prior[neighbour] = node
                    queue.append(neighbour)
                    visited.add(neighbour)
                    neighbour.to_explore() 

            draw()

            if node != start:
                node.visited()
        
        

        return False

            
    def dijkstras(self, draw, grid, start, end):
        count = 0  # If 2 nodes mid-path give the same distance, node with lower count can be given priority

        # Priority queue to store nodes with their respective distances
        queue_set = []
        heapq.heappush(queue_set, (0, count, start))

        # Store the distances from the start node to each node in the grid
        distances = {node: float("inf") for row in grid for node in row}
        distances[start] = 0

        # Store the previous node in the shortest path
        prior = {}

        # Set to keep track of visited nodes
        visited = set()

        while queue_set:
            # Get the node with the minimum distance from the priority queue
            present = heapq.heappop(queue_set)[2]
            visited.add(present)

            if present == end:  # If end node reached
                self.find_shortest_path(prior, end, draw)
                end.end_node()
                start.start_node()
                return True

            for neighbour in present.neighbours:
                new_distance = distances[present] + 1  # Distance from start to neighbour is always 1

                if new_distance < distances[neighbour]:  # If a shorter path is found
                    prior[neighbour] = present
                    distances[neighbour] = new_distance
                    if neighbour not in visited:
                        count += 1
                        heapq.heappush(queue_set, (distances[neighbour], count, neighbour))
                        neighbour.to_explore()

            draw()

            if present != start:
                present.visited()
        

    def A_Star(self, draw, grid, start, end):
        count = 0  # If 2 nodes mid-path give the same distance, node with lower count can be traversed.

        queue_set = []
        heapq.heappush(queue_set, (0, count, start))

        edge_total = {spot: float("inf") for row in grid for spot in row}
        edge_total[start] = 0

        total_distance = {spot: float("inf") for row in grid for spot in row}
        total_distance[start] = self.heuristic(start.get_position(), end.get_position())

        prior = {}
        in_queue = {start}

        start_time = time.time()

        while queue_set:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            present = heapq.heappop(queue_set)[2]
            in_queue.remove(present)

            if present == end:
                self.find_shortest_path(prior, end, draw)
                end.end_node()
                start.start_node()
                return True

            for neighbour in present.neighbours:
                new_edge_total = edge_total[present] + 1

                if new_edge_total < edge_total[neighbour]:
                    prior[neighbour] = present
                    edge_total[neighbour] = new_edge_total
                    total_distance[neighbour] = new_edge_total + self.heuristic(neighbour.get_position(), end.get_position())
                    if neighbour not in in_queue:
                        count += 1
                        heapq.heappush(queue_set, (total_distance[neighbour], count, neighbour))
                        in_queue.add(neighbour)
                        neighbour.to_explore()

            draw()

            if present != start:
                present.visited()
        
        
    
    def greedy(self, draw, grid, start, end):
        open_set = [start]
        visited = set()
        visited.add(start)
        prior = {}  # Store the parent nodes

        while open_set:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = open_set.pop()
            
            if current == end:
                self.find_shortest_path(prior, end, draw)
                end.end_node()
                start.start_node()
                return True

            for neighbour in current.neighbours:
                if neighbour not in visited:
                    prior[neighbour] = current
                    open_set.append(neighbour)
                    visited.add(neighbour)
                    neighbour.to_explore()

            draw()

            if current != start:
                current.visited()
        
        

        return False
