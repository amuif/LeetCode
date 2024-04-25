from string import ascii_lowercase

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # The length of the input string
        string_length = len(s)

        # Initialize the dp array where dp[i] represents the length of the longest ideal substring ending at index i
        dp = [1] * string_length
      
        # Dictionary to keep track of the last index of each character we have encountered so far.
        last_index_dict = {s[0]: 0}

        # Iterate through the string starting from the first character
        for i in range(1, string_length):
            # Get the ascii value of the current character
            current_char_ascii = ord(s[i])

            # Loop through all lowercase letters to find characters within the ideal distance from the current character
            for b in ascii_lowercase:
                if abs(current_char_ascii - ord(b)) > k:
                    # If the ascii difference is greater than k, skip this character
                    continue
                # If the character is within the ideal distance and we've seen this character before
                if b in last_index_dict:
                    # Update the dp value by considering the length of the ideal substring ending at the last index of character b plus the current character
                    dp[i] = max(dp[i], dp[last_index_dict[b]] + 1)

            # Update the last index for the current character
            last_index_dict[s[i]] = i

        # Return the maximum value in the dp array which represents the length of the longest ideal substring
        return max(dp)