# 함수
'''
프로그래밍을 하다 보면 들어가는 값만 바뀔 뿐 같은 코드가 계속 반복되는 경우가 많습니다.
특히 같은 코드를 반복해서 작성하면 코드도 길어지고 중간에 실수할 가능성이 높아집니다.

파이썬은 함수(function)라는 기능을 제공하는데 특정 용도의 코드를 한 곳에 모아 놓은 것을 뜻합니다.
그래서 함수는 처음 한 번만 작성해 놓으면 나중에 필요할 때 계속 불러 쓸 수 있습니다.
예를 들어 지금까지 사용했던 print, input 등도 모두 파이썬에서 미리 만들어 둔 함수입니다.

즉, 함수를 사용하면 이런 점이 좋습니다.

코드의 용도를 구분할 수 있다.
코드를 재사용할 수 있다.
실수를 줄일 수 있다.
'''

## 함수 만들기
'''
함수는 def에 함수 이름을 지정하고 ( )(괄호)와 :(콜론)을 붙인 뒤 다음 줄에 원하는 코드를 작성합니다
(함수의 이름을 짓는 방법은 변수와 같습니다).
이때 코드는 반드시 들여쓰기를 해야 합니다(들여쓰기 규칙은 if, for, while과 같습니다).

def 함수이름(...):
     코드

여기서 def는 정의하다(define)에서 따온 키워드입니다.
'''


def my_fun():
    print("내가 만든 함수, 너를 위해 구웠지")


my_fun()  # 소괄호! -> 호출


# my_fun -> () -> 응답

# 함수 호출 : 함수를 사용한다( () ) -> 함수를 호출(call)


# 함수를 만들고 호출 -> 함수를 만들기 전에 함수를 호출하면 X

# my_fun2()  # 안 만들었으니까 (위에서부터 -> 아래로...)
# NameError: name 'my_fun2' is not defined. Did you mean: 'my_fun'?
def my_fun2():
    print("식사는 없어 배고파도")


# 빈 함수
def empty():
    pass  # 빈 블록 (빈 조건문, 빈 반복문 -> pass => 블록을 유지하기 위해서)


# 공부한다는 함수
def study():
    sit()
    write()
    read()


def sit():
    pass


def write():
    # pass
    print("깜지를 썼다")


def read():
    pass


study()

"""
## 매개변수 (parameter)

함수에서 값을 받으려면 ( )(괄호) 안에 변수 이름을 지정해주면 됩니다. 특히 이 변수를 매개변수(parameter)라고 부릅니다.

```
def 함수이름(매개변수1, 매개변수2):
    코드
```
"""


# def solution(num1, num2): ... -> 프로그래머스.
def greeting(name, time):
    print(f"안녕하세요! 저는 {name}입니다. 지금은 {time}시네요!")


greeting("최코딩", 12)
greeting("유코딩", 1)

# 인수(인자)와 패러미터 -> 값 자체가 인수, 그 값이 들어가서 전달되는 '변수' -> 매개변수 패러미터.
"""함수를 호출할 때 넣는 값을 인수(argument)라고 부릅니다.

## 함수의 결과를 반환하기

함수 안에서 return을 사용하면 값을 함수 바깥으로 반환합니다(return에 값을 지정하지 않으면 None을 반환).

```
def 함수이름(매개변수):
    return 반환값
```
"""

v = print("hello")
print(v)


def add(x1, x2):
    return x1 + x2


x = add(10, 100)  # 안으로 들어오는 값은 '인자'라는 이름으로 불리고, 내부에서는 '매개변수'를 통해 호출
# 호출된 매개변수를 사용? => 마지막으로 밖으로 내보내고 싶은게 있다면 return 을 통해서 내보내는 것.
print(x)
print(add(10, 100))


def twopower():
    return 2 ** 2


print(twopower())
import random


def dice():
    return random.randint(1, 6)


print(f"dice : {dice()}")

"""return으로 반환하는 값은 반환값이라고 하며 함수를 호출해준 바깥에 결과를 알려주기 위해 사용합니다."""

# 반환값은 변수에 저장하지 않고 바로 다른 함수에 넣을 수도 있습니다.

"""### return으로 함수 중간에서 빠져나오기"""


