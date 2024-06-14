

#9주차#9주차#9주차
#9주차#9주차#9주차
#9주차#9주차#9주차


list1 = [11,22,33,44,55]
list2 = ['단촐하게','단아하게','당당하게']
list3 = []
print(list1)
print(list2)
print(list3)

n = 10

nums=[11, 22, 33, 44, 55]

list4 = [11,'홍길동',19,180.5]
print(list4[1],' 님의 키는', list4[-1], 'cm입니다.')
sub_list = list1[1:3]
print(sub_list)
print(sub_list[0])

nums[0] = -1
print(nums)

nums[1:3] = [100,200,300]
print(nums)

t1 = (11,22,33,44,55)
print(t1[0])
t2 = (66,77)
t3 = t1+t2
print(t3)

t4=t2*3

print(t4)

d = {'python':'파이썬','basic':'기초','programing':'프로그래밍'}
print(d['python'])


scores = []
print('[점수 입력]')
for i in range(3) :
    n = int(input(f'# {i+1} ?'))
    scores.append(n)

print('\n[점수 출력]')

average = f'{(scores[0]+scores[1]+scores[2])/len(scores)}'

print(f'평균 : {average:1f} ')

#연습문제 9.1
scores = []
print('점수 입력')
for i in range(3) :
    n = int(input(f'#{i + 1}? '))
    scores.append(n)

print('\n점수 출력')
print(f'입력 점수 : {scores[0]} {scores[1]} {scores[2]}')
avg = (scores[0] + scores[1] + scores[2]) / len(scores)
print(f'평균: {avg:.2f}')


#이어서 연습 9.2

print('\n[검색]')
s = int(input('찾고자 하는 점수는?'))
if s in scores :
    idx = scores.index(s)
    print(f'{s}점은 {idx + 1}번 학생의 점수입니다.')
else:
    print(f'{s}점을 받은 학생은 없습니다.')

#연습문제 9.3

shopping_bag = [] 
count =[]
while True :
    item = input('상품명?')
    
    if (len(item)) == 0 :
        break
    else :
        shopping_bag.append(item)
        howmany = input('수량은?')
        count.append(howmany)
        print(f'장바구니에 {item} {howmany}개가 담겼습니다.')


print(f'장바구니 보기 : {list(shopping_bag)}  {list(count)}')


#연습문제 9.4

shopping_bag = {}
print('[구입]')
while True:
    item = input('상품명? ')
    
    if len(item) == 0:
        break
    else:
        howmany = int(input('수량은? '))  
        shopping_bag[item] = howmany
        print(f'장바구니에 {item} {howmany}개가 담겼습니다.')
        print()
print(f'>>>장바구니 보기 : {shopping_bag}')
print()

print('[검색]')
product_name = input('장바구니에서 확인하고자 하는 상품은? ')
if product_name in shopping_bag:
    print(f'{product_name}은(는) {shopping_bag[product_name]}개 담겨 있습니다.')
else:
    print(f'{product_name}은(는) 장바구니에 없습니다.')







#10주차#10주차#10주차
#10주차#10주차#10주차
#10주차#10주차#10주차


def input_list() :
    name = input('이름? ')
    num = input('번호? ')

    lst = []
    lst.append(name)
    lst.append(num)
    return lst

userinfo = input_list()
print(f' {userinfo[1]}번 {userinfo[0]}')



def get_data() :
    y = int(input('연도? '))
    m = int(input('월? '))
    d = int(input('일?'))
    return(y, m, d)


print('당신의 생일을 입력하세요 : ')
bday = get_data()
print(f'당신의 만 60번째 생일은 {bday[0]+60}년 {bday[1]}월 {bday[2]}일 입니다.')



msgs = ['단촐하게', '단아하게', '당당하게']
for i in range(len(msgs)-1, -1, -1) :
    print(f'{msgs[i]}/', end='')


def input_num_of_pop() :
    npeople = []
    for f in range(4) :
        n = int(input(f'{f + 1}층의 거주 인원 수는? '))
        npeople.append(n)

    return npeople

def show_num_of_pop(p) :
    cnt = len(p)
    for i in range(cnt) :
        print(f'{i+1}층의 거주인원수는 {p[i]}명입니다.')


def flourpop(lst) :
    total = 0
    for n in lst :
        total += n

    return total

population = input_num_of_pop()

show_num_of_pop(population)

total = flourpop(population)

print(f'총 거주인원수는 {total}')




d= {'python' :'파이썬' , 'basic' : '기초', 'programing' : '프로그래밍'}

