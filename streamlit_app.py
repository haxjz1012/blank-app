import streamlit as st
import pandas as pd

# 1. 데이터 정의 (메뉴 리스트)
menu_data = {
    "아메리카노": 3000,
    "카페라떼": 3500,
    "아이스티": 3000,
    "유자차": 4000,
    "초코라떼": 4200
}

# 2. 스트림릿 세션 상태 초기화 (딕셔너리 구조로 변경하여 수량 관리 용이하게 수정)
if "cart" not in st.session_state:
    st.session_state.cart = {}  # {'메뉴명': 수량} 구조

# --- UI 레이아웃 설정 ---
st.title("☕ 스마트 디지털 키오스크")
st.markdown("원하는 메뉴와 수량을 선택하신 후 주문하기를 눌러주세요.")
st.divider()

# 3. 입력 위젯 섹션 (st.selectbox, st.number_input 활용)
col1, col2 = st.columns([2, 1])

with col1:
    # 메뉴 선택 셀렉트박스
    selected_item = st.selectbox("✨ 메뉴를 선택하세요", list(menu_data.keys()))
    st.info(f"선택한 메뉴 가격: {menu_data[selected_item]}원")

with col2:
    # 수량 선택 넘버인풋
    quantity = st.number_input("🔢 수량", min_value=1, max_value=10, value=1, step=1)

# 장바구니 담기 버튼
if st.button("🛒 장바구니에 담기", type="secondary", use_container_width=True):
    if selected_item in st.session_state.cart:
        st.session_state.cart[selected_item] += quantity
    else:
        st.session_state.cart[selected_item] = quantity
    st.toast(f"{selected_item} {quantity}잔이 장바구니에 추가되었습니다!")

st.divider()

# 4. 출력 섹션 (st.dataframe, st.success 활용)
st.subheader("🛍️ 현재 장바구니 내역")

if st.session_state.cart:
    # 데이터프레임 변환을 위한 데이터 가공
    cart_items = []
    total_price = 0
    
    for item, qty in st.session_state.cart.items():
        price = menu_data[item]
        subtotal = price * qty
        total_price += subtotal
        cart_items.append({
            "메뉴명": item,
            "단가": f"{price}원",
            "수량": f"{qty}잔",
            "금액": subtotal
        })
    
    df = pd.DataFrame(cart_items)
    
    # 깔끔한 표(Dataframe) 형태로 출력
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # 총 금액 표시
    st.metric(label="💰 총 결제 예정 금액", value=f"{total_price}원")
    
    # 기능 버튼들 (결제 및 초기화)
    btn_col1, btn_col2 = st.columns(2)
    
    with btn_col1:
        if st.button("💳 최종 결제하기", type="primary", use_container_width=True):
            st.balloons()
            st.success(f"🎉 주문이 완료되었습니다! 총 {total_price}원이 결제되었습니다.")
            st.session_state.cart = {}  # 장바구니 비우기
            st.rerun()
            
    with btn_col2:
        if st.button("❌ 장바구니 전체 비우기", use_container_width=True):
            st.session_state.cart = {}
            st.rerun()
else:
    st.info("장바구니가 비어 있습니다. 메뉴를 선택해 주세요.")