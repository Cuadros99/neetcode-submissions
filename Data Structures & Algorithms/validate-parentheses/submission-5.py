class Solution:
    def isValid(self, s: str) -> bool:
        open_brk = []
        bracket_map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for c in s:
            if c in bracket_map:
                open_brk.append(c)
            else:
                if len(open_brk) == 0:
                    return False
                elif bracket_map[open_brk.pop()] != c:
                    return False
                
        return len(open_brk) == 0