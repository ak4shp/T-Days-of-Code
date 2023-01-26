# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

"""
s = 'AABCAAADA'
k = 3

output = AB
         CA
         AD
"""

def merge_the_tools(strs, K):
    # your code goes here
    n = len(strs)
    for i in range(0, n, K):
        sub = strs[i:i+K]
        unique = []
        for ch in sub:
            if ch not in unique:
                unique.append(ch)
        
        ans = "".join(unique)
        print(ans)
        
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)