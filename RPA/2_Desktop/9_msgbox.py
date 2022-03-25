from unittest import result
import pyautogui

# print("3초 후 시작합니다.")
# pyautogui.countdown(3)
# print("자동화 시작")

# pyautogui.alert("자동화 수행에 실패하였습니다.", "Warnings") #확인 버튼만 있는 팝업
# result = pyautogui.confirm("계속 진행하시겠습니까?", "확인")
# if result == "OK":
#     print("계속 진행")
# result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")
# print(result)
result = pyautogui.password("비밀번호를 입력해주세요.")
print(result)