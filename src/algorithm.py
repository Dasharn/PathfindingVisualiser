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
                end.end()
                start.start()
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
                end.end()
                start.start()
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
                end.end()
                start.start()
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
                end.end()
                start.start()
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
        visited = set()
        visited.add(start)
        prior = {}  # Store the parent nodes

        while stack:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = stack.pop()

            if current == end:
                self.find_shortest_path(prior, end, draw)
                end.end()
                start.start()
                return True

            dead_ends = []

            for neighbor in current.neighbours:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    prior[neighbor] = current
                    neighbor.to_explore()
                elif neighbor.is_barrier():
                    dead_ends.append(neighbor)

            if len(dead_ends) == 3:
                for node in dead_ends:
                    node.make_barrier()
                    node.barrier_color()
                    draw()

            if current != start:
                current.visited()

        return False
    