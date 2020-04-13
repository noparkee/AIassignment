# 0: 비어있음
# 1: 흑색 돌       max player
# 2: 백색 돌       min player
# pan은 실제 print하는데 사용, state는 연산에 사용 pan을 그대로 연산에 사용해버리면 변하면 안 되는 위치의 값이 바뀌거나 바뀌어야 하는 위치의 값이 변하지 않음.

from pprint import pprint
import sys
import copy
import re
import time


def garo(state):
    sum = 0

    for i in range(0, 19):
        phang = state[i]
        phang = list(map(str, phang))  # str로 바꾸기
        panstr = (''.join(phang))  # 문자열로 합치기

        sum += len(re.findall(r'[0][1][1][1][1][1][0]', panstr)) * 300000
        sum += len(re.findall(r'[2][1][1][1][1][1][0]', panstr)) * 300000
        sum += len(re.findall(r'[0][1][1][1][1][1][2]', panstr)) * 300000
        sum += len(re.findall(r'[2][1][1][1][1][1][2]', panstr)) * 300000  # 완전 승리조건

        sum += len(re.findall(r'[0][1][1][1][1][0]]', panstr)) * 200000
        sum += len(re.findall(r'[0][1][1][1][1]', panstr)) * 300
        sum += len(re.findall(r'[1][1][1][1][0]', panstr)) * 300
        sum += len(re.findall(r'[1][1][1][1]', panstr)) * 500
        sum += len(re.findall(r'[1][1][1][0][1]', panstr)) * 1000
        sum += len(re.findall(r'[1][1][0][1][1]', panstr)) * 1000
        sum += len(re.findall(r'[1][0][1][1][1]', panstr)) * 1000
        sum -= len(re.findall(r'[1][1][1][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][1][2]', panstr)) * 100

        sum += len(re.findall(r'[0][1][1][1][0]', panstr)) * 500
        sum += len(re.findall(r'[0][1][1][1]', panstr)) * 200
        sum += len(re.findall(r'[1][1][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][1][1]', panstr)) * 300
        sum -= len(re.findall(r'[1][1][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][2]', panstr)) * 100

        sum += len(re.findall(r'[0][1][1][0][1][0]', panstr)) * 300
        sum += len(re.findall(r'[0][1][0][1][1][0]', panstr)) * 300
        sum += len(re.findall(r'[0][1][1][0][1]', panstr)) * 200
        sum += len(re.findall(r'[0][1][0][1][1]', panstr)) * 200
        sum += len(re.findall(r'[1][1][0][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][0][1][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][1][0][1]', panstr)) * 300
        sum += len(re.findall(r'[1][0][1][1]', panstr)) * 300
        sum -= len(re.findall(r'[2][1][1][0][1]', panstr)) * 50
        sum -= len(re.findall(r'[1][1][0][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][0][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[1][0][1][1][2]', panstr)) * 50

        sum += len(re.findall(r'[1][1]', panstr)) * 5
        sum -= len(re.findall(r'[1][2]', panstr)) * 1
        sum -= len(re.findall(r'[2][1]', panstr)) * 1
        sum -= len(re.findall(r'[2][2]', panstr)) * 1

        sum -= len(re.findall(r'[0][2][2][2][2][2][0]', panstr)) * 150000
        sum -= len(re.findall(r'[0][2][2][2][2][2][1]', panstr)) * 150000
        sum -= len(re.findall(r'[1][2][2][2][2][2][0]', panstr)) * 150000
        sum -= len(re.findall(r'[1][2][2][2][2][2][1]', panstr)) * 150000  # 백의 완전 승리 조건

        sum -= len(re.findall(r'[0][2][2][2][2][0]', panstr)) * 100000  # 흑의 수비 & 백의 공격
        sum -= len(re.findall(r'[2][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][2][0][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][0][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][0][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][0][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][0][2][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][0][2]', panstr)) * 50
        sum -= len(re.findall(r'[0][2][0][2][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][2][0][2][0]', panstr)) * 50
        sum -= len(re.findall(r'[2][0][2][2][0]', panstr)) * 50

    return sum


def sero(state):        # 세로
    sum = 0
    pyeol = []
    
    for j in range(0, 19):
        pyeol.clear()
        for i in range(0, 19):
            pyeol.append(state[i][j])

        pyeol = list(map(str, pyeol))
        panstr = (''.join(pyeol))

        sum += len(re.findall(r'[0][1][1][1][1][1][0]', panstr)) * 300000
        sum += len(re.findall(r'[2][1][1][1][1][1][0]', panstr)) * 300000
        sum += len(re.findall(r'[0][1][1][1][1][1][2]', panstr)) * 300000
        sum += len(re.findall(r'[2][1][1][1][1][1][2]', panstr)) * 300000  # 완전 승리조건

        sum += len(re.findall(r'[0][1][1][1][1][0]]', panstr)) * 200000
        sum += len(re.findall(r'[0][1][1][1][1]', panstr)) * 300
        sum += len(re.findall(r'[1][1][1][1][0]', panstr)) * 300
        sum += len(re.findall(r'[1][1][1][1]', panstr)) * 500
        sum += len(re.findall(r'[1][1][1][0][1]', panstr)) * 1000
        sum += len(re.findall(r'[1][1][0][1][1]', panstr)) * 1000
        sum += len(re.findall(r'[1][0][1][1][1]', panstr)) * 1000
        sum -= len(re.findall(r'[1][1][1][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][1][2]', panstr)) * 100

        sum += len(re.findall(r'[0][1][1][1][0]', panstr)) * 500
        sum += len(re.findall(r'[0][1][1][1]', panstr)) * 200
        sum += len(re.findall(r'[1][1][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][1][1]', panstr)) * 300
        sum -= len(re.findall(r'[1][1][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][2]', panstr)) * 100

        sum += len(re.findall(r'[0][1][1][0][1][0]', panstr)) * 300
        sum += len(re.findall(r'[0][1][0][1][1][0]', panstr)) * 300
        sum += len(re.findall(r'[0][1][1][0][1]', panstr)) * 200
        sum += len(re.findall(r'[0][1][0][1][1]', panstr)) * 200
        sum += len(re.findall(r'[1][1][0][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][0][1][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][1][0][1]', panstr)) * 300
        sum += len(re.findall(r'[1][0][1][1]', panstr)) * 300
        sum -= len(re.findall(r'[2][1][1][0][1]', panstr)) * 50
        sum -= len(re.findall(r'[1][1][0][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][0][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[1][0][1][1][2]', panstr)) * 50

        sum += len(re.findall(r'[1][1]', panstr)) * 5
        sum -= len(re.findall(r'[1][2]', panstr)) * 1
        sum -= len(re.findall(r'[2][1]', panstr)) * 1
        sum -= len(re.findall(r'[2][2]', panstr)) * 1

        sum -= len(re.findall(r'[0][2][2][2][2][2][0]', panstr)) * 150000
        sum -= len(re.findall(r'[0][2][2][2][2][2][1]', panstr)) * 150000
        sum -= len(re.findall(r'[1][2][2][2][2][2][0]', panstr)) * 150000
        sum -= len(re.findall(r'[1][2][2][2][2][2][1]', panstr)) * 150000  # 백의 완전 승리 조건

        sum -= len(re.findall(r'[0][2][2][2][2][0]', panstr)) * 100000  # 흑의 수비 & 백의 공격
        sum -= len(re.findall(r'[2][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][2][0][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][0][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][0][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][0][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][0][2][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][0][2]', panstr)) * 50
        sum -= len(re.findall(r'[0][2][0][2][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][2][0][2][0]', panstr)) * 50
        sum -= len(re.findall(r'[2][0][2][2][0]', panstr)) * 50

    return sum


