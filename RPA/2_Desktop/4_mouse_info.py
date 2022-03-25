import pyautogui
# pyautogui.mouseInfo()
# pyautogui.FAILSAFE = False #마우스를 네 귀퉁이에 갖다놓아도 끝나지 않음.
pyautogui.PAUSE = 1

for i in range(10):
    pyautogui.move(100, 100)
    print(i)
    # pyautogui.sleep(1)