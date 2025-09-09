from collections import deque
def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    start = (0, 0)
    q = deque([(start, [])])  
    visited = set([start])
    while q:
        (x, y), path = q.popleft()
        if x == target or y == target:
            return path + [(x, y)]
        possible_states = [
            (jug1_capacity, y), 
            (x, jug2_capacity),  
            (0, y),              
            (x, 0),              
            (max(0, x - (jug2_capacity - y)), min(jug2_capacity, y + x)),
            (min(jug1_capacity, x + y), max(0, y - (jug1_capacity - x))),
        ]
        for state in possible_states:
            if state not in visited:
                visited.add(state)
                q.append((state, path + [(x, y)]))
    return None  
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2
    result = water_jug_bfs(jug1_capacity, jug2_capacity, target)
    if result:
        print("Solution found:")
        for step in result:
            print(step)
    else:
        print("No solution exists.")
