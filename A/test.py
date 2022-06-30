from heapq import heappush, heappop
from re import M

class Node:
    def __init__(self,txt, val) -> None:
        self.txt = txt
        self.val = val
    def __lt__(self, other):
        return self.val > other.val
my_list = []
heappush(my_list, Node("1", 1))
heappush(my_list, Node("2", 1))
print(heappop(my_list).txt)
print(heappop(my_list).txt)

