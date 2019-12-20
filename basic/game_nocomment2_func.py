# 1. 모듈 가져오기
import random
import time

# 2. 전역변수 정의
GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9
IS_DEV_MODE         = False
# 전체적으로 한번만 수행하면 되는 코드 -----------------------------------
types = list('♠◆♥♣')
nums  = list('A23456789')+['10']+list('JQK')        # 동적 + 정적 + 동적 구성
cards = [ i+j for i in types for j in nums ]        # 리스트 내포 
score_table = dict()
for key in nums:score_table[ key ] = nums.index( key ) +1
# 트럼프 K는 트럼프를 주어서 -5점이다.
score_table[ 'K' ]  = -5
# 함수 지향적 프로그램으로 작성 중에 추가된 변수
gameTitle           = None
player_name         = None
myTotalScore        = 0
game_level          = 1
isOneGaming         = True

# 3. 함수들 나열
# 함수 지향적 프로그램은 대부분 시작점이 존재한다.
# 시작점, 엔트리 포인트!!
def main():
    step1()
    # 아래의 gameTitle 과 setp2() 안의 gameTitle은 서로 다른 변수다.
    # 그냥 편의상 이름만 동일하게 사용했다. (이후 코드를 안 고치기 위해)
    gameTitle = step2()
    step3()
    step4()
    step5()
    step6()
    step7()

def step1():print( "Enjoy Custom Game world" )
def step2():
    while True:
        global gameTitle
        tmp = input("게임 제목을 입력하시오, 단 {}자 \이내로 입력 가능합니다. => ".format(GAME_TITLE_LEN_MAX)).strip()       
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>GAME_TITLE_LEN_MAX:
            print(str(GAME_TITLE_LEN_MAX) + "자가 초과되었습니다.") 
        else:
            gameTitle = tmp
            break
    print( 'gameTitle', gameTitle )
    # gameTitle은 절차적 코드에서는 그냥 사용해도 되나,
    # 함수지향적으로 전개해서 함수 내부로 가면 지역변수가 된다.
    # 함수 밖에서 사용이 불가함으로, 값을 리턴하거나
    # 아예 전역변수로 빼야한다.
def step3():
    while True:
        global player_name
        tmp = input("플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다\n=>" % PLAYER_NAME_LEN_MAX).strip()
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>PLAYER_NAME_LEN_MAX:
            print("%s자가 초과되었습니다." % PLAYER_NAME_LEN_MAX) 
        else:
            player_name = tmp
            break
def step4():
    while True:
        global game_level
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

def step5():    # IS_DEV_MODE
    print( '-'*20 )
    print( '현재 까지 입력 상황' )
    print( 'gameTitle',   gameTitle )
    print( 'player_name', player_name )
    print( 'game_level',  game_level )
    print( '-'*20 )
    
def step6():
    print('='*40)
    print('+{0:^38}+'.format(gameTitle))
    print('+{0:^38}+'.format( 'lv : %s' % game_level ))
    print('+{0:^34}+'.format( '"%s"의 연대기' % player_name ))
    print('='*40)
    print('{0:^40}'.format('press enter key!!'))
    while True:input();break   # 한 줄에 여러 문장을 기술 할 때는 구분자로 사용
    
def step7():
    global isOneGaming
    global myTotalScore
    
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


# 4. 프로그램 시작
#
    # __name__ : 이 변수는 그냥 사용이 가능하고 값이 프로그램을 구동하는 방식에 따라 2가지로 변경된다.
    # 프로그램을 구동하는 방식에 따라 2가지로 변경된다.
    # 1) python 파일명.py 로 구동하면 => __name__ => '__main__' 세팅된다.
    # 2) 누군가가 파일명.py를 가져와서 사용하면 => __name__ => '파일명.py'
    # print('__name__ :', __name__)
    # if __name__ == '__main__':

main()