"""
# 클래스

클래스는 객체를 표현하기 위한 문법입니다.
예를 들어 게임을 만든다고 하면 기사, 마법사, 궁수, 사제 등 직업별로 클래스를 만들어서 표현할 수 있습니다.

물론 집, 자동차, 나무 등도 클래스로 표현할 수 있습니다.
특히 프로그래밍에서는 현실 세계에 있는 개념들뿐만 아니라 컴퓨터 안에서만 쓰이는 개념들도 클래스로 만들어서 표현합니다. 웹 브라우저에서 내용이 길어지면 보이는 스크롤 바, 프로그램에서 주로 볼 수 있는 버튼, 체크 박스 등이 대표적입니다.

지금까지 나온 기사, 마법사, 궁수, 사제, 집, 자동차, 나무, 스크롤 바,
버튼, 체크 박스처럼 특정한 개념이나 모양으로 존재하는 것을 객체(object)라고 부릅니다.
그리고 프로그래밍으로 객체를 만들 때 사용하는 것이 클래스입니다.

그럼 게임의 기사 캐릭터를 클래스로 표현하려면 무엇이 필요할까요? 간단합니다.
일단 게임 캐릭터는 체력, 마나, 물리 공격력, 주문력 등이 필요합니다.
그리고 기사 캐릭터는 칼로 베기, 찌르기 등의 스킬이 있어야 합니다.

여기서 체력, 마나, 물리 공격력, 주문력 등의 데이터를 클래스의 속성(attribute)이라
부르고, 베기, 찌르기 등의 기능을 메서드(method)라고 부릅니다.

이렇게 프로그래밍 방법을 객체지향(object oriented) 프로그래밍이라고 합니다.
객체지향 프로그래밍은 복잡한 문제를 잘게 나누어 객체로 만들고, 객체를 조합해서 문제를 해결합니다.
따라서 현실 세계의 복잡한 문제를 처리하는데 유용하며
기능을 개선하고 발전시킬 때도 해당 클래스만 수정하면 되므로 유지 보수에도 효율적입니다.

지금까지 숫자 1, 2, 3 문자 'a', 'b', 'c', 리스트, 딕셔너리 등을 조합해서 프로그램을 만들었는데
사실 파이썬에서는 이 모든 것이 객체입니다. 이번에는 클래스를 사용해서 객체를 표현하고 만드는 방법을 알아보겠습니다.

## 클래스와 메서드 만들기

클래스는 class에 클래스 이름을 지정하고 :(콜론)을 붙인 뒤 다음 줄부터 def로 메서드를 작성하면 됩니다. 여기서 메서드는 클래스 안에 들어있는 함수를 뜻합니다.

클래스 이름을 짓는 방법은 변수와 같습니다. 보통 파이썬에서는 클래스의 이름은 대문자로 시작합니다. 그리고 메서드 작성 방법은 함수와 같으며 코드는 반드시 들여쓰기를 해야 합니다(들여쓰기 규칙은 if, for, while과 같습니다). 특히 메서드의 첫 번째 매개변수는 반드시 self를 지정해야 합니다.

```
class 클래스이름:
    def 메서드(self):
        코드
```
"""

class MyClass:
    def hello(self):
        # print("안녕하세요!")
        print("안녕히계세요!")

mc = MyClass()  # 함수마냥 '실행' -> 생성
mc.hello() # -> 해당 클래스에 소속(소유)된 기능

"""그럼 이 클래스를 사용해봐야겠죠? 다음과 같이 클래스에 ()(괄호)를 붙인 뒤 변수에 할당합니다.

* `인스턴스 = 클래스()`
# 클래스 B를 통해서 객체 A를 만들면, (A) A라는 객체는, 클래스 B에 의해서 생성된 인스턴스다.
"""


"""Person으로 변수 james를 만들었는데 이 james가 Person의 인스턴스(instance)입니다.
클래스는 특정 개념을 표현만 할뿐 사용을 하려면 인스턴스를 생성해야 합니다.

### 메서드 호출하기

이제 메서드를 호출해보겠습니다. 메서드는 클래스가 아니라 인스턴스를 통해 호출합니다. 다음과 같이 인스턴스 뒤에 .(점)을 붙이고 메서드를 호출하면 됩니다.

* `인스턴스.메서드()`
"""
# 문자열, 리스트 => 객체.(기능)()


