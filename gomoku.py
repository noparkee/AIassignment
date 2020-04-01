# 0: 비어있음
# 1: 백색 돌
# -1: 흑색 돌
# (0, 0): 좌측 상단 꼭짓점
# (18, 18): 우측 하단 꼭짓점
# 입력은 'x y' 형식으로 x는 행, y는 열


from pprint import pprint
import sys
import time
import copy
from random import *

'''def vmax(pan):  # 흑
    for i in range(0, 19):
        cons = 0
        maxv = 0
        for j in range(0, 19):
            if pan[i][j] == -1:

                # 가로
                for x in range(0, 5):
                    if i - x >= 0:
                        if pan[i - x][j] == -1 or pan[i - x][j] == 0:  # 흑 또는 없음
                            cons += 1
                if cons >= 5:
                    maxv += 1
                cons = 0
                for x in range(0, 5):
                    if i + x < 19:
                        if pan[i + x][j] == -1 or pan[i + x][j] == 0:  # 흑 또는 없음
                            cons += 1
                if cons >= 5:
                    maxv += 1

                # 세로
                cons = 0
                for y in range(0, 5):
                    if j - y >= 0:
                        if pan[i][j - y] == -1 or pan[i][j - y] == 0:  # 흑 또는 없음
                            cons += 1
                if cons >= 5:
                    maxv += 1
                cons = 0
                for y in range(0, 5):
                    if j + y < 19:
                        if pan[i][j + y] == -1 or pan[i][j + y] == 0:  # 흑 또는 없음
                            cons += 1
                if cons >= 5:
                    maxv += 1

                # 대각선
                cons = 0
                for k in range(0, 5):  # 좌하향
                    if i - k >= 0 and j - k >= 0:
                        if pan[i - k][j - k] == -1 or pan[i - k][j - k] == 0:  # 흑 또는 없음
                            cons += 1
                if cons >= 5:
                    maxv += 1
                cons = 0
                for x in range(0, 5):  # 우상향
                    if i + k < 19 and j + k < 19:
                        if pan[i + k][j + k] == -1 or pan[i + k][j + k] == 0:  # 흑 또는 없음
                            cons += 1
                if cons >= 5:
                    maxv += 1

                cons = 0
                for k in range(0, 5):
                    if i + k < 19 and j - k >= 0:  # 우하향
                        if pan[i + k][j - k] == -1 or pan[i + k][j - k] == 0:  # 흑 또는 없음
                            cons += 1
                if cons >= 5:
                    maxv += 1
                cons = 0
                for x in range(0, 5):
                    if i - k > 0 and j + k < 19:  # 좌상향
                        if pan[i - k][j + k] == -1 or pan[i - k][j + k] == 0:  # 흑 또는 없음
                            cons += 1
                if cons >= 5:
                    maxv += 1

    return maxv'''

'''def vmin(state):  # 백
    for i in range(0, 19):
        cons = 0
        minv = 0
        for j in range(0, 19):
            if state[i][j] == 1:

                # 가로
                for x in range(0, 5):
                    if i - x >= 0:
                        if state[i - x][j] == 1 or state[i - x][j] == 0:  # 백 또는 없음
                            cons += 1
                if cons >= 5:
                    minv += 1
                cons = 0
                for x in range(0, 5):
                    if i + x < 19:
                        if state[i + x][j] == 1 or state[i + x][j] == 0:  # 백 또는 없음
                            cons += 1
                if cons >= 5:
                    minv += 1

                # 세로
                cons = 0
                for y in range(0, 5):
                    if j - y >= 0:
                        if state[i][j - y] == 1 or state[i][j - y] == 0:  # 백 또는 없음
                            cons += 1
                if cons >= 5:
                    minv += 1
                cons = 0
                for y in range(0, 5):
                    if j + y < 19:
                        if state[i][j + y] == 1 or state[i][j + y] == 0:  # 백 또는 없음
                            cons += 1
                if cons >= 5:
                    minv += 1

                # 대각선
                cons = 0
                for k in range(0, 5):  # 좌하향
                    if i - k >= 0 and j - k >= 0:
                        if state[i - k][j - k] == 1 or state[i - k][j - k] == 0:  # 백 또는 없음
                            cons += 1
                if cons >= 5:
                    minv += 1
                cons = 0
                for x in range(0, 5):  # 우상향
                    if i + k < 19 and j + k < 19:
                        if state[i + k][j + k] == 1 or state[i + k][j + k] == 0:  # 백 또는 없음
                            cons += 1
                if cons >= 5:
                    minv += 1

                cons = 0
                for k in range(0, 5):  # 우하향
                    if i + k < 19 and j - k >= 0:
                        if state[i + k][j - k] == 1 or state[i + k][j - k] == 0:  # 백 또는 없음
                            cons += 1
                if cons >= 5:
                    minv += 1
                cons = 0
                for x in range(0, 5):  # 좌상향
                    if i - k > 0 and j + k < 19:
                        if state[i - k][j + k] == 1 or state[i - k][j + k] == 0:  # 백 또는 없음
                            cons += 1
                if cons >= 5:
                    minv += 1

    return minv'''

