import queue
import math
def bfs(arr):
    queue  = queue.Queue()
    s = arr[0]
    pi = [None] * len(arr)
    d = [math.inf] * len(arr)
    color = ['white'] * len(arr)
    color[0] = 'gray'
    while not queue.empty():
        u = queue.get()
        
#print(queue.get())