def dict_get(dic, key) :
    if key in dic :
        return dic[key]
    else :
        return None
    
def dict_append(dic, key, value) :
    if key in dic :
        return False
    
    dic[key] = value
    return True

def dict_delete(dic, key) :
    if key in dic :
        del dic[key]
        return  True
    else :
        return False

if dict_append(d, 'PYTHON', '파이썬') :
    print('추가 성공')
else :
    print('추가 실패')

if dict_append(d, 'basic', '베이직') :
    print('두 번째 추가 성공')
else :
    print('두 번째 추가 실패')

print(d)

res = dict_get(d, 'python')
if res != None :
    print(res)
    
else :
    print('오류 : 잘못된 키')


res = dict_get(d,0)
if res != None :
    print(res)

else :
    print('오류 : 잘못된 키')

if dict_delete(d, 'basic') :
    print('삭제 성공')

else :
    print('삭제 실패')

print(d)



#연습문제 10.2

input_num = []
for f in range(5) :
    n = int(input('정수 입력: '))
    input_num.append(n)



def find_max(lst) :
    m=lst[0]
    for i in range(1, len(lst)) :
        if lst[i] > m :
            m = lst[i]
    return m


print(f'가장 큰 정수는 {find_max(input_num)} 입니다.')


#연습문제 10.3~10.4

def input_scores() :
    s = []
    i = 1
    while(True) : 
        n = int(input(f'#{i}? '))
        if n < 0 :
            break
        s.append(n)
        i += 1
    return s

def get_average(s) :
    total = 0
    for n in s :
        total += n 
    return total / len(s)

def show_scores(s) :
    for n in s :
        print(n, end= ' ')
    print()

def search(lst, n) :
    if n not in lst:
        return None
    
    return lst.index(n)

print('[점수 입력]')
scores = input_scores()
print('\n[점수 출력]')
print('개인점수: ', end='')
show_scores(scores)
avg = get_average(scores)
print(f'평균 : {avg:1f}')
print('\n[검색]')
s = int(input('찾고자 하는 학생의 점수는?'))
idx = search(scores, s)
if idx != None :
    print(f'{s} 점은 {idx+1}번 학생의 점수입니다.' )

else :
    print(f'{s} 점을 받은 학생은 없습니다.' )



#실전 과제

shopping_bag = {}

while True:
    print('[구입]')
    item = input('상품명? ')
    
    if len(item) == 0:
        break
    else:
        howmany = int(input('수량은? '))  
        shopping_bag[item] = howmany
        print(f'장바구니에 {item} {howmany}개가 담겼습니다.')
        print()
print()
print(f'>>>장바구니 보기 : {shopping_bag}')
print()

print('[검색]')
product_name = input('장바구니에서 확인하고자 하는 상품은? ')

if product_name in shopping_bag:
    print(f'{product_name}은(는) {shopping_bag[product_name]}개 담겨 있습니다.')
else:
    print(f'{product_name}은(는) 장바구니에 없습니다.')





#11주차#11주차#11주차
#11주차#11주차#11주차
#11주차#11주차#11주차

11-5
class Circle :
    def getCircumference(self) :
        result = 2*3.14159265*self.radius
        return result
        

    def getArea(self) :
        result = 3.14159265*self.radius**2
        return result

small = Circle()
big = Circle()

small.radius = 1
big.radius = 10
print(f'반지름 {small.radius}인 원의둘레는 {small.getCircumference():.2f}이고',end='')
print(f'넓이는 {small.getArea():.2f}이다.')
print(f'반지름 {big.radius}인 원의둘레는 {big.getCircumference():.2f}이고',end='')
print(f'넓이는 {big.getArea():.2f}이다.')

#11-6 11-7

class Circle :
    def __init__(self, radius) :
        self.__radius = radius
        

    def getCircumference(self) :
        result = 2*3.14159265*self.__radius
        return result
    
    def getArea(self) :
        result = 3.14159265*self.__radius**2
        return result
    def get_radius(self) :
        return self.__radius

small = Circle(1)
big = Circle(10)
print(f'반지름 {small.get_radius()}인 원의둘레는 {small.getCircumference():.2f}이고',end='')
print(f'넓이는 {small.getArea():.2f}이다.')
print(f'반지름 {big.get_radius()}인 원의둘레는 {big.getCircumference():.2f}이고',end='')
print(f'넓이는 {big.getArea():.2f}이다.')

