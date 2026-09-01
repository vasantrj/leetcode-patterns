"""
Problem: Smallest Divisible Digit Product II
LeetCode ID: 3348
Pattern: Dynamic Programming / Greedy / Mathematics
Difficulty: Hard

Time Complexity: O(S + n × 9 + L × 9)

where:
    S = number of DP states based on prime exponents
    n = length of the input string
    L = length of the constructed answer

Space Complexity: O(S)

Approach:
1. Factorize t into the prime factors {2, 3, 5, 7}.
2. If any other prime factor exists, return "-1".
3. Build a DP over exponent states:
      - Each state stores the minimum number of digits
        required to satisfy the remaining prime factors.
4. Traverse the number from right to left, trying to
   increase one digit while keeping the prefix unchanged.
5. Greedily construct the smallest valid suffix using
   the DP information.
6. If no solution of the same length exists, construct
   the smallest valid number with one extra digit.
"""

import math
from typing import List

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        T = t
        A = B = C = D = 0
        for p in (2, 3, 5, 7):
            while T % p == 0:
                T //= p
                if p == 2: A += 1
                elif p == 3: B += 1
                elif p == 5: C += 1
                else: D += 1
        if T != 1:
            return "-1"

        contrib = {
            1: (0,0,0,0), 2: (1,0,0,0), 3: (0,1,0,0), 4: (2,0,0,0),
            5: (0,0,1,0), 6: (1,1,0,0), 7: (0,0,0,1), 8: (3,0,0,0), 9: (0,2,0,0),
        }

        Ad, Bd, Cd, Dd = A+1, B+1, C+1, D+1

        def idx(a,b,c,d):
            return ((a*Bd+b)*Cd+c)*Dd+d

        size = Ad*Bd*Cd*Dd
        INF = float('inf')
        dist = [0]*size
        for a in range(Ad):
            for b in range(Bd):
                for c in range(Cd):
                    for d in range(Dd):
                        if a==0 and b==0 and c==0 and d==0:
                            dist[idx(0,0,0,0)] = 0
                            continue
                        best = INF
                        for dg in range(1,10):
                            ca,cb,cc,cd = contrib[dg]
                            na = a-ca if a-ca>0 else 0
                            nb = b-cb if b-cb>0 else 0
                            nc = c-cc if c-cc>0 else 0
                            nd = d-cd if d-cd>0 else 0
                            if na==a and nb==b and nc==c and nd==d:
                                continue
                            v = dist[idx(na,nb,nc,nd)] + 1
                            if v < best:
                                best = v
                        dist[idx(a,b,c,d)] = best

        def apply_state(state, dg):
            a,b,c,d = state
            ca,cb,cc,cd = contrib[dg]
            na = a-ca if a-ca>0 else 0
            nb = b-cb if b-cb>0 else 0
            nc = c-cc if c-cc>0 else 0
            nd = d-cd if d-cd>0 else 0
            return (na,nb,nc,nd)

        def get_dist(state):
            return dist[idx(*state)]

        n = len(num)
        full_state = (A,B,C,D)

        if '0' not in num:
            st = full_state
            for ch in num:
                st = apply_state(st, int(ch))
            if st == (0,0,0,0):
                return num

        z = n
        for i, ch in enumerate(num):
            if ch == '0':
                z = i
                break

        limit = z if z < n else n-1
        build_upto = z if z < n else n  # exclusive bound for source digits
        prefix_state = [None]*(limit+2)
        prefix_state[0] = full_state
        for i in range(0, min(limit+1, build_upto)):
            prefix_state[i+1] = apply_state(prefix_state[i], int(num[i]))

        def greedy_fill(state, length):
            res = []
            cur = state
            for pos in range(length):
                remaining_after = length-pos-1
                for dg in range(1,10):
                    ns = apply_state(cur, dg)
                    if get_dist(ns) <= remaining_after:
                        res.append(str(dg))
                        cur = ns
                        break
            return ''.join(res)

        ans = None
        for i in range(limit, -1, -1):
            ps = prefix_state[i]
            start_d = int(num[i]) + 1
            remaining = n-1-i
            found_d = None
            new_state = None
            for dg in range(start_d, 10):
                ns = apply_state(ps, dg)
                if get_dist(ns) <= remaining:
                    found_d = dg
                    new_state = ns
                    break
            if found_d is not None:
                suffix = greedy_fill(new_state, remaining)
                ans = num[:i] + str(found_d) + suffix
                break

        if ans is not None:
            return ans

        L = n+1
        needed = get_dist(full_state)
        if needed > L:
            L = needed
        return greedy_fill(full_state, L)