def daegack1(state):        # 좌하향
    sum = 0
    pdaegack = []

    for k in range(0, 37):      # 대각
        pdaegack.clear()
        for i in range(0, 19):      # 행
            j = k-i                 # 열
            if j >= 0 and j < 19:
                pdaegack.append(state[i][j])

        pdaegack = list(map(str, pdaegack))
        panstr = (''.join(pdaegack))

        sum += len(re.findall(r'[0][1][1][1][1][1][0]', panstr)) * 300000
        sum += len(re.findall(r'[2][1][1][1][1][1][0]', panstr)) * 300000
        sum += len(re.findall(r'[0][1][1][1][1][1][2]', panstr)) * 300000
        sum += len(re.findall(r'[2][1][1][1][1][1][2]', panstr)) * 300000  # 완전 승리조건

        sum += len(re.findall(r'[0][1][1][1][1][0]]', panstr)) * 200000
        sum += len(re.findall(r'[0][1][1][1][1]', panstr)) * 300
        sum += len(re.findall(r'[1][1][1][1][0]', panstr)) * 300
        sum += len(re.findall(r'[1][1][1][1]', panstr)) * 500
        sum += len(re.findall(r'[1][1][1][0][1]', panstr)) * 1000
        sum += len(re.findall(r'[1][1][0][1][1]', panstr)) * 1000
        sum += len(re.findall(r'[1][0][1][1][1]', panstr)) * 1000
        sum -= len(re.findall(r'[1][1][1][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][1][2]', panstr)) * 100

        sum += len(re.findall(r'[0][1][1][1][0]', panstr)) * 500
        sum += len(re.findall(r'[0][1][1][1]', panstr)) * 200
        sum += len(re.findall(r'[1][1][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][1][1]', panstr)) * 300
        sum -= len(re.findall(r'[1][1][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][2]', panstr)) * 100

        sum += len(re.findall(r'[0][1][1][0][1][0]', panstr)) * 300
        sum += len(re.findall(r'[0][1][0][1][1][0]', panstr)) * 300
        sum += len(re.findall(r'[0][1][1][0][1]', panstr)) * 200
        sum += len(re.findall(r'[0][1][0][1][1]', panstr)) * 200
        sum += len(re.findall(r'[1][1][0][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][0][1][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][1][0][1]', panstr)) * 300
        sum += len(re.findall(r'[1][0][1][1]', panstr)) * 300
        sum -= len(re.findall(r'[2][1][1][0][1]', panstr)) * 50
        sum -= len(re.findall(r'[1][1][0][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][0][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[1][0][1][1][2]', panstr)) * 50

        sum += len(re.findall(r'[1][1]', panstr)) * 5
        sum -= len(re.findall(r'[1][2]', panstr)) * 1
        sum -= len(re.findall(r'[2][1]', panstr)) * 1
        sum -= len(re.findall(r'[2][2]', panstr)) * 1

        sum -= len(re.findall(r'[0][2][2][2][2][2][0]', panstr)) * 150000
        sum -= len(re.findall(r'[0][2][2][2][2][2][1]', panstr)) * 150000
        sum -= len(re.findall(r'[1][2][2][2][2][2][0]', panstr)) * 150000
        sum -= len(re.findall(r'[1][2][2][2][2][2][1]', panstr)) * 150000  # 백의 완전 승리 조건

        sum -= len(re.findall(r'[0][2][2][2][2][0]', panstr)) * 100000  # 흑의 수비 & 백의 공격
        sum -= len(re.findall(r'[2][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][2][0][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][0][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][0][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][0][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][0][2][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][0][2]', panstr)) * 50
        sum -= len(re.findall(r'[0][2][0][2][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][2][0][2][0]', panstr)) * 50
        sum -= len(re.findall(r'[2][0][2][2][0]', panstr)) * 50

    return sum


