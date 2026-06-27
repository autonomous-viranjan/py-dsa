# -*- coding: utf-8 -*-
"""PDSA.ipynb

Motivating example
"""

def gcd_naive(m, n):
  comm_div = []
  for i in range(1, min(m, n)+1):
    if m%i==0 and n%i==0:
      comm_div.append(i)

  return max(comm_div)

print(gcd_naive(50, 25))

def gcd_euclid(m, n):
  (a, b) = (max(m, n), min(m, n))
  if a%b == 0:
    return b
  else:
    return gcd_euclid(b, a%b)

print(gcd_euclid(50, 25))

"""Number of operations in about 1 sec"""

import time
n = 1e7
print('n=', n)
a = 0
tic = time.perf_counter()
for i in range(int(n)):
  a += 1
toc = time.perf_counter()
print(toc - tic)

"""<u>**Searching in a list**</u>"""

# iterative O(n)
def linear_search(l, val):
  ops = 0
  for i in range(len(l)):
    ops += 1
    if l[i] == val:
      print("ops:", ops)
      return True
  print("worst case ops:", ops)
  return False

# # recursive O(n) due to slicing
# def binary_search(l, val, ops=0):
#   # needs sorted list

#   m = len(l) // 2
#   ops += 1

#   if m == 0:
#     print("worst case ops:", ops)
#     return False

#   if l[m] == val:
#     print("ops:", ops)
#     return True

#   if l[m] < val:
#     return binary_search(l[m+1:], val, ops)
#   else:
#     return binary_search(l[:m], val, ops)

# recursive O(log n)
def binary_search(L, v, lidx, ridx, ops=0):
  # needs a sorted list
  if ridx - lidx < 0:
    print("worst case ops:", ops)
    return False
  mid = (lidx + ridx) // 2
  ops += 1
  if v == L[mid]:
    print("found at index:", mid)
    return True
  if v <  L[mid]:
    return binary_search(L, v, lidx, mid-1, ops)
  elif v > L[mid]:
    return binary_search(L, v, mid+1, ridx, ops)

import numpy as np
np.random.seed(1)
l = np.random.randint(1, 100, 10000)
# print(f"list: {l}\nn: {len(l)}")
l.sort()

print(linear_search(l, 101))

print(binary_search(l, 101, 0, len(l)-1))

"""<u>**Sorting**</u>"""

def bubble_sort(L):
  swap = True
  while swap:
    swap = False
    for i in range(len(L)-1):
      if L[i] > L[i+1]:
        (L[i], L[i+1]) = (L[i+1], L[i])
        swap = True
  return L

def selection_sort(L):
  for i in range(len(L)):
    min_pos = i
    for j in range(i+1, len(L)):
      if L[min_pos] > L[j]:
        min_pos = j
    (L[min_pos], L[i]) = (L[i], L[min_pos])

  return L

def insertion_sort(L):
  for i in range(len(L)):
    j = i
    while j > 0 and L[j] < L[j-1]:
      (L[j], L[j-1]) = (L[j-1], L[j])
      j -= 1

  return L

def merge(LL, RR):
  m, n = len(LL), len(RR)
  M = []
  i, j = 0, 0

  # when LL, RR both non empty
  while i < m and j < n:
    if LL[i] <= RR[j]:
      M.append(LL[i])
      i += 1
    else:
      M.append(RR[j])
      j += 1

  # when only LL non-empty
  while i < m:
    M.append(LL[i])
    i += 1

  # when only RR non-empty
  while j < n:
    M.append(RR[j])
    j += 1

  return M

