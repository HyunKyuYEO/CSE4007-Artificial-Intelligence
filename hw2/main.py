import random
from enum import Enum

gamma = 0.9
actions = ['up', 'down', 'left', 'right']
reward = 1
n = 5


def choose_action(cur_position):
    floor_constraint = (n - 1) * n - 1
    first = 1
    check = 1
    while True:
        if first:
            # 맨 윗줄
            if cur_position < n:
                check *= 2
            # 맨 아랫줄
            if cur_position > floor_constraint:
                check *= 3
            # 맨 왼쪽 출
            if cur_position % n == 0:
                check *= 5
            # 맨 오른쪽 줄
            if cur_position % n == n - 1:
                check *= 7
        first = 0

        action = random.choice(actions)
        # 순서대로 맨 윗줄인데 위로 갈때, 맨 아랫줄인데 아래로 갈때, 맨 왼줄인데 왼으로 갈때, 맨 오른인데 오른쪽으로 갈때
        if check == 2 and action == 'up':
            continue
        elif check == 3 and action == 'down':
            continue
        elif check == 5 and action == 'left':
            continue
        elif check == 7 and action == 'right':
            continue
        # 순서대로 최자상점, 최우상점, 최좌하점, 최우하점
        elif check == 10 and (action == 'up' or action == 'left'):
            continue
        elif check == 14 and (action == 'up' or action == 'right'):
            continue
        elif check == 15 and (action == 'down' or action == 'left'):
            continue
        elif check == 21 and (action == 'down' or action == 'right'):
            continue
        return action


def move_and_update(board, score, cur_position, action):
    if action == 'right':
        tem = cur_position + 1
    elif action == 'down':
        tem = cur_position + n
    elif action == 'left':
        tem = cur_position - 1
    elif action == 'up':
        tem = cur_position - n

    if board[tem] == 'P':
        score[cur_position][actions.index(action)] = gamma * max(
            score[tem])
        return tem
    elif board[tem] == 'B':
        score[cur_position][actions.index(action)] = gamma * max(score[tem]) - 100
        return 0
    elif board[tem] == 'T':
        score[cur_position][actions.index(action)] = gamma * max(score[tem]) + reward
        return tem
    elif board[tem] == 'G':
        score[cur_position][actions.index(action)] = gamma * max(score[tem]) + 100
        return 0
    elif board[tem] == 'S':
        score[cur_position][actions.index(action)] = gamma * max(score[tem])
        return 0


def find_path(score):
    i = 0
    file_str = ''
    file_str = str(i) + ' '
    print(i, end=' ')
    f2 = open("output.txt", 'w')
    count = 0
    while i != 24:
        if count > 24:
            break
        move = actions[score[i].index(max(score[i]))]
        if move == 'up':
            i = i - n
            print(i, end=' ')
            file_str = file_str + str(i) + ' '
        elif move == 'down':
            i = i + n
            print(i, end=' ')
            file_str = file_str + str(i) + ' '
        elif move == 'left':
            i = i - 1
            print(i, end=' ')
            file_str = file_str + str(i) + ' '
        elif move == 'right':
            i = i + 1
            print(i, end=' ')
            file_str = file_str + str(i) + ' '
        count += 1

    print()
    print(max(score[0]))

    f2.write(file_str.rstrip())
    f2.write('\n')
    f2.write(str(max(score[0])))
    f2.close()


def q_learning(board):
    cur_position = 0
    score = [0 for i in range(25)]

    for i in range(25):
        score[i] = [0 for i in range(4)]
    k = 1

    while k < 10000:
        action = choose_action(cur_position)
        cur_position = move_and_update(board, score, cur_position, action)
        k += 1
    find_path(score)


def main():
    print("Q-learning")
    f = open("input.txt", 'r')
    board = []
    c = f.read()
    c = c.split()
    for i in range(5):
        for j in range(5):
            board.append(c[i][j])

    f.close()
    q_learning(board)


main()