def daegack2(state):        # 우하향
    sum = 0
    pdaegack = []

    for k in range(0, 37):      # 대각
        pdaegack.clear()
        for i in range(0, 19):      # 행
            j = 18 - (k-i)                 # 열
            if j >= 0 and j < 19:
                pdaegack.append(state[i][j])

        pdaegack = list(map(str, pdaegack))
        panstr = (''.join(pdaegack))

        sum += len(re.findall(r'[0][1][1][1][1][1][0]', panstr)) * 300000
        sum += len(re.findall(r'[2][1][1][1][1][1][0]', panstr)) * 300000
        sum += len(re.findall(r'[0][1][1][1][1][1][2]', panstr)) * 300000
        sum += len(re.findall(r'[2][1][1][1][1][1][2]', panstr)) * 300000  # 완전 승리조건

        sum += len(re.findall(r'[0][1][1][1][1][0]]', panstr)) * 200000
        sum += len(re.findall(r'[0][1][1][1][1]', panstr)) * 300
        sum += len(re.findall(r'[1][1][1][1][0]', panstr)) * 300
        sum += len(re.findall(r'[1][1][1][1]', panstr)) * 500
        sum += len(re.findall(r'[1][1][1][0][1]', panstr)) * 1000
        sum += len(re.findall(r'[1][1][0][1][1]', panstr)) * 1000
        sum += len(re.findall(r'[1][0][1][1][1]', panstr)) * 1000
        sum -= len(re.findall(r'[1][1][1][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][1][2]', panstr)) * 100

        sum += len(re.findall(r'[0][1][1][1][0]', panstr)) * 500
        sum += len(re.findall(r'[0][1][1][1]', panstr)) * 200
        sum += len(re.findall(r'[1][1][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][1][1]', panstr)) * 300
        sum -= len(re.findall(r'[1][1][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][1][1][2]', panstr)) * 100

        sum += len(re.findall(r'[0][1][1][0][1][0]', panstr)) * 300
        sum += len(re.findall(r'[0][1][0][1][1][0]', panstr)) * 300
        sum += len(re.findall(r'[0][1][1][0][1]', panstr)) * 200
        sum += len(re.findall(r'[0][1][0][1][1]', panstr)) * 200
        sum += len(re.findall(r'[1][1][0][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][0][1][1][0]', panstr)) * 200
        sum += len(re.findall(r'[1][1][0][1]', panstr)) * 300
        sum += len(re.findall(r'[1][0][1][1]', panstr)) * 300
        sum -= len(re.findall(r'[2][1][1][0][1]', panstr)) * 50
        sum -= len(re.findall(r'[1][1][0][1][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][1][0][1][1]', panstr)) * 50
        sum -= len(re.findall(r'[1][0][1][1][2]', panstr)) * 50

        sum += len(re.findall(r'[1][1]', panstr)) * 5
        sum -= len(re.findall(r'[1][2]', panstr)) * 1
        sum -= len(re.findall(r'[2][1]', panstr)) * 1
        sum -= len(re.findall(r'[2][2]', panstr)) * 1

        sum -= len(re.findall(r'[0][2][2][2][2][2][0]', panstr)) * 150000
        sum -= len(re.findall(r'[0][2][2][2][2][2][1]', panstr)) * 150000
        sum -= len(re.findall(r'[1][2][2][2][2][2][0]', panstr)) * 150000
        sum -= len(re.findall(r'[1][2][2][2][2][2][1]', panstr)) * 150000  # 백의 완전 승리 조건

        sum -= len(re.findall(r'[0][2][2][2][2][0]', panstr)) * 100000  # 흑의 수비 & 백의 공격
        sum -= len(re.findall(r'[2][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][2][0][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][0][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][0][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][2]', panstr)) * 100
        sum -= len(re.findall(r'[2][2][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][0][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][0][2][2][0]', panstr)) * 100
        sum -= len(re.findall(r'[0][2][2][0][2]', panstr)) * 50
        sum -= len(re.findall(r'[0][2][0][2][2]', panstr)) * 50
        sum -= len(re.findall(r'[2][2][0][2][0]', panstr)) * 50
        sum -= len(re.findall(r'[2][0][2][2][0]', panstr)) * 50

    return sum


def evaluationfunction(state):
    return garo(state) + sero(state) + daegack1(state) + daegack2(state)


def endgame(state):         # 장목은 승리로 보지 않음
    for i in range(0, 19):      # 가로
        phang = state[i]
        phang = list(map(str, phang))
        panstr = (''.join(phang))

        if len(re.findall(r'[0][1][1][1][1][1][0]', panstr)) > 0 or len(re.findall(r'[0][1][1][1][1][1][2]', panstr)) > 0\
                or len(re.findall(r'[2][1][1][1][1][1][0]', panstr)) > 0 or len(re.findall(r'[2][1][1][1][1][1][2]', panstr)) > 0:
            return 1
        elif len(re.findall(r'[0][2][2][2][2][2][0]', panstr)) > 0 or len(re.findall(r'[0][2][2][2][2][2][1]', panstr)) > 0\
                or len(re.findall(r'[1][2][2][2][2][2][0]', panstr)) > 0 or len(re.findall(r'[1][2][2][2][2][2][1]', panstr)) > 0:
            return 2

    pyeol = []
    for j in range(0, 19):      # 세로
        pyeol.clear()
        for i in range(0, 19):
            pyeol.append(state[i][j])       # 하나의 열을 다 추가한거

        pyeol = list(map(str, pyeol))
        panstr = (''.join(pyeol))

        if len(re.findall(r'[0][1][1][1][1][1][0]', panstr)) > 0 or len(re.findall(r'[0][1][1][1][1][1][2]', panstr)) > 0 \
                or len(re.findall(r'[2][1][1][1][1][1][0]', panstr)) > 0 or len(re.findall(r'[2][1][1][1][1][1][2]', panstr)) > 0:
            return 1
        elif len(re.findall(r'[0][2][2][2][2][2][0]', panstr)) > 0 or len(re.findall(r'[0][2][2][2][2][2][1]', panstr)) > 0 \
                or len(re.findall(r'[1][2][2][2][2][2][0]', panstr)) > 0 or len(re.findall(r'[1][2][2][2][2][2][1]', panstr)) > 0:
            return 2

    pdaegack1 = []
    for k in range(0, 37):      # 좌하향
        pdaegack1.clear()
        for i in range(0, 19):      # 행
            j = k-i                 # 열
            if j >= 0 and j < 19:
                pdaegack1.append(state[i][j])

        pdaegack1 = list(map(str, pdaegack1))
        panstr = (''.join(pdaegack1))

        if len(re.findall(r'[0][1][1][1][1][1][0]', panstr)) > 0 or len(re.findall(r'[0][1][1][1][1][1][2]', panstr)) > 0 \
                or len(re.findall(r'[2][1][1][1][1][1][0]', panstr)) > 0 or len(re.findall(r'[2][1][1][1][1][1][2]', panstr)) > 0:
            return 1
        elif len(re.findall(r'[0][2][2][2][2][2][0]', panstr)) > 0 or len(re.findall(r'[0][2][2][2][2][2][1]', panstr)) > 0 \
                or len(re.findall(r'[1][2][2][2][2][2][0]', panstr)) > 0 or len(re.findall(r'[1][2][2][2][2][2][1]', panstr)) > 0:
            return 2

    pdaegack2 = []
    for k in range(0, 37):      # 우하향
        pdaegack2.clear()
        for i in range(0, 19):      # 행
            j = 18 - (k-i)                 # 열
            if j >= 0 and j < 19:
                pdaegack2.append(state[i][j])

        pdaegack2 = list(map(str, pdaegack2))
        panstr = (''.join(pdaegack2))

        if len(re.findall(r'[0][1][1][1][1][1][0]', panstr)) > 0 or len(re.findall(r'[0][1][1][1][1][1][2]', panstr)) > 0 \
                or len(re.findall(r'[2][1][1][1][1][1][0]', panstr)) > 0 or len(re.findall(r'[2][1][1][1][1][1][2]', panstr)) > 0:
            return 1
        elif len(re.findall(r'[0][2][2][2][2][2][0]', panstr)) > 0 or len(re.findall(r'[0][2][2][2][2][2][1]', panstr)) > 0 \
                or len(re.findall(r'[1][2][2][2][2][2][0]', panstr)) > 0 or len(re.findall(r'[1][2][2][2][2][2][1]', panstr)) > 0:
            return 2

    return 0


