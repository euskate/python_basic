# 전체 Rule
# 1. 게임이 시작하면 카드를 섞는다 => 셔플 => random 모듈을 활용(외장함수, 구현을 위해 사용)
types = list('♠◆♥♣')
nums = list('A23456789')+['10']+list('JQK')
cards = [ i+j for i in types for j in nums ]
import random
random.shuffle(cards)
# 2. 카드를 순서대로 나 한장(0), 컴퓨터 한장(1), 나 한장(2), 컴퓨터 한장(3) 배치(순서대로 뽑는다)
my_cards = cards[:8:2]
com_cards = cards[1:8:2]
my_first_cards = my_cards[:2]
com_first_cards = com_cards[:2]

# 4. 승패 -> 내가 가진 카드 중 최대값 2개를 합산해서, 특별기능이 있다면 추가 계산해서 높은 쪽이 승리한다.
# 6. 카드를 받으면 1. 카드를 더 받겠습니까?  아니면 2. 승부를 내겠습니까?
choice = input( '1. 카드를 더 받겠습니까?  아니면 2. 승부를 내겠습니까?' )
while True:
    if choice == '1':
        pass
    elif choice == '2':
        pass
    else:
        print '1 또는 2를 입력하세요.'

# 3. 플레이어는 최대 2장까지 더 받을 수 없다.
#    다시 나 한 장(4,6), 컴퓨터 한 장(5,7) -> 최대 2번까지 가능
# my_first_cards = my_cards[:3]
# com_first_cards = com_cards[:3]

# 5. 한번에 이기면 (내 카드의 합-컴퓨터 카드의 합)*100, 카드를 한 번 받으면 20점씩 감소.
# 7. 다시하시겠습니까? yes => 다시 1번부터 시작, no -> game over!! 종료


# -> 정수값 추출: 멤버 하나씩 추출 -> 슬라이싱or추출or분해
score_table = dict()
for key in nums:
    # 1 ~ 13값을 차례대로 넣어라 
    score_table [ key ] = nums.index( key ) + 1

# A ~ K 까지를 키로 보고 이를 통해 값을 획득하면 간단하게 합산처리
# 이를 위해 점수 변환 표를 준비한다
# print( score_table )

# k = 1
# for key in nums:
#     score_table[ key ] = k
#     k += 1
# print(score_table)
# -> 합하기

sum = 0
for n in my_first_cards:
    sum += score_table [ n[1:] ]
print( '내 최초 카드 2장의 합', sum)
        


# my_com_cards = com_cards[:2]

# print( my_first_cards)