def give_me_n(n):
    result = ''
    current_number = 0
    try:
        n = int(n)
    except ValueError:
        return 'Нужно целое положительное число от 1'
    if n < 1:
        return 'Нужно целое положительное число от 1'
    while True:
        current_number += 1
        result = f'{result}{str(current_number)*current_number}'
        if len(result) >= n:
            result = result[:n]
            break
    return result


def main():
    n = input('Введите длину последовательности\n')
    print(give_me_n(n))

if __name__ == '__main__':
    main()