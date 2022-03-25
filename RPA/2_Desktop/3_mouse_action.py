import pyautogui

# print(pyautogui.position())

# pyautogui.click()
# pyautogui.click(56, 12, duration=1) #1초동안 이동 후 (56,12)를 마우스로 클릭하는 동작

# print(pyautogui.position())
# pyautogui.sleep(3)
# print(pyautogui.position())
#drag and drop할 때 활용 가능
# pyautogui.mouseDown(385, 241) #클릭하는 상태
# pyautogui.moveTo(747,422)
# pyautogui.mouseUp(747, 422) #마우스에서 손 뗀 상태

#더블클릭이다.
# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(200, 300)
# pyautogui.mouseDown()
# pyautogui.moveTo(300, 400)
# pyautogui.mouseUp()

pyautogui.sleep(3)
# pyautogui.rightClick()
# pyautogui.middleClick()
# print(pyautogui.position())
# pyautogui.moveTo(1289, 365)
# pyautogui.drag(-100, -219, duration=0.25) #너무 빠른 동작으로 drag수행이 안 될때는 duration을 설정
# pyautogui.dragTo(1000, 4, duration=1)

pyautogui.scroll(300) #양수면, 윗방향, 음수면 아랫방향으로 스크롤
# pyautogui.scroll(-400)
