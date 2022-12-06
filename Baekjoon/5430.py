import sys
from collections import deque

for test_case in range(int(sys.stdin.readline())):
  error = False
  reverse = False

  command_list = sys.stdin.readline().strip()
  num_cnt = int(sys.stdin.readline())
  num_list = deque(sys.stdin.readline().strip()[1:-1].split(","))
  
  if num_cnt == 0:
    num_list = deque()

  for command in command_list:
    if command == "R":
      if reverse:
        reverse = False
      else:
        reverse = True

    else: 
      if num_list:
        if reverse:
          num_list.pop()
        else:
          num_list.popleft()
      else:
        error = True
        break
      
  if error:
    print("error")
  elif reverse:
    num_list.reverse()
    print("["+",".join(num_list)+"]")
  else:
    print("["+",".join(num_list)+"]")