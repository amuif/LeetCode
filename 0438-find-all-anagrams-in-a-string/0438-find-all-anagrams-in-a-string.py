
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Length of the string 's' and the pattern 'p'
        s_length, p_length = len(s), len(p)
        # List to store the starting indices of the anagrams of 'p' in 's'
        anagram_indices = []
      
        # Early return if 's' is shorter than 'p', as no anagrams would fit
        if s_length < p_length:
            return anagram_indices
      
        # Count the occurrences of characters in 'p'
        p_char_count = Counter(p)
        # Count the occurrences of characters in the first window of 's'
        # This window has the size one less than the size of 'p'
        s_window_count = Counter(s[:p_length - 1])
      
        # Iterate over 's', starting from index where first full window can begin
        for i in range(p_length - 1, s_length):
            # Add the current character to the window's character count
            s_window_count[s[i]] += 1
          
            # If the character counts match, it's an anagram; record the start index
            if p_char_count == s_window_count:
                anagram_indices.append(i - p_length + 1)

            # Move the window to the right: subtract the count of the oldest character
            s_window_count[s[i - p_length + 1]] -= 1
            # Remove the character count from the dict if it drops to zero
            if s_window_count[s[i - p_length + 1]] == 0:
                del s_window_count[s[i - p_length + 1]]
      
        # Return the list of starting indices of anagrams
        return anagram_indices