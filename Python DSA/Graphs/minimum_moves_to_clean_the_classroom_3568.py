"""
Problem: Minimum Moves to Clean the Classroom
LeetCode ID: 3568
Pattern: Graph / BFS / Bitmask / State Tracking
Difficulty: Medium

Time Complexity: O(R * C * E * 2^L)
Space Complexity: O(R * C * E * 2^L)

where:
    R = number of rows
    C = number of columns
    E = maximum energy
    L = number of litter cells

Approach:
1. Find the starting position and assign an index to every litter cell.
2. Represent collected litter using a bitmask.
3. Use BFS because every movement has the same cost.
4. A BFS state contains:
      (row, column, remaining_energy, litter_mask)
5. Moving to an adjacent cell consumes one unit of energy.
6. Stepping on a litter cell sets its corresponding bit.
7. Stepping on a recharge cell restores energy to its maximum.
8. Return the number of moves when all litter has been collected.
"""

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows, cols = len(classroom), len(classroom[0])
        grid = classroom
        start = None
        litter_index = {}
        for i in range(rows):
            for j in range(cols):
                ch = grid[i][j]
                if ch == 'S':
                    start = (i, j)
                elif ch == 'L':
                    litter_index[(i, j)] = len(litter_index)

        full_mask = (1 << len(litter_index)) - 1
        max_energy = energy
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        sr, sc = start
        if full_mask == 0:
            return 0

        start_state = (sr, sc, energy, 0)
        visited = {start_state}
        q = deque([(sr, sc, energy, 0, 0)]) 

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == full_mask:
                return moves
            if e == 0:
                continue 
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'X':
                    ne = e - 1
                    nmask = mask
                    cell = grid[nr][nc]

                    if cell == 'R':
                        ne = max_energy
                    elif (nr, nc) in litter_index:
                        idx = litter_index[(nr, nc)]
                        nmask = mask | (1 << idx)

                    state = (nr, nc, ne, nmask)
                    if state not in visited:
                        visited.add(state)
                        q.append((nr, nc, ne, nmask, moves + 1))

        return -1