def maxvalue(state, a, b, depth, end, out):
    if depth == 0 or endgame(state) != 0 or end - time.time() <= 3.5:       # terminal state or cut off
        k = evaluationfunction(state)
        return k, 100, 100

    ran = setrange(listouter)
    print(ran[0], ran[1], ran[2], ran[3])
    v = -sys.maxsize-1
    for i in range(ran[0], ran[1]):
        for j in range(ran[2], ran[3]):
            if state[i][j] == 0 and samsamfunction(state, i, j, 1) != 33:
                state[i][j] = 1    # 현재 state에서 할 수 있는 action을 취한 결과 state (result)

                minv = minvalue(state, a, b, depth - 1, end, out)
                if v <= minv[0]:
                    v = minv[0]
                    x = i
                    y = j
                state[i][j] = 0

                if v >= b:
                    return v, i, j
                a = max(a, v)
    return v, x, y


def minvalue(state, a, b, depth, end, out):       # min
    if depth == 0 or endgame(state) != 0 or end - time.time() <= 3.5:
        k = evaluationfunction(state)
        return k, 100, 100

    ran = setrange(listouter)

    v = sys.maxsize
    for i in range(ran[0], ran[1]):
        for j in range(ran[2], ran[3]):
            if state[i][j] == 0 and samsamfunction(state, i, j, 2) != 33:           #삼삼 이렇게 넣어도 되는지도 더 고민해보자
                state[i][j] = 2     # (i, j)에 바둑돌을 올리는 action

                maxv = maxvalue(state, a, b, depth - 1, end, out)
                if v >= maxv[0]:
                    v = maxv[0]
                    x = i
                    y = j
                state[i][j] = 0

                if v <= a:
                    return v, i, j
                b = min(b, v)
    return v, x, y


def alphabeta(state, player, t):  # player: AI가 max player인지 min player 인지
    depth = 2     # iterative 하게 수정해야함
    if player == 1:  # 사용자가 흑, AI가 백 / 즉 AI가 min player
        start = time.time()
        end = start + t
        for i in range(1, 19*19):  # 여기도 수정!!!!   >> 시간 제한
            #print(i)
            v = minvalue(state, -sys.maxsize-1, sys.maxsize, i, end, t)
            if end - time.time() <= 3.5:
                break

        print(int(time.time()-start))
        print(v[1], v[2])
        return v[1], v[2]

    if player == 2:  # 사용자가 백, AI가 흑 / 즉 AI가 max player
        start = time.time()
        end = start + t
        for i in range(0, 19*19):
            v = maxvalue(state, -sys.maxsize-1, sys.maxsize, i, start+t, t)
            if end - time.time() <= 3.5:
                break

        return v[1], v[2]


