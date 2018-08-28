class VendingMachine:
    def __init__(self):
        self._change = 0

    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]

        if cmd == "잔액":
            return "잔액은 " + str(self._change) + "원입니다"

        elif cmd == "동전":
            coin = str(params[0])
            coin_list = ["10", "50", "100", "500"]
            self._change += int(coin)

            if coin in coin_list:
                # self._change += int(coin)
                return coin + "원을 넣었습니다"
            else:
                return "알 수 없는 동전입니다"

        elif cmd == "음료":
            known_beverage = {
                "커피":150,
                "우유":200,
                "우유커피":300,
            } #가독성이 좋게 dictionary수정. 마지막 줄에도 ,를 넣는다. 
            # known_beverage = ["커피", "우유", "우유커피"]
            # price = [150,200,300]
            beverage = params[0]
            if beverage not in known_beverage:
                return "알 수 없는 음료입니다"
            elif self._change < known_beverage[beverage]:
                return "잔액이 부족합니다"
            else:
                self._change = self._change - known_beverage[beverage]
                return beverage + "가 나왔습니다"

        elif cmd == "반환":
            if self._change > 0:
                a = (self._change // 500)
                b = (self._change-500*a)//100
                c = (self._change-500*a-100*b)//50
                d = (self._change-500*a-100*b-50*c)//10
                if d>1:
                    return "잔액이 반환되었습니다 :"+ " 500원"*a +','+ " 100원"*b +',' + " 50원"*c + ',' + " 10원,"*(d-1)+' 10원'
                else:
                    return "잔액이 반환되었습니다 :"+ " 500원"*a +','+ " 100원"*b +',' + " 50원"*c + ',' + " 10원"*d
            else:
                return "잔액이 0원입니다"
        else:
            return "알 수 없는 명령입니다"
