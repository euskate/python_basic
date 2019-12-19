GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9
IS_DEV_MODE         = True

if not IS_DEV_MODE: # release 버전의 코드가 작동
    # step1
    print( "Enjoy Custom Game world" )
    # step2 
    while True: #반드시 내부에 break가 있어야 한다.
        tmp = input('게임 제목을 입력하시오, 단 %s자 이내로 입력 가능합니다.\n > ' % GAME_TITLE_LEN_MAX).strip()
        if not tmp:             #   2=3 아무것도 입력하지 않고 엔터를 치면, 
            print('정확하게 입력하세요!')
            pass
        elif len(tmp) > 20:     #   2=4 20자 이상 입력하면, 
            print('%s자가 초과되었습니다.' % GAME_TITLE_LEN_MAX)
            pass
        else:                   #   2=5 20자 이내로 입력하면,
            gameTitle = tmp
            break
        pass

    # step3
    while True:
        tmp = input('플레이어의 닉네임을 입력하시오, 단 %s자 이내로 입력 가능합니다.\n > ' % PLAYER_NAME_LEN_MAX).strip()
        if not tmp:
            print('정확하게 입력하세요!')
        elif len(tmp) > PLAYER_NAME_LEN_MAX:
            print('%s자가 초과되었습니다.' % PLAYER_NAME_LEN_MAX)
        else:
            player_name = tmp
            break

    # step4
    while True:
        tmp = input(f'게임 난이도를 입력하시오. ( {GAME_LEVEL_MIN} ~ {GAME_LEVEL_MAX} ) : ').strip()
        if not tmp:
            print('정확하게 입력하세요!')
        elif not tmp.isdecimal():
            print('정수를 입력하세요')
        elif int(tmp) > GAME_LEVEL_MAX or int(tmp) < GAME_LEVEL_MIN:
            print('1~9 사이의 수를 입력하세요.')
        else:
            game_level = tmp
            break
else:               # test or dev(개발) 버전으로 코드가 작동
    # 매번 입력 받아서 테스트하기 시간이 많아 소요됨으로, 값을 고정하여 개발
    gameTitle   = 'test game'
    player_name = 'guest'
    game_level  = 1

# step 5
print( '-'*20 )
print( 'gameTitle :', gameTitle )
print( 'player_name :', player_name )
print( 'game_level :', game_level )
print( '-'*20 )

# step 6
# 인트로 (가로길이 40칸)
'''
========================================
+       게임제목(중앙정렬)             +
+           lv 레벨값                  +
+       "플레이어이름"의 연대기        +
========================================
        press any key!!
'''

print( '=' * 40 )

print( '+{0:^38}+'.format(gameTitle) )
# print( f'1231232{gameTitle}+'.center(40))
print( '+{0:^38}+'.format( 'lv : %s' % game_level) )
print( '+{0:^38}+'.format( '%s\'s chronicle' % player_name) )
print( '=' * 40 )
print( '{0:^40}'.format('press any key!!') )


# step 7
# 카드 게임
# 트럼프 카드 종류 -> 4타입, 타입별로 13장의 카드가 존재
# A는 합산값의 *2을 한다 : ex) A, 3 => (1+3)*2 = 8점
# J=>11, Q=>12, K=-5
'''
♠ : A, 2 ~ 10, J, Q, K
♥ : A, 2 ~ 10, J, Q, K
♣ : A, 2 ~ 10, J, Q, K
◆ : A , 2 ~ 10, J, Q, K
'''

# 전체 Rule
# 1. 게임이 시작하면 카드를 섞는다 => 셔플 => random 모듈을 활용(외장함수, 구현을 위해 사용)

