# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

"""
S = BANANA
ans = Stuart 12
"""
# Attempt 1: fun --> minion_game2  test: 6/14  Status: (TLE) 

def count_substring(sub_string, string):
    ct = 0
    n = len(string) 
    ss = len(sub_string)-1
    for i in range(n-ss):
        sub = string[i:i+ss+1]
        # print(sub)
        if sub == sub_string:
            ct += 1
    # print()
    # print(sub_string, "in", string, "Occurs....", ct)
    return ct

hm = {}
def all_subs(strs):
    ans = 0
    global hm
    n = len(strs)
    for i in range(n):
        sub = strs[:i+1]
        if sub not in hm.keys():
            hm[sub] = 1
            ans += count_substring(sub, strs)
    # print("MAP_____", hm) 
    # print("All subs ans -----", ans) 
    return ans
    
def minion_game2(string):
    # your code goes here
    vowel = ["A", "E", "I", "O", "U"]
    st_score, kv_score = 0, 0
    for i, ch in enumerate(string):
        if ch in vowel:
            kv_score += all_subs(string[i:])
        else:
            st_score += all_subs(string[i:])
            
    if st_score > kv_score:
        print("Stuart", st_score)
    elif kv_score > st_score:
        print("Kevin", kv_score)
    else:
        print("Draw")
            

# Attempt 2: fun --> minion_game() test: 14/14   Status: Success

       
def minion_game(strs):
    st_score, kv_score = 0, 0
    n = len(strs)
    for i, ch in enumerate(strs):
        if ch in "AEIOU":
            kv_score += n - i
        else:
            st_score += n - i
            
    if st_score > kv_score:
        print("Stuart", st_score)
    elif kv_score > st_score:
        print("Kevin", kv_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)