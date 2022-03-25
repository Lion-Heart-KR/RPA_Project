import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("I'll let you live", interval=0.1)

#automate the Boring Stuff with Python
pyautogui.write(["t", "e", "s", "t", "left","left", "right", "l", "a", "enter"], interval=0.1)

#special Character
#shift 4 -> $
pyautogui.keyDown("shift") #shift누르고
pyautogui.press("4") #4를 누르고
pyautogui.keyUp("shift") #shift를 뗀다

#조합 키 (Hot Key)
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a")
pyautogui.keyUp("ctrl")

#간편한 조합키
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "v")


#한글 처리
import pyperclip
# pyperclip.copy("나는 이제 잘래") #나는 이제 잘래 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v")

def korean_write(text):
    w.activate()
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

korean_write(input("입력해봐라!"))

#자동화 프로그램 종료
#win : ctrl + alt + del
#mac : cmd + shift + option + q