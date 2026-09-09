class Factorial:

    def solution(self, num):

        result=1

        for i in range(1, num + 1):

            result=result * i

        print(result)


fact_instance=Factorial()
fact_instance.solution(5)