def cons(state, c, num):       # c는 흑백 구분 용
    n = num-1
    x, y, z1, z2 = 0
    consx = 0
    consy = 0
    consz1 = 0      # 우하향
    consz2 = 0      # 좌상향

    for i in range(0, 19-n):
        for j in range(0, 19-n):
            if state[i][j] == c:
                for k in range(1, num):
                    if state[i][j+k] == c:
                        consx += 1
                    else:   # 연속이 끊겨
                        consx = 0
                    if state[i+k][j] == c:
                        consy += 1
                    else:
                        consy = 0
                    if state[i+k][j+k] == c:
                        consz1 += 1
                    else:
                        consz1 = 0

                    if consx == n:
                        x = 1
                    if consy == n:
                        y = 1
                    if consz1 == n:
                        z1 = 1

    for i in range(0, 19-n):
        for j in range(n, 19):
            if state[i][j] == c:
                for k in range(1, num):
                    if state[i+k][j+k] == c:
                        consz2 += 1
                    if consz2 == n:
                        z2 = 1

    return x, y, z1, z2


def numofop (state, i, j, c, consnum, ofde):       # c는 나의 부호 흑백 구분     ofde는 공격 수비 구분
    g = 0
    x, y, z1, z2 = cons(state, c, consnum)

    if consnum == 4 and ofde == 1:
        v1 = 1000
        v2 = 300
    if consnum == 3 and ofde == 1:
        v1 = 700
        v2 = 100
    if consnum == 2 and ofde == 1:
        v1 = 50
        v2 = 25

    if consnum == 4 and ofde == -1:
        v1 = 1000
        v2 = 1000
    if consnum == 3 and ofde == -1:
        v1 = 700
        v2 = 300
    if consnum == 2 and ofde == -1:
        v1 = 50
        v2 = 25

    if x == 1:  # 가로
        if j - 1 >= 0 and state[i][j - 1] == 0 and state[i][j + 4] == 0 and j + 4 < 19:  # 1) 양쪽 열린 연속 4
            g += v1
        elif j + 3 == 18 and state[i][j - 1] == 0 and i - 1 >= 0:
            g += v2
        elif j == 0 and state[i][j + 4] == 0 and j + 4 < 19:
            g += v2
        elif j - 1 >= 0 and state[i][j - 1] == -c and state[i][j + 4] == 0 and j + 4 < 19:
            g += v2
        elif j + 4 < 19 and state[i][j + 4] == -c and state[i][j - 1] == 0 and j - 1 >= 0:
            g += v2

    if y == 1:  # 세로
        if i - 1 >= 0 and state[i - 1][j] == 0 and state[i + 4][j] == 0 and i + 4 < 19:
            g += v1
        elif i == 0 and state[i + 4][j] == 0 and i + 4 < 19:
            g += v2
        elif i + 3 == 18 and state[i - 1][j] == 0 and i - 1 >= 0:
            g += v2
        elif i - 1 >= 0 and state[i - 1][j] == -c and state[i + 4][j] == 0 and i + 4 < 19:
            g += v2
        elif state[i - 1][j] == 0 and state[i + 4][j] == -c and i - 1 >= 0 and i + 4 < 19:
            g += v2

    if z1 == 1:  # 우하향
        if i - 1 >= 0 and j - 1 >= 0 and i + 4 < 19 and j + 4 < 19 and state[i - 1][j - 1] == 0 and state[i + 4][j + 4] == 0:
            g += v1
        elif i == 0 and j == 0 and state[i + 4][j + 4] == 0 and i + 4 < 19 and j + 4 < 19:
            g += v2
        elif i + 3 == 18 and j + 3 == 18 and state[i - 1][j - 1] == 0 and i - 1 >= 0 and j - 1 >= 0:
            g += v2
        elif state[i - 1][j - 1] == -c and state[i + 4][j + 4] == 0 and i - 1 >= 0 and j - 1 >= 0 and i + 4 < 19 and j + 4 < 19:
            g += v2
        elif state[i - 1][j - 1] == 0 and state[i + 4][j + 4] == -c and i - 1 >= 0 and j - 1 >= 0 and i + 4 < 19 and j + 4 < 19:
            g += v2

    if z2 == 1:  # 우상향
        if state[i + 4][j - 4] == 0 and state[i - 1][j + 1] == 0 and i + 4 < 19 and j - 4 >= 0 and i - 1 >= 0 and j + 1 < 19:
            g += v1
        elif i == 0 and j == 18 and state[i+4][j-4] == 0 and i+4 < 19 and j-4 >= 0:
            g += v2
        elif i+3 == 18 and j-3 == 0 and state[i-1][j+1] == 0 and i-1 >= 0 and j+1 < 19:
            g += v2
        elif state[i-1][j+1] == -c and state[i+4][j-4] == 0 and i-1 >= 0 and j+1 < 19 and i+4 < 19 and j-4 >= 0:
            g += v2
        elif state[i-1][j+1] == 0 and state[i+4][j-4] == -c and i-1 >= 0 and j+1 < 19 and i+4 < 19 and j-4 >= 0:
            g += v2

    return g


