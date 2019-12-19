# 랜덤 및 셔플 테스트
import random


ori_data     = data = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
target_data  = ori_data[:]

'''
♠ : A, 2 ~ 10, J, Q, K
♥ : A, 2 ~ 10, J, Q, K
♣ : A, 2 ~ 10, J, Q, K
◆ : A , 2 ~ 10, J, Q, K
'''

a = ['♠','♥','♣','◆']
b = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
[ a+b for i in range(a) for j in range(13) ]
for i in range(a):
    for j in range(13):



# 난 항상 일정하게 섞이는 값은 원한다 -> 난수가 항상 일정하게 나온다 -> seed고정
# random.seed(2)
# seed를 고정하면 난수가 나오는 순서가 동일 => 일정한 결과를 낼 수 있다.
# 일정한 결과를 내면 => 항상 같은 결과가 나오는 실험환경을 구축할 수 있다.
# 변수를 바꿔가면서 영향성 등 분석할 수 있다.
# seed를 고정하지 않으면 => 현재 시간이 seed가 된다.

random.shuffle(target_data)         # 섞기 함수
print(ori_data)
print(target_data)

