def better_than_average(class_points, your_points):
    sum = 0
    for x in class_points:
        sum = sum + x
    return True if sum/len(class_points) < your_points else False