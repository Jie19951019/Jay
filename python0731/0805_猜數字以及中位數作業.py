# import random

# error_count = 0

# answer = random.randint(1,10)
# print("answer= " + str(answer))

# while error_count < 3:

#     number = int(input("請輸入一個數字"))
        
#     if answer == number:
#         print("猜到了")
#         break
#     else:
#         error_count += 1
#         print("錯誤次數= "+str(error_count))

# print("程式結束")


MyList = [1,2,3,4,5,6,7]
List_Length = len(MyList)

if List_Length % 2 != 0:
    List_Index = int(List_Length/2+0.5)
    print("中位數:"+ str(MyList[List_Index-1]))
else:
    List_Index = int(List_Length/2)-1
    print("中位數:" + str((MyList[List_Index]+MyList[List_Index+1])/2))