def my_fun(a, b):  # concat - 문자열 연결
    # 숫자들어오면 안되는 함수
    # 숫자가 들어오면 'print'시켜주고, ""(빈 문자열)
    if type(a) != str or type(b) != str:
        print("a나 b 중에 문자열이 아닌게 있습니다")
        return ""  # 이 코드가 실행이 되면.... -> 멈춘다. 언제? def 안에 있을 때
    # ----- 여기 이후의 코드....
    # else로 처리... -> 들여쓰기가 필요한 복잡한 코드가 아니라...
    print("문자열을 처리합니다....")  # 이후의 코드가 무시!
    return a + b  # 문자열이라면...


print(my_fun("a", "b"))
print(my_fun(10, 100))


# return # <- 에러. => 함수 내부가 아닌 가장 밖의 return을 쓰면 에러.
# SyntaxError: 'return' outside function

def main():
    print("안녕하세요")
    return
    print("안녕히가세요")


main()  ## 내가 원할 때 언제는 return 사용을 해서 함수를 중단(실행을 중단)

"""return은 함수 중간에서 빠져나올 때 자주 사용합니다. 보통은 if와 조합해서 특정 조건일 때 함수 중간에서 빠져나옵니다.

## 함수에서 값을 여러 개 반환하기

함수에서 값을 여러 개 반환할 때는 다음과 같이 return에 값이나 변수를 ,(콤마)로 구분해서 지정하면 됩니다.

```
def 함수이름(매개변수):
    return 반환값1, 반환값2
```
"""


