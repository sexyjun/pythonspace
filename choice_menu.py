#1. 햄버거 단품 메뉴 선택하는 매서드
def choice_burger():
    print('################################################')
    print('## burger menu')
    print('## 1.새우버거: 3000원')
    print('## 2.불고기버거: 2500원')
    print('## 3.치즈버거 : 3500원')
    print('################################################')
    print('## 원하시는 메뉴의 번호를 입력해주세요.')

    while True:
        choice_num = int(input('>>번호: '))
        if choice_num >= 1 and choice_num <= 3:
            break
        else:
            print('# msg: 1~3의 번호만 입력해주세요 :)')
    return choice_num

# 2. 사이드 단품 메뉴 선택하는 매서드
def choice_side():
    print('############################')
    print('## side menu')
    print('## 1. 프렌치프라이:1500원')
    print('## 2.치킨너겟: 2000원')
    print('## 원하시는 메뉴의 번호를 입력해주세요')
    print('################################')

    while True:
        choice_num2 = int(input('>> 번호: '))
        if 1 <= choice_num2 <= 2:
            break
        else:
            print('# msg: 1~2의 번호만 입력해주세요:)')
    return choice_num2

# 3. 음료 단푸 메뉴 선택하는 매서드
def choice_drink():
    print('#########################')
    print('## drink menu')
    print('## 1. 코카콜라: 1000원')
    print('## 2. 커피: 1200원')
    print('## 3. 주스 : 1500원')
    print('############################')

    while True:
        choice_num3 = int(input('>> 번호: '))
        if 1 <= choice_num3 <= 3:
            break
        else:
            print('# msg: 1~3의 번호만 입력해주세요:)')
