

"""
Docstring for reverseVowels

Convert to List, reverse in String in place.

Use set for o(1) look up.

"""


# "AEIOU"
def reverseVowels(givenStr):
    vowels = set("aeiouAIEOU")
    start =0
    end = len(givenStr)-1
    giveStrList = list(givenStr)

    while end>start:
        while end >start & (givenStr[start] not in vowels) :
              
              start = start +1      
        while end > start & (givenStr[end] not in vowels) :
             
             end = end -1
        
        
        giveStrList[start] = givenStr[end]
        giveStrList[end] = givenStr[end]
        start+= 1
        end-= 1
        
    
    return "".join(giveStrList)         
                   
                
print(reverseVowels("DesignGUrus"))