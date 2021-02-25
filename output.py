def n_intersection(counters):
    n = 0
    for counter in counters:
        if len(counter) != 0:
            n += 1

    return n

def order_dict(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def output(filename, counters, inter_start):
    with open(filename, "w") as file:
        n = n_intersection(counters)
        file.write("{}\n".format(n))

        for i, counter in enumerate(counters):
            if len(counter) == 0:
                continue


            file.write("{}\n".format(i))

            file.write("{}\n".format(len(counter)))


            inter = order_dict(inter_start[i])

            output = {}
            for k in inter.keys():
                output[k] = counter[k]

            for street, sec in output.items():
                sec = max(sec, 1)
                file.write("{} {}\n".format(street, sec))

            for street, sec in counter.items():
                if street not in output.keys():
                    sec = max(sec, 1)
                    file.write("{} {}\n".format(street, sec))