def vmax(state):
    g = 0
    s = 0
    for i in range(0, 19):
        for j in range(0, 19):
            # 공격 - 내 돌 보고
            g += numofop(state, i, j, -1, 4, 1)       # 1) 양쪽 열린 연속 4     # 4) 한쪽 열린 연속 4
            g += numofop(state, i, j, -1, 3, 1)       # 2) 양쪽 열린 연속 3     # 5) 한쪽 열린 연속 3

            if g == 0:
                g += numofop(state, i, j, -1, 2, 1)    # 6) 1~5 해당x > 연속 2
    # 3) _oo_o_ 양쪽 열린
    #  ) _oo_o / oo_o_ 한쪽 열린


    # 수비 - 상대 돌 보고
            s += numofop(state, i, j, -1, 4, -1)        # 1) 4개 연속
            s += numofop(state, i, j, -1, 4, -1)        # 2) 양쪽 열린 연속 3     # 4) 한쪽 열린 3

            if s == 0:
                s += numofop(state, i, j, -1, 2, -1)    # 6) 1~5 해당x > 연속 2
    # / oo_oo
    # 3) _oo_o_ 양쪽 열린
    #  ) _oo_o / oo_o_ 한쪽 열린
    # 5) oo__o 이런 형태

    maxv = g-s
    return maxv

def vmin(state):
    return minv

def evaluationfunction(state):
    maxv = vmax(state)
    minv = vmin(state)
    return maxv - minv  # 흑 - 백


def endgame(state):  # state가 아마도 pan으로 들어가겠지
    # 가로
    for i in range(0, 19):  # 행
        max = 0
        min = 0
        for j in range(0, 18):  # 열
            if state[i][j] == -1 and state[i][j + 1] == -1:
                max += 1
            elif state[i][j] == -1 and state[i][j + 1] != -1:
                max = 0
            if max == 4:
                return -1

            if state[i][j] == 1 and state[i][j + 1] == 1:
                min += 1
            elif state[i][j] == 1 and state[i][j + 1] != 1:
                min = 0
            if min == 4:
                return 1
    # 세로
    for j in range(0, 19):  # 열
        max = 0
        min = 0
        for i in range(0, 18):  # 행
            if state[i][j] == -1 and state[i + 1][j] == -1:
                max += 1
            elif state[i][j] == -1 and state[i + 1][j] != -1:
                max = 0
            if max == 4:
                return -1

            if state[i][j] == 1 and state[i + 1][j] == 1:
                min += 1
            elif state[i][j] == -1 and state[i + 1][j] != 1:
                min = 0
            if min == 4:
                return 1
    # 대각선
    # 하향    # 상향

    #무승부
    draw = 0
    for i in range(0, 19):
        for j in range(0, 19):
            if state[i][j] == 0:
                draw += 1
    if draw == 0:       # 위의 경우에는 해당되지 않으나 바둑판 위에 빈 곳이 없을 때
        return 2
    else:
        return 0    # 가로, 세로, 대각선 모두에 연속한 5개의 같은 색의 바둑알이 없는 경우
                    # 즉 endgame이 아닌 경우


def maxvalue(state, a, b, depth):
    if depth == 0 or endgame(state) != 0:       # terminal state or cut off
        return evaluationfunction(state)

    v = -sys.maxsize-1

    for i in range(0, 19):
        for j in range(0, 19):
            if state[i][j] == 0:  # 여기서 나중에 3*3 체크 처리 해줘야 할 듯
                state[i][j] = -1    # 현재 state에서 할 수 있는 action을 취한 결과 state (result)
                v = max(v, minvalue(state, a, b, depth - 1))
                state[i][j] = 0
                if v >= b:
                    return v
                a = max(a, v)
    return v


