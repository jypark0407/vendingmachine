from vm import VendingMachine


def test_initial_change_should_be_zero():
    m = VendingMachine()
    assert "잔액은 0원입니다" == m.run("잔액")

def test_insert_coin_and_check():
    m = VendingMachine()
    assert "100원을 넣었습니다" == m.run("동전 100")
    assert "잔액은 100원입니다" == m.run("잔액")

def test_accumulation_of_change():
    m = VendingMachine()
    m.run("동전 100")
    m.run("동전 100")
    assert "잔액은 200원입니다" == m.run("잔액")

def test_음료_뽑기():
    m = VendingMachine()
    m.run("동전 500")
    assert "커피가 나왔습니다" == m.run("음료 커피")
    assert "잔액은 350원입니다" == m.run("잔액")

def test_모르는_음료_뽑기():
    m = VendingMachine()
    m.run("동전 500")
    assert "알 수 없는 음료입니다" == m.run("음료 맥주")
    assert "잔액은 500원입니다" == m.run("잔액")

def test_동전이_부족한_상황에서_음료_뽑기():
    m = VendingMachine()
    m.run("동전 100")
    assert "잔액이 부족합니다" == m.run("음료 커피")
    assert "잔액은 100원입니다" == m.run("잔액")

def test_unknown_command():
    m = VendingMachine()
    assert "알 수 없는 명령입니다" == m.run("웅앵")

# def test_valid_coins():
#     m = VendingMachine()
#     valid_coins = ["10", "50", "100", "500"]
#     for coin in valid_coins:
#         assert coin + "원을 넣었습니다" == m.run("동전 " + coin)

def test_인식_하는_동전():
    m = VendingMachine()
    valid_coins = ["10", "50", "100", "500"]
    for coin in valid_coins:
        assert coin + "원을 넣었습니다" == m.run("동전 " + coin)
        # 동전 뒤에 스페이스 없으면 오류난다...주의!

def test_인식할_수_없는_동전():
    m = VendingMachine()
    assert "알 수 없는 동전입니다" == m.run("동전 110")
