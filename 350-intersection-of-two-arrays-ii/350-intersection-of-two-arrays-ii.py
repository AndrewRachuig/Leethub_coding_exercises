class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = set(nums1).intersection(nums2)
        nums1 = [i for i in nums1 if i in intersect]
        nums2 = [i for i in nums2 if i in intersect]

        totals1 = {}
        for i in nums1:
            totals1[i] = 0
        for i in nums1:
            totals1[i] += 1

        totals2 = {}
        for i in nums2:
            totals2[i] = 0
        for i in nums2:
            totals2[i] += 1

        finals = {}
        for i in totals1:
            if totals1[i] < totals2[i]:
                finals[i] = totals1[i]
            else:
                finals[i] = totals2[i]

        finallist = []
        for i in finals:
            for j in range(finals[i]):
                finallist.append(i)
        return finallist