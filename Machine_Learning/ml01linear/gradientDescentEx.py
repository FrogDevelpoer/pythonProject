# 경사 하강법
import matplotlib.pyplot as plt

x, y, m = 1.0, 1.0, 1

# 새로운 w를 구해주는 함수
def calc(w, alpha):     # alpha : 학습률
    result = w - alpha * (1 / m) * (w * x - y) * x

    return result

def iteration(w, alpha):    # iteration : 반복 횟수
    cnt = 0     # 카운터 변수
    counter = []    # 카운터 변수들을 저장할 카운터 리스트
    data = []   # w값들의 추이를 저장할 리스트
    totaldata = []

    while True:
        if w < 1.01:
            message = '학습률이 ' + str(alpha) + '일 때 반복 횟수는 ' + str(cnt) + '입니다.'
            print(message)
            break
        cnt += 1
        w = calc(w, alpha)
        counter.append(cnt)
        data.append(w)

    # end while
    totaldata.append(counter)
    totaldata.append(data)
    return totaldata

def makeChart(draw_chart, index, learning_rate):
    plt.figure()
    plt.plot(draw_chart[0], draw_chart[1], color='b', linestyle='solid', linewidth=1)
    filename = 'gradientDescentEx' + str(index).zfill(2) + '.png'
    plt.savefig(filename)

alpha_list = [0.0001, 0.01, 0.1]
# alpha_list = [0.1]

for idx in range(len(alpha_list)):
    w = 5.0     # 초기값을 5라고 가정
    chartdata = iteration(w, alpha_list[idx])
    # print('chardata : ', chartdata)
    makeChart(chartdata, idx+1, alpha_list[idx])
print('fin')
