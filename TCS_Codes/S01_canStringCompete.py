def canCompete(partial, complete):
    found = ""

    for ch in partial:
        is_found = False
        while complete and not is_found:
            if ch == complete[0]:
                found += ch
                is_found = True
            else:
                is_found = False
            complete = complete[1:]
    
    if found == partial:
        return True
    return False

print(canCompete("abc", "ajbjcd"))      #true
print(canCompete("abbc", "ajbbvvgcd"))  #true
print(canCompete("abcz", "ajbjcd"))     #false
print(canCompete("abbc", "bajbjcd"))    #false
  
