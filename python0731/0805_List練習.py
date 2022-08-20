
# toeicGrades -> parent
toeicGrades = [700,800,900,750,650,800]     # 700,800,900 -> element/child

print(toeicGrades[-1])
print(toeicGrades[::2])     # slice     # parameter 1: start    # parameter 2: the start of don't show
                            #每兩個 列印出來

print(len(toeicGrades))     # length
# print(max(toeicGrades))    
# print(min(toeicGrades))     
# print(sum(toeicGrades))     

toeicGrades.sort()
# toeicGrades.reverse()
print(toeicGrades)
# print(toeicGrades.index(750))   #列印值750的索引

'''
stock_tsmc = []   #先新增一個空的List

stock_tsmc.append(500)   #新增值進去
stock_tsmc.append(505)
stock_tsmc.append(505)
stock_tsmc.append(510)

print(stock_tsmc)

x = stock_tsmc.count(505)   #計算List個數
for n in range(x):    #for迴圈會自動數到x-1個  所以直接打x個就好
    stock_tsmc.remove(505)  # param: value   #移除505
print(stock_tsmc)
stock_tsmc.pop(0)  # param: index
print(stock_tsmc)


# for x in range(10):
#     print(x)
'''

# user input 5 times toeic grades
# 1: highest to lowest
# 2: average