"""인스턴스를 통해 호출하는 메서드를 인스턴스 메서드라고 부릅니다.

### 파이썬에서 흔히 볼 수 있는 클래스

지금까지 사용한 int, list, dict 등도 사실 클래스입니다.
우리는 이 클래스로 인스턴스를 만들고 메서드를 사용했습니다.
"""



"""파이썬에서는 자료형도 클래스입니다.
다음과 같이 type을 사용하면 객체(인스턴스)가 어떤 클래스인지 확인할 수 있습니다.

* `type(객체)`
"""

print(type(MyClass))  # <class 'type'>
print(type([])) # <class 'list'>
print(type({})) # <class 'dict'>


"""### 인스턴스와 객체의 차이점?

클래스는 객체를 표현하는 문법이라고 했는데,
클래스로 인스턴스를 만든다고 하니 좀 헷갈리죠? 사실 인스턴스와 객체는 같은 것을 뜻합니다.
보통 객체만 지칭할 때는 그냥 객체(object)라고 부릅니다.
하지만 클래스와 연관지어서 말할 때는 인스턴스(instance)라고 부릅니다.
그래서 다음과 같이 리스트 변수 a, b가 있으면 a, b는 객체입니다.
그리고 a와 b는 list 클래스의 인스턴스입니다.
"""



"""### 빈 클래스 만들기"""

# 내용이 없는 빈 클래스를 만들 때는 코드 부분에 pass를 넣어줍니다.

class Empty:
    pass # pass.

"""### 메서드 안에서 메서드 호출하기

메서드 안에서 메서드를 호출할 때는 다음과 같이 self.메서드() 형식으로 호출해야 합니다. self 없이 메서드 이름만 사용하면 클래스 바깥쪽에 있는 함수를 호출한다는 뜻이 되므로 주의해야 합니다.
"""

class FishBread:
    def eat(self):
        print("냠냠")

    def sound(self):
        print("붕어빵 먹는 소리")
        # self -> 이 클래스를 통해서 만들어진 객체(인스터스)가 갖고 있는 데이터와 기능
        self.eat()

bread = FishBread()
bread.sound()



"""### 특정 클래스의 인스턴스인지 확인하기

현재 인스턴스가 특정 클래스의 인스턴스인지 확인할 때는 isinstance 함수를 사용합니다. 특정 클래스의 인스턴스가 맞으면 True, 아니면 False를 반환합니다.

* `isinstance(인스턴스, 클래스)`
"""
print(isinstance(bread, FishBread))
print(isinstance([], FishBread))
print(isinstance([], list))

"""isinstance는 주로 객체의 자료형을 판단할 때 사용합니다. 예를 들어 팩토리얼 함수는 1부터 n까지 양의 정수를 차례대로 곱해야 하는데, 실수와 음의 정수는 계산할 수 없습니다. 이런 경우에 isinstance를 사용하여 숫자(객체)가 정수일 때만 계산하도록 만들 수 있습니다."""

# n! = n * (n-1)! = ... = n * ... * 1
# factorial 자연수 -> int
def factorial(n):
    print(n, end=' ')
    if n == 1 : return 1
    return n * factorial(n-1)

print(factorial(10))
# print(factorial("1234"))  # TypeError: unsupported operand type(s) for -: 'str' and 'int'

def factorial2(n):
    if not isinstance(n, int):
        print("정수가 아닙니다")
        return 0
    print(n, end=' ')
    if n == 1 : return 1
    return n * factorial(n-1)
print(factorial2("1234"))

"""## 속성 사용하기

지금까지 클래스에서 메서드를 만들고 호출해보았습니다.
이번에는 클래스에서 속성을 만들고 사용해보겠습니다.
속성(attribute)을 만들 때는 `__init__` 메서드 안에서 self.속성에 값을 할당합니다.

```
class 클래스이름:
    def __init__(self):
        self.속성 = 값
```
"""

