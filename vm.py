change = 0

def init():
    global change
    change = 0

def run(raw):
    global change

    token = raw.split(" ")
    cmd, params = token[0], token[1:]

    if cmd == "잔액":
        return "잔액은 " + str(change) + "원입니다"
    else:
        coin = params[0]
        change += int(params[0])
        return coin + "원을 넣었습니다"
