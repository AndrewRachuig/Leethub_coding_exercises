class Solution:
	def myAtoi(self, s: str) -> int:


		s=s.strip()

		asn = re.findall('(^[\+\-0-9][0-9]*)', s)
		try:
			result = int(''.join(asn))
			MAX_INT = 2147483647
			MIN_INT = -2147483648
			if result > MAX_INT > 0:
				return MAX_INT
			elif result < MIN_INT < 0:
				return MIN_INT
			else:
				return result
		except ValueError:
			return 0      