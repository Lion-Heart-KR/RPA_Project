from time import sleep
import pyautogui

# #1805,22 71,71,72 #474748
# pyautogui.moveTo(1805, 22, duration=1)
# pyautogui.click()

# coupang = pyautogui.locateOnScreen("./RPA/2_Desktop/Files/logo.png")
# # print(file_menu)
# pyautogui.click(coupang, duration=0.5)

# file_menu = pyautogui.locateOnScreen("./RPA/2_Desktop/Files/file_menu.png", confidence=0.95)
# pyautogui.moveTo(file_menu, duration=3)
# pyautogui.click()

# pyautogui.sleep(1)
# for i in pyautogui.locateAllOnScreen("./RPA/2_Desktop/Files/checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# prob_icon = pyautogui.locateOnScreen("./RPA/2_Desktop/Files/problem.png")
# pyautogui.moveTo(prob_icon)

# 속도 개선 1
# 1.Gray Scale : 흑백으로만 비교함으로써 비교를 단순하게 함
# prob_icon = pyautogui.locateOnScreen("./RPA/2_Desktop/Files/problem.png", grayscale=True)
# pyautogui.moveTo(prob_icon)
# print(prob_icon)

# 속도 개선 2 : 범위지정
# prob_icon = pyautogui.locateOnScreen("./RPA/2_Desktop/Files/problem.png", region=(300, 750, 300, 50))
# pyautogui.moveTo(prob_icon)
# print(prob_icon)

# 속도 개선 3 : 정확도 조정
# prob_icon = pyautogui.locateOnScreen("./RPA/2_Desktop/Files/problem.png", confidence=0.95)
# pyautogui.moveTo(prob_icon)

# 자동화 대상이 바로 보여지지 않는 경우
# notepad_filemenu = pyautogui.locateOnScreen("./RPA/2_Desktop/Files/notepad_filemenu.png")
# if notepad_filemenu:
#     pyautogui.click(notepad_filemenu)
# else:
#     print("fail to found")

#1. 계속 기다리기
# while notepad_filemenu == None:
#     notepad_filemenu = pyautogui.locateOnScreen("./RPA/2_Desktop/Files/notepad_filemenu.png")
# print("발견실패")
# pyautogui.click(notepad_filemenu, duration=0.25)

#2. 일정시간 기다리기
import time
import sys

timeout = 5  # 5초 대기


def find_target(img_file, timeout=30):
    start = time.time()  # 시작 시간 설정
    target = None
    while target is None:
        target = pyautogui.locateOnScreen("./RPA/2_Desktop/Files/"+img_file)
        end = time.time()

        if end-start > timeout:
            print("시간종료")
            break
        
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}).\nTerminate program")
        sys.exit()

my_click("notepad_filemenu.png", 10)