def merge_sort(l):
  n = len(l)
  if n <= 1:
    return l

  LL = merge_sort(l[:n//2])
  RR = merge_sort(l[n//2:])

  M = merge(LL, RR)

  return M

def partion(L, start, end):
  piv = L[start]
  i = start
  for j in range(start+1, end):
    if L[j] < piv:
      i += 1
      L[i], L[j] = L[j], L[i]
  # swap pivot to median pos
  L[i], L[start] = L[start], L[i]

  return i

def quick_sort(L, start=None, end=None):
  if start == None or end == None:
    start, end = 0, len(L)

  if start < end:
    # obtain pivot index (at median pos)
    piv_idx = partion(L, start, end)
    # recursion on left part
    quick_sort(L, start, piv_idx-1)
    # recursion on right part
    quick_sort(L, piv_idx+1, end)

  return L

import numpy as np
np.random.seed(1)
L = np.random.randint(1, 100, 10)
# print(L)

import time

tic = time.perf_counter()
print(bubble_sort(L))
toc = time.perf_counter()
# print(toc-tic)

tic = time.perf_counter()
print(selection_sort(L))
toc = time.perf_counter()
# print(toc-tic)

tic = time.perf_counter()
print(insertion_sort(L))
toc = time.perf_counter()
# print(toc-tic)

tic = time.perf_counter()
print(merge_sort(L))
toc = time.perf_counter()
# print(toc-tic)
# print(L) # not in place

tic = time.perf_counter()
print(quick_sort(L))
toc = time.perf_counter()
# print(toc-tic)
# print(L) # in place

"""<u>**Graphs**</u>

Directed Graph
"""

V = [0, 1, 2, 3, 4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

import numpy as np

def adj_matrix_directed(V, E):
  AdjM = np.zeros((len(V), len(V)))
  for e in E:
    AdjM[e[0], e[1]] = 1

  return AdjM

print(adj_matrix_directed(V, E))

def adj_list_directed(V, E):
  AdjL = {}
  for v in V:
    AdjL[v] = []
    for e in E:
      if e[0] == v:
        AdjL[v].append(e[1])

  return AdjL

print(adj_list_directed(V, E))

"""Undirected Graph"""

V = [0, 1, 2, 3, 4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# Note: same G(V, E) rep but bidirectional edges now

def adj_matrix_undirected(V, E):
  AdjM = np.zeros((len(V), len(V)))
  for e in E:
    AdjM[e[0], e[1]] = 1
    AdjM[e[1], e[0]] = 1

  return AdjM

print(adj_matrix_undirected(V, E))

def adj_list_undirected(V, E):
  AdjL = {}
  for v in V:
    AdjL[v] = []

  for v in V:
    for e in E:
      if e[0] == v:
        AdjL[v].append(e[1])
        AdjL[e[1]].append(v)

  return AdjL

print(adj_list_undirected(V, E))

"""Queue data structure: FIFO"""

class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, v):
    self.queue.append(v)
    # self.queue.extend(v)

  def dequeue(self):
    if not self.queue:
      return None
    else:
      v = self.queue[0]
      self.queue = self.queue[1::]
      # v = self.queue.pop(0) # expensive O(n)
      return v

  def __str__(self):
    return str(self.queue)

"""Test"""

V = [i for i in range(5)]

Q = Queue()
for i in range(len(V)):
  Q.enqueue(V[i])
  print(Q)
for i in range(len(Q.queue)):
  print(Q.dequeue(), Q)

"""**BFS**:

$O(V^2)$ for Adjacecy matrix and $O(V + E)$ Adjacency list
"""

def bfs(AdjL, v_0):
  visited = [v_0]
  Q = Queue()
  Q.enqueue(v_0) # to expand

  while Q.queue:
    print("visited: ", visited)
    v_0 = Q.dequeue()

    for v_adj in AdjL[v_0]:
      if v_adj not in visited:
        # print(f"v_0:{v_0}, v_adj:{v_adj}")
        Q.enqueue(v_adj)
        visited.append(v_adj)
    print("queue:", Q.queue)

  return visited

# AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []} # directed
AList = {0: sorted([2, 1]), 1: sorted([4, 3, 0]), 2: sorted([4, 3, 0]),
         3: sorted([4, 2, 1]), 4: sorted([3, 2, 1])} # undirected
print(AList)
print("\nvisited:", bfs(AList,0))

"""Adding parent"""

def bfs_with_parent(AdjL, v):
  v_0 = v
  visited = [v_0]
  Q = Queue()
  Q.enqueue(v_0)
  parent = {}
  parent[v_0] = None
  while Q.queue:
    Q.dequeue()
    for v_adj in AdjL[v_0]:
      if v_adj not in visited:
        visited.append(v_adj)
        Q.enqueue(v_adj)
        parent[v_adj] = v_0
    v_0 = Q.dequeue()

  return visited, parent

AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
v, src = bfs_with_parent(AList, 0)
print(f"\nvisited: {v}\nparent: {src}")

"""Adding level"""

def bfs_with_level(AdjL, v0):
  v_0 = v0
  visited = [v_0]
  Q = Queue()
  Q.enqueue(v_0)
  level, parent = {}, {}
  parent[v_0] = None
  level[v_0] = 0
  while Q.queue:
    v_0 = Q.dequeue()
    for v_adj in AdjL[v_0]:
      if v_adj not in visited:
        visited.append(v_adj)
        Q.enqueue(v_adj)
        parent[v_adj] = v_0
        level[v_adj] = level[v_0] + 1

  return parent, level

AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
src, level = bfs_with_level(AList, 0)
print(f"\nparent: {src}\nlevel: {level}")

"""Stack data structure: LIFO"""

class Stack:
  def __init__(self):
    self.stack = []

  def enstack(self, item):
    self.stack.append(item)

  def destack(self):
    v = None
    if self.stack:
      v = self.stack.pop()

    return v

  def __str__(self):
    return str(self.stack)

"""Test"""

V = [i for i in range(5)]

s = Stack()
for i in range(len(V)):
  s.enstack(V[i])
  print(s)

while s.stack:
  print(s.destack(), s)

def dfs(AdjL, v0):
  v_0 = v0
  visited = [v_0]
  s = Stack()
  s.enstack(v_0)

  while s.stack:
    v_0 = s.destack()
    if v_0 not in visited:
      visited.append(v_0)
    print('visited: ', visited)

    for v_adj in AdjL[v_0]:
      if v_adj not in visited:
        s.enstack(v_adj)
    print('stack: ', s)

  return visited

# AList = {0: [2, 1], 1: [4, 3], 2: [4, 3], 3: [4], 4: []} # directed
AList = {0: sorted([2, 1], reverse=True), 1: sorted([4, 3, 0], reverse=True),
         2: sorted([4, 3, 0], reverse=True), 3: sorted([4, 2, 1], reverse=True),
         4: sorted([3, 2, 1], reverse=True)} # undirected
# sorted to ensure smaller vertex visited first
# can have some other rule too
print(AList)

dfs(AList, 0)

"""**Directed Acyclic Graph (DAG)**
- No cycles
- Has at least 1 node/vertex with 0 indegree

*Topological sorting*

$O(V+E)$ on adjacency list; $O(V^2)$ on adjacency matrix
"""

def topo_sort(AdjL):
  topolist = []
  indegree = {}
  for v in AdjL.keys():
    indegree[v] = 0

  for v in AdjL.keys():
    for v_adj in AdjL[v]:
      indegree[v_adj] += 1
  # print(indegree)

  zero_indeg_q = Queue()
  for v in indegree.keys():
    if indegree[v] == 0:
      zero_indeg_q.enqueue(v)

  while zero_indeg_q.queue:
    v_current = zero_indeg_q.dequeue()

    for v_adj in AdjL[v_current]:
      indegree[v_adj] -= 1
      if indegree[v_adj] == 0:
        zero_indeg_q.enqueue(v_adj)

    topolist.append(v_current)

  return topolist

AList={0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
print(topo_sort(AList))

"""Longest path (gives min time to completion since the bottleneck path is what determines the min time required)"""

def longest_path_dag(AdjL):
  indegree, longest_path = {}, {}
  for v in AdjL.keys():
    indegree[v] = 0
    longest_path[v] = 0

  for v in AdjL.keys():
    for v_adj in AdjL[v]:
      indegree[v_adj] += 1

  q_toposort = Queue()
  for v in indegree.keys():
    if indegree[v] == 0:
      q_toposort.enqueue(v)

  while q_toposort.queue:
    v0 = q_toposort.dequeue()
    for v_adj in AdjL[v0]:
      indegree[v_adj] -= 1
      longest_path[v_adj] = max(longest_path[v_adj], longest_path[v0] + 1)
      if indegree[v_adj] == 0:
        q_toposort.enqueue(v_adj)

  return longest_path

AList={0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
print(longest_path_dag(AList))

"""Weighted Graph"""

# Adjacency list
edges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)] # (i, j, weight)

# obtaining vertices
V = []
for i,j,w in edges:
  if i not in V:
    V.append(i)
  if j not in V:
    V.append(j)
V.sort()
print(V)
AdjL = {}
for n in range(len(V)):
  AdjL[n] = []

for i,j,w in edges:
  AdjL[i].append((j, w))

# list(AdjL.keys())
print(AdjL)

"""**Dijkstra's Algorithm**:
- Greedy shortest (weighted) path search (from single source)
  - immediate min cost vertex visited
  - each vertex visited (and updated) once
- $O(|V|^2)$ with both adjacency mat and list
"""

def dijkstra(AdjL, v_src):
  inf = 1e3
  # ideally: max(weight)*v + 1: requires O(V^2) time
  cost, visited = {}, []

  for v in AdjL.keys():
    cost[v] = inf
  cost[v_src] = 0

  for v in AdjL.keys():
    print("Iter: ", v)
    # choose unvisited vertex and has min cost
    min_cost = inf
    for vert in cost.keys():
      if vert not in visited and cost[vert] < min_cost:
        min_cost = cost[vert]
        u = vert

    print("Current vertex:", u)
    visited.append(u)

    # expand and update adj vertex cost
    for v_adj, w in AdjL[u]:
      if v_adj not in visited:
        cost[v_adj] = min(cost[v_adj], cost[u] + w)

  return cost, visited

dijkstra(AdjL, v_src=0)

c, v = dijkstra(AdjL, 0)
if c == {0: 0, 1: 10, 2: 16, 3: 86, 4: 30, 5: 80, 6: 35} and len(v) == len(V):
  print('correct')

"""**Bellman-Ford Algorithm**
- Can handle <u>negative</u> weights
- Can detect negative cycles
* $O(V*E)$ with adjacency list and $O(V^3)$ with adj mat
"""

edges = [(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]
V = []
for i,j,w in edges:
  if i not in V:
    V.append(i)
  if j not in V:
    V.append(j)
V.sort()
print(V)

AdjL = {}
for v in V:
  AdjL[v] = []
for i,j,w in edges:
  AdjL[i].append((j, w))
print(AdjL)

def bellman_ford(AdjL, v0):
  inf = 1e3
  cost = {}
  for v in AdjL.keys():
    cost[v] = inf
  cost[v0] = 0

  for i in AdjL.keys():
    print("Iter: ", i)
    for u in AdjL.keys():
      print(f"Vertex: {u} Cost: {cost[u]}")
    for u in AdjL.keys():
      for v,w in AdjL[u]:
        cost[v] = min(cost[v], cost[u] + w) # DP update of each adj vert of each vertex

  return cost

sol = bellman_ford(AdjL, 0)
print(sol)

ans = {0: 0, 1: 5, 2: 5, 3: 6, 4: 9, 5: 7, 6: 9, 7: 8}

for v in ans.keys():
  if sol[v] != ans[v]:
    print('incorrect')
    break
  else:
    print('correct')

"""All pair shortest path:
**Floyd-Warshall** -- DP based

$O(|V|^3)$ time complexity
"""

edges = [(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]

V = []
for i,j,w in edges:
  if i not in V:
    V.append(i)
  if j not in V:
    V.append(j)
n = len(V)

import numpy as np
Wmat = np.inf * np.ones((n, n))
for i,j,w in edges:
  Wmat[i, j] = w
print(Wmat)

def floydwarshall(Wmat):

  (rows, cols) = Wmat.shape
  C = np.inf * np.ones((rows, cols, cols+1))
  for r in range(rows):
    for c in range(cols):
      C[r, c, 0] = Wmat[r, c]

  for k in range(1, cols+1):
    for i in range(rows):
      for j in range(cols):
        C[i, j, k] = min(C[i, j, k-1], C[i, k-1, k-1] + C[k-1, j, k-1])

  return C[:, :, -1]

print(floydwarshall(Wmat))

def floydwarshall_reduced_space(Wmat):
  r, c = Wmat.shape
  C = np.inf * np.ones((r, c, 2))

  for i in range(r):
    for j in range(c):
      C[i, j, 0] = Wmat[i, j]

  for k in range(0, c):
    for i in range(r):
      for j in range(c):
        C[i, j, 1] = min(C[i, j, 0], C[i, k, 0] + C[k, j, 0]) # DP

    C[:, :, 0] = C[:, :, 1]  # at the end if each iter make updated C as the initial

  return C[:, :, 1]

print(floydwarshall_reduced_space(Wmat))

"""<u>Minimum Cost Spanning Tree</u>

Tree => 1. All nodes connected 2. No cycles (unique pairs) 3. N nodes => N-1 edges

Prim's Algorithm:

Vertex by vertex expansion

$O(|V|^2)$ time
"""

dir_edges = [(0,1,10),(0,3,18),(1,2,20),(1,3,6),(2,4,8),(3,4,70)]
edges = dir_edges + [(j, i, w) for i, j, w in dir_edges]
# print(edges)
V = []
for i,j,w in edges:
  if i not in V:
    V.append(i)
  if j not in V:
    V.append(j)
V.sort()
# print(V)
Wlist = {}
for v in V:
  Wlist[v] = []
for i,j,w in edges:
  Wlist[i].append((j, w))
print(Wlist)

import numpy as np
def prims_mcst(AdjL, v0=0):
  visited = []
  TreeEdges = []

  N = len(AdjL.keys())
  u_add = v0

  while len(TreeEdges) != N-1:
    visited.append(u_add)
    print("visited: ", u_add)
    w_min = np.inf
    for u in visited:
      for v,w in AdjL[u]:
        if (v not in visited) and w < w_min:
          w_min = w
          u_add = u
          v_add = v

    visited.append(v_add)
    print("added: ", v_add)
    # adding node pair (u, v) s.t. u in visited and v not visited yet and has min cost
    TreeEdges.append((u_add, v_add))

  return TreeEdges

print("Min Cost Spanning Tree:", prims_mcst(Wlist))

"""Kruskal's algorithm:

Edge by edge expansion

$O(|V|^2)$ time
"""

def kruskals_mcst(AdjL):
  edges, lead, TreeEdges = [], {}, []

  for u in AdjL.keys():
    edges.extend([(w,u,v) for (v,w) in AdjL[u]]) # weight as first element for sorting
    lead[u] = u # initially components include individual edges only

  edges.sort()
  # print(edges)

  for (w,u,v) in edges:
    if lead[u] != lead[v]: # prevents cycles
      TreeEdges.append((u, v))
      c = lead[u]
      # update lead of all nodes with u as lead
      for n in AdjL.keys():
        if lead[n] == c:
          lead[n] = lead[v] # assign v as lead when (u,v) edge appended

  return TreeEdges

dedges = [(0,1,10),(0,2,18),(1,2,6),(1,4,20),(2,3,70),(4,5,10),(4,6,10),(5,6,5)]
edges = dedges + [(j,i,w) for (i,j,w) in dedges]
V = []
for (i,j,w) in edges:
  if i not in V:
    V.append(i)
V.sort()
# print(V)

Wlist = {}
for v in V:
  Wlist[v] = []
for u,v,w in edges:
  Wlist[u].append((v, w))
# print(Wlist)

kruskals_mcst(Wlist)

"""[(5, 6), (1, 2), (0, 1), (4, 5), (1, 4), (2, 3)]

grows the tree in order of edge weights (starting with min)

<u>**Data Structures**</u> and usage

Union find
"""

# Naive implementation

class UnionFind:
  def __init__(self):
    self.lead = {}
    self.size = len(self.lead)

  def singletons(self, n_vertices):
    self.size = n_vertices
    for v in range(n_vertices):
      self.lead[v] = v

  def find_lead(self, vertex):
    return self.lead[vertex]

  def union(self, u, v):
    c_old = self.lead[u]
    c_new = self.lead[v]
    for i in range(self.size):
      if self.lead[i] == c_old:
        self.lead[i] = c_new

"""- singletons $O(n)$
- find $O(1)$
- union $O(n)$
"""

# Improved implementation

class UnionFindStar:
  def __init__(self):
    self.lead, self.members, self.size = {}, {}, {}

  def singleton(self, n_vertices):
    for v in range(n_vertices):
      self.lead[v] = v
      self.members[v] = [v]
      self.size[v] = 1

  def find_lead(self, vertex):
    return self.lead[vertex]

  def union(self, u, v):
    c_old = self.lead[u]
    c_new = self.lead[v]
    if self.size[c_old] < self.size[c_new]:
      for vert in self.members[c_old]:
        self.members[c_new].append(vert)
        self.lead[vert] = c_new
        self.size[c_new] += 1
    else:
      for vert in self.members[c_new]:
        self.members[c_old].append(vert)
        self.lead[vert] = c_old
        self.size[c_old] += 1

uds = UnionFindStar()
uds.singleton(5)
uds.lead

"""- union now $O(log\;n)$

Improving Kruskal's algorithm with improved Union Find Data Structure
"""

def kruskal_star(AdjL):
  UnionDS = UnionFindStar()
  UnionDS.singleton(len(AdjL.keys()))
  edges, TreeEdges = [], []

  for u in AdjL.keys():
    edges.extend([(w,u,j) for j,w in AdjL[u]])

  edges.sort()

  for (w,u,v) in edges:
    if UnionDS.find_lead(u) != UnionDS.find_lead(v):
      UnionDS.union(u, v)
      TreeEdges.append((u, v, w))

  return TreeEdges

kruskal_star(Wlist)

edge = [(0,1,10),(0,2,18),(0,3,6),(0,4,20),(0,5,13),(1,2,10),(1,3,10),(1,4,5),(1,5,7),(2,3,2),(2,4,14),(2,5,15),(3,4,17),(3,5,12),(4,5,10)]

size = 6
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in edge:
    WL[i].append((j,d))

kruskal_star(WL)

"""sorting takes $O(mlogm)$ time and union now takes $O(nlogn)$ time. Since $m < n^2$, overall time now $O((m+n)logn)$

<u>Heap data structure</u>
"""

class MaxHeap:
  def __init__(self):
    self.H = []

  def build_heap(self, L):
    n_half = int(len(L) // 2)
    self.H = L
    # parents till (n_half-1) index; after that it's all leaves => no children
    for n in range(n_half-1, -1, -1):
      self.max_heapyfy(n)

  def max_heapyfy(self, n):
    l = 2*n + 1
    r = 2*n + 2
    n_larger = n
    if l < len(self.H) and self.H[l] > self.H[n_larger]:
      n_larger = l
    if r < len(self.H) and self.H[r] > self.H[n_larger]:
      n_larger = r
    if n_larger != n:
      self.H[n], self.H[n_larger] = self.H[n_larger], self.H[n]
      self.max_heapyfy(n_larger) # need to ensure heap down the line

  def insert(self, val):
    self.H.append(val)
    # self.build_heap(self.H) # will take O(n) - can do O(log n) as follows
    idx = len(self.H) - 1
    while idx > 0:
      idx_parent = (idx - 1) // 2
      if self.H[idx] > self.H[idx_parent]:
        self.H[idx], self.H[idx_parent] = self.H[idx_parent], self.H[idx]
        idx = idx_parent
      else:
        break

  def del_max(self):
    self.H[0], self.H[-1] = self.H[-1], self.H[0]
    v_max = self.H.pop()
    self.max_heapyfy(0)
    return v_max

max_heap = MaxHeap()
L = [1,2,3,4,5,6]
max_heap.build_heap(L)
print(max_heap.H)
max_heap.insert(7)
print(max_heap.H)
max_heap.insert(8)
print(max_heap.H)
v = max_heap.del_max()
print(v)
print(max_heap.H)
v = max_heap.del_max()
print(v)
print(max_heap.H)

L = [6, 5, 3, 4, 2, 1]
Root, T = [L[-1]], L[0:-1]
Root.extend(T)
print(Root)

class MinHeap:
  def __init__(self):
    self.H = []

  def build_heap(self, L):
    self.H = L
    n_half = len(L) // 2
    for n in range(n_half-1, -1, -1):
      self.min_heapyfy(n)

  def min_heapyfy(self, n):
    smaller = n
    l = 2*n + 1
    r = 2*n + 2
    if l < len(self.H) and self.H[l] < self.H[smaller]:
      smaller = l
    if r < len(self.H) and self.H[r] < self.H[smaller]:
      smaller = r
    if smaller != n:
      self.H[n], self.H[smaller] = self.H[smaller], self.H[n]
      self.min_heapyfy(smaller)

  def insert(self, val):
    self.H.append(val)
    idx = len(self.H) - 1
    while idx > 0:
      idx_parent = (idx - 1) // 2
      if self.H[idx_parent] > self.H[idx]:
        self.H[idx], self.H[idx_parent] = self.H[idx_parent], self.H[idx]
        idx = idx_parent
      else:
        break

  def del_min(self):
    # v_min = self.H.pop(0) # O(n) - can do better by swapping first, last and then pop()
    self.H[0], self.H[-1] = self.H[-1], self.H[0]
    v_min = self.H.pop() # O(1)
    self.min_heapyfy(0)
    return v_min

L = [6,5,4,3,2]
min_heap = MinHeap()
min_heap.build_heap(L)
print(min_heap.H)
min_heap.insert(1)
print(min_heap.H)
min_heap.insert(8)
print(min_heap.H)
print(min_heap.del_min())
print(min_heap.H)
print(min_heap.del_min())
print(min_heap.H)

"""build_heap() - $O(n)$

insert() - $O(log n)$

del_max(), del_min() - $O(logn)$

* Improving Dijkstra's shortest path algo with Heaps
"""

# previous implementation
def dijkstra(Weighted_AdjL, v0):
  inf = 1e3
  visited, cost = [], {}
  for v in Weighted_AdjL.keys():
    cost[v] = inf
  cost[v0] = 0

  for i in Weighted_AdjL.keys():
    print("Iter:", i)
    min_cost = inf
    for v in cost.keys():
      if v not in visited and cost[v] < min_cost:
        min_cost = cost[v]
        u = v
        print("u set to:", v)

    print("Expanding:", u)
    visited.append(u)

    for vert, w in Weighted_AdjL[u]:
      if vert not in visited:
        cost[vert] = min(cost[vert], cost[u]+w)

  return visited, cost

dijkstra(AdjL, 0)

class HeapDijkstra:
  def __init__(self, AdjL):
    self.v_src = None
    self.AdjL = AdjL
    self.vertex_to_heapindex = {} # maps vertex number to heap index
    self.heapindex_to_vertex = {} # maps heap index to [vertex, cost to vertex]

  def build_heap(self, size):
    n_half = size // 2
    for h in range(n_half-1, -1, -1):
      self.min_heapyfy(h, size)

  def min_heapyfy(self, h, size):
    smaller = h
    l = 2*h + 1
    r = 2*h + 2
    if l < size and self.heapindex_to_vertex[l][1] < self.heapindex_to_vertex[smaller][1]:
      smaller = l
    if r < size and self.heapindex_to_vertex[r][1] < self.heapindex_to_vertex[smaller][1]:
      smaller = r
    if smaller != h:
      self.vertex_to_heapindex[self.heapindex_to_vertex[h][0]] = smaller
      self.vertex_to_heapindex[self.heapindex_to_vertex[smaller][0]] = h

      self.heapindex_to_vertex[h], self.heapindex_to_vertex[smaller] = self.heapindex_to_vertex[smaller], self.heapindex_to_vertex[h]

      self.min_heapyfy(smaller, size)

  def del_min(self, size):
    self.vertex_to_heapindex[self.heapindex_to_vertex[size-1][0]] = 0
    self.vertex_to_heapindex[self.heapindex_to_vertex[0][0]] = size - 1

    self.heapindex_to_vertex[0], self.heapindex_to_vertex[size-1] = self.heapindex_to_vertex[size-1], self.heapindex_to_vertex[0]

    node, cost = self.heapindex_to_vertex[size-1]

    new_size = size - 1
    self.min_heapyfy(0, new_size)

    return node, cost, new_size

  def update_min_heap(self, i, size):
    while i > 0:
      parent = (i - 1) // 2
      if self.heapindex_to_vertex[i][1] < self.heapindex_to_vertex[parent][1]:
        self.vertex_to_heapindex[self.heapindex_to_vertex[i][0]] = parent
        self.vertex_to_heapindex[self.heapindex_to_vertex[parent][0]] = i

        self.heapindex_to_vertex[i], self.heapindex_to_vertex[parent] = self.heapindex_to_vertex[parent], self.heapindex_to_vertex[i]
      else:
        break
      i = parent

  def run(self, v_src=0):
    inf = float('inf')
    visited = []
    for v in self.AdjL.keys():
      self.vertex_to_heapindex[v] = v
      self.heapindex_to_vertex[v] = [v, inf]
    self.heapindex_to_vertex[v_src] = [v_src, 0]

    n = len(self.AdjL)
    self.build_heap(n)

    for i in self.AdjL.keys():
      print("Iter:", i)
      u, u_cost, n = self.del_min(n) # O(log n)
      print("expanding:", u)
      visited.append(u)

      for vert, cost in self.AdjL[u]:
        if vert not in visited:
          # update cost
          self.heapindex_to_vertex[self.vertex_to_heapindex[vert]][1] = min(self.heapindex_to_vertex[self.vertex_to_heapindex[vert]][1], u_cost+cost) # O(m)
          self.update_min_heap(self.vertex_to_heapindex[vert], n) # O(logn)

    return visited, self.heapindex_to_vertex

v_src = 0
print("Graph:", AdjL)
heap_dijkstra = HeapDijkstra(AdjL)
heap_dijkstra.run(v_src)

"""Example usage of heap id to vertex and vice-versa dictionary"""

HtoV = {0:6, 1:4, 2:2}
VtoH = {2:2, 4:1, 6:0}
n = len(VtoH)
h=0
smaller = h
l = 2*h + 1
r = 2*h + 2
if l < n and HtoV[l] < HtoV[smaller]:
  smaller = l
if r < n and HtoV[r] < HtoV[smaller]:
  smaller = r
if smaller != h:
  print(f"smaller index: {smaller}; vertex: {HtoV[smaller]}")
  # HtoV[h], HtoV[smaller] = HtoV[smaller], HtoV[h]
  # VtoH[HtoV[h]], VtoH[HtoV[smaller]] = VtoH[HtoV[smaller]], VtoH[HtoV[h]]

  # VtoH[HtoV[h]], VtoH[HtoV[smaller]] = VtoH[HtoV[smaller]], VtoH[HtoV[h]]
  # HtoV[h], HtoV[smaller] = HtoV[smaller], HtoV[h]

  ### order of update matters in this but less typing
  VtoH[HtoV[h]], VtoH[HtoV[smaller]] = smaller, h
  HtoV[h], HtoV[smaller] = HtoV[smaller], HtoV[h]

  # HtoV[h], HtoV[smaller] = HtoV[smaller], HtoV[h]
  # VtoH[HtoV[h]], VtoH[HtoV[smaller]] = smaller, h


print(VtoH)
print(HtoV)

"""Implementing Dijkstra with heap results in

$O(|V|log|V|)$ min node search [$|V|$ iters $O(log|V|)$ heapyfy]

$O(|E|log|V|)$ in cost update [each node visited only once, $|E|$ distance updates and $O(log|V|)$ heap update]

Total $O((|V| + |E|)log|V|)$

Heap sort
"""

class HeapSort:
  def __init__(self):
    self.H = []

  def sort(self, L):
    self.H = L
    size = len(L)

    for i in range(size, 0, -1):
      self.build_heap(i)
      self.move_max(i)

    return self.H

  def heapyfy(self, h_index, size):
    larger = h_index
    l = 2*h_index + 1
    r = 2*h_index + 2
    if l < size and self.H[l] > self.H[larger]:
      larger = l
    if r < size and self.H[r] > self.H[larger]:
      larger = r
    if larger != h_index:
      self.H[h_index], self.H[larger] = self.H[larger], self.H[h_index]
      self.heapyfy(larger, size)

  def build_heap(self, size):
    n_half = size // 2
    for n in range(n_half-1, -1, -1):
      self.heapyfy(n, size)

  def move_max(self, size):
    self.H[0], self.H[size-1] = self.H[size-1], self.H[0]
    # size -= 1
    # return size

L = [8,6,9,3,4,5,61,6666]
sorter = HeapSort()
sorter.sort(L)

"""Trees"""

class Tree:
  def __init__(self, value=None):
    self.value = value
    if self.value:
      self.left = Tree()
      self.right = Tree()
    else:
      self.left = None
      self.right = None

  def isempty(self):
    return self.value == None

  def isleaf(self):
    return self.left == None and self.right == None

  def inorder(self):
    if self.isempty():
      return []
    else:
      return self.left.inorder() + [self.value] + self.right.inorder()

  def find(self, val):
    if self.isempty():
      return False

    elif self.value == val:
      return True
    elif val < self.value:
      return self.left.find(val)
    else:
      return self.right.find(val)

  def minval(self):
    if self.left.isempty():
      return self.value
    else:
      return self.left.minval()

  def maxval(self):
    if self.right.isempty():
      return self.value
    else:
      return self.right.maxval()

  def insert(self, v):
    if self.value == v:
      return
    if self.isempty():
      self.value = v
      self.left = Tree()
      self.right = Tree()
    elif v < self.value:
      self.left.insert(v)
    else:
      self.right.insert(v)

  def delete(self, v):
    if self.isempty():
      return
    if v == self.value:
      if self.isleaf():
        self.value = None
      if self.left.isempty():
        # promote right
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
      elif self.right.isempty():
        # promote left
        self.value = self.left.value
        self.left = self.left.left
        self.right = self.left.right
      else:
        self.value = self.right.minval()
        self.delete(self.right.minval())

    if v < self.value:
      self.left.delete(v)
    elif v > self.value:
      self.right.delete(v)

  def __str__(self):
    return str(self.inorder())

test_tree = Tree()
# test_tree.isempty()
# test_tree.isleaf()
# test_tree.inorder()
print(test_tree)
for i in range(10):
  test_tree.insert(i)
print(test_tree)
print(test_tree.minval())
test_tree.delete(5)
print(test_tree)

"""AVL Tree: self balancing tree

Balance factor/Slope = |height(right) - height(left)| <= 1

Ensures find, insert, delete etc. $O(log n)$. In unbalanced tree, in the worst case these operations can become $O(n)$
"""

class AVLTree:
  def __init__(self, value=None):
    self.value = value
    if self.value:
      self.left = AVLTree()
      self.right = AVLTree()
      self.height = 1
    else:
      self.left = None
      self.right = None
      self.height = 0

  def isempty(self):
    return self.value == None

  def inorder(self):
    if self.isempty():
      return []
    return self.left.inorder() + [self.value] + self.right.inorder()

  def insert(self, v):
    if self.isempty():
      self.value = v
      self.left = AVLTree()
      self.right = AVLTree()
      self.height = 1
      return
    if self.value == v:
      return
    if v < self.value:
      self.left.insert(v)
      self.rebalance()
      self.height = 1 + max(self.left.height, self.right.height)
    if v > self.value:
      self.right.insert(v)
      self.rebalance()
      self.height = 1 + max(self.left.height, self.right.height)

  def rebalance(self):
    if self.left:
      hl = self.left.height
    else:
      hl = 0
    if self.right:
      hr = self.right.height
    else:
      hr = 0

    if hl - hr > 1:
      if self.left.left.height > self.left.right.height:
        self.rotate_right()
      if self.left.right.height > self.left.left.height:
        self.left.rotate_left()
        self.rotate_right()
      self.update_height()
    if hr - hl > 1:
      if self.right.right.height > self.right.left.height:
        self.rotate_left()
      if self.right.left.height > self.right.right.height:
        self.right.rotate_right()
        self.rotate_left()
      self.update_height()

  def update_height(self):
    if self.isempty():
      return
    else:
      self.left.update_height()
      self.right.update_height()
      self.height = 1 + max(self.left.height, self.right.height)

  def rotate_left(self):
    v = self.value
    vr = self.right.value
    # subtree tips
    nl = self.left
    nrl = self.right.left
    nrr = self.right.right
    # new
    self.value = vr
    self.left = AVLTree(v)
    self.right = nrr
    self.left.left = nl
    self.left.right = nrl

  def rotate_right(self):
    v = self.value
    vl = self.left.value
    # subtree tips
    nll = self.left.left
    nlr = self.left.right
    nr = self.right
    # new
    self.value = vl
    self.left = nll
    self.right = AVLTree(v)
    self.right.left = nlr
    self.right.right = nr

A = AVLTree()
for i in range(10):
    A.insert(i)

print(A.inorder())
A.height

if __name__ == "__main__":
    """ Run the test cases for the module """