#11.1
class Point:
    def __init__(self, x=0, y=0) :
        self.__x = x
        self.__y = y
    
    def show(self):
        print(f'({self.__x},{self.__y})')

    def set(self, x, y):
        self.__x = x
        self.__y = y
    def get(self):
        return (self.__x, self.__y)
#주프로그램부
def test() :
    p1 = Point()
    p2 = Point(2, 3)

    p1.show();
    p1.set(10, 20); p1.show();
    p2.show();
    x,y = p2.get()
    print(f'x={x}, y={y}')

if __name__ == '__main__':
    test()

#연습문제 11.2
class Time :
    def __init__(self, hour = 0, minute = 0):
        self.__hour = hour
        self.__minute = minute

    def display(self) :
        print(f'{self.__hour:02d}:{self.__minute:02d}')

    def add(self, time):
        h = self.__hour+time.__hour
        m = self.__minute +time.__minute
        if m>=60:
            h+=1
            m-=60
        return Time(h, m)
    @staticmethod
    def is_vaild(hour,minute):
        if 0<=hour < 24 and 0 <= minute < 60:
            return True
        return False
#주프로그램부 
def main() :
    t1 =Time(9)
    t2 =Time(9,30)

    t1.display()
    t2.display()

    later = t1.add(Time(1,15))
    later.display()

    if Time.is_vaild(25,0):
        print('유효한 시각')
    else :
        print('유효하지 않은 시각')

if __name__ == '__main__':
    main()

# 11.3

from point import Point

class Rectangle:
    def __init__(self, lt_x, lt_y, rb_x, rb_y):
        self.__lt = Point(lt_x, lt_y)
        self.__rb = Point(rb_x, rb_y)

    def show(self):
        print(f'좌측 상단 꼭지점이 {self.__lt.toString()}이고')
        print(f'우측 하단 꼭지점이 {self.__rb.toString()}인 사각형입니다.')

    def getWidth(self):
        return self.__rb.getX() - self.__lt.getX()

    def getHeight(self):
        return self.__rb.getY() - self.__lt.getY()

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return (self.getWidth() + self.getHeight()) * 2

def main():
    r1 = Rectangle(5, 5, 20, 10)
    a = r1.getArea()
    p = r1.getPerimeter()

    r1.show()
    print(f'넓이는 {a}, 둘레는 {p}')

if __name__ == '__main__':
    main()



#12주차#12주차#12주차
#12주차#12주차#12주차
#12주차#12주차#12주차

import os 
filename = 'example.txt'
if os.path.exists(filename) :
    file = open(filename, 'r')
    file.close()
    print('파일 열고 닫기 완료')
else :
    print(f'ERROR: {filename}이 존재하지 않습니다!')

print('끝')



num = 2
name = '홍길동'

with open('exeample.txt', 'w') as file:
    file.write('1 이찬수\n')
    file.write(f'{num} {name}\n')

print('끝')



with open('예제/example.txt', 'r') as file:
    all = file.read()

print(all)


lines = []
with open('예제/example.txt', 'r')as file:
    while True:
        line = file.readline()

        if line =='':
            break
        lines.append(line.strip())

print(lines)



import pickle

filepath = '예제/example.bin'

def save_data(num, name, height, scores) :
    with open(filepath, 'wb') as file:
        pickle.dump(num, file)
        pickle.dump(name, file)
        pickle.dump(height, file)
        pickle.dump(scores, file)

def load_data():
    with open(filepath, 'wb')as file:
        num = pickle.load(file)
        name = pickle.load(file)
        height = pickle.load(file)
        scores = pickle.load(file)

    return num, name, height, scores

num,name,height = 123, '홍길동', 180.5
scores = {'mid':90, 'fin':95, 'rep':10, 'att':10}

save_data(num, name, height, scores)

r_num ,r_name, r_height, r_scores = load_data()


print(r_num)
print(r_name)
print(r_height)
print(r_scores)



#연습문제 12.1

with open('readme.txt', 'w') as file:
    file.write('1 : 안녕하세요, 반갑습니다.\n')
    file.write('2 : 이 파일은 테스트파일 저작을 위해 작성된 텍스트 문서입니다.\n')
    file.write('3 : 조금 낯설더라도 포기하지 마세요.')

with open('readme.txt', 'r') as file:
    all = file.read()

print(all)



def buy (sbag) :
    print ('[구입]')
    item = input('상품명? ')
    if item == ' ' :
        return False
    sbag. append (item)
    print(f' 장바구니에{item}가(이)담겼습니다\n')
    return True

