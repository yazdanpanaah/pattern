def creat_pattern(row):
    for i in range(0,row):
        for j in range(row-1,i,-1):
            print(j,'',end = '')
        for l in range(i):
            print('    ', end= '')
        for k in range(i+1 ,row):
            print(k ,'',end='')
        print() 

while True:
    row_num = input('enter num of rows:')
    if row_num.isnumeric():
        if int(row_num) > 3: 
            creat_pattern(int(row_num))
            break
        else:
            print('enter num greater than 3')
    else:
        print('it must be integer!!!')
