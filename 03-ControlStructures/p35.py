i = 0
for i in range(1,31):
    print(i)
    if (i % 5) == 0 and (i % 3) == 0:
        print('BINGO')
    elif (i % 5) == 0:
        print('FIVE')
    elif (i % 3) == 0:
        print('THREE')