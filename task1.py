# Дан массив чисел, состоящий из некоторого количества подряд идущих единиц,
# За которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
# Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)


def task(array):
    for i, item in enumerate(array):
        if item == '0':
            return i
    return None


if __name__ == '__main__':
    print(task('111111111110000000000000000'))
