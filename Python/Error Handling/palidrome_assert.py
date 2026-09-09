def is_palidrome(words):

    result = words==words[::-1]

    return result

try:

    assert is_palidrome("dad") == True,"test case 1 falied"
    assert is_palidrome("tab") == False,"test case 2 failed"
    assert is_palidrome("malayalam") == True,"test case 3 failed"

except:
    print("Error")

else:
    print("Success")    