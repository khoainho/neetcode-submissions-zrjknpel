class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Build all characters that appear
        adj: Dict[str, Set[str]] = {c: set() for w in words for c in w}

        # Build edges: a -> b means a must come before b
        for w1, w2 in zip(words, words[1:]):
            min_len = min(len(w1), len(w2))
            i = 0
            while i < min_len and w1[i] == w2[i]:
                i += 1
            if i < min_len:
                adj[w1[i]].add(w2[i])
            else:
                # If w1 is longer than w2 and w2 is a prefix of w1, invalid
                if len(w1) > len(w2):
                    return ""

        # DFS with cycle detection
        state: Dict[str, int] = {c: 0 for c in adj}  # 0=unvisited, 1=visiting, 2=done
        order: List[str] = []
        has_cycle = False

        def dfs(u: str) -> bool:
            nonlocal has_cycle
            if state[u] == 1:
                # found a cycle
                return False
            if state[u] == 2:
                return True

            state[u] = 1
            for v in adj[u]:
                if not dfs(v):
                    return False
            state[u] = 2
            order.append(u)
            return True

        for c in adj:
            if state[c] == 0:
                if not dfs(c):
                    return ""

        order.reverse()
        return "".join(order)