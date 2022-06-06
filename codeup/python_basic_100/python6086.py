# 6086
#
# 1, 2, 3 ... 을 순서대로 계속 더해 합을 만드는데,
# 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.
#
# 즉, 1부터 n까지 정수를 하나씩 더해 합을 만드는데,
# 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.
#
# 하지만, 이번에는 그 때 까지의 합을 출력해야 한다.
#
# 예를 들어, 57을 입력하면
# 1+2+3+...+8+9+10=55에서 그 다음 수인 11을 더해 66이 될 때,
# 그 값 66이 출력되어야 한다.
#
# 예시
# ...
# while True :
#   s += c
#   c += 1
#   if s>=n :
#     break
#
# print(s)

inputNum = int(input())
sum = 0
startNum = 0
while inputNum >= sum:
    startNum += 1
    sum += startNum
    if inputNum <= sum:
        break

# print(f'sum -> {sum}')
print(sum)