def show (sbag):
    print(' \n>>>장바구니 보기 : ', end='')
    print (sbag)

# 주 프로그램부

shopping_bag = []
while True:
    if buy(shopping_bag) == False:
        break
show (shopping_bag)


#연습문제 12.4

#13-14주차#13-14주차#13-14주차
#13-14주차#13-14주차#13-14주차
#13-14주차#13-14주차#13-14주차

import tkinter as tk
from tkinter import ttk

class SayHellowin :
    def __init__(self):
        self.win = tk.Tk()
        self. win.title('버튼 위젯 예-OPP')
        self.__buildGUI()

    def __buildGUI(self):
        self.text_label = ttk.Label(self.win, text='안녕하세요')

        self.name = tk.StringVar()
        input_entry = ttk.Entry(self.win,textvariable=self.name)

        input_btn = ttk.Button(self.win, text='입력', command=self.__input_btn_handler)
        quit_btn = ttk.Button(self.win, text='종료', command=self.win.destroy)

        self.text_label.pack()
        input_entry.pack()
        input_btn.pack()
        quit_btn.pack()

    def __input_btn_handler(self):
        self.text_label.configure( text= '반가워요, ' + self.name.get())
        self.name.set('')

hello = SayHellowin()
hello.win.mainloop()



#연습문제 13.1-13.3

import tkinter as tk
from tkinter import ttk

class ConvTempWin() :

    def __init__(self):
        self.win = tk.Tk()
        self. win.title('온도변환기 -3단계')
        self.__buildGUI()

    def __buildGUI(self):
        self.__create_input_frame().pack()
        self.__create_button_frame().pack()
    
    def __create_input_frame(self) :
        frame = ttk.Frame(self.win)

        fahr_Label = ttk.Label(frame, text='화씨')
        
        self.__fahr = tk.IntVar()
        fahr_entry = ttk.Entry(frame, justify=tk.RIGHT, width=11, textvariable=self.__fahr)

        cel_Label = ttk.Label(frame,text='섭씨')

        self.__cels = tk.DoubleVar()
        cel_entry = ttk.Entry(frame, justify=tk.RIGHT, width=11,textvariable=self.__cels)

        fahr_Label.pack(side=tk.LEFT)
        fahr_entry.pack(side=tk.LEFT)
        cel_Label.pack(side=tk.LEFT)
        cel_entry.pack(side=tk.LEFT)

        return frame
    
    def __create_button_frame(self):
        frame = ttk.Frame(self.win)
        f2c_btn = ttk.Button(frame, text='화씨 -> 섭씨', command=self.__f2c_handler)
        c2f_btn = ttk.Button(frame, text='섭씨 -> 화씨', command=self.__c2f_handler)
        reset_btn = ttk.Button(frame, text='리셋', command=self.__reset_handler)
        quit_btn = ttk.Button(frame, text='종료', command=self.win.quit)

        f2c_btn.pack(side=tk.LEFT)
        c2f_btn.pack(side=tk.LEFT)
        reset_btn.pack(side=tk.LEFT)
        quit_btn.pack(side=tk.LEFT)

        return frame
    
    def __f2c_handler(self) :
        fahr = self.__fahr.get()
        cels = (fahr - 32)* 5/9
        self.__cels.set(f'{cels:.2f}')

    def __c2f_handler(self) :
        cels = self.__cels.get()
        fahr = cels *9/5+32
        self.__fahr.set(f'{fahr:.0f}')

    def __reset_handler(self):
        self.__fahr.set('')
        self.__cels.set('')

    def start(self):
        self.win.mainloop()

tConverter = ConvTempWin()
tConverter.start()


#연습문제 13.4 GPT ver.

import tkinter as tk
from tkinter import ttk

GRADE = ['1학년', '2학년', '3학년', '4학년']
HOBBY = ['영화시청', '음악감상', '사진찍기', '운동']

class UserInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("회원 가입")
        
        self.__buildGUI()

    def __buildGUI(self):
        name_frame = ttk.Frame(self.root)
        name_label = ttk.Label(name_frame, text="이름:")
        name_label.pack(side=tk.LEFT)
        self.name_var = tk.StringVar()
        name_entry = ttk.Entry(name_frame, textvariable=self.name_var)
        name_entry.pack(side=tk.LEFT)
        name_frame.pack(fill=tk.X)
        
        grade_frame = ttk.Frame(self.root)
        grade_label = ttk.Label(grade_frame, text="학년:")
        grade_label.pack(side=tk.LEFT)
        self.grade_var = tk.StringVar()
        grades = ["1학년", "2학년", "3학년", "4학년"]
        for grade in grades:
            grade_radio = ttk.Radiobutton(grade_frame, text=grade, value=grade, variable=self.grade_var)
            grade_radio.pack(side=tk.LEFT)
        grade_frame.pack(fill=tk.X)
        
        hobby_frame = ttk.Frame(self.root)
        hobby_label = ttk.Label(hobby_frame, text="취미:")
        hobby_label.pack(side=tk.LEFT)
        self.hobbies = {"영화시청": tk.BooleanVar(), "음악감상": tk.BooleanVar(), "사진찍기": tk.BooleanVar(), "운동": tk.BooleanVar()}
        for hobby, var in self.hobbies.items():
            hobby_check = ttk.Checkbutton(hobby_frame, text=hobby, variable=var)
            hobby_check.pack(side=tk.LEFT)
        hobby_frame.pack( fill=tk.X)
        
        button_frame = ttk.Frame(self.root)
        quit_button = ttk.Button(button_frame, text="종료", command=self.root.quit)
        quit_button.pack(side=tk.RIGHT)
        submit_button = ttk.Button(button_frame, text="입력", command=self.submit)
        submit_button.pack(side=tk.RIGHT)
        button_frame.pack( fill=tk.X)

    def submit(self):
        name = self.name_var.get()
        grade = self.grade_var.get()
        hobbies = [hobby for hobby, var in self.hobbies.items() if var.get()]
        print(f"{name}")
        print(f"{grade}")
        print(format('\n'.join(hobbies)))

if __name__ == "__main__":
    root = tk.Tk()
    app = UserInfoApp(root)
    root.mainloop()



#연습문제 13.4 교수님 ver
import tkinter as tk
from tkinter import ttk

class MerberReg() :
    hobby_list = ['영화시청', '음악감상', '사진찍기', '운동']

    def __init__(self):
        self.win = tk.Tk()
        self.win.title('회원가입')
        #self.win.geometry('250x300')
        self.__buildGUI()

    def __buildGUI(self) :
        self. __create_name_input_frame().grid(row=0, column=0, sticky='w')
        self. __create_grade_input_frame().grid(row=1, column=0, sticky='w')
        self. __create_hobby_input_frame().grid(row=2, column=0, sticky='w')
        self. __create_button_frame().grid(row=3, column=0, sticky='e')
    
    def __create_name_input_frame(self) :
        frame = ttk.Frame(self.win)
        self.text_label = ttk.Label(frame, text = '이름:')
        self.name = tk.StringVar()
        input_entry = ttk.Entry(frame, textvariable = self.name)

        self.text_label.grid(row=0, column=0)
        input_entry.grid(row=0, column=1)

        return frame

    def __create_grade_input_frame(self) :
        frame = ttk.Frame(self.win)
        self.text_label = ttk.Label(frame, text = '학년:')
        self.text_label.grid(row=0, column=0)
        
        sub_frame = ttk.Frame(frame)
        self.grade = tk.IntVar()
        for i in range(1, 5) :
            grade_btn = ttk.Radiobutton(sub_frame, text=f'{i}학년', value=i,variable=self.grade)
            grade_btn.pack(side=tk.LEFT)
        sub_frame.grid(row=0,column=1)
        return frame
    
    def __create_hobby_input_frame(self) :
        frame = ttk.Frame(self.win)

        self.text_label = ttk.Label(frame, text = '취미:')
        self.text_label.grid(row=0, column=0)

        sub_frame = ttk.Frame(frame)
        self.hobby = []
        for i in range(4) :
            self.hobby.append(tk.IntVar())
            hobby_btn = ttk.Checkbutton(sub_frame, text=self.hobby_list[i], variable=self.hobby[i])
            hobby_btn.pack(side=tk.LEFT)
        sub_frame.grid(row=0,column=1)
        return frame
    def __create_button_frame(self):
        frame = ttk.Frame(self.win)

        input_btn = ttk.Button(frame, text='입력',command=self.__input_btn_clicked)
        quit_btn = ttk.Button(frame, text='종료',command=self.win.destroy)

        input_btn.pack(side=tk.LEFT)
        quit_btn.pack(side=tk.LEFT)

        return frame
    
    def __input_btn_clicked(self) :
        print(self.name.get())
        print(self.grade.get())

        for i in range(4):
            if self.hobby[i].get() == True :
                print(self.hobby_list[i])

member = MerberReg()
member.win.mainloop()

#13.5