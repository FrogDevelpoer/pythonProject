class Television:
    def __init__(self, name, channel, volume, price):
        self.name = name
        self.channel = channel
        self.volume = volume
        self.price = price

    def showData(self):
        print('이름 : ', self.name)
        print('채널 : ', self.volume)

        vol = '볼륨 크기 : '
        msg = vol + str(self.volume)
        print(msg)

        print('가격 : ', self.price)


samsung = Television('삼성 OLED', 11, 10, 10000)     # TV 이름, 채널, 볼륨
samsung.showData()

