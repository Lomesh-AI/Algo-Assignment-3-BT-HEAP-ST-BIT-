from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        dq = deque()

        for i in range(len(deck) - 1, -1, -1):
            if dq:
                x = dq.pop()
                dq.appendleft(x)
            dq.appendleft(deck[i])
        return list(dq)        
                