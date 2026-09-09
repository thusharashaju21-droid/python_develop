def divisible_by_three(num):

    result=True

    if num%3==0:

        result=True

    else:

        result=False

    return result


#debugging
assert divisible_by_three(3)==True,"test case1 failed"
assert divisible_by_three(11)==False,"test case2 failed"
assert divisible_by_three(19)==False,"test case3 failed"
assert divisible_by_three(12)==True,"test case4 failed"