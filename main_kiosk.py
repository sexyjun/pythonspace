#######################################################
## cnu 버거 키오스크 프로그램
## 일자 : 2021. 10. 12
## 작성자: 김준혁
## 내용: console기반의 햄버거를 판매하는 키오스크 프로그램

# 조건
# 사용자는 최대로 버거1개, 사이드 1개, 음료1개 주문할 수 있습니다.

# 메뉴와 가격표
burger_name = {1: '새우버거', 2: '불고기버거' , 3: '치즈버거'}
side_name = {1: '프렌치프라이', 2: '치킨너겟'}
drink_name = {1: '코카콜라', 2: '커피', 3: '주스'}

burger_price = {1: 3500, 2: 3000, 3: 2500}
side_price = {1: 1500, 2: 2000}
drink_price = {1: 1000, 2: 1200, 3: 1500}
# 고객 주문 기록 저장
menu_save = {} # 고객 주문 메뉴 기록
price_save ={} # 고객 주문 금액 기록

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
    menu_num = int(input('>> 번호:')) # 사용자로부터 주문 menu 입력

    if menu_num >= 1 and menu_num <= 4:
        break
    else:
        print('# msg: 1~4의 번호만 입력해주세요 :)')

if menu_num == 1:
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
            menu_save['bureger'] = burger_name[choice_num]
            price_save['burger'] = burger_price[choice_num]
            break
        else:
            print('# msg: 1~3의 번호만 입력해주세요 :)')

    print('############################')
    print('## side menu')
    print('## 1. 프렌치프라이:1500원')
    print('## 2.치킨너겟: 2000원')
    print('## 원하시는 메뉴의 번호를 입력해주세요')
    print('################################')

    while True:
        choice_num2 = int(input('>> 번호: '))
        if 1 <= choice_num2 <= 2:
            menu_save['side'] = side_name[choice_num2]
            price_save['side'] = side_price[choice_num2]
            break
        else:
            print('# msg: 1~2의 번호만 입력해주세요:)')

    print('#########################')
    print('## drink menu')
    print('## 1. 코카콜라: 1000원')
    print('## 2. 커피: 1200원')
    print('## 3. 주스 : 1500원')
    print('############################')

    while True:
        choice_num3 = int(input('>> 번호: '))
        if 1 <= choice_num3 <= 3:
            menu_save['drink'] = drink_name[choice_num3]
            price_save['drink'] = drink_price[choice_num3]
            break
        else:
            print('# msg: 1~3의 번호만 입력해주세요:)')

elif menu_num == 2: # 햄버거 단품
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
            menu_save['bureger'] = burger_name[choice_num]
            price_save['burger'] = burger_price[choice_num]
            break
        else:
            print('# msg: 1~3의 번호만 입력해주세요 :)')


elif menu_num == 3: # 사이드 메뉴
    print('############################')
    print('## side menu')
    print('## 1. 프렌치프라이:1500원')
    print('## 2.치킨너겟: 2000원')
    print('## 원하시는 메뉴의 번호를 입력해주세요')
    print('################################')

    while True:
        choice_num2 = int(input('>> 번호: '))
        if 1 <= choice_num2 <= 2:
            menu_save['side'] = side_name[choice_num2]
            price_save['side'] = side_price[choice_num2]
            break
        else:
            print('# msg: 1~2의 번호만 입력해주세요:)')


elif menu_num == 4: # 음료
    print('#########################')
    print('## drink menu')
    print('## 1. 코카콜라: 1000원')
    print('## 2. 커피: 1200원')
    print('## 3. 주스 : 1500원')
    print('############################')

    while True:
        choice_num3 = int(input('>> 번호: '))
        if 1 <= choice_num3 <= 3:
            menu_save['drink'] = drink_name[choice_num3]
            price_save['drink'] = drink_price[choice_num3]
            break
        else:
            print('# msg: 1~3의 번호만 입력해주세요:)')

###########################
# 주문 메뉴와 금액 정산 및 출력
###########################

# total 주문 금액 계산
total_price = 0 # total 주문 금액

for price in price_save.values():
    total_price += price

print('##############################')
print('## 고객님의 주문하신 메뉴는')
for i, menu in enumerate(menu_save.values()):
    print(f'## {i+1}. {menu}')
print(f'## 으로 총 주문 금액은 {total_price}원 입니다.')
print('###########################################')
print('## 이용해주셔서 감사합니다.')
print('###########################################')