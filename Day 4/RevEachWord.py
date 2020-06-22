# Code 

def word_flipper(our_string):

    final=""
    for i in our_string.split(" "):
        final += i[::-1] + " "
    
    return final.strip()

# Test Cases

print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")