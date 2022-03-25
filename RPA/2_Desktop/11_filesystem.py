import os
# print(os.getcwd()) #current working directory
# os.chdir("RPA")
# print(os.getcwd())
# # os.chdir("../..") #상위 폴더 이동
# # print(os.getcwd())
# os.chdir("C:/vscode_python/RPA/1_Excel")
# print(os.getcwd())

#파일 경로 만들기
# file_path=os.path.join(os.getcwd(), "/RPA/2_Desktop/Files/my_file.txt") #절대경로 생성
# print(file_path)

#파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\vscode_python\RPA\2_Desktop\Files\file_menu.png")) # r은 이스케이프 문자를 신경안쓴다는 의미
#저 경로를 알면 폴더 정보도 아는거 아님?ㅋㅋ

#파일 정보 가져오기
import time
import datetime

# file_path = "./RPA/2_Desktop/Files/file_menu.png"

#파일의 생성날짜
# ctime = os.path.getctime(file_path)
# # print(ctime)
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y년%m월%d일 %H:%M"))

# #파일의 수정날짜
# mtime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y년%m월%d일 %H:%M"))

# #파일의 마지막 접근 날짜
# atime = os.path.getatime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y년%m월%d일 %H:%M"))

# file_size = os.path.getsize(file_path) #바이트 단위
# print(file_size)

#파일 목록 가져오기
# print(os.listdir())
# print(os.listdir("RPA")) #주어진 폴더 밑의 모든 폴더, 파일 목록 가져오기

#파일 목록 가져오기(하위 폴더 모두 포함)
# result = os.walk("RPA") #주어진 폴더 밑의 모든 폴더, 파일 목록 가져오기
# result = os.walk(".")  #현재 작업공간 밑의 모든~
# for root, dirs, files in result:
#     print(root, dirs, files)

#폴더 내의 특정 파일들을 찾는 방법(존재 유무)
# name = "11_filesystem.py"
# result = []

# for root, dirs, files in os.walk(os.getcwd()):
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)

#특정 키워드를 가진 파일
# keyword = ".py"
# for root, dirs, files, in os.walk("."):
#     for file in files:
#         if keyword in file:
#             print(file)

#특정 패턴을 가진 파일을 찾기
import fnmatch
pattern = "*.py" #.py로 끝나는 모든 파일
result = []

for root, dirs, files in os.walk("."):
    for fname in files:
        if fnmatch.fnmatch(fname, pattern):
            result.append(os.path.join(root, fname))

print(result)