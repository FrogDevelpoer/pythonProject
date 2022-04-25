# 클래스 정의
class Calculate:
    # self 키워드는 타 프로그램의 this와 거의 유사한 개념
    # self 키워드를 제외하고 매개 변수의 개수를 맞춰주어야 한다.
    def __init__(self, first, second):  # 생성자
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return '더하기 : %d' % result

    def sub(self):
        result = self.first - self.second
        return '빼기 : %d' % result

    def mul(self):
        result = self.first * self.second
        return '곱하기 : %d' % result

    def div(self):
        if self.second == 0:
            self.second = 5
            result = self.first / self.second
        return '나누기 : %.3f' % result


calc = Calculate(14, 0)  # 객체 생성
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())