def samsamfunction(state, i, j, player):        # x하고 y는 각각 행, 열  player는 이제 수를 둘 player
    sam = 0
    samg = []
    sams = []
    samd = []
    samdd = []

    if state[i][j] == 0:
        state[i][j] = c
        # 이제 여기는 -0-00- / -00-0- 이런 꼴 넣어야하는데
        if i - 1 >= 0 and i + 4 <= 18 and state[i - 1][j] == 0 and state[i][j] == c and state[i + 1][j] == 0 and state[i + 2][j] == c and \
                state[i + 3][j] == c and state[i + 4][j] == 0:
            sam += 1
        if i - 1 >= 0 and i + 4 <= 18 and state[i - 1][j] == 0 and state[i][j] == c and state[i + 1][j] == c and state[i + 2][j] == 0 and \
                state[i + 3][j] == c and state[i + 4][j] == 0:
            sam += 1
        if i - 2 >= 0 and i + 3 <= 18 and state[i - 2][j] == 0 and state[i - 1][j] == c and state[i][j] == c and state[i + 1][j] == 0 and \
                state[i + 2][j] == c and state[i + 3][j] == 0:
            sam += 1
        if i - 3 >= 0 and i + 2 <= 18 and state[i - 3][j] == 0 and state[i - 2][j] == c and state[i - 1][j] == 0 and state[i][j] == c and \
                state[i + 1][j] == c and state[i + 2][j] == 0:
            sam += 1
        if i - 4 >= 0 and i + 1 <= 18 and state[i - 4][j] == 0 and state[i - 3][j] == c and state[i - 2][j] == 0 and state[i - 1][j] == c and \
                state[i][j] == c and state[i + 1][j] == 0:
            sam += 1
        if i - 4 >= 0 and i + 1 <= 18 and state[i - 4][j] == 0 and state[i - 3][j] == c and state[i - 2][j] == c and state[i - 1][j] == 0 and \
                state[i][j] == c and state[i + 1][j] == 0:
            sam += 1

        if j - 1 >= 0 and j + 4 <= 18 and state[i][j - 1] == 0 and state[i][j] == c and state[i][j + 1] == 0 and state[i][j + 2] == c and state[i][
            j + 3] == c and state[i][j + 4] == 0:
            sam += 1
        if j - 1 >= 0 and j + 4 <= 18 and state[i][j - 1] == 0 and state[i][j] == c and state[i][j + 1] == c and state[i][j + 2] == 0 and state[i][
            j + 3] == c and state[i][j + 4] == 0:
            sam += 1
        if j - 2 >= 0 and j + 3 <= 18 and state[i][j - 2] == 0 and state[i][j - 1] == c and state[i][j] == c and state[i][j + 1] == 0 and state[i][
            j + 2] == c and state[i][j + 3] == 0:
            sam += 1
        if j - 3 >= 0 and j + 2 <= 18 and state[i][j - 3] == 0 and state[i][j - 2] == c and state[i][j - 1] == 0 and state[i][j] == c and state[i][
            j + 1] == c and state[i][j + 2] == 0:
            sam += 1
        if j - 4 >= 0 and j + 1 <= 18 and state[i][j - 4] == 0 and state[i][j - 3] == c and state[i][j - 2] == 0 and state[i][j - 1] == c and \
                state[i][j] == c and state[i][j + 1] == 0:
            sam += 1
        if j - 4 >= 0 and j + 1 <= 18 and state[i][j - 4] == 0 and state[i][j - 3] == c and state[i][j - 2] == c and state[i][j - 1] == 0 and \
                state[i][j] == c and state[i][j + 1] == 0:
            sam += 1

        if i - 1 >= 0 and i + 4 <= 18 and j-1 >= 0 and j+4 <= 18 and state[i - 1][j - 1] == 0 and state[i][j] == c and state[i + 1][j + 1] == 0 and state[i + 2][j + 1] == c and \
                state[i + 3][j+3] == c and state[i + 4][j+4] == 0:
            sam += 1
        if i - 1 >= 0 and i + 4 <= 18 and j-1 >= 0 and j+4 <= 18 and state[i - 1][j-1] == 0 and state[i][j] == c and state[i + 1][j+1] == c and state[i + 2][j+2] == 0 and \
                state[i + 3][j+3] == c and state[i + 4][j+4] == 0:
            sam += 1
        if i - 2 >= 0 and i + 3 <= 18 and j-2 >= 0 and j+3 <= 18 and state[i - 2][j-2] == 0 and state[i - 1][j-1] == c and state[i][j] == c and state[i + 1][j+1] == 0 and \
                state[i + 2][j+2] == c and state[i + 3][j+3] == 0:
            sam += 1
        if i - 3 >= 0 and i + 2 <= 18 and j-3 >= 0 and j+2 <= 18 and state[i - 3][j-3] == 0 and state[i - 2][j-2] == c and state[i - 1][j-1] == 0 and state[i][j] == c and \
                state[i + 1][j+1] == c and state[i + 2][j+2] == 0:
            sam += 1
        if i - 4 >= 0 and i + 1 <= 18 and j-4 >= 0 and j+1 <= 18 and state[i - 4][j-4] == 0 and state[i - 3][j-3] == c and state[i - 2][j-2] == 0 and state[i - 1][j-1] == c and \
                state[i][j] == c and state[i + 1][j+1] == 0:
            sam += 1
        if i - 4 >= 0 and i + 1 <= 18 and j-4 >= 0 and j+1 <= 18 and state[i - 4][j-4] == 0 and state[i - 3][j-3] == c and state[i - 2][j-2] == c and state[i - 1][j-1] == 0 and \
                state[i][j] == c and state[i + 1][j+1] == 0:
            sam += 1

        if i - 1 >= 0 and i + 4 <= 18 and j+1 <= 18 and j-4 >= 0 and state[i - 1][j + 1] == 0 and state[i][j] == c and state[i + 1][j - 1] == 0 and state[i + 2][j - 1] == c and \
                state[i + 3][j-3] == c and state[i + 4][j-4] == 0:
            sam += 1
        if i - 1 >= 0 and i + 4 <= 18 and j+1 <= 18 and j-4 >= 0 and state[i - 1][j+1] == 0 and state[i][j] == c and state[i + 1][j-1] == c and state[i + 2][j-2] == 0 and \
                state[i + 3][j-3] == c and state[i + 4][j-4] == 0:
            sam += 1
        if i - 2 >= 0 and i + 3 <= 18 and j+2 <= 18 and j-3 >= 0 and state[i - 2][j+2] == 0 and state[i - 1][j+1] == c and state[i][j] == c and state[i + 1][j-1] == 0 and \
                state[i + 2][j-2] == c and state[i + 3][j-3] == 0:
            sam += 1
        if i - 3 >= 0 and i + 2 <= 18 and j+3 <= 18 and j-2 >= 0 and state[i - 3][j+3] == 0 and state[i - 2][j+2] == c and state[i - 1][j+1] == 0 and state[i][j] == c and \
                state[i + 1][j-1] == c and state[i + 2][j-2] == 0:
            sam += 1
        if i - 4 >= 0 and i + 1 <= 18 and j+4 <= 18 and j-1 >= 0 and state[i - 4][j+4] == 0 and state[i - 3][j+3] == c and state[i - 2][j+2] == 0 and state[i - 1][j+1] == c and \
                state[i][j] == c and state[i + 1][j-1] == 0:
            sam += 1
        if i - 4 >= 0 and i + 1 <= 18 and j+4 <= 18 and j-1 >= 0 and state[i - 4][j+4] == 0 and state[i - 3][j+3] == c and state[i - 2][j+2] == c and state[i - 1][j+1] == 0 and \
                state[i][j] == c and state[i + 1][j-1] == 0 :
            sam += 1
        state[i][j] = 0     # 다시 원래대로 되돌리기

        if player == 1:
            state[i][j] = 1
            for k in range(-1, 4):  # 가로 -000-- / --000-
                if 0 <= j + k <= 18:
                    samg.append(state[i][j + k])
            samg = list(map(str, samg))
            samgstr = (''.join(samg))
            if len(re.findall(r'[0][1][1][1][0]', samgstr)) > 0:
                if j + 4 <= 18 and state[i][j + 4] == 0:
                    sam += 1
                elif j - 2 >= 0 and state[i][j - 2] == 0:
                    sam += 1
            samg.clear()

            for k in range(-2, 3):
                if 0 <= j + k <= 18:
                    samg.append(state[i][j + k])
            samg = list(map(str, samg))
            samgstr = (''.join(samg))
            if len(re.findall(r'[0][1][1][1][0]', samgstr)) > 0:
                if j + 3 <= 18 and state[i][j + 3] == 0:
                    sam += 1
                elif j - 3 >= 0 and state[i][j - 3] == 0:
                    sam += 1
            samg.clear()

            for k in range(-3, 2):
                if 0 <= j + k <= 18:
                    samg.append(state[i][j + k])
            samg = list(map(str, samg))
            samgstr = (''.join(samg))
            if len(re.findall(r'[0][1][1][1][0]', samgstr)) > 0:
                if j + 2 <= 18 and state[i][j + 2] == 0:
                    sam += 1
                elif j - 4 >= 0 and state[i][j - 4] == 0:
                    sam += 1
            samg.clear()

            for k in range(-1, 4):  # 세로 -000-- / --000-
                if 0 <= i + k <= 18:
                    sams.append(state[i + k][j])
            sams = list(map(str, sams))
            samsstr = (''.join(sams))
            if len(re.findall(r'[0][1][1][1][0]', samsstr)) > 0:
                if i + 4 <= 18 and state[i + 4][j] == 0:
                    sam += 1
                elif i - 2 >= 0 and state[i - 2][j] == 0:
                    sam += 1
            sams.clear()

            for k in range(-2, 3):
                if 0 <= i + k <= 18:
                    sams.append(state[i + k][j])
            sams = list(map(str, sams))
            samsstr = (''.join(sams))
            if len(re.findall(r'[0][1][1][1][0]', samsstr)) > 0:
                if i + 3 <= 18 and state[i + 3][j] == 0:
                    sam += 1
                elif i - 3 >= 0 and state[i - 3][j] == 0:
                    sam += 1
            sams.clear()

            for k in range(-3, 2):
                if 0 <= i + k <= 18:
                    sams.append(state[i + k][j])
            sams = list(map(str, sams))
            samsstr = (''.join(sams))
            if len(re.findall(r'[0][1][1][1][0]', samsstr)) > 0:
                if i + 2 <= 18 and state[i + 2][j] == 0:
                    sam += 1
                elif i - 4 >= 0 and state[i - 4][j] == 0:
                    sam += 1
            sams.clear()

            for k in range(-1, 4):  # 대각 좌하향 -000-- / --000-
                if 0 <= i + k <= 18 and 0 <= j - k <= 18:
                    samd.append(state[i + k][j - k])
            samd = list(map(str, samd))
            samdstr = (''.join(samd))
            if len(re.findall(r'[0][1][1][1][0]', samdstr)) > 0:
                if i + 4 <= 18 and j - 4 >= 0 and state[i + 4][j - 4] == 0:
                    sam += 1
                elif i - 2 >= 0 and j + 2 <= 18 and state[i - 2][j + 2] == 0:
                    sam += 1
            samd.clear()

            for k in range(-2, 3):
                if 0 <= i + k <= 18 and 0 <= j - k <= 18:
                    samd.append(state[i + k][j - k])
            samd = list(map(str, samd))
            samdstr = (''.join(samd))
            if len(re.findall(r'[0][1][1][1][0]', samdstr)) > 0:
                if i + 3 <= 18 and j - 3 >= 0 and state[i + 3][j - 3] == 0:
                    sam += 1
                elif i - 3 >= 0 and j + 3 <= 18 and state[i - 3][j + 3] == 0:
                    sam += 1
            samd.clear()

            for k in range(-3, 2):
                if 0 <= i + k <= 18 and 0 <= j - k <= 18:
                    samd.append(state[i + k][j - k])
            samd = list(map(str, samd))
            samdstr = (''.join(samd))
            if len(re.findall(r'[0][1][1][1][0]', samdstr)) > 0:
                if i + 2 <= 18 and j - 2 >= 0 and state[i + 2][j - 2] == 0:
                    sam += 1
                elif i - 4 >= 0 and j + 4 <= 18 and state[i - 4][j + 4] == 0:
                    sam += 1
            samd.clear()

            for k in range(-1, 4):  # 대각 우하향 -000-- / --000-
                if 0 <= i + k <= 18 and 0 <= j + k <= 18:
                    samdd.append(state[i + k][j + k])
            samdd = list(map(str, samdd))
            samddstr = (''.join(samdd))
            if len(re.findall(r'[0][1][1][1][0]', samddstr)) > 0:
                if i + 4 <= 18 and j + 4 >= 0 and state[i + 4][j + 4] == 0:
                    sam += 1
                elif i - 2 >= 0 and j - 2 <= 18 and state[i - 2][j - 2] == 0:
                    sam += 1
            samdd.clear()

            for k in range(-2, 3):
                if 0 <= i + k <= 18 and 0 <= j + k <= 18:
                    samdd.append(state[i + k][j + k])
            samdd = list(map(str, samdd))
            samddstr = (''.join(samdd))
            if len(re.findall(r'[0][1][1][1][0]', samddstr)) > 0:
                if i + 3 <= 18 and j + 3 >= 0 and state[i + 3][j + 3] == 0:
                    sam += 1
                elif i - 3 >= 0 and j - 3 <= 18 and state[i - 3][j - 3] == 0:
                    sam += 1
            samdd.clear()

            for k in range(-3, 2):
                if 0 <= i + k <= 18 and 0 <= j + k <= 18:
                    samdd.append(state[i + k][j + k])
            samdd = list(map(str, samdd))
            samddstr = (''.join(samdd))
            if len(re.findall(r'[0][1][1][1][0]', samddstr)) > 0:
                if i + 2 <= 18 and j + 2 >= 0 and state[i + 2][j + 2] == 0:
                    sam += 1
                elif i - 4 >= 0 and j - 4 <= 18 and state[i - 4][j - 4] == 0:
                    sam += 1
            samdd.clear()
            state[i][j] = 0

        if player == 2:
            state[i][j] = 2
            for k in range(-1, 4):      # 가로 -000-- / --000-
                if 0 <= j+k <= 18:
                    samg.append(state[i][j+k])
            samg = list(map(str, samg))
            samgstr = (''.join(samg))
            if len(re.findall(r'[0][2][2][2][0]', samgstr)) > 0:
                if j+4 <= 18 and state[i][j+4] == 0:
                    sam += 1
                elif j-2 >=0 and state[i][j-2] == 0:
                    sam += 1
            samg.clear()

            for k in range(-2, 3):
                if 0 <= j+k <= 18:
                    samg.append(state[i][j+k])
            samg = list(map(str, samg))
            samgstr = (''.join(samg))
            if len(re.findall(r'[0][2][2][2][0]', samgstr)) > 0:
                if j+3 <= 18 and state[i][j+3] == 0:
                    sam += 1
                elif j-3 >=0 and state[i][j-3] == 0:
                    sam += 1
            samg.clear()

            for k in range(-3, 2):
                if 0 <= j+k <= 18:
                    samg.append(state[i][j+k])
            samg = list(map(str, samg))
            samgstr = (''.join(samg))
            if len(re.findall(r'[0][2][2][2][0]', samgstr)) > 0:
                if j+2 <= 18 and state[i][j+2] == 0:
                    sam += 1
                elif j-4 >= 0 and state[i][j-4] == 0:
                    sam += 1
            samg.clear()

            for k in range(-1, 4):      # 세로 -000-- / --000-
                if 0 <= i+k <= 18:
                    sams.append(state[i+k][j])
            sams = list(map(str, sams))
            samsstr = (''.join(sams))
            if len(re.findall(r'[0][2][2][2][0]', samsstr)) > 0:
                if i+4 <= 18 and state[i+4][j] == 0:
                    sam += 1
                elif i-2 >=0 and state[i-2][j] == 0:
                    sam += 1
            sams.clear()

            for k in range(-2, 3):
                if 0 <= i+k <= 18:
                    sams.append(state[i+k][j])
            sams = list(map(str, sams))
            samsstr = (''.join(sams))
            if len(re.findall(r'[0][2][2][2][0]', samsstr)) > 0:
                if i+3 <= 18 and state[i+3][j] == 0:
                    sam += 1
                elif i-3 >=0 and state[i-3][j] == 0:
                    sam += 1
            sams.clear()

            for k in range(-3, 2):
                if 0 <= i+k <= 18:
                    sams.append(state[i+k][j])
            sams = list(map(str, sams))
            samsstr = (''.join(sams))
            if len(re.findall(r'[0][2][2][2][0]', samsstr)) > 0:
                if i+2 <= 18 and state[i+2][j] == 0:
                    sam += 1
                elif i-4 >= 0 and state[i-4][j] == 0:
                    sam += 1
            sams.clear()

            for k in range(-1, 4):      # 대각 좌하향 -000-- / --000-
                if 0 <= i+k <= 18 and 0<= j-k <= 18:
                    samd.append(state[i+k][j-k])
            samd = list(map(str, samd))
            samdstr = (''.join(samd))
            if len(re.findall(r'[0][2][2][2][0]', samdstr)) > 0:
                if i+4 <= 18 and j-4 >= 0 and state[i+4][j-4] == 0:
                    sam += 1
                elif i-2 >= 0 and j + 2 <= 18 and state[i-2][j+2] == 0:
                    sam += 1
            samd.clear()

            for k in range(-2, 3):
                if 0 <= i+k <= 18 and 0 <= j-k <= 18:
                    samd.append(state[i+k][j-k])
            samd = list(map(str, samd))
            samdstr = (''.join(samd))
            if len(re.findall(r'[0][2][2][2][0]', samdstr)) > 0:
                if i+3 <= 18 and j-3 >=0 and state[i+3][j-3] == 0:
                    sam += 1
                elif i-3 >=0 and j+3 <= 18 and state[i-3][j+3] == 0:
                    sam += 1
            samd.clear()

            for k in range(-3, 2):
                if 0 <= i+k <= 18 and 0 <= j-k <= 18:
                    samd.append(state[i+k][j-k])
            samd = list(map(str, samd))
            samdstr = (''.join(samd))
            if len(re.findall(r'[0][2][2][2][0]', samdstr)) > 0:
                if i+2 <= 18 and j-2 >= 0 and state[i+2][j-2] == 0:
                    sam += 1
                elif i-4 >= 0 and j+4 <= 18 and state[i-4][j+4] == 0:
                    sam += 1
            samd.clear()

            for k in range(-1, 4):      # 대각 우하향 -000-- / --000-
                if 0 <= i+k <= 18 and 0 <= j+k <= 18:
                    samdd.append(state[i+k][j+k])
            samdd = list(map(str, samdd))
            samddstr = (''.join(samdd))
            if len(re.findall(r'[0][2][2][2][0]', samddstr)) > 0:
                if i+4 <= 18 and j+4 >= 0 and state[i+4][j+4] == 0:
                    sam += 1
                elif i-2 >= 0 and j - 2 <= 18 and state[i-2][j-2] == 0:
                    sam += 1
            samdd.clear()

            for k in range(-2, 3):
                if 0 <= i+k <= 18 and 0 <= j+k <= 18:
                    samdd.append(state[i+k][j+k])
            samdd = list(map(str, samdd))
            samddstr = (''.join(samdd))
            if len(re.findall(r'[0][2][2][2][0]', samddstr)) > 0:
                if i+3 <= 18 and j+3 >=0 and state[i+3][j+3] == 0:
                    sam += 1
                elif i-3 >=0 and j-3 <= 18 and state[i-3][j-3] == 0:
                    sam += 1
            samdd.clear()

            for k in range(-3, 2):
                if 0 <= i+k <= 18 and 0 <= j+k <= 18:
                    samdd.append(state[i+k][j+k])
            samdd = list(map(str, samdd))
            samddstr = (''.join(samdd))
            if len(re.findall(r'[0][2][2][2][0]', samddstr)) > 0:
                if i+2 <= 18 and j+2 >= 0 and state[i+2][j+2] == 0:
                    sam += 1
                elif i-4 >= 0 and j-4 <= 18 and state[i-4][j-4] == 0:
                    sam += 1
            samdd.clear()

            state[i][j] = 0     # 원래대로

        if sam >= 2:
            #state[i][j] = 3
            return 33
    return 0


