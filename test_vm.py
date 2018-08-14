from vm import run, init

def test_initial_change_should_be_zero():
    init()
    assert "잔액은 0원입니다" == run("잔액")

def test_insert_coin_and_check():
    init()
    assert "100원을 넣었습니다" ==  run("동전 100")
    assert "잔액은 100원입니다" == run("잔액")


def test_accumulation_of_change():
    init()
    run ("동전 100")
    run ("동전 100")
    assert "잔액은 200원입니다" == run("잔액")