class Student:
    def __init__(self):  # __init__ -> 자동으로 실행
        # class -> 클래스명() -> 생성자
        print("Student가 생성되었습니다!")
        # self -> 클래스로 생성된 자기 자신
        # self.변수명 -> 클래스로 생성된 객체(인스턴스)에 소속된 변수 == 속성을 대입.
        # self.name = "아메리카노"
        self.name = "투샷아메리카노"

s = Student()  # Student 클래스로, 인스턴스를 생성해서 객체를 s라는 변수에 할당
print(s.name)

"""```
__init__ 메서드는 james = Person()처럼 클래스에 ( )(괄호)를 붙여서 인스턴스를 만들 때 호출되는 특별한 메서드입니다.
즉, __init__(initialize)이라는 이름 그대로 인스턴스(객체)를 초기화합니다.

특히 이렇게 앞 뒤로 __(밑줄 두 개)가 붙은 메서드는 파이썬이 자동으로 호출해주는 메서드인데,
스페셜 메서드(special method) 또는 매직 메서드(magic method)라고 부릅니다.
앞으로 파이썬의 여러 가지 기능을 사용할 때 이 스페셜 메서드를 채우는 식으로 사용하게 됩니다.
```

```
속성은 __init__ 메서드에서 만든다는 점과 self에 .(점)을 붙인 뒤 값을 할당(=)한다는 점이 중요합니다.
클래스 안에서 속성을 사용할 때도 self.hello처럼 self에 점을 붙여서 사용하면 됩니다.
```
"""

kim = Student()
print(f"kim.name {kim.name}")
kim.name = "김커피"  # 외부에서도 새로운 값을 할당
print(f"kim.name {kim.name}")

lee = kim  # 할당
print(f"lee.name {lee.name}")
lee.name = "이커피"
print(f"lee.name {lee.name}")
print(f"kim.name {kim.name}")
# 할당 -> 객체 = 컴퓨터에 저장되어있는 데이터 => 할당 (주소값)
# kim.copy()
import copy
# 클래스를 통해서 직접 객체를 만들어서 사용하는 경우, 복사시에는 할당이 아니라 import copy
park = copy.copy(lee)
print(park.name)
park.name = "박커피"
print(park.name)
print(lee.name)

park.name = ["박", "커피"]  # 객체
# choi = copy.copy(park)
choi = copy.deepcopy(park)
print(choi.name)
choi.name.append("최")
print(choi.name)
print(park.name)
# deepcopy > copy : 더 많은 cpu 자원.
"""

### self의 의미

그런데 도데체 self는 뭘까요? self는 인스턴스 자기 자신을 의미합니다.
우리는 인스턴스가 생성될 때 self.hello = '안녕하세요.'처럼 자기 자신에 속성을 추가했습니다.
여기서 `__init__`의 매개변수 self에 들어가는 값은 Person()이라 할 수 있습니다.
그리고 self가 완성된 뒤 james에 할당됩니다. 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어옵니다.
그래서 greeting 메서드에서 print(self.hello)처럼 속성을 출력할 수 있었던 것입니다.

### 인스턴스를 만들 때 값 받기

`__init__` 메서드에서 self 다음에 값을 받을 매개변수를 지정합니다. 그리고 매개변수를 self.속성에 넣어줍니다.

```
class 클래스이름:
    def __init__(self, 매개변수1, 매개변수2):
        self.속성1 = 매개변수1
        self.속성2 = 매개변수2
```
"""

class Store:
    def __init__(self):
        self.title = "중화반점"
        self.menu = ["소꼬리무침", "가지무침", "계란프라이스테이크"]
        self.location = "신대방삼거리점"

store1 = Store()  # 신대방삼거리점
print(store1.title, store1.menu, store1.location)
store2 = Store()  # 보라매점
print(store2.title, store2.menu, store2.location)
store2.location = "보라매점"
print(store2.title, store2.menu, store2.location)