def add_sub(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    # return [add, sub]
    # return (add, sub)
    return add, sub  # 튜플은 소괄호를 생략 가능


print(add_sub(10, 5))
add, sub = add_sub(10, 5)
print(f"add: {add}, sub:{sub}")

"""# 함수 심화

## 위치 인수와 리스트 언패킹 사용하기

함수에 인수를 순서대로 넣는 방식을 위치 인수(positional argument)라고 합니다. 즉, 인수의 위치가 정해져 있습니다.
"""

print(1)
print(1, 2)
print(1, 2, 3)

"""### 위치 인수를 사용하는 함수를 만들고 호출하기"""


def order(menu1, menu2, menu3):
    print(menu1)
    print(menu2)
    print(menu3)


order("아메리카노", "", "")


# order("아메리카노", "카페라떼") # TypeError: order() missing 1 required positional argument: 'menu3'
# order("아메리카노", "카페라떼", "프라푸치노", "페페론치노")
# TypeError: order() takes 3 positional arguments but 4 were given

def order(menu_list):
    for menu in menu_list:
        print(menu)


order(["아메리카노"])
order(["아메리카노", "아메리카노"])

"""### 언패킹 사용하기

인수를 순서대로 넣을 때는 리스트나 튜플을 사용할 수도 있습니다. 다음과 같이 리스트 또는 튜플 앞에 *(애스터리스크)를 붙여서 함수에 넣어주면 됩니다.

* `함수(*리스트)`
* `함수(*튜플)`
"""

import random

print(random.randint(1, 6))  # a : 시작하는 수, b : 끝나는 수 (포함)
l = [1, 100]
print(random.randint(*l))  # * : 별표, 아스타, 애스터, 애스터리스크... -> 언패킹.
# 단, 이때 함수의 매개변수 개수와 리스트의 요소 개수는 같아야 합니다.
# 만약 개수가 다르면 함수를 호출할 수 없습니다.
print(1, 2, 3, 4)
print(*range(1, 5))
print("가변 인수 함수 만들기")
print(*"가변 인수 함수 만들기")  # 한 글자씩.

"""### 가변 인수 함수 만들기

그럼 위치 인수와 리스트 언패킹은 어디에 사용할까요? 이 기능들은 인수의 개수가 정해지지 않은 가변 인수(variable argument)에 사용합니다. 즉, 같은 함수에 인수 한 개를 넣을 수도 있고, 열 개를 넣을 수도 있습니다. 또는, 인수를 넣지 않을 수도 있습니다.

다음과 같이 가변 인수 함수는 매개변수 앞에 *를 붙여서 만듭니다.

```
def 함수이름(*매개변수):
    코드
```
"""


def order(*menu):  # * -> 전달받은 인자들을 패킹.
    for m in menu:
        print(f"메뉴 : {m}")


order('돈까스', '새우튀김', '계란프라이')  # '돈까스', '새우튀김', '계란프라이'


# <- 인자로 전달된 것들을 패킹시켜서 menu라고하는 변수에 집어넣음.
def my_sum(*numbers):
    answer = 0
    for n in numbers:  # 튜플 -> 시퀀스.
        answer += n
    return answer


print(my_sum(10, 10000, 101001213, 213214, 231321))

"""매개변수 이름은 원하는 대로 지어도 되지만 관례적으로 arguments를 줄여서 args로 사용합니다. 특히 이 args는 튜플이라서 for로 반복할 수 있습니다.


"""

l = list(range(10))
print(l)
print(*l)  # print -> 가변인수를 받는 함수.

# 이렇게 함수에 인수 여러 개를 직접 넣어도 되고, 리스트(튜플) 언패킹을 사용해도 됩니다.

"""### 고정 인수와 가변 인수를 함께 사용하기

고정 인수와 가변 인수를 함께 사용할 때는 고정 매개변수를 먼저 지정하고, 그 다음 매개변수에 *를 붙여주면 됩니다.
"""


def order(category, *args):  # 가변 인수를 나타내는 매개변수보다, 고정 매개변수가 앞에 존재
    print(f"{category}의 종류의 음식을 원하시는 군요")
    print(*args, "들을 드리겠습니다")


order("중식", "마라탕", "마라샹궈", "마라룽샤")

"""단, 이때 def print_numbers(*args, a):처럼 *args가 고정 매개변수보다 앞쪽에 오면 안 됩니다. 매개변수 순서에서 *args는 반드시 가장 뒤쪽에 와야 합니다.


## 키워드 인수 사용하기

파이썬에서는 인수의 순서와 용도를 매번 기억하지 않도록 키워드 인수(keyword argument)라는 기능을 제공합니다.
키워드 인수는 말 그대로 인수에 이름(키워드)을 붙이는 기능인데 키워드=값 형식으로 사용합니다.

* `함수(키워드=값)`
"""


def order(category, price):
    print(f"{category} 종류의 음식을 {price}원 어치 주문하셨네요")


order("중식", 15000)
order(category="중식", price=15000)
order(price=15000, category="중식")

# 키워드 인수를 사용하면 인수의 순서를 맞추지 않아도 키워드에 해당하는 값이 들어갑니다.

"""## 키워드 인수와 딕셔너리 언패킹 사용하기

지금까지 함수를 호출할 때 키워드 인수로 직접 값을 넣었습니다.
이번에는 딕셔너리를 사용해서 키워드 인수로 값을 넣는 딕셔너리 언패킹을 사용해보겠습니다.
다음과 같이 딕셔너리 앞에 **(애스터리스크 두 개)를 붙여서 함수에 넣어줍니다.

* `함수(**딕셔너리)`
"""
# order = category, price
d = {
    "category": "일식",
    "price": 20000,
}
print("딕셔너리 언패킹")
order(**d)

"""이제 딕셔너리에 '키워드': 값 형식으로 인수를 저장하고, 앞에 **를 붙여서 함수에 넣어줍니다. 이때 딕셔너리의 키워드(키)는 반드시 문자열 형태라야 합니다."""

d2 = {
    "name": "John",
    "age": 12,
}
new_d2 = {
    "name": "Johnson",
    "age": 22,
}
print(d2)
d2.update(**new_d2)
print(d2)

"""**x처럼 딕셔너리를 언패킹하면 딕셔너리의 값들이 함수의 인수로 들어갑니다.

딕셔너리 언패킹을 사용할 때는 함수의 매개변수 이름과 딕셔너리의 키 이름이 같아야 합니다. 또한, 매개변수 개수와 딕셔너리 키의 개수도 같아야 합니다.
"""

"""### *를 두 번 사용하는 이유

그런데 딕셔너리는 **처럼 *를 두 번 사용할까요? 왜냐하면 딕셔너리는 키-값 쌍 형태로 값이 저장되어 있기 때문입니다. 먼저 *를 한 번만 사용해서 함수를 호출해봅니다.
"""

"""딕셔너리를 한 번 언패킹하면 키를 사용한다는 뜻이 됩니다. 따라서 **처럼 딕셔너리를 두 번 언패킹하여 값을 사용하도록 만들어야 합니다."""

print(*d)

"""### 키워드 인수를 사용하는 가변 인수 함수 만들기

키워드 인수를 사용하는 가변 인수 함수는 매개변수 앞에 **를 붙여서 만듭니다.

```
def 함수이름(**매개변수):
    코드
```
"""


def order(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{k} {v}")


order(first="짜장면", second="북경오리", third="짱아찌")

"""매개변수 이름은 원하는 대로 지어도 되지만 관례적으로 keyword arguments를 줄여서 kwargs로 사용합니다.
특히 이 kwargs는 딕셔너리라서 for로 반복할 수 있습니다."""

"""인수 함수를 만들 수 있습니다. 그리고 이런 함수를 호출할 때는 키워드와 인수를 각각 넣거나 딕셔너리 언패킹을 사용하면 됩니다.

보통 **kwargs를 사용한 가변 인수 함수는 다음과 같이 함수 안에서 특정 키가 있는지 확인한 뒤 해당 기능을 만듭니다.
"""


def introduce(**kwargs):  # kw + args : kwargs (dictionary)
    if 'name' in kwargs:
        print(f"이름 : {kwargs['name']}")
    if 'age' in kwargs:
        print(f"나이 : {kwargs['age']}")
    if 'address' in kwargs:
        print(f"주소 : {kwargs['address']}")


# introduce(**a)
introduce(name="붕붕이")

"""### 고정 인수와 가변 인수(키워드 인수)를 함께 사용하기

고정 인수와 가변 인수(키워드 인수)를 함께 사용할 때는 다음과 같이 고정 매개변수를 먼저 지정하고, 그 다음 매개변수에 **를 붙여주면 됩니다.
"""


# 고정 인수, 위치 가변 인수, 키워드 가변 인수
# (아무것도X), *붙은거, **붙은거.
def my_fun(param1, param2, *args, **kwargs):
    pass


"""단, 이때 `def personal_info(**kwargs, name):`처럼 `**kwargs`가 고정 매개변수보다 앞쪽에 오면 안 됩니다. 매개변수 순서에서 `**kwargs`는 반드시 가장 뒤쪽에 와야 합니다.

### 위치 인수와 키워드 인수를 함께 사용하기

함수에서 위치 인수를 받는 `*args`와 키워드 인수를 받는 `**kwargs`를 함께 사용할 수도 있습니다. 대표적인 함수가 print인데 print는 출력할 값을 위치 인수로 넣고 sep, end 등을 키워드 인수로 넣습니다. 다음과 같이 함수의 매개변수를 `*args`, `**kwargs`로 지정하면 위치 인수와 키워드 인수를 함께 사용합니다.
"""

import random


def game(start, end, *args, multiple=2, **kwargs):
    # 플레이어의 이름을 받고, name
    if 'name' not in kwargs:
        return print("이름을 입력해주세요!")
    # 플레이어가 지불한 금액. money
    if 'money' not in kwargs:
        return print("금액을 지불해주세요!")
    if not len(args):
        return print("당첨 숫자를 입력해주세요!")
    # start, end(포함)는 수를 뽑는 범위
    number = random.choice(range(start, end + 1))
    # for i in range(start, end+1):
    #     # args를 당첨 숫자들
    # if i in args:
    #     print(f"당첨되었습니다! {i} / \\{kwargs['money'] * 2}")
    if number in args:
        print(f"{kwargs['name']}님, 당첨되었습니다! {number} / \\{kwargs['money'] * 2:.2f}")
        return kwargs['money'] * multiple
    else:
        print(f"실패입니다! {number}")
        return 0


game(1, 6)
game(start=1, end=6)
game(1, 6, name="만렙토끼")
game(1, 6, name="만렙토끼", money=10000)
game(1, 6, 3, name="만렙토끼", money=10000)
game(1, 6, 1, 2, 3, 4, 5, 6, name="만렙토끼", money=10000)
game(1, 6, *(1, 2, 3, 4, 5, 6), name="만렙토끼", money=10000)
game(1, 6, multiple=10)
"""```
단, 이때 def custom_print(**kwargs, *args):처럼
**kwargs가 *args보다 앞쪽에 오면 안 됩니다.
매개변수 순서에서 **kwargs는 반드시 가장 뒤쪽에 와야 합니다.

특히 고정 매개변수와 *args, **kwargs를 함께 사용한다면
def custom_print(a, b, *args, **kwargs):처럼
매개변수는 고정 매개변수, *args, **kwargs 순으로 지정해야 합니다.
```

## 매개변수에 초깃값 지정하기

지금까지 함수를 호출할 때 항상 인수를 넣어서 값을 전달했습니다. 그러면 인수를 생략할 수는 없을까요? 이때는 함수의 매개변수에 초깃값을 지정하면 됩니다. 초깃값은 다음과 같이 함수를 만들 때 매개변수=값 형식으로 지정합니다.

```
def 함수이름(매개변수=값):  # 해당 매개변수 이름 혹은 위치에 해당하는 전달받은 인지가 없다면...
    코드
```

함수이름(...) -> 먼저 준비가 되고...
=> 바깥에서 함수호출 시 함수이름(...) => 덮어씌우는 형태.

매개변수의 초깃값은 주로 사용하는 값이 있으면서 가끔 다른 값을 사용해야 할 때 활용합니다. 대표적인 예가 print 함수인데, print 함수의 sep는 초깃값이 ' '(공백)으로 지정되어 있어서 대부분 그대로 사용하고, 가끔 sep에 다른 값을 넣어서 사용합니다.
"""


def greeting(word="안녕! 좋은 아침이야"):
    print(word)


greeting()
greeting("좋은 아침은 무슨~")
greeting(word="좋은 아침은 무슨~")

# 매개변수에 초깃값이 지정되어 있더라도 값을 넣으면 해당 값이 전달됩니다.

"""### 초깃값이 지정된 매개변수의 위치

매개변수의 초깃값을 지정할 때 한 가지 주의할 점이 있습니다. 초깃값이 지정된 매개변수 다음에는 초깃값이 없는 매개변수가 올 수 없습니다.
"""

"""초깃값이 지정된 매개변수는 뒤쪽에 몰아주면 됩니다.
```
def personal_info(name, age, address='비공개'):
def personal_info(name, age=0, address='비공개'):
def personal_info(name='비공개', age=0, address='비공개'):
# def 함수명(기본값이없는매개변수, *위치가변인자매개변수, 기본값이있는매개변수=(기본값), **키워드가변인자매개변수)
```

# 람다 표현식

람다 표현식은 식 형태로 되어 있다고 해서 람다 표현식(lambda expression)이라고 부릅니다.
특히 람다 표현식은 함수를 간편하게 작성할 수 있어서 다른 함수의 인수로 넣을 때 주로 사용합니다.

## 람다 표현식으로 함수 만들기
"""


def plus_ten(x):
    return x + 10


print(plus_ten(1))

"""람다 표현식은 다음과 같이 lambda에 매개변수를 지정하고 :(콜론) 뒤에 반환값으로 사용할 식을 지정합니다.

* `lambda 매개변수들: 식`
"""
plus_ten = lambda x: x + 10
print(plus_ten)
print(plus_ten(100))

"""실행을 해보면 함수 객체가 나오는데, 이 상태로는 함수를 호출할 수 없습니다. 왜냐하면 람다 표현식은 이름이 없는 함수를 만들기 때문입니다. 그래서 람다 표현식을 익명 함수(anonymous function)로 부르기도 합니다.

lambda로 만든 익명 함수를 호출하려면 다음과 같이 람다 표현식을 변수에 할당해주면 됩니다.
"""

"""### 람다 표현식 자체를 호출하기

람다 표현식은 변수에 할당하지 않고 람다 표현식 자체를 바로 호출할 수 있습니다. 다음과 같이 람다 표현식을 ( )(괄호)로 묶은 뒤에 다시 ( )를 붙이고 인수를 넣어서 호출하면 됩니다.

* `(lambda 매개변수들: 식)(인수들)`
"""

print((lambda x: x + 10)(150))

"""### 람다 표현식 안에서는 변수를 만들 수 없다
# 할당 연산자를 사용할 수 X
람다 표현식에서 주의할 점은 람다 표현식 안에서는 새 변수를 만들 수 없다는 점입니다. 따라서 반환값 부분은 변수 없이 식 한 줄로 표현할 수 있어야 합니다. 변수가 필요한 코드일 경우에는 def로 함수를 작성하는 것이 좋습니다.
"""
# print((lambda x: y = 10; x + y)(1))
# SyntaxError: invalid syntax

y = 10
print((lambda x: x + y)(10))
# 단, 람다 표현식 바깥에 있는 변수는 사용할 수 있습니다.

"""### 람다 표현식을 인수로 사용하기

람다 표현식을 사용하는 이유는 함수의 인수 부분에서 간단하게 함수를 만들기 위해서 입니다. 이런 방식으로 사용하는 대표적인 예가 map입니다.
"""
# map -> 입력 -> input().split() => int => 괄호를 넣은 인트가 아니라 int를 집어넣었다 => 아직 실행하지 않은 준비 상태의 함수
# 소괄호를 붙이지 않으면 = 람다 상태와 유사.

a = range(10)  # 2배로 만들어준다
a2 = [i * 2 for i in a]
print(f"a2 : {a2}")
a3 = list(map(lambda x: x * 2, a))  # 요소는 순차적으로 1개씩
print(f"a3 : {a3}")

print((lambda: 100)())
x = 10
y = 10
print((lambda: x + y)())
print((lambda x, y: x + y)(10, 100))