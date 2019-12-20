# 모듈 가져오기는 가급적 맨 위에서 작성한다. 1회만 로드.
import random   # 모듈 가져오기
import time     # 시간 가져오기

GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9
IS_DEV_MODE         = False

if not IS_DEV_MODE: # release 버전의 코드가 작동
    # step1
    print( "Enjoy Custom Game world" )
    # step2 
    while True:
        tmp = input("게임 제목을 입력하시오, 단 {}자 \이내로 입력 가능합니다. => ".format(GAME_TITLE_LEN_MAX)).strip()       
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>GAME_TITLE_LEN_MAX:
            print(GAME_TITLE_LEN_MAX + "자가 초과되었습니다.") 
        else:
            gameTitle = tmp
            break
    print( 'gameTitle', gameTitle )
    # step 3
    while True:
        tmp = input("플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다\n=>" % PLAYER_NAME_LEN_MAX).strip()
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>PLAYER_NAME_LEN_MAX:
            print("%s자가 초과되었습니다." % PLAYER_NAME_LEN_MAX) 
        else:
            player_name = tmp
            # 플레이어 이름으로 저장된 점수를 읽어서 로드, 만약 없으면 0점으로 시작
            # 영속적으로 저장하는 API를 찾아야 한다.
            myTotalScore       = 0  # 나의 총 점수
            break
    # step4
    while True:
        tmp = input("게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
        if not tmp:
            print('정확하게 입력하세요')
            continue
        if not tmp.isnumeric():
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue
        tmp = int(tmp)
        if tmp>9 or tmp<1:
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue    
        game_level = tmp
        break
else:   # test or dev(개발) 버전으로 코드가 작동
    gameTitle   = 'test game'
    player_name = 'guest'
    game_level  = 1
    myTotalScore       = 0  # 나의 총 점수

# step 5
if IS_DEV_MODE: # 개발시에만 작동한다
    print( '-'*20 )
    print( '현재 까지 입력 상황' )
    print( 'gameTitle',   gameTitle )
    print( 'player_name', player_name )
    print( 'game_level',  game_level )
    print( '-'*20 )

# step 6
print('='*40)
print('+{0:^38}+'.format(gameTitle))
print('+{0:^38}+'.format( 'lv : %s' % game_level ))
print('+{0:^34}+'.format( '"%s"의 연대기' % player_name ))
print('='*40)
print('{0:^40}'.format('press enter key!!'))
while True:input();break   # 한 줄에 여러 문장을 기술 할 때는 구분자로 사용


# step 7 : 실제 게임
# 전체적으로 한번만 수행하면 되는 코드 -----------------------------------
types = list('♠◆♥♣')
nums  = list('A23456789')+['10']+list('JQK')        # 동적 + 정적 + 동적 구성
cards = [ i+j for i in types for j in nums ]        # 리스트 내포 
score_table = dict()
for key in nums:score_table[ key ] = nums.index( key ) +1
# 트럼프 K는 트럼프를 주어서 -5점이다.
score_table[ 'K' ] = -5

# 매번 게임을 새로 수행할 때마다 수행해야 하는 코드 ----------------------
# 원본 카드의 사본
isOneGaming = True
while isOneGaming:
    gamecards = cards[:]
    random.shuffle(gamecards)
    my_cards  = gamecards[:8:2]
    my_first_cards = my_cards[:2]
    com_cards = gamecards[1:9:2]
    com_first_cards= com_cards[:2]

    cnt = 0 # 카드를 추가로 준 횟수
    isGaming = True # 게임 중이다.
    while isGaming:
        msg = '''
            나의 카드:%s, %s vs 컴의 카드 : %s, [Hidden]
        ''' % ( my_first_cards[0], my_first_cards[1], com_first_cards[0] )
        print( msg )
        # x = 1
        # while True:
        #     time.sleep(0.5)
        #     print('-'*x)
        #     x += 1
        #     if x == 4:break

        for n in range(4):time.sleep(0.1);print('-'*n)


        choice = input( '1. 카드를 더 받겠습니까? 아니면 2. 승부를 내겠습니까?' )
        if choice == '1' and cnt <2:
            cnt += 1
            my_first_cards  = my_cards[:2+cnt]
            com_first_cards = com_cards[:2+cnt]
        elif choice == '2':
            # 비교시 A는 합산값의 *2를 한다 :
            # ex) A, 3 => (1+3)*2 = 8점
            # 저장 = (내점수-컴점수)*100 + 카드를 더 받은 횟수*(-20)
            myScore  = 0
            comScore = 0
            for n in my_first_cards:  myScore += score_table[ n[1:] ]
            for n in com_first_cards: comScore += score_table[ n[1:] ]
            print('myScore',myScore)
            print('comScore',comScore)
            
            # 엔터키를 누르면 아래 진행
            if myScore > comScore:
                # 점수 산출 및 표시
                myGetScore = (myScore-comScore) * 100 + cnt * (-20)
                # 내 점수에 합산
                myTotalScore += myGetScore 
                print(f'축하합니다. {myGetScore} 점 총 {myTotalScore} 점 획득하였습니다.')
                print('You Win, try again? 1.yes, 2.no')
            elif myScore < comScore:
                # 점수 산출 및 표시
                myGetScore = -5 # 지면 5점 뺀다.
                # 내 점수에 합산
                myTotalScore += myGetScore
                print(f'아쉽습니다.. {myGetScore} 점  잃었습니다. 총 {myTotalScore} 점입니다.')
                print('You Lose, try again? 1.yes, 2.no')
            else:
                print(f'아~ 비겼네요.. 점수 변동 없습니다.')
                print('무승부, try again? 1.yes, 2.no')
            # 게임 저장
            # 1 혹은 2를 입력받으면 게임을 끝내거나, 게임을 다시
            while True:
                # 대문자, 소문자 어떤 것을 넣던 Ok
                # 내부적으로는 결정한다. (어느쪽으로 처리할 것인지)
                c_number = input().strip().lower()
                if c_number == '1' or c_number == 'y' or c_number == 'yes':
                    isGaming = False
                    break
                elif c_number == '2' or c_number == 'n' or c_number == 'no':
                    isGaming = False
                    isOneGaming = False
                    break
                else:
                    print('정확하게 1 또는 2를 입력하세요.')
        else:
            print('정확하게 1 or 2를 입력하세요')
            if cnt == 2:
                print('이미 추가 카드를 다 받았습니다. 2번만 선택할수 있습니다.')
print('bye bye ~ \ngame over!')