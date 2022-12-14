

def decide(cars, number_of_cars, prev_st):
    if number_of_cars == 0:
        return []

    rm = 0
    let_it_pass = []
    for i, car in enumerate(cars):
        if prev_st == car[1]:
            if rm == number_of_cars:
                break
            let_it_pass.append(i)
            rm += 1

    if rm < number_of_cars:
        for i, car in enumerate(cars):
            if i in let_it_pass:
                continue
            if rm == number_of_cars:
                break
            let_it_pass.append(i)
            rm += 1

    return [i for i in let_it_pass]


def func(arr, st):
    in_list = [[arr[0], st[0]]]
    instant = arr[0]
    old_instant = arr[0]
    prev_street = 1
    order = []

    save_return = []
    for i in range(1, len(arr)):
        if arr[i] == instant:
            in_list.append([arr[i], st[i]])
            old_instant = arr[i]
        else:
            pass_cars = arr[i] - instant
            instant = arr[i]
            to_rm = decide(in_list, pass_cars, prev_street)

            if pass_cars > len(in_list):
                prev_street = 1
            else:
                prev_street = in_list[to_rm[0]][1]

            l = 0
            for pos, j in enumerate(to_rm):
                save_return.append(in_list[j][0] + j)
                l += 1

            in_list = [in_list[j]
                       for j, car in enumerate(in_list) if j not in to_rm]

            in_list.append([arr[i], st[i]])

    l = 0
    # All all the left out
    to_rm = decide(in_list, 10000000000, prev_street)
    for pos, j in enumerate(to_rm):
        save_return.append(in_list[j][0] + j)
        l += 1
    print(save_return)


a = [0, 0, 1, 4]
s = [0, 1, 1, 0]
func(a, s)
