import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime


if False:
    # squares = [1, 4, 9, 16, 25, 36, 49, 64]
    # squares1 = [1, 3, 6, 10, 15, 21, 28, 36]
    # squares2 = [1, 7, 15, 26, 40, 57, 77, 100]
    # seq = [1, 2, 3, 4, 5, 6, 7, 8]

    squares = [3367,4120, 5539]
    squares1 = [4000, 3590, 4423]
    squares2 = [5200, 4930, 5350]
    seq = [2018, 2019, 2020]
    # plt.plot(seq, squares, "g*-", seq, squares1, "r-^", seq, squares2, "k.-",  linewidth=1)
    line1, = plt.plot(seq, squares, "g*-",  linewidth=1, label="line1")
    line2, = plt.plot(seq, squares1, "r-^",  linewidth=2, label="line2")
    line3, = plt.plot(seq, squares2, "k.-",  linewidth=3, label="line3")
    plt.legend(handles=[line1, line2, line3], loc="best", bbox_to_anchor=(1, 1))
    # plt.tight_layout(pad=7)       # 設定留白的功能
    # plt.tight_layout(h_pad=15)
    plt.tight_layout(w_pad=9)
    plt.title("Test Chart", fontsize=24)
    plt.xlabel("Value")
    plt.xticks(seq)             # x 軸的刻度
    plt.ylabel("Square")
    plt.tick_params(axis="both", labelsize=12, color="red")     # 線的屬性
    # plt.axis([0, 8, 0, 70])         # 設定最小和最大刻度
    file_name = "./resource/123.jpg"
    plt.savefig(file_name, bbox_inches="tight")                 # 存檔
    plt.show()

if False:
    squares = [1, 4, 9, 16, 25, 36, 49, 64]
    squares1 = [1, 3, 6, 10, 15, 21, 28, 36]
    # plt.scatter(squares, squares1, color="y")
    # plt.scatter(squares, squares1, c=(0, 1, 0))

    xpt = np.linspace(0, 10, 500)
    ypt1 = np.sin(xpt)
    ypt2 = np.cos(xpt)
    # plt.figure(1)                                   # 獨立的張數第 1 張
    plt.subplot(2, 1, 1)                            # 同一個程式有多張圖，(y 軸的張數, x 軸的張數, 第幾張)
    plt.title("Test Chart", fontsize=24)
    plt.scatter(xpt, ypt1, color=(0, 1, 0))

    num = 100
    x = np.random.random(num)                       # 取亂數
    y = np.random.random(num)
    t = x
    # plt.figure(2)                                   # 獨立的張數第 2 張
    plt.subplot(2, 1, 2)
    plt.title("Test", fontsize=24)
    plt.scatter(x, y, s=100, c=t, cmap="brg")       # s:點的大小，c:顏色
    # plt.axes().get_xaxis().set_visible(False)       # 隱藏位標軸: 如果要顯示多張，這裡設定後會顯示不出來
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()

if False:
    votes = [135, 412, 397]
    N = len(votes)
    x = np.arange(N)
    width = 0.35
    plt.bar(x, votes, width)

    plt.xticks(x, ("James", "Peter", "Norton"))
    plt.yticks(np.arange(0, 450, 30))
    plt.show()

if True:
    fn = "./resource/TaipeiWeatherJan.csv"
    with open(fn) as csvFile:
        csvReader = csv.reader(csvFile)
        headerRow = next(csvReader)
        dates, highTemps, lowTemps = [], [], []
        for row in csvReader:
            try:
                currentDate = datetime.strptime(row[0], "%Y/%m/%d")
                highTemp = int(row[1])
                lowTemp = int(row[3])
            except Exception:
                print("有缺值")
            else:
                dates.append(currentDate)
                highTemps.append(highTemp)
                lowTemps.append(lowTemp)

    fig = plt.figure(dpi=80, figsize=(12, 8))               # 設定繪圖區的大小, 沒有這一行就用預設的
    plt.plot(dates, highTemps)
    plt.plot(dates, lowTemps)
    plt.fill_between(dates, highTemps, lowTemps, color="y", alpha=0.2)      # 填滿二個區間
    fig.autofmt_xdate()                                     # 旋轉 x 軸的刻度，參數 rotation=xx, 沒有設定就用預設
    plt.title("Weather Report, Jan. 2007", fontsize=24)
    plt.xlabel("", fontsize=14)
    plt.ylabel("Temperature (C)", fontsize=14)
    plt.tick_params(axis="both", labelsize=12, color="red")
    plt.axis([dates[0], dates[30], 0, 40])         # 設定最小和最大刻度
    plt.show()

