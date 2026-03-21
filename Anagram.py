



def anagram(s,t):

    if(len(s)!=len(t)):
        return False
    digitsDic = {}
    for ch in s:
        digitsDic[ch] = digitsDic.get(ch,0) +1

    for ch in t:
        if ch in digitsDic:
            digitsDic[ch] = digitsDic.get(ch) -1
            if digitsDic[ch] == 0:
                del digitsDic[ch]
        else: 
            return False
    return True                    


