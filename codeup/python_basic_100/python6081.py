# 6081
#
# 16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
# 영일이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.
#
# A, B, C, D, E, F 중 하나가 입력될 때,
# 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
# (단, A ~ F 까지만 입력된다.)


# num = int(input())
# hexRange = list(a for a in range(1,17))
#
# for calc in hexRange:
#     print(calc)
#     # print('X%'%num +'*'+calc+'='+'X%'%(num*calc))
#     # print(f'{num}*{calc}')
#     print('%X' % num, '*%X' % calc, '=%X' % (num * calc), sep='')


n = input()
# print(f'n->{n}')
listn = ['A','B','C','D','E','F']
if n in listn:
    n = int(n, 16)
    for i in range(1,16):
        print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
