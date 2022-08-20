# Example 1   Function回傳
# def NTD_to_JPY(price):
#     price_jpy = 4.46*price
#     return price_jpy

# savings = 700
# savings_jpy = NTD_to_JPY(savings)
# print(savings_jpy)

# Example 2   module使用

# from datetime import datetime   #我們實際要用的是後面這個datetime(子模組)  它存在於前面這個datetime(母模組裡面)
#有的作者會認為，為了不顯得奇怪所以子模組名字不要跟母一樣
#但有的作者相反，他覺得子模組裡面最重要的那個，就直接沿襲母模組名稱就好
# now = datetime.now()
# dateAndTime = now.strftime("%Y_%m%d_%H%M%S")
# print(dateAndTime)


# Example 2.5   module使用
# 我想引用A資料夾中的B   from A import B
# 如果A資料夾中 有B資料夾 想引用其中的C   from A.B import C
 

# Example 3  下載外部module  範例  下載圖表
#在以下終端機 輸入  pip install matplotlib
#之後使用引入  可以自己幫她取名字   像是 : import matplotlib.pyplot as plt
#使用這個圖表模組  的範例程式
# import matplotlib.pyplot as plt

# x = [0,1,2]
# y = [3,4,5]

# plt.plot(x,y)
# plt.show()

# Example 4  使用自定義module
# 假設我打了一個.py檔  名叫show.py
# 我在main.py檔要使用
# 就直接在main.py檔上 打 import show 就好


# Example 5  _NAME_  的使用
# 假設現在有A.py 與 B.py
# 我在A.py 中 import B
# B裡面的程式碼  使用方法以及使用_NAME_的程式碼  不會執行  
# 其他全部都會直接執行  包括print 什麼都是
# 所以使用_NAME_  就是讓import進去時  不會一import 就執行程式碼
# 所以可以這樣打  if __name__ == '__main__':   (這個判斷是就是這樣打 一個字都不用改)
# 如果此時在B中  是這樣打
# if __name__ == '__main__':
#     print('Execute sub_analyzer...')
# 如果我在A , impport B  然後執行
# 此時  不會打出print那段
# 但如果我是在B  直接執行
# print 那段就會打出來


# #Example 6   Try except else
# try:
#     print("有可能會出錯的")
# except Exception as e:
#     print("錯誤",e)
# else:
#     print("正確的話")


# Example 7 __init__  的使用
# 一般想在這裡引用  這個資料夾( 0814__init__練習 )  中的 A.py  B.py
# from 練習_0814_init import A
# from 練習_0814_init import B

# 但如果想要一次引用整個資料夾  一個一個打太麻煩
# 所以在  練習_0814_init  中  加入__init__.py  這個檔案
# 然後直接import 練習_0814_init  即可一次import 裡面所有檔案
import 練習_0814_init    

# 
# # 作業  輸入錯誤要重複輸入  再上傳git
# Grade = [10,20,30,40,50,60]
# Grade.sort(reverse = True)

# InputCorrectFlag = 0
# while(InputCorrectFlag == 0) :
#     try:
#         InputInteger = input("請輸入取前幾高:")
#         for n in range(int(InputInteger)):
#             print(Grade[n])
#     except:
#         print("輸入數量超出List邊界")
#     else:
#         if(int(InputInteger) > 0):
#             print("正確")
#             InputCorrectFlag = 1
#         else:
#             print("輸入必須大於0")

