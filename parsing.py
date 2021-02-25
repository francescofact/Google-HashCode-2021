def readfile(filepath):
    with open(filepath, "r") as file:

        first_line = file.readline()
        raw_first_line = first_line.strip().split(" ")
        sim_duration = int(raw_first_line[0])
        n_intersections = int(raw_first_line[1])
        n_streets = int(raw_first_line[2])
        n_cars = int(raw_first_line[3])
        points = int(raw_first_line[4])

        line = file.readline()
        line_number = 0

        streets = {}

        while (line_number < n_streets):
            raw_street = line.strip().split(" ")
            streets[raw_street[2]] = [int(raw_street[0]), int(raw_street[1]), int(raw_street[3])]
            line = file.readline()
            line_number += 1

        paths = []
        while (line != ""):
            raw_path = line.strip().split(" ")
            paths.append(raw_path[1:])
            line = file.readline()

    return n_intersections, sim_duration, streets, paths
