# Graph - DFS and BFS Traversal Patterns

> **Core idea:** Traverse connected nodes. DFS explores a path before backtracking; BFS explores with a queue. In a grid, each cell is a node connected to its valid neighbors.

## Problems

| # | Problem | LeetCode | Time | Space | Condition | Why | Approach | Special Attention |
|---|---------|----------|------|-------|-----------|-----|----------|-------------------|
| 1 | **Flood Fill** | [#733](https://leetcode.com/problems/flood-fill/) | O(R * C) | O(R * C) | Same original color and within bounds | Find all same-color cells connected to the starting cell | DFS from `(sr, sc)`; recolor each matching cell and explore up, down, left, and right. | Return early if the original color already equals the new color. Recolor before exploring neighbors to mark a cell visited. |
| 2 | **Flood Fill (BFS)** | [#733](https://leetcode.com/problems/flood-fill/) | O(R * C) | O(R * C) | Same original color and within bounds | Find all same-color cells connected to the starting cell | Use a queue; recolor each matching cell and add it to the queue. | Recolor before enqueueing to mark the cell visited and prevent other neighbors from enqueueing it again. |
| 3 | **Island Perimeter (DFS)** | [#463](https://leetcode.com/problems/island-perimeter/) | O(R * C) | O(R * C) | Neighbor is outside the grid or water | Count exposed sides of the island | DFS from the first land cell; add one for each side facing water or outside the grid. | Mark visited land in place as `-1`; skip cells already marked. |
| 4 | **Island Perimeter (BFS)** | [#463](https://leetcode.com/problems/island-perimeter/) | O(R * C) | O(R * C) | Neighbor is outside the grid or water | Count exposed sides of the island | BFS from the first land cell; add one for each side facing water or outside the grid. | Mark land `-1` before enqueueing so it is only queued once. |
| 5 | **Max Area of Island (DFS)** | [#695](https://leetcode.com/problems/max-area-of-island/) | O(R * C) | O(R * C) | | | Scan all cells; DFS returns `1 +` the areas from four neighbors. Keep the largest island area. Use direct recursive summation or a direction loop. | Water and out-of-bounds return `0`. Mark visited land as `0` before recursion. Reset the area for each island, but keep `max_area` across islands. |
| 6 | **Max Area of Island (BFS)** | [#695](https://leetcode.com/problems/max-area-of-island/) | O(R * C) | O(R * C) | | | Start BFS at each unvisited land cell with area `1`; count newly discovered land cells and update `max_area`. | Mark land `0` before enqueueing. Count the starting cell once and reset the area for each BFS. |
| 7 | **Number of Islands (DFS)** | [#200](https://leetcode.com/problems/number-of-islands/) | O(R * C) | O(R * C) | | | Scan the grid; each DFS from unvisited land clears one whole island. Count these DFS starts. Use four direct calls or a direction loop. | Grid values are strings: `"1"` and `"0"`. Mark land as `"0"` before recursion; increment the island count once per traversal, not once per cell. |
| 8 | **Number of Islands (BFS)** | [#200](https://leetcode.com/problems/number-of-islands/) | O(R * C) | O(R * C) | | | Scan the grid; BFS visits all connected land from each new starting cell. Count one island per BFS. | Mark the starting cell and each discovered neighbor as `"0"` before enqueueing to avoid duplicate queue entries. |
| 9 | **Number of Provinces (DFS)** | [#547](https://leetcode.com/problems/number-of-provinces/) | O(n^2) | O(n) direct matrix; O(n^2) with adjacency list | | | Scan all cities; each unvisited city starts a province. DFS visits connected cities using matrix rows directly, or a separately built adjacency list. | This is a connectivity matrix, not a land/water grid: neighbors are city indices, not four directions. Use a visited array. Building the adjacency list adds O(n^2) worst-case space. |
| 10 | **Number of Provinces (BFS)** | [#547](https://leetcode.com/problems/number-of-provinces/) | O(n^2) | O(n) | | | Each unvisited city starts a province. Use a queue and scan each visited city's matrix row for connected, unvisited neighbors. | Mark cities visited before enqueueing. The queue's `while` loop processes neighbors; do not recursively call `bfs()` inside it. |

All complexities are worst case. `R` and `C` are the grid's row and column counts; grid DFS uses up to O(R * C) call-stack space and grid BFS uses up to O(R * C) queue space. For Number of Provinces, `n` is the number of cities; the visited array and stack or queue use O(n) auxiliary space, excluding any separately built adjacency list.

---

## Traversal Templates From These Five Problems

**Shared steps:** Check whether a cell/node can be visited, mark it visited, explore its neighbors, and update or return the required answer.

**Important:** Direct calls and direction loops are two ways to explore neighbors. Either can be used with return-value DFS, shared-variable DFS, or DFS that only modifies the grid.

### 1. Return-Value DFS (Tree-Like DFS)

Use when each recursive call contributes a value to its caller: island area or perimeter. These are grid graphs, not actual trees; visited marking prevents cycles.

Example template for island area, inside the outer method with `rows`, `cols`, and `grid` available:

```python
def dfs(row, col):
	if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
		return 0

	grid[row][col] = 0

	return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
```

The same aggregation using a direction loop:

```python
def dfs(row, col):
	if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
		return 0

	grid[row][col] = 0
	area = 1

	for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		area += dfs(row + dr, col + dc)

	return area
```

| Problem | Water / Outside Grid | Already Visited | Current Land Contribution | Combine |
|---------|----------------------|-----------------|---------------------------|---------|
| Max Area of Island | Return `0` | Return `0` (marked as water) | `1` | `1 +` four neighbor results |
| Island Perimeter | Return `1` for an exposed side | Return `0` (marked `-1`) | `0` | Sum four neighbor results |

For perimeter, check water/out-of-bounds first, then visited `-1`. Visited land is **not water** and contributes no exposed edge.

### 2. DFS That Modifies the Grid (No Returned Answer)

Use for Flood Fill and Number of Islands. The helper modifies the grid; the outer method returns the image or counts traversal starts.

Example template for Number of Islands:

```python
def dfs(row, col):
	if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
		return

	grid[row][col] = "0"

	for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		dfs(row + dr, col + dc)
```

This helper returns `None`. A positive-validity `if` with the work inside it is equally valid: invalid calls reach the function's end and implicitly return `None`.

For Flood Fill, accept only the saved original color and recolor to the new color. Return early from the outer method when both colors match, otherwise recoloring cannot mark visited cells.

### 3. Shared-Variable DFS (`nonlocal`)

Use when recursive calls update one counter instead of returning contributions. Our Island Perimeter example uses this approach:

```python
perimeter = 0

def dfs(row, col):
	nonlocal perimeter

	if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
		perimeter += 1
		return
	if grid[row][col] == -1:
		return

	grid[row][col] = -1

	for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		dfs(row + dr, col + dc)
```

Place `perimeter` and this helper inside the outer method. `nonlocal perimeter` lets `+=` update that enclosing variable; without it, Python treats the counter as local to `dfs` and raises `UnboundLocalError`.

### 4. BFS (Mark Visited Before Enqueueing)

Example template returning one island's area:

```python
from collections import deque

def bfs(sr, sc):
	grid[sr][sc] = 0
	qq = deque([(sr, sc)])
	area = 1

	while qq:
		row, col = qq.popleft()

		for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			nr = row + dr
			nc = col + dc

			if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
				grid[nr][nc] = 0
				area += 1
				qq.append((nr, nc))

	return area
```

**Special attention:** Mark the starting cell and each newly discovered neighbor visited before enqueueing. If marking waits until dequeueing, multiple neighbors can enqueue the same waiting cell. Do not recursively call `bfs()`; the `while` loop drains the queue.

Only the **visited mark** must happen before enqueueing. Other work can happen at discovery or during queue processing, as long as it is counted correctly:

- **Area:** Count each newly discovered land cell once, including the starting cell.
- **Flood Fill:** Recoloring is the visited mark; no area counter is needed.
- **Island count:** Count one traversal start, not every queued cell.
- **Perimeter:** While processing land, count each neighbor that is water or outside the grid. Skip visited land; do not count it as an exposed side.

### 5. Choosing Where to Start

| Problem | Traversal Starts | Answer |
|---------|------------------|--------|
| Flood Fill | Only `(sr, sc)` | Modified image |
| Island Perimeter | First land cell (single-island assumption) | Sum of exposed sides |
| Max Area of Island | Every still-unvisited land cell during the grid scan | Maximum area across traversals |
| Number of Islands | Every still-unvisited land cell during the grid scan | Number of traversal starts |
| Number of Provinces | Every unvisited city during the city scan | Number of traversal starts |

### 6. Provinces: Change How Neighbors Are Found

Keep the same DFS/BFS structure, but replace four grid directions with city neighbors:

```python
for neighbour in range(n):
	if isConnected[node][neighbour] == 1 and not visited[neighbour]:
		# DFS: call dfs(neighbour), which marks the city at entry.
		# BFS: mark visited[neighbour] = True, then enqueue it.
		pass
```

With an adjacency list, iterate over `adj[node]` instead. Use a separate `visited` array rather than recoloring the connectivity matrix. Direct-matrix traversal takes O(n^2) time and O(n) auxiliary space.

**Quick rule:** DFS marks at entry before exploring neighbors; BFS marks at discovery before enqueueing. Recursive grid DFS may hit Python's recursion-depth limit; iterative BFS avoids that limitation.

---

## BFS Focus: Shortest Distance in Unweighted Graphs

Everything above treats BFS as one traversal option alongside DFS. From here on, the focus narrows to what BFS is actually *for*: BFS is the right tool whenever every edge costs the same non-negative amount - most commonly "weight 1," i.e. an unweighted graph (or, in a grid, every move costs exactly one step). Because every step costs the same, exploring in strict increasing-distance order (ripples expanding one layer at a time, from a FIFO queue) guarantees the first time a node is reached is via the fewest possible steps. That is the one-sentence reason every "shortest path / shortest distance / fewest steps / minimum minutes" problem below reaches for BFS instead of DFS.

Where this stops applying:
- **Non-negative weights that are NOT all equal** -> Dijkstra's algorithm (a priority queue instead of a plain FIFO queue) replaces BFS.
- **Negative weights allowed** -> Bellman-Ford is required instead.
- BFS is the special case of both where every edge weight is identical - no priority queue needed, a plain queue already explores in the correct order for free.

The three problems below additionally introduce **multi-source BFS** (seed the queue with every starting point at once, not just one) and contrast two equivalent ways to track "how far has BFS gotten" - see *BFS Bookkeeping Styles*, immediately after this section.

### Problems

| # | Problem | LeetCode | Time | Space | Condition | Why | Approach | Special Attention |
|---|---------|----------|------|-------|-----------|-----|----------|-------------------|
| 1 | **Shortest Path in Binary Matrix (Tag Style)** | [#1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | O(n^2) | O(n^2) | Cell value `0`, in bounds (8-directional), not yet visited | Single target cell (bottom-right); every move costs 1, so BFS's first-reached = shortest | Push `(row, col, dist)` into the queue; when the target cell is popped, its `dist` is the answer directly. **More intuitive: Tag** - the answer is one specific cell's own value, no translation needed. | Separate `visited` set, marked at push time, not pop time; input grid left untouched; check all 8 directions, not 4. |
| 2 | **Shortest Path in Binary Matrix (Wave Style)** | [#1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | O(n^2) | O(n^2) | Same as above | Same reasoning, alternate bookkeeping | Process the queue one full wave (`for _ in range(len(queue))`) per step; `level` tracks distance externally, starting at 1. Must `return level + 1` for the target - the off-by-one translation tag-style avoids. | Marks visited by mutating the grid (`grid[r][c] = 1`); checks if a neighbor IS the target BEFORE enqueueing it. |
| 3 | **Rotting Oranges (Tag Style)** | [#994](https://leetcode.com/problems/rotting-oranges/) | O(R * C) | O(R * C) | Cell value `1` (fresh), 4-directionally adjacent to a `2` (rotten) | Multi-source BFS - every rotten orange starts at minute 0 simultaneously; answer = time of the LAST rot | Seed queue with `(r, c, 0)` per rotten orange; track the minute as nodes pop. The answer (last rot time) is a derived max/last-value insight, not the node's own obvious purpose. | FIFO pop order is non-decreasing (no edge skips a layer), so plain `minutes_elapsed = minute` already captures the max; `max()` is correct but redundant here. |
| 4 | **Rotting Oranges (Wave Style)** | [#994](https://leetcode.com/problems/rotting-oranges/) | O(R * C) | O(R * C) | Same as above | Minutes are a shared global clock ticking for the whole grid at once | Snapshot `len(q)` per wave; `time` increments once per full minute, shared by all oranges. **More intuitive: Wave** - "minutes elapsed" IS a global tick counter, matching this style exactly. | Grid mutation (`1 -> 2`) does double duty as visited-marker AND the actual rotting; stop early once `fresh == 0`. |
| 5 | **01 Matrix (Tag Style)** | [#542](https://leetcode.com/problems/01-matrix/) | O(R * C) | O(R * C) | Cell is non-zero, still marked `"#"` (unassigned) | Multi-source BFS - every `0` starts at distance 0 simultaneously; the output is a value per cell | `mat[nrr][ncc] = mat[r][c] + 1` - the parent's distance already sits in the grid, read it for free. **More intuitive: Tag** - the output format already IS "each cell knows its own value." | Grid doubles as both the output AND the visited marker (`"#"` = unassigned); no level loop needed at all. |
| 6 | **01 Matrix (Wave Style)** | [#542](https://leetcode.com/problems/01-matrix/) | O(R * C) | O(R * C) | Same as above | Confirms wave-style also works even though the matrix is mutated in place | External `level` counter (starting at 1) supplies the value written into each newly discovered cell instead of `mat[r][c] + 1`. Duplicates information the grid already provides for free. | Proves grid mutation does not block wave-style - mutation handles "visited," `level` independently handles "what number." |

All complexities are worst case. `R` and `C` are the grid's row and column counts. For Shortest Path in Binary Matrix the grid is `n x n`, so `n` here means the grid's side length (equivalent to `R = C = n`).

---

## BFS Bookkeeping Styles: Tag-Each-Node vs Batch-By-Wave

From three more BFS problems (`bfs/ShortestBinaryPath.py`, `bfs/Rotting_Oranges.py`, `bfs/01Matrix.py`): the generic BFS template above (section 4) marks visited before enqueueing, which every BFS below still does. What differs is HOW each one tracks "what distance/level am I on" while draining the queue. There are two equivalent styles, and each file implements both side by side (`SolutionTagEachNode` / `SolutionBatchByWave`), verified to agree on every test case.

### 7. Tag-Each-Node

Glue the distance directly onto each queue item - no separate level loop needed, since whoever pops an item already knows how far it is from the start.

```python
queue = deque([(start_row, start_col, 0)])
visited = {(start_row, start_col)}

while queue:
	row, col, dist = queue.popleft()

	if (row, col) == target:
		return dist

	for dr, dc in directions:
		nr, nc = row + dr, col + dc
		if in_bounds(nr, nc) and is_open(nr, nc) and (nr, nc) not in visited:
			visited.add((nr, nc))
			queue.append((nr, nc, dist + 1))
```

### 8. Batch-By-Wave

Snapshot the queue length before processing a layer, and track distance with one shared counter incremented once per full wave.

```python
queue = deque([(start_row, start_col)])
visited = {(start_row, start_col)}
level = 0

while queue:
	for _ in range(len(queue)):
		row, col = queue.popleft()

		for dr, dc in directions:
			nr, nc = row + dr, col + dc
			if in_bounds(nr, nc) and is_open(nr, nc) and (nr, nc) not in visited:
				visited.add((nr, nc))
				queue.append((nr, nc))

	level += 1
```

Both visit the same cells in the same order and always agree - the same algorithm wearing two outfits. Snapshotting `len(queue)` is safe because an edge can never skip a layer: everything currently in the queue belongs to the current wave, and anything discovered during this pass lands at the back, safely outside the frozen loop count.

### 9. Which Style Is More Intuitive - Decision Rule

| The answer you need | Natural style | Why |
|---|---|---|
| The distance of **one specific** target node | **Tag** | the target's own carried value *is* the answer - no translation needed |
| A distance value for **every** node (output is per-cell) | **Tag** | the output format already *is* "each node knows its own value" |
| **One global** number for the whole system (total time, round count) | **Wave** | that number is a shared clock ticking for everyone - exactly the wave counter's job |

**Applied to the three problems above:**

| Problem | What's actually being asked | More intuitive style | Why |
|---|---|---|---|
| Shortest Path in Binary Matrix | distance of **one** target cell (bottom-right) | **Tag** | `dist` on the popped target cell is the answer directly; wave needs a `level + 1` off-by-one translation |
| Rotting Oranges | **one global** elapsed-time number (when the LAST orange rots) | **Wave** | minutes are a shared clock; tag-style needs the extra derived insight that the last-popped minute is the answer |
| 01 Matrix | distance of **every** cell (output is a full grid of distances) | **Tag** | the parent's distance is already sitting in `mat[row][col]`, free - no external counter needed |

**Quick rule:** say the question out loud first. "Distance of this one thing" or "distance of every thing" -> reach for Tag. "One number for everything" -> reach for Wave.

---

# Dijkstra - Shortest Paths With Nonnegative Weights

> **Core idea:** Repeatedly finalize the currently cheapest known route. Use a min-heap when edges have nonnegative weights and the question asks for a minimum-cost or shortest-weighted path.

### When to Use Dijkstra

- The graph has weighted edges, and each edge weight is nonnegative.
- The goal is the minimum total cost/distance from one source to other nodes, or to one destination.
- A plain BFS is not enough because different moves can have different costs.

Do not use ordinary Dijkstra with negative edge weights. If all edge weights are equal, use BFS. For negative weights, consider Bellman-Ford; for a DAG with negative weights, topological-order relaxation is another option.

### Problems

| # | Problem | LeetCode | Time | Space | Approach | Special Attention |
|---|---------|----------|------|-------|----------|-------------------|
| 1 | **Dijkstra Algorithm** | — | O(V + (E + 1) log(E + 1)) | O(V + E) | Find shortest distances from one source to every reachable vertex. See [implementation](Dijkstra/Dijkstra_Algorithm.py). | Skip stale heap entries. Requires nonnegative weights. |
| 2 | **Network Delay Time** | [#743](https://leetcode.com/problems/network-delay-time/) | O(V + (E + 1) log(E + 1)) | O(V + E) | Run Dijkstra from `k`; if every node is reached, return the largest finalized distance. See [implementation](Dijkstra/networkDelayTime.py). | Heap can contain duplicate candidates, so its size can be O(E), not only O(V). |
| 3 | **Cheapest Flights Within K Stops** | [#787](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Depends on implementation | Depends on implementation | Add flights-used to the search state; at most `k + 1` flights are allowed. See [implementation](Dijkstra/Cheapest_FlightsWithinKStops.py). | One cheapest price per city is not enough. Track city and flights used. An unpruned heap of route prefixes may grow exponentially. |
| 4 | **Path With Minimum Effort** | [#1631](https://leetcode.com/problems/path-with-minimum-effort/) | O(R * C log(R * C)) | O(R * C) | Dijkstra on a grid; path cost is the maximum edge difference along the path. | Relax with `max(current_effort, edge_difference)`, not addition. |

Let `V` be vertices and `E` edges. For a lazy min-heap implementation, each edge is scanned once and can cause at most one successful push; there are at most `E + 1` pushes and pops. Heap size can therefore be O(E).

Time derivation:

```text
O(E)                              # build adjacency list
+ O(V) + O(E)                    # finalize vertices and scan edges
+ O(log(E + 1))                   # push the source
+ E * O(log(E + 1))               # up to E edge-candidate pushes
+ (E + 1) * O(log(E + 1))         # up to E + 1 pops
= O(V + 2E + (2E + 2) log(E + 1))
= O(V + (E + 1) log(E + 1))
```

For a simple graph, `E <= V^2`, so `log(E + 1) = O(log V)` and the bound is commonly written as O((V + E) log V). Keep the `O(V)` term explicit in the general bound: a graph may have many vertices but few edges. The adjacency list, distance array, and heap together use O(V + E) space.

### 1. Standard Dijkstra Template

Use a distance array and push a new heap entry whenever an edge relaxation improves a distance. Old entries remain in the heap; skip them when popped if they no longer match the best distance.

```python
import heapq

def dijkstra(graph, source):
	vertex_count = len(graph)
	distances = [float("inf")] * vertex_count
	distances[source] = 0
	min_heap = [(0, source)]

	while min_heap:
		distance, node = heapq.heappop(min_heap)

		if distance != distances[node]:
			continue

		for neighbor, weight in graph[node]:
			new_distance = distance + weight

			if new_distance < distances[neighbor]:
				distances[neighbor] = new_distance
				heapq.heappush(min_heap, (new_distance, neighbor))

	return distances
```

If only one destination is needed, it is safe to return when that destination is popped with its current best distance. For all-node results, finish processing the heap and return the distance array.

### Quick Selection

| Problem shape | Choose | Reason |
|---|---|---|
| Minimum number of equal-cost steps | BFS | FIFO order explores by step count. |
| Minimum total cost with nonnegative, differing weights | Dijkstra | Min-heap explores the lowest accumulated cost first. |
| Minimum cost with a stop/step/resource limit | Dijkstra-style search with that limit in the state, or a bounded-relaxation method | A node alone does not capture how much of the limit remains. |
| Negative edge weights | Not ordinary Dijkstra - use Bellman-Ford below | Dijkstra's "once popped, never reconsidered" assumption is unsound the moment a later edge can make the total cost go down instead of up. |

---

# Bellman-Ford - Shortest Paths With Negative Weights

> **Core idea:** Relax every edge, over and over, `V - 1` times. Where Dijkstra greedily commits to the cheapest known route and never revisits it, Bellman-Ford makes no such gamble - it simply gives every edge enough chances to improve every distance, which is slower but works even when some edges subtract instead of add.

### Why Dijkstra Cannot Be Patched For This

- Dijkstra assumes a popped vertex's distance is final - that only holds if edges can never make a path cheaper later.
- A negative edge breaks that assumption, so Bellman-Ford instead relaxes every edge `V - 1` times instead of trusting one pass.

### Constraints and When to Use It

- Works only on **directed graphs** - an undirected negative edge is automatically a negative cycle (walk it both ways, cost keeps dropping).
- Tolerates negative edge weights, but not a **negative-weight cycle** reachable from the source - shortest path is undefined if one exists.
- One extra relaxation round after the normal `V - 1` doubles as a negative-cycle detector for free.
- **O(V * E) time** - much slower than Dijkstra's O((V + E) log V); only use it when negative weights force your hand.

### 1. Standard Bellman-Ford Template

```python
def bellman_ford(vertex_count, edges, source):
	distances = [float("inf")] * vertex_count
	distances[source] = 0

	# Relax every edge, V - 1 times. The shortest path between any two
	# vertices uses at most V - 1 edges (assuming no negative cycle), so
	# this many rounds is always enough for every distance to settle.
	for _ in range(vertex_count - 1):
		for u, v, weight in edges:
			if distances[u] != float("inf") and distances[u] + weight < distances[v]:
				distances[v] = distances[u] + weight

	# One more round: if anything STILL improves, a negative cycle exists.
	for u, v, weight in edges:
		if distances[u] != float("inf") and distances[u] + weight < distances[v]:
			raise ValueError("Graph contains a negative-weight cycle")

	return distances
```

### Problems

| # | Problem | Platform | Time | Space | Approach | Special Attention |
|---|---------|----------|------|-------|----------|-------------------|
| 1 | **Bellman-Ford Shortest Path** | [GeeksforGeeks](https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1) | O(V * E) | O(V) | Relax every edge `V - 1` times from a single source. | Run one extra round to detect a negative cycle; do not trust the result if one exists. |
| 2 | **Cheapest Flights Within K Stops** | [LeetCode #787](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | O(k * E) | O(n) | Bound the round count at `k + 1` instead of `V - 1`; snapshot distances before each round. | One round = one more stop allowed. Contrast with this repo's unpruned-heap Dijkstra variant above, which can blow up exponentially on the same problem. |

---

# Floyd-Warshall - Shortest Paths Between Every Pair

> **Core idea:** Dynamic programming over "which vertices am I allowed to pass through so far." Progressively allow vertex `0`, then `0` and `1`, then `0`, `1`, and `2`, and so on as an intermediate stop; after allowing all `V` vertices, every pair's shortest path has been found.

### Why This Is a Different Question Than Dijkstra or Bellman-Ford

- Dijkstra and Bellman-Ford both answer "shortest path from ONE source" - Floyd-Warshall answers "shortest path between EVERY pair at once."
- Running Dijkstra/Bellman-Ford from every vertex gets the same answer, but Floyd-Warshall's flat **O(V^3)** (independent of `E`) wins on dense graphs and is simpler to implement.

### Constraints and When to Use It

- Use it only when the problem needs **all-pairs** shortest paths, not just a single source.
- Tolerates negative edge weights, not a negative-weight cycle; a negative `dist[i][i]` after running means a cycle passes through vertex `i`.
- With negative weights, this only works on **directed graphs** - same reason as Bellman-Ford: an undirected negative edge is automatically a negative cycle (walk it both ways, cost keeps dropping).
- **O(V^3) time, O(V^2) space** - only scales to small/medium graphs; beyond that, run Dijkstra per source instead.

### 1. Standard Floyd-Warshall Template

```python
def floyd_warshall(distance_matrix):
	# distance_matrix[i][j] is the direct edge weight from i to j, or
	# infinity if no direct edge exists; distance_matrix[i][i] is 0.
	vertex_count = len(distance_matrix)
	dist = [row[:] for row in distance_matrix]   # copy - do not mutate the input

	# k is the "newly allowed" intermediate vertex for this round.
	for k in range(vertex_count):
		for i in range(vertex_count):
			for j in range(vertex_count):
				if dist[i][k] + dist[k][j] < dist[i][j]:
					dist[i][j] = dist[i][k] + dist[k][j]

	return dist
```

**The loop order `k, i, j` is not arbitrary - `k` must be the outermost loop.** `k` represents "every intermediate vertex allowed so far"; by the time the `i, j` loops run for a given `k`, every path using only vertices `0..k` as intermediates must already be fully settled, or the DP's correctness breaks. Swapping `k` to an inner loop silently produces wrong answers for some graphs, since it would mix "allowed through vertex k" paths with paths that have not actually earned that status yet.

### Problems

| # | Problem | Platform | Time | Space | Approach | Special Attention |
|---|---------|----------|------|-------|----------|-------------------|
| 1 | **Floyd-Warshall All-Pairs Shortest Path** | [GeeksforGeeks](https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1) | O(V^3) | O(V^2) | Progressively allow each vertex as an intermediate stop; `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`. | Loop order must be `k, i, j`. A negative `dist[i][i]` after running means a negative cycle exists. |
| 2 | **Find the City With the Smallest Number of Neighbors at a Threshold Distance** | [LeetCode #1334](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | O(V^3) | O(V^2) | Run Floyd-Warshall once to get every pairwise distance, then count each city's reachable neighbors within the threshold. | A classic "all-pairs is the actual requirement" signal - counting per-city reachable neighbors needs every pair's distance, not just one source's. |

---

# Topological Sort - Ordering Dependencies

> **Core idea:** A topological order is a linear ordering of a directed acyclic graph (DAG) where every directed edge `u -> v` places `u` before `v`. It orders tasks so that each prerequisite comes before the work that depends on it.

> **Constraint:** The graph must be directed and acyclic. If it contains a directed cycle, no topological ordering exists.

### When to Use Topological Sort

- The graph is **directed** and the problem asks for a valid order that respects dependencies.
- Common examples include course prerequisites, build steps, task scheduling, and dependency resolution.
- A valid ordering exists only when the graph has no directed cycle. If a cycle exists, some dependencies require each other and no topological ordering is possible.
- A DAG can have more than one valid topological order; any order that respects every edge is correct.

### Problems

| # | Problem | Platform | Time | Space | Approach | Special Attention |
|---|---------|----------|------|-------|----------|-------------------|
| 1 | **Topological Sort (Kahn's Algorithm)** | [GeeksforGeeks](https://www.geeksforgeeks.org/problems/topological-sort/1) | O(V + E) | O(V) auxiliary | Add every vertex with in-degree zero to a queue. Repeatedly take a ready vertex, append it to the order, and reduce the in-degree of its outgoing neighbors. See [implementation](topological_Sort/topoSort_Khan_algo.py). | If fewer than `V` vertices are processed, the graph contains a cycle. |
| 2 | **Course Schedule** | [LeetCode #207](https://leetcode.com/problems/course-schedule/) | O(V + E) | O(V + E) | Build edges from each prerequisite to its dependent course, then return whether Kahn's algorithm processes all courses. See [implementation](topological_Sort/Course_Schedule_using_khan_Algo.py). | For a pair `[course, prerequisite]`, add `prerequisite -> course`. |
| 3 | **Course Schedule II** | [LeetCode #210](https://leetcode.com/problems/course-schedule-ii/) | O(V + E) | O(V + E) | Use the same graph and queue; return the processed order if all courses are included, otherwise return an empty list. See [implementation](topological_Sort/Course%20ScheduleII.py). | Any valid order is accepted; return `[]` when a cycle prevents completing all courses. |

Let `V` be the number of vertices and `E` the number of directed edges. Building or scanning the adjacency list and in-degree counts takes O(V + E) time. The in-degree array, queue, and output order take O(V) auxiliary space; when the adjacency list is built from input pairs, it adds O(V + E) space.

### Kahn's Algorithm Template

Use an adjacency list where `graph[u]` contains every vertex reached by an outgoing edge `u -> v`. For prerequisite problems, point each edge from the prerequisite to the dependent task.

```python
from collections import deque

def topological_sort(graph):
	vertex_count = len(graph)
	in_degree = [0] * vertex_count

	for neighbors in graph:
		for neighbor in neighbors:
			in_degree[neighbor] += 1

	queue = deque()
	for node in range(vertex_count):
		if in_degree[node] == 0:
			queue.append(node)
	order = []

	while queue:
		node = queue.popleft()
		order.append(node)

		for neighbor in graph[node]:
			in_degree[neighbor] -= 1
			if in_degree[neighbor] == 0:
				queue.append(neighbor)

	return order if len(order) == vertex_count else []
```

The queue contains vertices whose prerequisites have all been processed. A neighbor becomes ready exactly when its in-degree reaches zero. The final length check detects a cycle: vertices in or blocked behind a cycle never reach in-degree zero. For Course Schedule, use the same process but return `len(order) == numCourses` instead of the order itself.

---

# Disjoint Set Union (DSU) - Track Connected Groups

> **Core idea:** DSU, also called Union-Find, maintains a collection of disjoint groups. `find(x)` returns the representative of the group containing `x`; `union(x, y)` merges the groups if they are different.

> **Constraint:** DSU tracks whether nodes belong to the same connected component; it does not store paths or preserve edge direction. It is most directly applicable to undirected connectivity and to edges processed as undirected connections. It does not answer shortest-path or directed-reachability questions.

### When to Use DSU

- Edges or connections are added over time, and you need to efficiently check whether two nodes are already connected.
- You need to count connected components while processing edges.
- You need to detect whether an undirected edge joins nodes that are already connected; that edge closes a cycle.
- You need to check whether an undirected graph is a tree: it must have `n - 1` edges and no cycle.

Use path compression in `find` and union by rank or size to keep the sets shallow. With both optimizations, operations take O(α(V)) amortized time, where α is the inverse Ackermann function and grows so slowly that it is at most a small constant for practical input sizes.

### Problems

| # | Problem | Platform | Time | Space | Approach | Special Attention |
|---|---------|----------|------|-------|----------|-------------------|
| 1 | **Redundant Connection** | [LeetCode #684](https://leetcode.com/problems/redundant-connection/) | O(E * α(V)) | O(V) | Process edges in order. If an edge's endpoints already have the same root, return that edge; otherwise union their sets. See [implementation](disjoint_set/1_Redundant_Connection.py). | Node labels are `1` through `n`, so the arrays have length `n + 1`; index `0` is unused. |
| 2 | **Graph Valid Tree** | [LeetCode #261](https://leetcode.com/problems/graph-valid-tree/) | O(E * α(V)) | O(V) | Reject unless there are `n - 1` edges, then reject if any edge joins nodes already in the same set. See [implementation](disjoint_set/2_Graph_ValidTree.py). | With exactly `n - 1` edges, no cycle implies the graph is connected. |
| 3 | **Number of Connected Components in an Undirected Graph** | [LeetCode #323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | O(V + E * α(V)) | O(V) | Start with `V` components and decrement the count whenever an edge successfully merges two sets. See [implementation](disjoint_set/3_Number%20of%20Connected_Components_UndirectedGraph.py). | The graph is undirected; repeated connections inside one component do not reduce the count. |

Here `V` is the number of vertices and `E` the number of edges. Initializing the parent and rank arrays costs O(V); processing all edges costs O(E * α(V)) amortized.

### Path Compression and Union by Rank Template

This template assumes vertices are numbered from `0` to `n - 1`. For 1-indexed labels, allocate arrays of length `n + 1` and leave index `0` unused.

```python
parent = list(range(n))
rank = [0] * n

def find(node):
	if parent[node] != node:
		parent[node] = find(parent[node])
	return parent[node]

def union(node_a, node_b):
	root_a = find(node_a)
	root_b = find(node_b)

	if root_a == root_b:
		return False

	if rank[root_a] < rank[root_b]:
		parent[root_a] = root_b
	elif rank[root_a] > rank[root_b]:
		parent[root_b] = root_a
	else:
		parent[root_b] = root_a
		rank[root_a] += 1

	return True
```

`union` returns `True` only when it merges two previously separate groups. A `False` result means the endpoints were already connected; use that to detect a redundant edge or avoid decrementing a component count. Rank increases only when equal-rank trees are merged. With union by size instead, attach the smaller root under the larger one and add the smaller component's size to the larger root after every successful merge.

---

# Minimum Spanning Tree (MST) - Connect Every Vertex at Minimum Cost

> **Spanning tree:** For a connected, undirected graph, a spanning tree is a subset of its edges that connects every vertex without a cycle. A spanning tree with `V` vertices always has exactly `V - 1` edges.

> **Minimum spanning tree:** In a connected, weighted, undirected graph, an MST is a spanning tree with the minimum possible sum of edge weights. If edge weights tie, there can be multiple MSTs with the same minimum total cost.

> **Constraint:** Kruskal's and Prim's algorithms apply to weighted, undirected graphs. A connected graph has an MST; a disconnected graph has no spanning tree, though these algorithms can produce a minimum spanning forest.

### When to Use MST Algorithms

- The goal is to connect all vertices while minimizing the total cost, such as connecting locations, computers, or network components.
- Use **Kruskal's** when considering edges globally from cheapest to most expensive is convenient; DSU efficiently rejects edges that would create a cycle.
- Use **Prim's** when growing one connected tree from a starting vertex is convenient; a min-heap selects the cheapest edge that adds a new vertex.
- An MST minimizes the total cost of connecting the graph; it does not necessarily give the shortest path between every pair of vertices.

### Problems

| # | Problem | Platform | Time | Space | Approach | Special Attention |
|---|---------|----------|------|-------|----------|-------------------|
| 1 | **Min Cost to Connect All Points (Kruskal)** | [LeetCode #1584](https://leetcode.com/problems/min-cost-to-connect-all-points/) | O(E log E), O(V^2 log V) for this complete graph | O(E + V), O(V^2) for this complete graph | Build every pairwise edge weighted by Manhattan distance, sort edges, and use DSU to accept only edges joining different components. See [implementation](Minimum_Spanning_Tree/Min_Costto_ConnectAllPoints_Kruskal_Algo.py). | Stop after accepting `V - 1` edges. |
| 2 | **Min Cost to Connect All Points (Prim)** | [LeetCode #1584](https://leetcode.com/problems/min-cost-to-connect-all-points/) | O(E log V), O(V^2 log V) for this complete graph | O(E + V), O(V^2) for this complete graph | Build the weighted adjacency list and grow the MST from vertex `0`, using a min-heap to choose the next cheapest edge. See [implementation](Minimum_Spanning_Tree/Min_Costto_ConnectAllPoints_Prims_Algo.py). | Skip heap entries for vertices already added to the MST. |

Here `V` is the number of vertices and `E` the number of edges. For this problem, every pair of points is connected, so `E = V(V - 1) / 2 = O(V^2)`. Both listed implementations explicitly build this complete graph.

### Kruskal's Algorithm Template

Sort all edges by weight and add an edge only when its endpoints belong to different DSU components. This prevents cycles; stop once `V - 1` edges have been accepted.

```python
edges.sort()
parent = list(range(vertex_count))
rank = [0] * vertex_count

def find(node):
	if parent[node] != node:
		parent[node] = find(parent[node])
	return parent[node]

def union(node_a, node_b):
	root_a = find(node_a)
	root_b = find(node_b)
	if root_a == root_b:
		return False
	if rank[root_a] < rank[root_b]:
		parent[root_a] = root_b
	elif rank[root_a] > rank[root_b]:
		parent[root_b] = root_a
	else:
		parent[root_b] = root_a
		rank[root_a] += 1
	return True

total_cost = 0
edges_used = 0
for weight, node_a, node_b in edges:
	if union(node_a, node_b):
		total_cost += weight
		edges_used += 1
		if edges_used == vertex_count - 1:
			break
```

### Prim's Algorithm Template

Start from any vertex. The heap may contain multiple candidate edges to the same vertex, so skip an entry when its vertex is already in the MST.

```python
import heapq

min_heap = [(0, start)]
in_mst = [False] * vertex_count
total_cost = 0
vertices_added = 0

while min_heap and vertices_added < vertex_count:
	weight, node = heapq.heappop(min_heap)
	if in_mst[node]:
		continue

	in_mst[node] = True
	vertices_added += 1
	total_cost += weight

	for neighbor, edge_weight in graph[node]:
		if not in_mst[neighbor]:
			heapq.heappush(min_heap, (edge_weight, neighbor))
```

For a connected graph, Prim adds all `V` vertices and returns the MST cost. If fewer than `V` vertices are reached, the graph is disconnected; to build a minimum spanning forest, restart Prim from each unvisited vertex.