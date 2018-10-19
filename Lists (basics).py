def makeHistogram(gradeList):
    # Create a 10 element histogram.
    histogram = [0] * 10

    # Count the number of each grade.
    i = 0
    while i < len(gradeList):
        grade = gradeList[i]
        print(grade)
        histogram[grade] += 1
        i += 1

    # Return the histogram.
    return histogram

gradeList = [3, 4, 2, 5, 8, 2, 2, 7, 4, 9]
histogram = makeHistogram(gradeList)
print()
print(histogram)
histogram
# print()
# print(str(histogram))

