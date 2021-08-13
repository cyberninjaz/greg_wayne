go = 0
while go == 0:
    import math
    def palindrome(s):
        mid = math.floor(len(s)/2)
        x = len(s)
        for i in range (mid):
            j = -(i+1)
            if s[i] != s[j]:
                return False
        return True

    userInput = input ("Type in word. Type 'end' to end. ")
    if userInput == "end":
        print("ended")
        print()
        break
    elif palindrome(userInput):
        print("Yes. Palindrome")
    else:
        print("No. Not Palindrome")