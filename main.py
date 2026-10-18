def max_dragon_power(n: int) -> int:
    """
    Вычисляет максимально возможную силу стаи драконов
    при суммарном количестве голов n (1 <= n < 100).
    Сила = произведение количеств голов каждого дракона,
    у каждого дракона от 1 до 7 голов.
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3

    remainder = n % 3
    quotient = n // 3

    if remainder == 0:
        return 3 ** quotient
    elif remainder == 1:
        # 3 + 1 -> 2 + 2, т.е. убираем одну тройку и добавляем 4
        return 4 * (3 ** (quotient - 1))
    else:  # remainder == 2
        return 2 * (3 ** quotient)


if __name__ == "__main__":
    n = int(input("Введите количество голов N (0 < N < 100): "))
    print(f"Максимальная сила стаи: {max_dragon_power(n)}")