class Store:
    def __init__(self, location):  # self <- 건들지 않는 선에서....
        # 외부에서 주입하고 싶은, 전달받고 싶은... 매개변수
        self.title = "중화반점"
        self.menu = ["소꼬리무침", "가지무침", "계란프라이스테이크"]
        # self.location = "신대방삼거리점"
        self.location = location

# store1 = Store("신대방삼거리점")
store1 = Store(location="신대방삼거리점")  # 신대방삼거리점
print(store1.title, store1.menu, store1.location)
store2 = Store(location="보라매점")  # 보라매점
print(store2.title, store2.menu, store2.location)
# store2.location = "보라매점"
# print(store2.title, store2.menu, store2.location)
store3 = Store(location="대방점")  # 보라매점
print(store3.title, store3.menu, store3.location)

"""### 클래스의 위치 인수, 키워드 인수

클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수를 사용할 수 있습니다. 규칙은 함수와 같습니다. 위치 인수와 리스트 언패킹을 사용하려면 다음과 같이 *args를 사용하면 됩니다. 이때 매개변수에서 값을 가져오려면 args[0]처럼 사용해야 합니다.
"""


# class 클래스명:
# (1) class (2) ' ' (3) 클래스명:
class BungeoppangStore:
    # 생성자 -> 매개변수들 전달 -> 내부의 속성(변수) 지정
    # 생성자 = 함수 -> 위치 인수, 가변 인수, 키워드 가변인수, 기본값...
    def __init__(self, name, *args, price=1200, **kwargs) -> None:
        self.name = name  # 필수
        self.menu = args  # 메뉴들
        self.price = price  # 기본값이 있어서 입력 안해줘도 됨
        self.visitors = kwargs

    def introduce(self):
        print(f"안녕하세요 여러분! {self.name} 붕어빵 가게가 오픈했습니다")
        for i in self.menu:
            print(f"저희는 {i} 메뉴가 있습니다")

    # def sell(self, visitor):
    #     if visitor in self.visitors:
    #         print(f"단골은 반값이에요! {self.price // 2}원만 내세요")
    #         # self.visitors[visitor] += self.price // 2
    #         self.visitors.update({visitor :
    #                              self.visitors[visitor] + (self.price // 2)})
    #         return
    #     self.visitors[visitor] = self.price
    #     print("처음 방문이시네요~ 자주 오세요!")

    def sell(self, visitor, item="치약붕어빵"):
        if item not in self.menu:
            print(f"{item}은 판매하는 메뉴중에 없습니다!")
            return
        if item == '치약붕어빵':
            print(f"오늘 재료소진으로 치약붕어빵은 마감입니다")
            return
        if visitor in self.visitors:  # 딕셔너리 (visitors) -> keys
            print(f"단골은 반값이에요! {self.price // 2}원만 내세요")
            # self.visitors[visitor] += self.price // 2
            self.visitors.update({visitor:
                                      self.visitors[visitor] + (self.price // 2)})
            return
        self.visitors[visitor] = self.price
        print("처음 방문이시네요~ 자주 오세요!")

"""키워드 인수와 딕셔너리 언패킹을 사용하려면 다음과 같이 **kwargs를 사용하면 됩니다. 이때 매개변수에서 값을 가져오려면 kwargs['name']처럼 사용해야 합니다."""

store1 = BungeoppangStore('민트초코붕어빵 1호점', # name
                          '치약붕어빵', '번데기붕어빵', '취두부붕어빵', # 가변인수 -> 여러 메뉴
                          price=2000,  # 1200 -> 2000.
                          james=5000, john=2000, kate=500  # 키워드가변인자 => kwargs => 방문자리스트
                          )
print(store1.visitors, store1.menu, store1.price)
store1.introduce()
store1.sell('dongdong')
store1.sell('dongdong', '마약붕어빵')
# https://sharegpt.com/c/ms0PWXZ

"""### 인스턴스를 생성한 뒤에 속성 추가하기, 특정 속성만 허용하기

지금까지 클래스의 인스턴스 속성은 `__init__` 메서드에서 추가한 뒤 사용했습니다.
하지만 클래스로 인스턴스를 만든 뒤에도 인스턴스.속성 = 값 형식으로 속성을 계속 추가할 수 있습니다.
다음 Person 클래스는 빈 클래스이지만 인스턴스를 만든 뒤 name 속성을 추가합니다.
"""



# 이렇게 추가한 속성은 해당 인스턴스에만 생성됩니다.
# 따라서 클래스로 다른 인스턴스를 만들었을 때는 추가한 속성이 생성되지 않습니다.

# 인스턴스는 생성한 뒤에 속성을 추가할 수 있으므로 __init__ 메서드가 아닌
# 다른 메서드에서도 속성을 추가할 수 있습니다. 단, 이때는 메서드를 호출해야 속성이 생성됩니다.


"""## 클래스 속성과 인스턴스 속성 알아보기

속성에는 클래스 속성과 인스턴스 속성 두 가지 종류가 있습니다. `__init__` 메서드에서 만들었던 속성은 인스턴스 속성입니다.

### 클래스 속성 사용하기

"""

class Store:
    name = "붕어빵 가게"  # class에 공통으로 존재 # 클래스 변수들
    def __init__(self, name="붕어빵 스토어"):
        # self에 아무것도 대입이 되지 않았다면... 자체 Class에 소속된 -> 클래스 변수들이 먼저 할당.
        # self.... -> 필요한 변수들을 넣어서.
        # self.속성 => 인스턴스 속성 => 변수 -> 인스턴스(객체) => 개별적으로 존재하는...
        print(f"(1) self.name : {self.name}")
        self.name = name
        print(f"(2) self.name : {self.name}")
        print(f"Store.name : {Store.name}")

s1 = Store()
print(f"(3) name : {s1.name}")
"""


```
class 클래스이름:
    속성 = 값
```
"""



"""put_bag 메서드에서 클래스 속성 bag에 접근할 때 self를 사용했습니다.
사실 self는 현재 인스턴스를 뜻하므로 클래스 속성을 지칭하기에는 조금 모호합니다."""



"""그래서 클래스 속성에 접근할 때는 다음과 같이 클래스 이름으로 접근하면 좀 더 코드가 명확해집니다.

* `클래스.속성`
"""



"""Person.bag이라고 하니 클래스 Person에 속한 bag 속성이라는 것을 바로 알 수 있습니다.
마찬가지로 클래스 바깥에서도 다음과 같이 클래스 이름으로 클래스 속성에 접근하면 됩니다."""



"""### 인스턴스 속성 사용하기"""

class Car:
    brand = "기아"
    def __init__(self, owner):
        self.owner = owner
        print(f"이 차의 브랜드는 {Car.brand}이고, 주인은 {self.owner}입니다")
car1 = Car("김코딩")
car2 = Car("이코딩")
car3 = Car("박코딩")

"""* 클래스 속성: 모든 인스턴스가 공유. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
* 인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용

## 클래스 상속 사용하기

지금까지 클래스의 기본적인 사용 방법을 알아보았습니다. 이번에는 클래스 상속(inheritance)을 사용해보겠습니다.

상속은 무언가를 물려받는다는 뜻입니다. 그래서 클래스 상속은 물려받은 기능을 유지한채로 다른 기능을 추가할 때 사용하는 기능입니다. 여기서 기능을 물려주는 클래스를 기반 클래스(base class), 상속을 받아 새롭게 만드는 클래스를 파생 클래스(derived class)라고 합니다.

보통 기반 클래스는 부모 클래스(parent class), 슈퍼 클래스(superclass)라고 부르고, 파생 클래스는 자식 클래스(child class), 서브 클래스(subclass)라고도 부릅니다.

클래스 상속은 생물 분류를 떠올리면 이해하기 쉽습니다. 예를 들어 조류, 어류는 공통된 조상인 척추동물로부터 물려받은 특성을 공유하면서 각자 고유한 특성을 가집니다. 척추를 가졌다는 특성은 변함이 없지만 날개를 가졌으면 조류, 물속에 살면 어류인 식입니다. 즉, 같은 계통으로 특성을 공유하며 전혀 상관없이 어류가 꽃식물의 특성을 가지지는 않습니다.

마찬가지로 클래스 상속도 기반 클래스의 능력을 그대로 활용하면서 새로운 클래스를 만들 때 사용합니다. 동물을 예로 들면 척추동물에서 포유류, 조류, 파충류 등을 만드는 식이죠.

그런데 그냥 새로운 클래스를 만들면 되지 왜 이런 상속 개념을 만들었을까요? 만약 새로운 기능이 필요할 때마다 계속 클래스를 만든다면 중복되는 부분을 반복해서 만들어야 합니다. 이럴 때 상속을 사용하면 중복되는 기능을 만들지 않아도 됩니다. 따라서 상속은 기존 기능을 재사용할 수 있어서 효율적입니다.

클래스 상속은 다음과 같이 클래스를 만들 때 ( )(괄호)를 붙이고 안에 기반 클래스 이름을 넣습니다.

```
class 기반클래스이름:
    코드

class 파생클래스이름(기반클래스이름):
    코드
```
"""

# 상속 -> 클래스 (재사용)
class Car:
    def __init__(self):
        self.fuel = "기름"
    def drive(self):
        print(f"{self.fuel}(으)로 갑니다")

c1 = Car()
c1.drive()

class EletricCar(Car):  # 이미 만들어놓은 걸 가지고 와서 재사용
    def __init__(self):
        self.fuel = '전기'  # fuel 연료
    def charge(self):
        print("전기를 충전합니다!")

c2 = EletricCar()
c2.drive()  # Car -> EletricCar (상속)
c2.charge()

class HydrogenCar(Car):  # 이미 만들어놓은 걸 가지고 와서 재사용
    def __init__(self):
        self.fuel = '수소'  # fuel 연료

c3 = HydrogenCar()
c3.drive()  # Car -> EletricCar (상속)


"""이처럼 클래스 상속은 기반 클래스의 기능을 유지하면서 새로운 기능을 추가할 수 있습니다.
특히 클래스 상속은 연관되면서 동등한 기능일 때 사용합니다.
즉, 학생은 사람이므로 연관된 개념이고, 학생은 사람에서 역할만 확장되었을 뿐 동등한 개념입니다.
-> 차 -> 전기차, 수소차, 기름차... 
## 기반 클래스의 속성 사용하기

이번에는 기반 클래스에 들어있는 인스턴스 속성을 사용해보겠습니다.
다음과 같이 Person 클래스에 hello 속성이 있고, Person 클래스를 상속받아 Student 클래스를 만듭니다.
그다음에 Student로 인스턴스를 만들고 hello 속성에 접근해봅니다.
"""
class Programmer:
    def __init__(self):  # 생성자가...
        print("Programmer __init__")
        self.habit = "머리를 쥐어 뜯는다"
        self.money = 20000

class PythonProgrammer(Programmer):
    # Programmer.__init__ -> 새롭게 정의한 __init__ 덮어씌워지기 => 오버라이딩
    def __init__(self, habit):  # <- 여기에도 들어가는 거 아냐?
        print("PythonProgrammer __init__")
        # 오버라이딩 -> 같은 이름의 메소드(함수)를 재정의.
        self.habit = habit

kim = Programmer()
print(kim.habit, kim.money)
# lee = PythonProgrammer()
lee = PythonProgrammer("콧잔등 긁기")
# TypeError: PythonProgrammer.__init__() missing 1 required positional argument: 'habit'
# 'PythonProgrammer' object has no attribute 'money'
# print(lee.habit, lee.money)



"""```
실행을 해보면 에러가 발생합니다.
왜냐하면 기반 클래스 Person의 __init__ 메서드가 호출되지 않았기 때문입니다.
실행 결과를 잘 보면 'Student __init__'만 출력되었습니다.

즉, Person의 __init__ 메서드가 호출되지 않으면,
self.hello = '안녕하세요.'도 실행되지 않아서 속성이 만들어지지 않습니다.
```

### super()로 기반 클래스 초기화하기

이때는 super()를 사용해서 기반 클래스의 __init__ 메서드를 호출해줍니다. 다음과 같이 super() 뒤에 .(점)을 붙여서 메서드를 호출하는 방식입니다.

* `super().메서드()`
"""

print("----------------------")
class PythonProgrammer(Programmer):
    # Programmer.__init__ -> 새롭게 정의한 __init__ 덮어씌워지기 => 오버라이딩
    def __init__(self, habit):  # <- 여기에도 들어가는 거 아냐?
        # Programmer
        super().__init__()  # self와 연결이 되어서... # Programmer __init__
        print(self.money, self.habit)
        print("PythonProgrammer __init__")
        # 오버라이딩 -> 같은 이름의 메소드(함수)를 재정의.
        self.habit = habit
lee = PythonProgrammer("콧잔등 긁기")
print(lee.habit, lee.money)

"""### 기반 클래스를 초기화하지 않아도 되는 경우 # super().__init__() 

`만약 파생 클래스에서 __init__ 메서드를 생략한다면 기반 클래스의 __init__이 자동으로 호출되므로 super()는 사용하지 않아도 됩니다.`
"""



"""### 좀 더 명확하게 super 사용하기

super는 다음과 같이 파생 클래스와 self를 넣어서 현재 클래스가 어떤 클래스인지 명확하게 표시하는 방법도 있습니다. 물론 super()와 기능은 같습니다.

* `super(파생클래스, self).메서드`
"""

class Human:
    def run(self):
        print("달려간다")

class MetaHuman(Human):
    def run(self):
        super().run()
        print("나는 MetaHuman, 더 빠르게 달려간다")
'''
달려간다
더 빠르게 달려간다
'''
print("m = MetaHuman()")
m = MetaHuman()
m.run()

class MetaMetaHuman(MetaHuman):
    def run(self):
        # super().run() # MetaHuman run
        # super(MetaMetaHuman, self).run() # MetaHuman run
        # Human run
        super(MetaHuman, self).run() # MetaHuman(Human):
        print("상당히 더 빠르게 달려간다")
'''
달려간다
상당히 더 빠르게 달려간다
'''
print("joy = MetaMetaHuman()")
joy = MetaMetaHuman()
joy.run()

"""## 메서드 오버라이딩 사용하기
-> 같은 이름의 새로운 함수(메소드)를 지정해서 다른 용도로 메소드를 사용하는 것

이번에는 파생 클래스에서 기반 클래스의 메서드를 새로 정의하는 메서드 오버라이딩에 대해 알아보겠습니다.
다음과 같이 Person의 greeting 메서드가 있는 상태에서 Student에도 greeting 메서드를 만듭니다.
"""



"""오버라이딩(overriding)은 무시하다, 우선하다라는 뜻을 가지고 있는데
말 그대로 기반 클래스의 메서드를 무시하고 새로운 메서드를 만든다는 뜻입니다.
여기서는 Person 클래스의 greeting 메서드를 무시하고 Student 클래스에서 새로운 greeting 메서드를 만들었습니다.

그럼 메서드 오버라이딩은 왜 사용할까요?
보통 프로그램에서 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할 때 메서드 오버라이딩을 활용합니다.

기반 클래스의 메서드를 재활용하면 중복을 줄일 수 있습니다.
다음과 같이 오버라이딩된 메서드에서 super()로 기반 클래스의 메서드를 호출해봅니다.
"""

# 상속 -> 상호호환성
class Flight: # 프로펠러 비행기
    def fly(self):
        print("프로펠러로 난다")

class LuxuryFlight(Flight):  # 고급 비행기
    pass  # 상속받은 그대로...

class ZetFlight(Flight):
    def fly(self):  # 오버라이딩
        print("제트엔진으로 난다")

f1 = Flight()  # 원본
f2 = ZetFlight() # 건들였지만 fly라는 기능이 최소 있을 것...
f3 = LuxuryFlight() # 이름만 -> 안 건들였음
flight_list = [f1, f2, f3]

for f in flight_list: # 비행기 리스트
    f.fly()  # 비행 -> fly라는 기능은 존재한다