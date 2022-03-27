""" try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요.")))
    nums.append(int(input("두 번째 숫자를 입력하세요.")))
    # nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러가 발생해떠염")
except ZeroDivisionError as err:
    print(err)
    # print("can not divide by zero")
except Exception as err:
    print("알 수 없는 오류가 발생했습니다.")
    print(err) """

""" class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력해주세요"))
    num2 = int(input("두 번째 숫자를 입력해주세요"))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력해주세요.")
except BigNumberError as err:
    print("에러가 발생했습니다. 한 자리 숫자만 입력해주세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.") """

########################################### Quiz ###########################################
""" class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print("남은 치킨 : {0}".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? : "))
        if order < 1:
            raise ValueError
        if order > chicken:
            print("재료가 부족합니다.")
        else :
            print("대기번호 : {0}\n{1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
        
        if chicken <= 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
    finally:
        print() """

########################################### Module ###########################################
""" import theater_module
theater_module.price(3) #일반인 3명이 영화보러감
theater_module.priceMorning(4) #일반인 4명 조조영화
theater_module.priceMilitary(30) #군바리 셋이서 귀멸의 칼날 보러감 """

""" import theater_module as mv
mv.priceMilitary(3) """

""" from theater_module import *
priceMilitary(3)
price(2)
priceMorning(10) """

""" 
from theater_module import price, priceMorning
priceMorning(10)
"""
""" 
from theater_module import priceMilitary as price
price(5)
"""

# import travel.thailand
""" from travel.thailand import ThailandPackage
trip_to = ThailandPackage() #클래스 생성자
trip_to.detail() """

""" from travel import vietnam
trip_to = vietnam.VietnamPacage()
trip_to.detail() """

from travelTemp import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(thailand))