def minvalue(state, a, b, depth):
    if depth == 0 or endgame(state) != 0:
        return evaluationfunction(state)

    v = sys.maxsize
    for i in range(0, 19):
        for j in range(0, 19):
            if state[i][j] == 0:
                state[i][j] = 1     # (i, j)에 바둑돌을 올리는 action
                v = min(v, maxvalue(state, a, b, depth - 1))
                state[i][j] = 0
                if v <= a:
                    return v
                b = min(b, v)
    return v

def vvaluteaction(state, v):
    for i in range (0, 19):
        for j in range(0, 19):
            if state[i][j] == 0:
                state[i][j] = 1
                #pprint(state)
                if evaluationfunction(state) == v:
                    print(i, j)
                    return i, j
                state[i][j] = 0
#    return x, y

def alpabeta(state, player):  # player: AI가 max player인지 min player 인지
    depth = 1     # 342 이상되면 error
    tem = copy.deepcopy(state)

    if player == 1:  # 사용자가 흑, AI가 백 / 즉 AI가 min player
        for i in range(0, depth+1):  # 여기도 수정!!!!   >> 시간 제한
            v = minvalue(state, -sys.maxsize-1, sys.maxsize, i)  # v값을 가지는 action을 취해야함. 여기도 수정
            print(v)
            #pprint(state)
            #pprint(tem)
        x, y = vvaluteaction(tem, v)
        print(x, y)
        # r1 = randint(0, len(x)-1)
        # r2 = randint(0, len(y)-1)
        return x, y  # ?


    if player == 2:  # 사용자가 백, AI가 흑 / 즉 AI가 max player
        for i in range(0, depth + 1):
            v = maxvalue(state, -sys.maxsize-1, sys.maxsize, i)
        x, y = vvaluteaction(tem, v)
        return x, y


def playerturn(pan, c):  # 사용자 차례
    while True:
        p = str(input(">> "))
        x = int(p.split(' ')[0])
        y = int(p.split(' ')[1])
        if pan[x][y] == 0:
            if c == 1:
                pan[x][y] = -1
            elif c == 2:
                pan[x][y] = 1
            break
        else:
            print('이미 돌이 있는 곳입니다.')

    return pan  # 변경된 state return




pan = []
for i in range(0, 19):  # 오목판 초기화. 비어있는 상태
    hang = []  # 행
    for j in range(0, 19):
        hang.append(0)  # 비어있는 것 표현 위해 0
    pan.append(hang)  # 전체 리스트에 안쪽 리스트를 추가
# pan[0][9] = 1
# pprint(pan)

c = int(input("1. 흑돌\n2. 백돌\n>> "))
lmtime = float(input("원하는 Time Limit을 초 단위로 입력하세요\n>> "))
print("--- Game Start !!! ---")
if c == 1:  # 사용자가 흑, AI가 백
    '''while endgame(pan) == 0:
            playerturn(pan, c)
            pprint(pan)
            print('\n\n\n')
            alpabeta(pan, c)
            pprint(pan)
            print('\n\n\n')'''
    while True:
        playerturn(pan, c)
        #pprint(pan)
        if endgame(pan) != 0:
            break

        state = copy.deepcopy(pan)          # 깊은 복사
        x, y = alpabeta(state, c)
        pan[x][y] = 1
        #pprint(pan)
        if endgame(pan) != 0:
            break

    if endgame(pan) == 1:
        print("백의 승리")
    elif endgame(pan) == -1:
        print("흑의 승리")
    elif endgame(pan) == 2:
        print('무승부')

if c == 2:  # 사용자가 백, AI가 흑
    pan[9][9] = -1  # AI가 선일 때는 처음 두는 곳 고정

    while True:
        playerturn(pan, c)
        if endgame(pan) != 0:
            break
        state = copy.deepcopy(pan)
        x, y = alpabeta(state, c)
        pan[x][y] = 1
        if endgame(pan) != 0:
            break
    if endgame(pan) == 1:
        print("백의 승리")
    elif endgame(pan) == -1:
        print("흑의 승리")
    elif endgame(pan) == 2:
        print('무승부')

# time limit은 아래와 같이 구현하면 될 듯
'''t = time.time()     # 시작 시간
while True:
    if time.time() - t >= float(lmtime):        # 현재 시간 - 시작 시간이 limit을 넘어가면 종료
        break
'''
''' p = str(input(">> "))  # p를 띄어쓰기 단위로 나눠서 x좌표, y좌표 잡아서 pan 채우기
        if time.time() - t >= lmtime:  # 이 때 중간에 끊기지 않고 입력후에야 time out임을 알 수 있음.
            print("time out")
            break
        if p != "":
            x = p.split(' ')[0]
            y = p.split(' ')[1]
            if pan[int(x)][int(y)] == 0:
                pan[int(x)][int(y)] = -1
            else:
                print('이미 돌이 있는 곳입니다.')
            break'''
