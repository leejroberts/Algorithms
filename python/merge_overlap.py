# merge overlapping intervals for a list of intervals


intervals = [(1,3),(3,9),(11,12),(13,22),(14, 23),(22,24),(27,33),(34,44),(35,36),(38,42),(45,50)]



def merge_overlap(intervals_array):
    merged_intervals_array = []
    merged_interval = list(intervals_array[0])
    remaining_intervals = intervals_array[1:]

    for index, next_interval in enumerate(remaining_intervals):
        if next_interval[0] <= merged_interval[1]:  # if intervals overlap
            if next_interval[1] > merged_interval[1]:
                merged_interval[1] = next_interval[1]
        else:
            # if intervals do not overlap
            merged_intervals_array.append(merged_interval)
            merged_interval = list(next_interval)
        if index == len(remaining_intervals) - 1:
            # if this is the last time around loop, append the final merged_interval
            merged_intervals_array.append(merged_interval)

    return merged_intervals_array


print(merge_overlap(intervals))

