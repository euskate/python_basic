# 트럼프 카드는 => 타입이 4개, 타입별 카드가 13장
# 총 카드 수 = 13 * 4 = 52 -> 일렬로 배치하면
CARD_TYPE = 4
CARD_PER_TYPE_SIZE = 13
TOTAL_CARD_COUNT = CARD_TYPE * CARD_PER_TYPE_SIZE

# 모든 카드 생성
all_cards = list(range(TOTAL_CARD_COUNT))
seq = list('♠◆♥♣')
card_id = list('A23456789')+['10']+list('JQK')
print( seq, card_id )
target_num = 38
print( seq[int(target_num/CARD_PER_TYPE_SIZE)] )
print( card_id[target_num%CARD_PER_TYPE_SIZE] )