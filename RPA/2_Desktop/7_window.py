import pyautogui

# fw = pyautogui.getActiveWindow() #현재 활성화된 창 정보를 가져옴(ex : vscode)
# print(fw.title) #창의 제목 정보
# print(fw.size) #창의 크기 정보(width, height)
# print(fw.left, fw.right, fw.top, fw.bottom)
# pyautogui.click(fw.left+50, fw.top+15, duration=1)

# for w in pyautogui.getAllWindows():
#     print(w)

#특정 제목을 갖는 윈도우를 가져오기
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w.isActive)
if w.isActive == False:
    w.activate() #활성화=맨 앞으로 가져오기

if w.isMaximized == False:
    w.maximize() #최대화

pyautogui.sleep(1)

w.restore()
w.close() #윈도우 닫기

# if w.isMinimized == False:
#     w.minimize()