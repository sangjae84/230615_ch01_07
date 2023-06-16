"""
# 예외 처리

예외(exception)란 코드를 실행하는 중에 발생한 에러를 뜻합니다.
다음과 같이 10을 어떤 값으로 나누는 함수 ten_div가 있을 때
인수에 따라 정상으로 동작하기도 하고 에러가 나기도 합니다.
"""

# print(10 / 0)  # ZeroDivisionError: division by zero

def ten_div(x):
    return 10 / x

print(ten_div(10))
print(ten_div(2))
# print(ten_div(0))  # ZeroDivisionError: division by zero




"""ZeroDivisionError뿐만 아니라 지금까지 만난 AttributeError,
NameError, TypeError 등 다양한 에러들도 모두 예외입니다. (Exception)
-> 예외(에러) => 더 이상 파이썬의 실행 X

이번에는 예외가 발생했을 때도 스크립트 실행을 중단하지 않고
계속 실행하게 해주는 예외 처리 방법에 대해 알아보겠습니다.

## try except로 사용하기

예외 처리를 하려면 다음과 같이 try에 실행할 코드를 넣고 except에 예외가 발생했을 때 처리하는 코드를 넣습니다.

```
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
```
"""
# try except. -> try catch?
def ten_div2(x):
    try:
        return 10 / x  # 시도 -> 에러가 나면 except라는 블록으로 이동
    except:
        print("에러가 났습니다!")
        return 0

print(ten_div2(10))
print(ten_div2(0))

"""### 특정 예외만 처리하기

이번에는 except에 예외 이름을 지정해서 특정 예외가 발생했을 때만 처리 코드를 실행하도록 만들어보겠습니다.

```
try:
    실행할 코드
except 예외이름:
    예외가 발생했을 때 처리하는 코드
```
"""

# ten_div("10")  # TypeError: unsupported operand type(s) for /: 'int' and 'str'
ten_div2("10") # 어떤 에러든 상관없이 에러가 났습니다 ~ 0 return.

def ten_div3(x):
    try:
        return 10 / x  # 시도 -> 에러가 나면 except라는 블록으로 이동
    except ZeroDivisionError:
        print("0으로 나누려고 시도했습니다!")
        return -1
    except TypeError:
        print("문자열로 나누려고 시도했습니다!")
        return -2
    except:
        print("알 수 없는 에러입니다")
        return -3

ten_div3(0)
ten_div3("1")
ten_div3([])

"""### 예외의 에러 메시지 받아오기

특히 except에서 as 뒤에 변수를 지정하면 발생한 예외의 에러 메시지를 받아올 수 있습니다.

```
try:
    실행할 코드
except 예외 as 변수:
    예외가 발생했을 때 처리하는 코드
```

앞에서 만든 코드의 except에 as e를 넣습니다. 보통 예외( exception)의 e를 따서 변수 이름을 e로 짓습니다.
"""

def ten_div4(x):
    try:
        return 10 / x  # 시도 -> 에러가 나면 except라는 블록으로 이동
    except Exception as ex:
        print(ex)
        print(type(ex))
        return 0
ten_div4(0)
ten_div4("")

"""참고로 모든 예외의 에러 메시지를 출력하고 싶다면 다음과 같이 except에 Exception을 지정하고 as 뒤에 변수를 넣으면 됩니다.

```
except Exception as e:    # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
    print('예외가 발생했습니다.', e)
```

이처럼 예외 처리는 에러가 발생하더라도 스크립트의 실행을 중단시키지 않고 계속 실행하고자 할 때 사용합니다.

## else와 finally 사용하기

이번에는 예외가 발생하지 않았을 때 코드를 실행하는 else를 사용해보겠습니다. 다음과 같이 else는 except 바로 다음에 와야 하며 except를 생략할 수 없습니다.

```
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
```
"""
import random
r = random.randint(0, 1)
print("---------")
try:
    print(r)
    a = 10 / r
except:
    print("0이 뽑혔네요 ㅠㅠ")
else:
    print(f"a = 10 / r이면, a는 {a}")

"""### 예외와는 상관없이 항상 코드 실행하기

이번에는 예외 발생 여부와 상관없이 항상 코드를 실행하는 finally를 사용해보겠습니다. 특히 finally는 except와 else를 생략할 수 있습니다.

```
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    예외 발생 여부와 상관없이 항상 실행할 코드
```
"""

import random
r = random.randint(0, 1)
print("---------")
try:
    # 카드 거래 요청...
    print(r)
    a = 10 / r
except:
    # 이상 거래 -> 보고
    print("0이 뽑혔네요 ㅠㅠ")
else:
    # 돈이 차감
    print(f"a = 10 / r이면, a는 {a}")
