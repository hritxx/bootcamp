from collections import deque

dq = deque()
dq.append(1)        
dq.appendleft(2)   
print("Pop right:", dq.pop())     
print("Pop left:", dq.popleft())  