class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        i = n - 1
        
        # Skip any trailing spaces at the end of the string
        while s[i] == ' ':
            i -= 1
        
        letter_count = 0
        
        # Count the length of the last word
        for i in range(i+1):
            if s[i] != ' ':
                letter_count += 1
            else:
                letter_count = 0
        
        return letter_count

# Create an instance of the Solution class
sol = Solution()

# Define the sentence you want to check
sentence = "Hello World"

# Call the lengthOfLastWord method
length = sol.lengthOfLastWord(sentence)

# Print the result
print(f"The length of the last word is: {length}")
