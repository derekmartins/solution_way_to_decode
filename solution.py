class Solution:
	# @param A : string
	# @return an integer
    def numDecodings(self, A):
        
        if(A[0] == "0"):
            return 0
        
        t = [1, 1]
    
        for x in range(1, len(A)):
            
            if A[x] == "0":
                if A[x-1] in "12":
                   t.pop()
                  
                else:
                    return 0
           
            
            elif int(A[x-1] + A[x]) in range(1, 27) and A[x-1] != "0" or A [x] == 0:
                t.append((t[-1] + t[-2]) % (10 ** 9 + 7))
                
                
            else:
                t.append(t[-1])
                
        return t[-1]