finally:
    # 거래가 종료 -> 안내.
    print("안녕히계세요!")


"""## 예외 발생시키기

지금까지 숫자를 0으로 나눴을 때 에러, 리스트의 범위를 벗어난 인덱스에 접근했을 때 에러 등
파이썬에서 정해진 예외만 처리했습니다. 이번에는 우리가 직접 예외를 발생시켜 보겠습니다.

예외를 발생시킬 때는 raise에 예외를 지정하고 에러 메시지를 넣습니다(에러 메시지는 생략할 수 있음).

* `raise 예외('에러메시지')`
"""

# v = int(input("얼마를 투입하시겠나요?"))
# # 1000 이상 입력해야 작동
# try:
#     if v < 1000:
#         raise Exception("1000원 이상이어야 합니다")  # Exception: 1000원 이상이어야 합니다
#     print(f"{v}원을 입력하셨습니다")
# except:
#     print("1000원이 넘게 넣어주세요")

def my_fun():
    # 이 내부에서 다양한 에러나 처리가 발생.
    # raise 에러를 통해서 외부로 어떠한 상태를 알리는게 최선.
    return 1  # 한 개의 처리 값.

"""### raise의 처리 과정

이번에는 raise의 처리 과정을 알아보겠습니다. 다음은 함수 안에서 raise를 사용하지만 함수 안에는 try except가 없는 상태입니다
"""



"""안에 try except가 없는 상태에서 raise로 예외를 발생시켰습니다. 이렇게 되면 함수 바깥에 있는 except에서 예외가 처리됩니다. 즉, 예외가 발생하더라도 현재 코드 블록에서 처리해줄 except가 없다면 except가 나올 때까지 계속 상위 코드 블록으로 올라갑니다.

만약 함수 바깥에도 처리해줄 except가 없다면 코드 실행은 중지되고 에러가 표시됩니다.
"""



"""### 현재 예외를 다시 발생시키기

이번에는 try except에서 처리한 예외를 다시 발생시키는 방법입니다. except 안에서 raise를 사용하면 현재 예외를 다시 발생시킵니다(re-raise).

* `raise`
"""

# v = int(input("얼마를 투입하시겠나요?"))
# # 1000 이상 입력해야 작동
# try:
#     try:
#         if v < 1000:
#             raise Exception("1000원 이상이어야 합니다")  # Exception: 1000원 이상이어야 합니다
#         print(f"{v}원을 입력하셨습니다")
#     except Exception as e:
#         print("1000원이 넘게 넣어주세요")
#         raise e  # 여러 번 처리해야되는 에러
# except:
#     # 기록을 남기고 싶다던가... 추가적인 처리를 해줘야할때
#     print("에러가 발생 했었네요?")

"""함수 안에서 발생한 예외를 함수 안의 except에서 한 번 처리하고, raise로 예외를 다시 발생시켜서 상위 코드 블록으로 넘겼습니다. 그다음에 함수 바깥의 except에서 예외를 처리했습니다. 이런 방식으로 같은 예외를 계속 처리해줄 수 있습니다.

참고로 raise만 사용하면 같은 예외를 상위 코드 블록으로 넘기지만 raise에 다른 예외를 지정하고 에러 메시지를 넣을 수도 있습니다.

## 예외 만들기

프로그래머가 직접 만든 예외를 사용자 정의 예외라고 합니다.

예외를 만드는 방법은 간단합니다. 그냥 Exception을 상속받아서 새로운 클래스를 만들면 됩니다. 그리고 `__init__` 메서드에서 기반 클래스의 `__init__` 메서드를 호출하면서 에러 메시지를 넣어주면 됩니다.

```
class 예외이름(Exception):
    def __init__(self):
        super().__init__('에러메시지')
```
"""

class MyError(Exception):
    pass

class MyError2(Exception):  # 오버라이딩
    def __init__(self):
        super().__init__("강사님이 수업을 너무 길게 한다")  # 메시지

class MintNoNo(Exception):
    def __init__(self):
        super().__init__("감히 민트 초코를!")  # 메시지

order = input("민트초코 빼고 다 주문하세요! : ")
try:
    # raise MyError
    # raise MyError2
    if order == "민트초코":
        raise MintNoNo  # 에러가 발생한 순간 처리가 멈춤 (return)
    print(f"{order}를 맛있게 드세요!")
except Exception as e:
    print(e, type(e))
    print("*** 에러가 발생했습니다!")

"""참고로 다음과 같이 Exception만 상속받고 pass를 넣어서 아무것도 구현하지 않아도 됩니다."""



# 이때는 예외를 발생시킬 때 에러 메시지를 넣어주면 됩니다.