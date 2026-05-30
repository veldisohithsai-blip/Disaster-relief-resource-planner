# Disaster Relief Resource Planner
# Combines:
# 1. Path Search (Dijkstra's Algorithm)
# 2. Constraint Satisfaction (Supply and Vehicle Constraints)

import heapq

# -----------------------------
# Graph of locations and roads
# -----------------------------
graph = {
    'Warehouse': {'CampA': 4, 'CampB': 2},
    'CampA': {'Hospital': 5, 'Shelter': 10},
    'CampB': {'CampA': 1, 'Shelter': 8},
    'Hospital': {'Shelter': 2},
    'Shelter': {}
}

# -----------------------------
# Relief requests at locations
# -----------------------------
demands = {
    'CampA': {'food': 20, 'water': 10},
    'Hospital': {'food': 15, 'water': 20},
    'Shelter': {'food': 25, 'water': 30}
}

# -----------------------------
# Available supplies
# -----------------------------
available_resources = {
    'food': 70,
    'water': 70
}

# -----------------------------
# Vehicle capacity constraint
# -----------------------------
vehicle_capacity = 40

# -----------------------------
# Dijkstra shortest path search
# -----------------------------
def dijkstra(graph, start):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        yield (node, cost, path)

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))

# -----------------------------
# Allocate resources
# -----------------------------
def allocate_resources():
    print("\n--- Disaster Relief Resource Planner ---\n")

    for location, distance, path in dijkstra(graph, 'Warehouse'):

        if location in demands:

            required_food = demands[location]['food']
            required_water = demands[location]['water']

            total_required = required_food + required_water

            print(f"\nLocation: {location}")
            print(f"Shortest Path: {' -> '.join(path)}")
            print(f"Distance: {distance} km")

            # Constraint 1: Check resource availability
            if (required_food <= available_resources['food'] and
                required_water <= available_resources['water']):

                # Constraint 2: Check vehicle capacity
                if total_required <= vehicle_capacity:

                    available_resources['food'] -= required_food
                    available_resources['water'] -= required_water

                    print("Status: Allocation Successful")
                    print(f"Food Delivered: {required_food}")
                    print(f"Water Delivered: {required_water}")

                else:
                    print("Status: Vehicle capacity exceeded!")

            else:
                print("Status: Not enough resources available!")

    print("\nRemaining Resources:")
    print(available_resources)

# -----------------------------
# Run the planner
# -----------------------------
allocate_resources()
