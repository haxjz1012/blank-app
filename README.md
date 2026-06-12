menu = {"1": "아메리카노", "2": "카페라떼", "3": "아이스티"}
prices = {"1": 3000, "2": 3500, "3": 3000}
cart = []
total = 0

print("--- ☕ 키오스크 메뉴 ---")
for key, name in menu.items():
    print(f"[{key}] {name} : {prices[key]}원")
print("[0] 종료 및 결제")
print("----------------------")

while True:
    choose = input("원하는 메뉴의 번호를 입력하세요 (종료는 0): ")
    
    if choose == "0":
        print("\n--- 주문이 완료되었습니다! ---")
        break
    elif choose in menu:
        selected_item = menu[choose]
        price = prices[choose]
        
        cart.append(selected_item)
        total += price
        
        print(f"🛒 {selected_item}(이)가 장바구니에 담겼습니다. (현재 총액: {total}원)")
    else:
        print("❌ 잘못된 번호입니다. 다시 입력해주세요.")

print(f"\n🛍️ 담은 상품: {', '.join(cart) if cart else '없음'}")
print(f"💵 총 결제 금액: {total}원")
