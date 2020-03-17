


def parse_ranges(ranges_string="1-2,4-4,8-10"):
    ranges_list = ranges_string.split(",")
    first_generator = (ran.split("-") for ran in ranges_list)
    list_nums = []
    for start, stop in first_generator:
        list_nums += [num for num in range(int(start), int(stop) + 1)]
    return list_nums




print(parse_ranges())
print(list(parse_ranges("0-0,4-8,20-21,43-45")))