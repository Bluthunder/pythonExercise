import os


def gradingStudents(grades):
    for i in range(len(grades)):
        x = grades[i] % 5
        if grades[i] < 38:
            grades[i] = grades[i]
        elif x != 0:
            if (5 - x) < 3:
                grades[i] = grades[i] + (5 - x)
            elif (5 - x) >= 3:
                grades[i] = grades[i]
        elif x == 0:
            grades[i] = grades[i]
    return grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