def playerturn(pan, c, t):  # 사용자 차례
    while True:
        try:
            start = time.time()
            end = start + t
            p = str(input(">> "))
            if time.time() > end:
                p = "시간이 지났습니다. 상대에게 순서가 넘어갑니다."
                print(p)
                break

            x = int(p.split(' ')[0])
            y = int(p.split(' ')[1])
            if pan[x][y] == 0 and samsamfunction(pan, x, y, c) != 33:
                if c == 1:
                    pan[x][y] = 1
                    if x < listouter[0]:
                        listouter[0] = x
                    if x > listouter[1]:
                        listouter[1] = x
                    if y < listouter[2]:
                        listouter[2] = y
                    if y > listouter[3]:
                        listouter[3] = y
                    break
                elif c == 2:
                    pan[x][y] = 2
                    if x < listouter[0]:
                        listouter[0] = x
                    if x > listouter[1]:
                        listouter[1] = x
                    if y < listouter[2]:
                        listouter[2] = y
                    if y > listouter[3]:
                        listouter[3] = y
                    break
            elif samsamfunction(pan, x, y, c) == 33:
                print('금수 위치입니다.')
            else:
                print('이미 돌이 있는 곳입니다.')
        except:
            print("바르게 입력해주세요")

def setrange(listouter):
    if listouter[0] - 5 <= 0:
        up = 0
    else:
        up = listouter[0] - 5

    if listouter[1] + 6 >= 19:
        down = 19
    else:
        down = listouter[1] + 6

    if listouter[2] - 5 <= 0:
        left = 0
    else:
        left = listouter[2] - 5

    if listouter[3] + 6 >= 19:
        right = 19
    else:
        right = listouter[3] + 6

    return up, down, left, right


