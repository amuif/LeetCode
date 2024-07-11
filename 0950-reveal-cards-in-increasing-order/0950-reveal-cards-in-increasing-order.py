class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort the deck
        deck.sort()
        
        # Initialize a deque to store the indices
        indices = deque(range(len(deck)))
        
        # Initialize the result array
        result = [0] * len(deck)
        
        # Iterate over sorted deck and populate result array
        for card in deck:
            # Take the index of the next unrevealed card
            idx = indices.popleft()
            # Assign the revealed card to the correct position
            result[idx] = card
            
            # If there are still unrevealed cards, move the next unrevealed card to the end
            if indices:
                indices.append(indices.popleft())
        
        return result