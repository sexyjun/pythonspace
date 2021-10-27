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
    return choice_num3

def choice_main():
    # >> view단: 메뉴 선택(최초)
    print('##################################################')
    print('## == cnu 버거 (ver.01) ==')
    print('## cnu 버거에 방문해주셔서 감사합니다.')
    print('##################################################')
    print('## 메뉴')
    print('## 1.햄버거 세트')
    print('## 2.햄버거 단품')
    print('## 3.사이드 메뉴')
    print('## 4.음료')
    print('##################################################')

    while True:
        print('## 원하시는 메뉴의 번호를 입력해주세요.')
        menu_num = int(input('>> 번호:'))  # 사용자로부터 주문 menu 입력

        if menu_num >= 1 and menu_num <= 4:
            break
        else:
            print('# msg: 1~4의 번호만 입력해주세요 :)')
    return menu_num