class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """                
        n = range(len(gain))
        gain.append(0)
        for i in n:
            gain[i] = gain[i] + gain[i-1]

        return max(gain)