import networkx as nx
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.split() for a in f.readlines()]

g = nx.DiGraph([(line[1], line[7]) for line in lines])
print("Part 1: ", "".join(nx.lexicographical_topological_sort(g)))

workers = 5
def timeForTask(c):
    return ord(c)-4

t = 0
taskTimes = []
tasks = []
while tasks or g:
    openTasks = [a for a in g if a not in tasks and g.in_degree(a) == 0]
    if openTasks and len(tasks) < workers:
        task = min(openTasks)
        taskTimes.append(timeForTask(task))
        tasks.append(task)
    else:
        minTime = min(taskTimes)
        finished = [tasks[i] for i,v in enumerate(taskTimes) if v == minTime]
        taskTimes = [v-minTime for v in taskTimes if v > minTime]
        tasks = [t for t in tasks if t not in finished]
        t += minTime
        g.remove_nodes_from(finished)
print("Part 2: ", t)
