from collections import defaultdict, deque

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.predecessors = []
        self.successors = []

def topological_sort(tasks):
    in_degree = {task: 0 for task in tasks}
    for task in tasks:
        for successor in tasks[task].successors:
            in_degree[successor] += 1
    
    queue = deque([task for task in tasks if in_degree[task] == 0])
    top_order = []
    
    while queue:
        current = queue.popleft()
        top_order.append(current)
        
        for successor in tasks[current].successors:
            in_degree[successor] -= 1
            if in_degree[successor] == 0:
                queue.append(successor)
    
    if len(top_order) == len(tasks):
        return top_order
    else:
        raise ValueError("The graph has at least one cycle")

def calculate_earliest_times(tasks, top_order):
    for task in top_order:
        tasks[task].EST = 0 if not tasks[task].predecessors else max(tasks[p].EFT for p in tasks[task].predecessors)
        tasks[task].EFT = tasks[task].EST + tasks[task].duration

def calculate_latest_times(tasks, top_order):
    project_duration = max(tasks[task].EFT for task in tasks)
    for task in tasks:
        tasks[task].LFT = project_duration
        tasks[task].LST = tasks[task].LFT - tasks[task].duration
    
    for task in reversed(top_order):
        if tasks[task].successors:
            tasks[task].LFT = min(tasks[s].LST for s in tasks[task].successors)
            tasks[task].LST = tasks[task].LFT - tasks[task].duration

def main():
    # Define tasks and their durations
    task_data = {
        'A': (3, []),
        'B': (2, ['A']),
        'C': (4, ['A']),
        'D': (2, ['B', 'C']),
        'E': (3, ['D']),
    }
    
    # Initialize tasks
    tasks = {name: Task(name, data[0]) for name, data in task_data.items()}
    
    # Add dependencies
    for name, data in task_data.items():
        for predecessor in data[1]:
            tasks[name].predecessors.append(predecessor)
            tasks[predecessor].successors.append(name)
    
    # Perform topological sort
    top_order = topological_sort(tasks)
    
    # Calculate earliest times
    calculate_earliest_times(tasks, top_order)
    
    # Calculate latest times
    calculate_latest_times(tasks, top_order)
    
    # Output results
    for task in tasks:
        print(f"Task {task}: EST={tasks[task].EST}, EFT={tasks[task].EFT}, LST={tasks[task].LST}, LFT={tasks[task].LFT}")
    
    project_duration = max(tasks[task].EFT for task in tasks)
    print(f"Earliest time all tasks will be completed: {project_duration}")
    print(f"Latest time all tasks will be completed: {project_duration}")

if __name__ == "__main__":
    main()
