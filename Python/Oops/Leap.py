class LeapYear:

    def solution(self,year):

        result=False

        if year%100==0 and year%400==0 or year%1000!=0 and year%4==0:

            result=True

        print(result)

leap_instance=LeapYear()
leap_instance.solution(2023)          
leap_instance.solution(2024)          