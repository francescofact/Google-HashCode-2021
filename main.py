import collections
from collections import Counter
import parsing, output
from math import gcd
from functools import reduce

streets = {}
paths = {}


def get_intersections_traffic(total_intersections: int):
    global streets, paths
    # initialize a counter for each intersection
    intersections = []
    for i in range(total_intersections):
        intersections.append(Counter())

    for path in paths:
        for street in path[:-1]:
            street_name = street
            street_obj = streets[street]
            intersections[street_obj[1]][street_name] += 1

    return intersections

def get_intersections_traffic_start(total_intersections: int):
    global streets, paths
    # initialize a counter for each intersection
    intersections = []
    for i in range(total_intersections):
        intersections.append(Counter())

    for path in paths:
        first_steet = path[0]
        street_name = first_steet
        street_obj = streets[first_steet]
        intersections[street_obj[1]][street_name] += 1

    return intersections


def gcd_for_list(numbers: list):
    numbers = list(numbers)
    numbers = [i for i in numbers if i != 0]

    if len(numbers) == 0:
        return 1
    return reduce(gcd, numbers)


def compute_semaphores(intersections: list):
    global sim_duration

    for i, inter in enumerate(intersections):
        # if no car ever pass, always red
        if len(inter) == 0:
            continue
        tot = sum(inter.values())
        # compute street's percentage (kinda)
        for k in inter.keys():
            intersections[i][k] = round(inter[k] * 10 / tot)

        # reduce |number| -> we want smallest numbers possible respecting proportion
        divisor = gcd_for_list(intersections[i].values())
        if divisor != 1:
            for k in intersections[i].keys():
                green_time = max(intersections[i][k] // divisor, 1)
                intersections[i][k] = min(green_time, sim_duration)
        else:
            green_time = max(intersections[i][k], 1)
            intersections[i][k] = min(green_time, sim_duration)

    return intersections


if __name__ == '__main__':
    in_filenames = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt"]
    for fn in in_filenames:
        num_intersections, sim_duration, streets, paths = parsing.readfile(fn)
        inter123 = get_intersections_traffic(num_intersections)
        inter_start = get_intersections_traffic_start(num_intersections)
        semaphores = compute_semaphores(inter123)
        out_fn = fn[0] + "_out.txt"
        output.output(out_fn, semaphores, inter_start)
