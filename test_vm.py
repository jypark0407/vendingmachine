from vm import VendingMachine

def test_initial_change_should_be_zero():
    m = VendingMachine() # 자판기의 instance를 만들어서 m이라는 변수에 assign.
    assert "잔액은 0원입니다" == m.run("잔액")

def test_insert_coin_and_check():
    m = VendingMachine()
    assert "100원을 넣었습니다" == m.run("동전 100")

def test_accumulation_of_change():
    m = VendingMachine()
    m.run ("동전 100")
    m.run ("동전 100")
    assert "잔액은 200원입니다" == m.run("잔액")

def test_unknown_command():
    m = VendingMachine()
    assert "알 수 없는 명령입니다" == m.run("아무거나")

def test_check_leftover_charge():
    m = VendingMachine()
    assert "잔액은 100원입니다" == m.run("잔액")

def test_insert_coin_and_check():
    m = VendingMachine()
    assert "100원을 넣었습니다" == m.run("동전 100")
    assert "잔액은 100원입니다" == m.run("잔액")

def test_enough_change():
    m = VendingMachine()
    assert "커피가 나왔습니다" == m.run("동전 100")

def test_not_enough_change():
    m = VendingMachine()
    assert "잔액이 부족합니다" == m.run("동전 100")
