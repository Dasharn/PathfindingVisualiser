from collections import deque
from queue import PriorityQueue
import heapq
import pygame
import time

class Algorithm:

    INFINITY = float('inf')
    

    def heuristic(self, present, target):
        # Unpack the coordinates of the present and target nodes
        # Unpack the coordinates of the present and target nodes
        (x1, y1), (x2, y2) = present, target

        # Calculate the Manhattan distance between the present and target nodes
        return abs(x1 - x2) + abs(y1 - y2)
        

    def find_shortest_path(self, before, present, draw):
        # Traverse the path from the end node to the start node
        while present in before:
            present = before[present]  # Update the present node to its predecessor
            present.shortest_path()  # Color the present node as YELLOW
            draw()  # Redraw the grid with the updated colors


    def bfs(self, draw, grid, start, end):
        queue = deque([start])
        visited = {start}
        prior = {}  # Track parent nodes for shortest path reconstruction
    
        while queue:
            # Handle Pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    
            current_node = queue.popleft()
    
            # If the end node is reached, reconstruct the path
            if current_node == end:
                self.find_shortest_path(prior, end, draw)
                end.end()  # Mark the end node
                start.start()  # Mark the start node
                return True
    
            # Explore the neighbors of the current node
            for neighbor in current_node.neighbours:
                if neighbor not in visited:
                    prior[neighbor] = current_node
                    queue.append(neighbor)
                    visited.add(neighbor)
                    neighbor.to_explore()  # Mark the neighbor as being explored
    
            # Draw the updated grid
            draw()
    
            # Mark the current node as visited, excluding the start node
            if current_node != start:
                current_node.visited()
    
        return False

            
    def dijkstras(self, draw, grid, start, end):
        count = 0  # Priority counter to break ties in distances
        priority_queue = []
        heapq.heappush(priority_queue, (0, count, start))
    
        # Initialize distances with infinity for all nodes, except the start node
        distances = {node: float("inf") for row in grid for node in row}
        distances[start] = 0
    
        # Dictionary to store the previous nodes for path reconstruction
        prior = {}
    
        # Set to track visited nodes
        visited = set()
    
        while priority_queue:
            # Pop the node with the smallest distance from the priority queue
            current_node = heapq.heappop(priority_queue)[2]
            visited.add(current_node)
    
            # Check if the end node has been reached
            if current_node == end:
                self.find_shortest_path(prior, end, draw)
                end.end()  # Mark the end node
                start.start()  # Mark the start node
                return True
    
            # Explore each neighbor of the current node
            for neighbor in current_node.neighbours:
                new_distance = distances[current_node] + 1  # Assume all edges have a weight of 1
    
                # If a shorter path to the neighbor is found
                if new_distance < distances[neighbor]:
                    prior[neighbor] = current_node
                    distances[neighbor] = new_distance
    
                    if neighbor not in visited:
                        count += 1
                        heapq.heappush(priority_queue, (new_distance, count, neighbor))
                        neighbor.to_explore()  # Mark the neighbor for exploration
    
            # Redraw the grid to visualize the algorithm's progress
            draw()
    
            # Mark the current node as visited, excluding the start node
            if current_node != start:
                current_node.visited()
    
        return False
        

    def A_Star(self, draw, grid, start, end):
        count = 0  # Counter to prioritize nodes with equal distances
        priority_queue = []
        heapq.heappush(priority_queue, (0, count, start))
    
        # Distance from the start node to each node (g score)
        g_score = {node: float("inf") for row in grid for node in row}
        g_score[start] = 0
    
        # Estimated total distance (g score + heuristic) to the end (f score)
        f_score = {node: float("inf") for row in grid for node in row}
        f_score[start] = self.heuristic(start.get_position(), end.get_position())
    
        prior = {}  # To reconstruct the path
        in_queue = {start}  # Track nodes in the priority queue
    
        while priority_queue:
            # Handle Pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    
            # Pop the node with the lowest f score
            current_node = heapq.heappop(priority_queue)[2]
            in_queue.remove(current_node)
    
            # Check if the end node is reached
            if current_node == end:
                self.find_shortest_path(prior, end, draw)
                end.end()
                start.start()
                return True
    
            # Explore each neighbor of the current node
            for neighbor in current_node.neighbours:
                tentative_g_score = g_score[current_node] + 1  # Assume all edges have a weight of 1
    
                # If a better path to the neighbor is found
                if tentative_g_score < g_score[neighbor]:
                    prior[neighbor] = current_node
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor.get_position(), end.get_position())
    
                    if neighbor not in in_queue:
                        count += 1
                        heapq.heappush(priority_queue, (f_score[neighbor], count, neighbor))
                        in_queue.add(neighbor)
                        neighbor.to_explore()
    
            # Visualize the grid updates
            draw()
    
            # Mark the current node as visited, excluding the start node
            if current_node != start:
                current_node.visited()
    
        return False
        
        
    
    def greedy(self, draw, grid, start, end):
        open_set = [start]
        visited = {start}
        prior = {}  # Store the parent nodes for path reconstruction
    
        while open_set:
            # Handle Pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    
            # Pop the last node added to the open set
            current = open_set.pop()
    
            # If the end node is reached, reconstruct the path
            if current == end:
                self.find_shortest_path(prior, end, draw)
                end.end()
                start.start()
                return True
    
            # Explore neighbors of the current node
            for neighbor in current.neighbours:
                if neighbor not in visited:
                    prior[neighbor] = current
                    open_set.append(neighbor)  # Add the neighbor to the open set
                    visited.add(neighbor)  # Mark it as visited
                    neighbor.to_explore()  # Mark the neighbor as being explored
    
            # Redraw the grid to visualize the algorithm's progress
            draw()
    
            # Mark the current node as visited, excluding the start node
            if current != start:
                current.visited()
    
        return False
    
    def bidirectional_search(self, draw, grid, start, end):
        start_queue = deque([start])
        end_queue = deque([end])
        start_visited = set()
        end_visited = set()
        start_visited.add(start)
        end_visited.add(end)
        start_prior = {}
        end_prior = {}

        intersect_node = None

        while start_queue and end_queue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            start_node = start_queue.popleft()
            end_node = end_queue.popleft()

            # Check if the start node has reached the end node
            if start_node in end_visited:
                intersect_node = start_node
                break

            # Check if the end node has reached the start node
            if end_node in start_visited:
                intersect_node = end_node
                break

            for start_neighbor in start_node.neighbours:
                if start_neighbor not in start_visited and not start_neighbor.is_barrier():
                    start_visited.add(start_neighbor)
                    start_queue.append(start_neighbor)
                    start_prior[start_neighbor] = start_node
                    start_neighbor.to_explore()

            for end_neighbor in end_node.neighbours:
                if end_neighbor not in end_visited and not end_neighbor.is_barrier():
                    end_visited.add(end_neighbor)
                    end_queue.append(end_neighbor)
                    end_prior[end_neighbor] = end_node
                    end_neighbor.to_explore()

            draw()

            if start_node != start:
                start_node.visited()

            if end_node != end:
                end_node.visited()

        if intersect_node is None:
            return False

        self.connect_nodes(start_prior, end_prior, intersect_node, draw)
        end.end()
        start.start()

        return True

    
    def connect_nodes(self, start_prior, end_prior, intersect_node, draw):
        
        # Traverse the path from the intersect node to the start node
        path = []
        while intersect_node in start_prior:
            path.append(intersect_node)
            intersect_node = start_prior[intersect_node]
            
        # Reverse the path to go from start to intersect
        path.reverse()
        
        # Traverse the path from the intersect node to the end node
        while intersect_node in end_prior:
            path.append(intersect_node)
            intersect_node = end_prior[intersect_node]
            
        # Add the intersect node to the path
        path.append(intersect_node)
        
        # Color the nodes in the path
        for node in path:
            node.shortest_path()
            draw()
        
    

    def dead_end_filling(self, draw, grid, start, end):
        stack = [start]
        visited = {start}
        prior = {}  # Store the parent nodes for path reconstruction
    
        while stack:
            # Handle Pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    
            current = stack.pop()
    
            # If the end node is reached, reconstruct the path
            if current == end:
                self.find_shortest_path(prior, end, draw)
                end.end()
                start.start()
                return True
    
            dead_ends = []
    
            # Explore neighbors of the current node
            for neighbor in current.neighbours:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)  # Add neighbor to stack for further exploration
                    prior[neighbor] = current  # Track the path
                    neighbor.to_explore()
                elif neighbor.is_barrier():  # Check if the neighbor is a barrier
                    dead_ends.append(neighbor)
    
            # If the current node is a dead-end (surrounded by 3 barriers), convert them visually
            if len(dead_ends) == 3:
                for dead_end in dead_ends:
                    dead_end.make_barrier()  # Mark as barrier
                    dead_end.barrier_color()  # Apply barrier color for visualization
                draw()  # Redraw the grid
    
            # Mark the current node as visited, excluding the start node
            if current != start:
                current.visited()
    
            draw()  # Redraw the grid after visiting the node
    
        return False
    
        
