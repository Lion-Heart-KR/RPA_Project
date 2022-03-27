#일반 가격
def price(people):
    print("{0}명 가격은 {1:,}원 입니다.".format(people, people*12000))

#조조 할인
def priceMorning(people):
    print("{0}명의 조조 할인 가격은 {1:,}원 입니다.".format(people, people*7000))

#군인 할인
def priceMilitary(people):
    print("{0}명의 군인 할인 가격은 {1:,}원 입니다.".format(people, people*6000))