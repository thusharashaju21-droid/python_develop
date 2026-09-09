class GCD:

    def solution(self, num1, num2):

        result=1

        for i in range(1,min(num1,num2)+1):

            if num1 % i == 0 and num2 % i == 0:

                result = i

        print(result)


gcd_instance=GCD()
gcd_instance.solution(12, 18)
gcd_instance.solution(13,15)