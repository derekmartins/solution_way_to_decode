class Solution:
	# @param A : string
	# @return an integer
    def numDecodings(self, A):

        if A[0] == 0:
            return 0

        t = [1]

        for x in range(1, len(A)):

            if (int(A[x-1]) in [1,2]) and (int(A[x-1] + A[x]) % 10 == 0):
                return 0
                
            if int(A[x-1] + A[x]) in range(0, 27):
                t.append((t[-1] + 2) % (10 ** 9 + 7))
            else:
                t.append(t[-1]) 
                
        return t[-1]
