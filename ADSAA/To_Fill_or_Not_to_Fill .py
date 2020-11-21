# https://qsctech-sange.github.io/1033-To-Fill-or-Not-to-Fill.html#sample-output-2
def next_station(station, now_tank_can_run, price):
    global num_sta, stations, tank, max_dis, per_unit, distance
    if station == num_sta:
        return True, price
    # next_sta 先是下一个车站
    next_sta = station + 1
    
    # 如果下一个车站到这个车站的距离超过了最大能开的距离，报错
    if stations[next_sta][1] - stations[station][1] > max_dis:
        return False, stations[station][1] + max_dis
    
    # 否则，next_sta 找到下一个要前去的车站，应当是油价比现在低的第一个车站。'先遍历里程范围内的第一个油价比此车站低的车站'
    # ‘离开这个循环可能是因为next_sta油价<station油价，或者 next_sta 超出当前station的最大距离’
    while stations[next_sta][0] > stations[station][0] and stations[next_sta + 1][1] - stations[station][1] <= max_dis:
        next_sta += 1
    
    # 如果next_sta还是比现在的价格高，说明里程范围内没有比现在更低的油价，'那么就把现在的邮箱拉满，同时找到下一个里程范围内价格相对更低的车站'
    if stations[next_sta][0] > stations[station][0]:
        next_sta = station + 1
        temp = next_sta
        while stations[temp + 1][1] - stations[station][1] <= max_dis:
            temp += 1
            if stations[temp][0] < stations[next_sta][0]:
                next_sta = temp
        return next_station(next_sta, max_dis - stations[next_sta][1] + stations[station][1],
                            price + (max_dis - now_tank_can_run) / per_unit * stations[station][0])
    
    # 否则，next_sta油价更低，
    # 正好移动到next_station为止
    else:
        return next_station(next_sta, 0,
                            price + (stations[next_sta][1] - stations[station][1] - now_tank_can_run) / per_unit *
                            stations[station][0])

# get input
tank, distance, per_unit, num_sta = list(map(float, input().split()))
max_dis = tank * per_unit
stations = []

# initial
for _ in range(int(num_sta)):
    info = input().split()
    stations.append([float(info[0]), float(info[1])])

# add destation as a station with 0 price
stations.append([0, distance])

# sort by distance
stations.sort(key=lambda x: x[1])


if stations[0][1] != 0: # no station at begin
    print("The maximum travel distance = 0.00")
else:
    status, price = next_station(0, 0, 0)
    if status:
        print("%0.2f" % price)
    else:
        print("The maximum travel distance = %0.2f" % price)