#Check if word is a palindrome ex: kaika -> kaiak
#Check if word is an anagram ex: 
def is_palindrome(s):
    #pass
    list_s = list(s)
    reveresed_s = list(s)
    reveresed_s.reverse()
    #if list(s) == list(s).reverse():
        #print(list(s))
    return list_s == reveresed_s

#is_palindrome(input("Give your word: "))


#Version 2:
def is_palindrome_v2(s):
    #pass
    reveresed_string =''.join(reversed(s))
    return reveresed_string == s


#Version 3:
def is_palindrome_v3(s):
    #with slice function
    return s == s [::-1]

print(is_palindrome("kaiak"))
print(is_palindrome_v2("kaiak"))
print(is_palindrome_v3("kaiak"))