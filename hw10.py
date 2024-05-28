import pickle
import os

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = sum(s)
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def search(lst, n):
    if n not in lst:
        return None
    return lst.index(n)

def save_scores(scores, filename):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_scores(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return None

filename = 'score.bin'

scores = load_scores(filename)
if scores is None:
    print('[점수 입력]')
    scores = input_scores()
    save_scores(scores, filename)

print('[파일 읽기]')
print('\n[점수 출력]')
print('개인점수: ', end='')
show_scores(scores)
avg = get_average(scores)
print(f'평균: {avg:.1f}')

