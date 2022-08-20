## TXT:讀
# File = open("note.txt") 

##3種讀法
# TextList = File.read()   #全部顯示出來
# TextList = File.readline()  #File.readline()  執行第一次 表示第一列資料+\n   再執行一次 表示第2列資料+\n  以此類推
# TextList = File.readlines()  #把每一列+\n  化為List

# print(TextList)

##-------------------------------------------------------------------------------------------------------------------
# ## TXT:復寫   

# FileWrite = open("note.txt",'w')  # w的寫是直接復寫 之前的資料會不見
# #兩種復寫法
# FileWrite.write("Stock No : 0813\n") #這裡記得加上\n 從下行開始寫
# FileWrite.writelines(["Stock No : 0814\n" , "Stock No : 0815\n"]) #寫一個 List of string 進去檔案

# #TXT:新增至舊資料上 之前資料不會不見
# FileWrite = open("note.txt",'a')  # w的寫是直接復寫 之前的資料會不見
# FileWrite.writelines(["Stock No : 0814\n" , "Stock No : 0815\n"])

##-------------------------------------------------------------------------------------------------------------------
#CSV  首先先 import csv
##CSV 寫
# csv_fileA = open('class.csv', mode='w',newline='')	# or mode='a'
# csvWriterA = csv.writer(csv_fileA)   #這裡是  要先轉成物件  然後才可以writerow  csv都要這樣寫
# csvWriterA.writerow(['number', 'name', 'score'])
##CSV 讀
# csv_fileA = open('class.csv', mode='r',newline='')
# rows = csv.reader(csv_fileA)
# for row in rows:
#     print(row)

##-------------------------------------------------------------------------------------------------------------------

## 字串操作 : strip 跳過某個字元
# str_with_headntail = '====Name:Andrew===='
# str_with_headntail = str_with_headntail.strip('=')
# print(str_with_headntail)

## 字串操作 : replace 替換某個字元
# str_with_headntail = str_with_headntail.replace('=','-')

## 字串操作 : 將英文變大小寫
# str_with_headntail = str_with_headntail.upper()  # 或是lower

## 字串操作 : split 以某個字元為分界來切割字串  以本例為例   切割完後放入list_of_data  裡面會有兩個元素 ['Name', 'Andrew']
# str_with_headntail = 'Name:Andrew'
# list_of_data = str_with_headntail.split(':')
# print(list_of_data)

# ## 字串操作 : find 找字串  有找到就返回索引 沒找到就返回-1
# str_with_headntail = 'Name:Andrew'

# pos_of_Andrew = str_with_headntail.find('Andrew')
# pos_of_Bob = str_with_headntail.find('Bob')

# print(pos_of_Andrew)
# print(pos_of_Bob)



# #作業  找日期顯示其後面的數值
# Date = input("Please input date: ")

# File = open("0812_note.txt")
# TextList = File.readlines()
# print(TextList)

# for Row in range(len(TextList)) :
#     if TextList[Row].find(Date) != -1:
#         SplitTextList = TextList[Row].split(',')
#         print("第" + str(Row+1) + "個元素存在" + Date+ ", 其數值為:" + SplitTextList[1] , end = '')



##關於Path   打字串一定會用到這個r 來避免跳脫字元
# Example 1    Use r-string (stands for raw string) to avoid escape character (such as \n, \t)
# escaped_str = 'files\nana_savings.txt'
# raw_str = r'files\nana_savings.txt'

# print(escaped_str)
# print(raw_str)

#Example 2 查看路徑是否存在
# import os   #(要輸入os)
# print(os.path.exists(r'D:\savings.txt'))

#Example 3 創建新目錄
# import os

# if os.path.exists(r'D:\savings') == False:
#     os.mkdir(r'D:\savings')