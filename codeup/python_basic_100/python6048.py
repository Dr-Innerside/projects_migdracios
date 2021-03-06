# 6048

# 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

# 예시
# print(123<456)  #비교 연산자 < 의 계산 결과인 True(참)가 출력된다.
# (123, 456 은 숫자로 작성된 단어이기 때문에 10진수로 인식된다.)

# 참고
# 어떤 값을 비교하기 위해 비교/관계(comparison/relational) 연산자(operator)를 사용할 수 있다.

# 비교/관계연산자 < (less than sign) 는
# 왼쪽의 값이 오른쪽 값 보다 작은 경우 True(참)로 계산하고,
# 그 외의 경우에는 False(거짓)로 계산한다.

# 비교/관계연산자도 일반적인 사칙연산자처럼 주어진 두 수를 이용해 계산을 수행하고,
# 그 결과를 True(참), 또는 False(거짓)로 계산해 주는 연산자이다.

# 비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다

# 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

# 예시
# print(123<456)  #비교 연산자 < 의 계산 결과인 True(참)가 출력된다.
# (123, 456 은 숫자로 작성된 단어이기 때문에 10진수로 인식된다.)

# 참고
# 어떤 값을 비교하기 위해 비교/관계(comparison/relational) 연산자(operator)를 사용할 수 있다.

# 비교/관계연산자 < (less than sign) 는
# 왼쪽의 값이 오른쪽 값 보다 작은 경우 True(참)로 계산하고,
# 그 외의 경우에는 False(거짓)로 계산한다.

# 비교/관계연산자도 일반적인 사칙연산자처럼 주어진 두 수를 이용해 계산을 수행하고,
# 그 결과를 True(참), 또는 False(거짓)로 계산해 주는 연산자이다.

# 비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다

a, b = map(int, input().split())
print(a < b)
