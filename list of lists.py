
def enrollment_stats():
    '''Возвращает два списка.
Первый содержит все данные о
зачисленных зарегистрированных студентах,
а второй — все данные о плате за
обучение.'''
    total_students = 0
    total_tuition = 0
    for i in universities:
        i = i[1]
        total_students += i
    for i in universities:
        i = i[2]
        total_tuition += i
    return total_students, total_tuition

def mean():
    '''Возвращается среднее значение аргумента'''
    sum_students = 0
    sum_tuition = 0
    for i in universities:
        i = i[1]
        sum_students += i
    mean_students = sum_students / len(universities)
    mean_students = round(mean_students, 2)
    for i in universities:
        i = i[2]
        sum_tuition += i
    mean_tuition = sum_tuition / len(universities)
    mean_tuition = round(mean_tuition, 2)
    return mean_students, mean_tuition

def median():
    '''Возвращается медиану аргумента'''
    list_students = []
    list_tuition = []
    for i in universities:
        list_students.append(i[1])
    list_students.sort()
    # Выбираем элемент с середины списка
    if len(list_students) % 2 == 0:
    # Размер списка четный, выбираем среднее значение двух элементов с середины
        median_students = (list_students[len(list_students) // 2 - 1] + list_students[len(list_students) // 2]) / 2
    else:
    # Размер списка нечетный, выбираем элемент с середины
        median_students = list_students[len(list_students) // 2]
    for i in universities:
        list_tuition.append(i[2])
    list_tuition.sort()
    # Выбираем элемент с середины списка
    if len(list_tuition) % 2 == 0:
    # Размер списка четный, выбираем среднее значение двух элементов с середины
        median_tuition = (list_tuition[len(list_tuition) // 2 - 1] + list_tuition[len(list_tuition) // 2]) / 2
    else:
    # Размер списка нечетный, выбираем элемент с середины
        median_tuition = list_tuition[len(list_tuition) // 2]
    return median_students, median_tuition
    

universities = [
['California Institute of Technology', 2175,
37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology',
10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

total_students, total_tuition  = enrollment_stats()
student_mean, tuition_mean = mean()
student_median, tuition_median = median()

print("*****" * 6)
print(f'Total students: {total_students:,d}')
print(f'Total tuition: $ {total_tuition:,d} \n')
print(f'Student mean: {student_mean:,.2f}')
print(f'Student median: {student_median:,d} \n')
print(f'Tuition mean: $ {tuition_mean:,.2f}')
print(f'Tuition median: $ {tuition_median:,d}')
print("*****" * 6)