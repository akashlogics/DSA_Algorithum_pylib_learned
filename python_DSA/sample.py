from collections import deque

# Create a double-ended queue
double_ended_queue = deque()

# Add elements to the right side of the queue
double_ended_queue.append('element1')
double_ended_queue.append('element2')

# Add elements to the left side of the queue
double_ended_queue.appendleft('element3')
double_ended_queue.appendleft('element4')

# Remove and return an element from the right side of the queue
right_element = double_ended_queue.pop()

# Remove and return an element from the left side of the queue
left_element = double_ended_queue.popleft()

print(double_ended_queue)  # Output: deque(['element4', 'element3', 'element1', 'element2'])
print(right_element)  # Output: element2
print(left_element)  # Output: element4


from collections import deque

# Create a double-ended queue
double_ended_queue = deque(['element4', 'element3', 'element1', 'element2'])

def reverse_queue(queue):
    if len(queue) == 0:
        return queue
    else:
        temp = queue.popleft()
        reverse_queue(queue)
        queue.append(temp)

reverse_queue(double_ended_queue)

print(double_ended_queue)  # Output: deque(['element2', 'element1', 'element3', 'element4'])