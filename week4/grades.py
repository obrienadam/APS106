def compute_grade(percentage):
    if percentage > 90:
        return 'A+', 4.
    elif percentage > 85:
        return 'A', 4.
    elif percentage > 80:
        return 'A-', 3.7
    elif percentage > 77.:
        return 'B+', 3.4
    elif percentage > 74:
        return 'B', 3.1
    else:
        return 'F', 0.

if __name__ == '__main__':
    percentage = float(input('Enter grade %: '))
    grade, gpa = compute_grade(percentage)

    print('Grade: {} (GPA: {})'.format(grade, gpa))