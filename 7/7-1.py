#!/usr/bin/python
#coding: UTF-8
"""
题目：打印出杨辉三角形（要求打印出10行如下图）。　　
程序分析：规律 如从0行0列，  第4行，4-2的位置为4 表示a[4][1]=4  a[4][1]=a[3][1]+a[3][0]  a[4][2]=a[3][2]+a[3][1],
                             每一行第0列数都是1，第n行m列  当 m=n是 a[n][m]=1

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
"""
#注意python的灵魂格式写法：缩进对齐与不对齐
#采用列表方式利用“类似”不规则二维数组实现{其他语言有数组，而python没有，但有打了“激素”的列表}
def rule(n):
    ls =[1] #初始化第一个，第0行0列
    print 1
    for i in range(1,n):  #第1行到n-1行   (第0行加n-1行共n行)
        ls.append([1])  #每一行（第1~n-1行）第一个数为1
        print 1,
        for j in range(1,i): #第 x行，m列
            ls[i].append(ls[i-1][j-1] + ls[i-1][j])
            print ls[i-1][j-1] + ls[i-1][j],
        ls[i].append(1)   #为每一行末尾加上1
        print 1

    
    #结注意print后面加逗号表示不换行


    return ls
a =rule(10)    
"""

列表实现后的 样子
ls =[ [ 1 ],
      [ 1, 1 ],
      [ 1 ,2, 1 ],
      [ 1 ,3 ,3,  1 ],
      [ 1 ,4 ,6 , 4 1 ],
      [ 1 ,5 ,10 ,10, 5 ,1 ],
      [ 1 ,6 ,15 ,20, 15  ,6 ,  1 ],
      [ 1 ,7 ,21 ,35, 35  ,21 , 7, 1 ],
      [ 1 ,8 ,28 ,56, 70  ,56  ,28 ,8 ,1 ],
      [ 1 ,9, 36 ,84, 126, 126, 84, 3,6 ,9 1 ]]   
 

"""