# 2. 카드를 순서대로 나 한장(0), 컴퓨터 한장(1), 나 한장(2), 컴퓨터 한장(3) 배치(순서대로 뽑는다)
# 3. 플레이어는 최대 2장까지 더 받을 수 없다.
#    다시 나 한 장(4,6), 컴퓨터 한 장(5,7) -> 최대 2번까지 가능
# 4. 승패 -> 내가 가진 카드 중 최대값 2개를 합산해서, 특별기능이 있다면 추가 계산해서 높은 쪽이 승리한다.
# 5. 한번에 이기면 (내 카드의 합-컴퓨터 카드의 합)*100, 카드를 한 번 받으면 20점씩 감소.
# 6. 카드를 받으면 1. 카드를 더 받겠습니까?  아니면 2. 승부를 내겠습니까?
# 7. 다시하시겠습니까? yes => 다시 1번부터 시작, no -> game over!! 종료

# 전체 Rule
# 1. 게임이 시작하면 카드를 섞는다 => 셔플 => random 모듈을 활용(외장함수, 구현을 위해 사용)
totalScore = 0
keepGame = True
while keepGame:    
    types = list('♠◆♥♣')
    nums = list('A23456789')+['10']+list('JQK')
    # 카드 초기화
    cards = [ i+j for i in types for j in nums ]
    # 점수표 초기화
    score_table = dict()
    for key in nums:score_table [ key ] = nums.index( key ) + 1
    import random
    random.shuffle(cards)
    # 2. 카드를 순서대로 나 한장(0), 컴퓨터 한장(1), 나 한장(2), 컴퓨터 한장(3) 배치(순서대로 뽑는다)
    my_cards = cards[:8:2]
    com_cards = cards[1:8:2]
    my_first_cards = my_cards[:2]
    com_first_cards = com_cards[:2]

    print("내 카드 :", my_first_cards)
    print("컴 카드 :", com_first_cards[:1], "['?']")
    # 4. 승패 -> 내가 가진 카드 중 최대값 2개를 합산해서, 특별기능이 있다면 추가 계산해서 높은 쪽이 승리한다.
    # 6. 카드를 받으면 1. 카드를 더 받겠습니까?  아니면 2. 승부를 내겠습니까?

    # 플래그 변수 : 변수로 흐름을 제어한다. => cnt
    cnt = 0     # 카드를 추가로 준 횟수
    while True:
        choice = input( '1. 카드를 더 받겠습니까?  아니면 2. 승부를 내겠습니까?' )
        if choice == '1' and cnt < 2:
            cnt += 1
            # 2>3, 3->4 4->1 1번 선택불가
            my_first_cards = my_cards[:2+cnt]
            com_first_cards = com_cards[:2+cnt]
            print(my_first_cards)
        elif choice == '2':
            # 판정을 위해 점수를 획득
            myScore  = 0 
            comScore = 0

            for n in my_first_cards:  myScore += score_table [ n[1:] ]
            for n in com_first_cards: comScore += score_table [ n[1:] ]
            print('\nplayer\'s card : ', my_first_cards, ', score', myScore)
            print('computer\'s card : ', com_first_cards, ', score', comScore)
            phaseScore = myScore - comScore
            totalScore += phaseScore
            if myScore > comScore:print('You Win')
            elif myScore < comScore:print('You Lose')
            else:print('무승부')
            
            print('\nthis phase your score : ', phaseScore)
            print('your Total Score : ', totalScore)
            
            choice = input('\ntry again? 1. Yes  2. No')
            if choice == '1':break
            if choice == '2':keepGame = False
            else:print('1 또는 2를 입력하세요')
            break

        else:
            print('1 또는 2를 입력하세요.')
            if cnt == 2:
                print('이미 추가 카드를 다 받았습니다. 2번만 선택할 수 있습니다.')

# 3. 플레이어는 최대 2장까지 더 받을 수 없다.
#    다시 나 한 장(4,6), 컴퓨터 한 장(5,7) -> 최대 2번까지 가능
# 5. 한번에 이기면 (내 카드의 합-컴퓨터 카드의 합)*100, 카드를 한 번 받으면 20점씩 감소.
# 7. 다시하시겠습니까? yes => 다시 1번부터 시작, no -> game over!! 종료