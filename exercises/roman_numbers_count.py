# calculate Roman numerals
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summ = 0
        n = len(s)
        i = 0
        while i < n:
            if i < n - 1 and d[s[i]] < d[s[i+1]]:
                summ += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                summ += d[s[i]]
                i += 1
        return summ

# Create an instance of the Solution class
solution_instance = Solution()

# Call the romanToInt method with a Roman numeral string
roman_numeral = "IX"  # Example Roman numeral
integer_value = solution_instance.romanToInt(roman_numeral)

# Print the result
print(f"The integer value of the Roman numeral {roman_numeral} is {integer_value}")
