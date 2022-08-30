class Solution:
    def romanToInt(self, s: str) -> int:
        number_vals = { "I" : 1,
                        "V" : 5,
                        "X" : 10,
                        "L" : 50,
                        "C" : 100,
                        "D" : 500,
                        "M" : 1000}
        total = 0
        for i in range(len(s)):
            amount =number_vals[s[i]]
            if i+1 < len(s) and amount < number_vals[s[i+1]]:
                total -= amount
            else:
                total += amount
        return total