pan = []        # 보여지는 판
listouter = [100, -100, 100, -100]           # 함수 검색할 때 가장 바깥 쪽에 있는거 확인하기 가장 위쪽, 가장 아래쪽, 가장 왼쪽, 가장 오른쪽

for i in range(0, 19):  # 오목판 초기화. 비어있는 상태
    hang = []  # 행
    for j in range(0, 19):
        hang.append(0)  # 비어있는 것 표현 위해 0
    pan.append(hang)  # 전체 리스트에 안쪽 리스트를 추가

c = int(input("1. 흑돌\n2. 백돌\n>> "))
t = int(input("제한 시간을 입력해주세요. 4초 이상으로 입력해주세요.\n>> "))

print("--- Game Start !!! ---")
# 여기 나중에 try - except
if c == 1:  # 사용자가 흑, AI가 백
    while True:
        playerturn(pan, c, t)       # 사용자가 두기
        pprint(pan)

        if endgame(pan) != 0:
            break

        state = copy.deepcopy(pan)          # 깊은 복사
        x, y = alphabeta(state, c, t)       # alpha-beta 알고리즘 통해서 평가함수가 가장 작은 값을 가지는 위치를 알아냄, x는 행 y는 열
        print("(%d, %d)" %(x, y))
        pan[x][y] = 2                   # 알아낸 위치에 백돌 둠.
        pprint(pan)

        if endgame(pan) != 0:
            break

        if x < listouter[0]:
            listouter[0] = x
        if x > listouter[1]:
            listouter[1] = x
        if y < listouter[2]:
            listouter[2] = y
        if y > listouter[3]:
            listouter[3] = y
        print(listouter)

    if endgame(pan) == 2:
        print("백의 승리")
    elif endgame(pan) == 1:
        print("흑의 승리")


if c == 2:  # 사용자가 백, AI가 흑
    pan[9][9] = 1  # AI가 선일 때는 처음 두는 곳 고정
    pprint(pan)

    while True:
        state = copy.deepcopy(pan)
        playerturn(pan, c, t)
        pprint(pan)

        if endgame(pan) != 0:
            break

        state = copy.deepcopy(pan)
        x, y = alphabeta(state, c, t)
        pan[x][y] = 1
        pprint(pan)

        if endgame(pan) != 0:
            break

        if x < listouter[0]:
            listouter[0] = x
        if x > listouter[1]:
            listouter[1] = x
        if y < listouter[2]:
            listouter[2] = y
        if y > listouter[3]:
            listouter[3] = y

    if endgame(pan) == 2:
        print("백의 승리")
    elif endgame(pan) == 1:
        print("흑의 승리")
