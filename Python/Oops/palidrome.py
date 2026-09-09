class Palindrome:

    def solution(self,word):

        result=True

        left=0

        right=len(word)

        word=list(word)

        while(left<right):

            word[left],word[right]=word[right],word[left]

            left+=1

            right-=1

        print(word)    