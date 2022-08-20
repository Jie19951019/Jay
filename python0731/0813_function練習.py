#作業  讀取兩個txt檔內容  計算數值平均後  寫入csv檔

import csv

#IO Function
def CalculateAvg(Name):
    File = open(Name + ".txt") 
    FileList = File.readlines()   #全部顯示出來
    Sum = 0
    ListLength = len(FileList)

    for n in range(ListLength):
        Sum += int(FileList[n].strip('\n'))

    CsvFile_Open = open('CalculateAvg.csv', mode='a',newline='')	# or mode='w'
    CsvWriter = csv.writer(CsvFile_Open)   #這裡是  要先轉成物件  然後才可以writerow  csv都要這樣寫
    CsvWriter.writerow([Name + " Average is: " + str(Sum/ListLength)])

#
CalculateAvg("0813_Mary")
CalculateAvg("0813_Bob")