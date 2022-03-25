import pyautogui
#screen shot
# img = pyautogui.screenshot()
# img.save(".\RPA\\2_Desktop\Files.screenshot.png")


# pyautogui.mouseInfo()
# 16,16 26,135,209 #1A87D1
pixel = pyautogui.pixel(16, 16)
print(pixel)

# print(pyautogui.pixelMatchesColor(16, 16, (26, 135, 209)))
print(pyautogui.pixelMatchesColor(16, 16, (26, 135, 209)))