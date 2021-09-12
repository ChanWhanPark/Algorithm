import math

def make_records(records):
    time = []
    car_number = []
    status = []
    for record in records:
        time.append(record[0:5])
        car_number.append(record[6:10])
        status.append(record[11:])

    return time, car_number, status

def time_change(time):
    hour = ""
    minute = ""
    new_time = []
    for t in time:
        hour += t[0:2]
        minute += t[3:5]
        new_time.append(int(hour) * 60 + int(minute))
        hour, minute = "", ""

    return new_time

def sort_cars(car_num):
    count = {}
    for c in car_num:
        try: count[c] = 0
        except: count[c] = 0

    return count

def calculate_fee(visited_time, fee):
    basic_time = fee[0]
    basic_fee = fee[1]
    per_time = fee[2]
    per_fee = fee[3]

    if visited_time <= basic_time:
        return basic_fee
    else:
        return int(basic_fee + math.ceil((visited_time - basic_time) / per_time) * per_fee)


def solution(fees, records):
    answer = []
    time, car_num, status = make_records(records)
    new_time = time_change(time)
    print(car_num)
    print(status)
    print(new_time)
    visited = []
    visited_index = []
    visited_time = []
    car_list = sort_cars(car_num)

    for i in range(len(car_num)):
        if car_num[i] in visited:
            main_index = visited.index(car_num[i])
            visited.pop(visited.index(car_num[i]))
            visited_index.pop(main_index)
            in_time = new_time[i] - visited_time.pop(main_index)
            car_list[car_num[i]] += in_time
        else:
            visited.append(car_num[i])
            visited_time.append(new_time[i])
            visited_index.append(i)
        print(visited_index)

    print(visited)
    print(visited_index)
    if visited:
        for i in range(len(visited_index)):
            idx = int(visited_index[i])
            in_time = 1439 - new_time[idx]
            print(idx, in_time, new_time[idx])
            #fee = calculate_fee(in_time, fees)
            car_list[car_num[idx]] += in_time

    new_car_list = sorted(car_list.items())
    for value in new_car_list:
        print(value)
        fee = calculate_fee(value[1], fees)
        answer.append(fee)

    print(answer)
    return answer


fee = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
solution(fee, records)