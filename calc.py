# 2개의 변수 선언과 input과 형변환
print('2개의 숫자를 입력하면 다양한 계산을 해드립니다!!!')
one = int(input('첫 번째 숫자를 입력하세요 : '))
two = int(input('두 번째 숫자를 입력하세요 : '))

# 계산 작업
add = one + two
sub = one - two
mul = one * two
div = one / two
share = one % two
remain = one // two
power = one ** two

# 출력
print('첫 번째 입력한 숫자는', one,'입니다!!!')
print('두 번째 입력한 숫자는 ', two, '입니다!!!')
print('두 수의 덧셈의 결과는 ', add, '입니다!!!')
print('두 수의 뺄셈의 결과는 ', sub, '입니다!!!')
print('두 수의 곱셈의 결과는 ', mul, '입니다!!!')
print('두 수의 나눗셈의 결과는 ', div, '입니다!!!')
print('두 수의 나눗셈 후 몫의 결과는 ', share, '입니다!!!')
print('두 수의 나눗셈 후 나머지의 결과는 ', remain, '입니다!!!')
print('두 수의 거듭제곱의 결과는 ', power, '입니다!!!')
