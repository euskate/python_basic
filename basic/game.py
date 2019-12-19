# 환경변수 or 게임데이터 ->  프로그램에 영향을 미치는 고정값(임계값) 상수로 빼고
# 향후에는 *.py 바깥쪽으로 빼서 저장(file or DB or server)
# 고정값을 바깥으로 뺀다.
GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9

if True:
    # 절차적 프로그램 실습
    # 간단한 게임을 구현하여 
    # 긴 단위의 프로그램을 작성하고, 절차적 프로그램을 이해한다
    # 머드 게임 스타일로 터미널에서 입력하면서 게임을 진행
    # 목적, 파이썬 타입, 연산, 조건, 반복, 흐름제어등을 프로그램을 개발하면서 
    # 심화 학습한다
    # --------------------------------------------------------------------
    # step1 게임이 시작하면 "Enjoy Custom Game world"라는 문구를 출력한다
    # step2 
    #   2-1 "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구 출력
    #   2-2 사용자가 입력할때가 무제한으로 대기한다
    #   2-3 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!" 출력하고
    #       다시 입력 대기한다
    #   2-4 20자 이상 입력하면 "20자가 초과되었습니다." 출력하고, 다시 입력 
    #       대기한다   
    #   2-5 20자 이내로 입력하면 gameTitle라는 변수에 게임 제목을 담고 다음 
    #       3 단계로 진입한다
    # step3
    #   3-1 "플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
    #   3-2 입력에 대한 처리는 step2와 동일하다
    #   3-3 플레이어의 이름은 player_name이라는 변수에 담는다
    # step4
    #   4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다"
    #   4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
    #   4-3 게임 난이도는 game_level 이라는 변수에 담는다
    # ==================================================================

    # step1 게임이 시작하면 "Enjoy Custom Game world"라는 문구를 출력한다
    print( "Enjoy Custom Game world" )

    # step2 
    #   2-2 사용자가 입력할때가 무제한으로 대기한다
    while True: #반드시 내부에 break가 있어야 한다.

        #   2-1 "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구 출력
        #       -> 매번 입력을 대기할 때마다 해당 프롬프트 출력하겠다.
        # 사용자가 엔터키를 칠 때까지 코드를 블럭하고 있다.

        tmp = input('게임 제목을 입력하시오, 단 %s자 이내로 입력 가능합니다.\n > ' % GAME_TITLE_LEN_MAX).strip()
        # or tmp = input('게임 제목을 입력하시오, 단 {}자 이내로 입력 가능합니다. > '.format(GAME_TITLE_LEN_MAX)).strip()
        # or tmp = input('게임 제목을 입력하시오, 단' + GAME_TITLE_LEN_MAX + '자 이내로 입력 가능합니다. > ').strip()

        if not tmp:             #   2-3 아무것도 입력하지 않고 엔터를 치면, 
            # 스페이스바를 몇번 치고 엔터를 친 것도 같이 처리한다.
            # 2-3-1 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다
            print('정확하게 입력하세요!')
            pass
        elif len(tmp) > 20:     #   2-4 20자 이상 입력하면, 
            # 2-4-1 "20자가 초과되었습니다." 출력하고, 다시 입력 대기한다   
            print('%s자가 초과되었습니다.' % GAME_TITLE_LEN_MAX)
            pass
        else:                   #   2-5 20자 이내로 입력하면,
            # gameTitle라는 변수에 게임 제목을 담고 
            gameTitle = tmp
            # 다음 3 단계로 진입한다
            break
        pass

    # step3
    # gameTitle이 정의된 곳 -> while 안에 else 안에서 정의
    # while 밖에서도 사용이 가능하다?
    # 함수나 클래스 내부에서 정의된 변수가 아닌 변수들은 모두 전역변수이다.
    # 전역변수 : 어느 곳에서나 사용 가능하다. <- variable scope(범위)

    #   3-1 "플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
    #   3-2 입력에 대한 처리는 step2와 동일하다
    #   3-3 플레이어의 이름은 player_name이라는 변수에 담는다

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
    #   4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다"
    # tmp = input('게임 난이도를 입력하시오. ( {} ~ {} ) : '.format(GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
    tmp = input(f'게임 난이도를 입력하시오. ( {GAME_LEVEL_MIN} ~ {GAME_LEVEL_MAX} ) : ').strip()
    #   4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
    #       사용자가 넣을 수 있는 케이스를 고려하여 점점 범위가 줄어들게 배치(논리적 사고 익히기)
    #       공백입력, 정수가 될 수 없는 값, 1~9 이외의 값, 정확하게 넣을 경우
    if not tmp:
        print('정확하게 입력하세요!')
    elif not tmp.isdecimal():
        print('정수를 입력하세요')
    elif int(tmp) > GAME_LEVEL_MAX or int(tmp) < GAME_LEVEL_MIN:
        print('1~9 사이의 수를 입력하세요.')
    #   4-3 게임 난이도는 game_level 이라는 변수에 담는다
    else:
        game_level = tmp
        break
    # #################################################
    # if condition:   # 공백은 잡는다
    #     pass
    # elif condition: # 뭔가는 들었다 -> 정수가 안되면 컷
    #     continue
    #     pass
    # # 입력값의 정수변환
    # if condition:   # 1-9 이외값이면 컷
    #     pass
    # else:           # 정상값
    #     pass
    # elif
    # #################################################
    # if condition:   # 공백이면 컷
    #     pass
    # elif condition: # 정수 아니면 컷
    #     pass
    # else:           # 정수가 될 수 있는 놈들
    #     # 정수변환
    #     if condition:# 1-9가 아닌 값 컷
    #         pass
    #     else:       # 정확한 입력
    #         pass
    # #################################################
    # C style 
    # 계속 continue로 처음으로 보낸다.
        # if not tmp:              # 공백은 잡는다 컷
        #     print('정확하게입력하세요')
        #     continue
        # if not tmp.isnumeric():  # 뭔가는 들었다 -> 정수가 안되면 컷
        #     print('1-9까지 사이값으로 정확하게 입력하세요')
        #     continue
        # # 입력값의 정수변환
        # tmp = int(tmp)
        # if tmp>9 or tmp<1:       # 1-9 이외 값이면 컷
        #     print('1-9까지 사이값으로 정확하게 입력하세요')
        #     continue
        # game_level = tmp
        # break
    # 정상값
    # #################################################

    # # 긍정 상황을 잡아서처리
    #     try: # 오류가 발생하면 잡아서 처리 -> s/w가 다운되지 않는다:예외처리
    #         if 1<=int(tmp)<=9:
    #             game_level = tmp
    #             break
    #         else:
    #             print('1-9까지 사이값으로 정확하게 입력하세요')
    #     except Exception as e:
    #         print('1-9까지 사이값으로 정확하게 입력하세요')
    #         break

# step 5
      
        
print( '-'*20 )
print( 'gameTitle :', gameTitle )
print( 'player_name :', player_name )
print( 'game_level :', game_level )
print( '-'*20 )
