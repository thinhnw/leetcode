class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(1, numRows):
            prevRow = output[-1]
            output.append([1])            
            for j in range(1, len(prevRow)):
                output[-1].append(prevRow[j] + prevRow[j-1])
            output[-1].append(1)
            
        return output
