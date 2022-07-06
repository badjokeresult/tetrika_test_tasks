# Мы сохраняем время присутствия каждого пользователя на уроке в виде интервалов.

# В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах):
#  - lesson – начало и конец урока
#  - pupil – интервалы присутствия ученика
#  - tutor – интервалы присутствия учителя

# Интервалы устроены следующим образом – это всегда список из четного количества элементов.
# Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.

# Нужно написать функцию,
# Которая получает на вход словарь с интервалами
# И возвращает время общего присутствия ученика и учителя на уроке (в секундах).



def appearance(intervals):
    lesson = merge_intervals(intervals['lesson'])
    pupil = merge_intervals(intervals['pupil'])
    tutor = merge_intervals(intervals['tutor'])

    compress_intervals(pupil, lesson)
    compress_intervals(tutor, lesson)

    start_time = max(lesson[0], pupil[0], tutor[0])
    end_time = min(lesson[-1], pupil[-1], tutor[-1])

    result = end_time - start_time

    result -= absence_time(pupil, lesson)
    result -= absence_time(tutor, lesson)

    return result


def merge_intervals(intervals):
    res = []
    tupled = [(intervals[i], intervals[i + 1]) for i in range(0, len(intervals), 2)]
    tupled.sort(key=lambda x: x[0])
    result = [tupled[0]]
    for i in range(1, len(tupled)):
        cur = tupled[i]
        if cur[0] <= result[-1][1]:
            old = result[-1]
            result.pop()
            result.append([old[0], max(cur[1], old[1])])
        else:
            result.append(cur)
    for item in result:
        res.extend(list(item))
    return res


def compress_intervals(intervals, lesson):
    for i in range(len(intervals)):
        if intervals[i] < lesson[0]:
            intervals[i] = lesson[0]
        elif intervals[i] > lesson[1]:
            intervals[i] = lesson[1]


def absence_time(intervals, lesson):
    time = 0
    for i in range(2, len(intervals), 2):
        time += min(intervals[i], lesson[1]) - min(intervals[i - 1], lesson[1])
    return time


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    print('Successful!')