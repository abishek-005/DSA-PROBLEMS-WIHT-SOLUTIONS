class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        def __repr__(self):
            return f"Task('{self.description}', {self.priority})"
def quicksort_tasks(tasks):
    if len(tasks) <= 1:
        return tasks
    pivot = tasks[len(tasks) // 2]
    left = [t for t in tasks if t.priority < pivot.priority]
    middle = [t for t in tasks if t.priority == pivot.priority]
    right = [t for t in tasks if t.priority > pivot.priority]
    return quicksort_tasks(right) + middle + quicksort_tasks(left)#this guy is the reason why the list is sorted in desc order
                                                           #because the arguments passed are right+middle+left soo desc
                                                        #for retrun the ascen pass the argument as left+middle+right
# Example usage
tasks = [
Task("Complete project report", 3),
Task("Buy groceries", 2),
Task("Call client", 1),
Task("Prepare presentation", 3),
Task("Schedule team meeting", 2)
]
sorted_tasks = quicksort_tasks(tasks)
for task in sorted_tasks:
    print(f"Priority {task.priority}: {task.description}")
