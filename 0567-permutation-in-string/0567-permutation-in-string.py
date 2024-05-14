from collections import Counter
class Solution:
    def checkInclusion(self, pattern: str, text: str) -> bool:
        pattern_length, text_length = len(pattern), len(text)
      
        if pattern_length > text_length:
            return False
      
        char_counter = Counter()
      
        for pattern_char, text_char in zip(pattern, text[:pattern_length]):
            char_counter[pattern_char] -= 1
            char_counter[text_char] += 1
      
        diff_count = sum(x != 0 for x in char_counter.values())
      
        if diff_count == 0:
            return True
      
        for i in range(pattern_length, text_length):
            char_out = text[i - pattern_length]
            char_in = text[i]
          
            if char_counter[char_in] == 0:
                diff_count += 1
            char_counter[char_in] += 1
            if char_counter[char_in] == 0:
                diff_count -= 1
          
            if char_counter[char_out] == 0:
                diff_count += 1
            char_counter[char_out] -= 1
            if char_counter[char_out] == 0:
                diff_count -= 1
          
            if diff_count == 0:
                return True
      
        return False