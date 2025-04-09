def main(n, start, goal, helper, poles):

    if n == 1:
        poles[goal].append(poles[start].pop())
        print(
            f"Перемістіть диск 1 з {start} на {goal}")
        print(f"Шести: {poles}")
    else:
        main(n - 1, start, helper, goal, poles)
        poles[goal].append(poles[start].pop())
        print(f"Перемістіть диск {n} з {start} на {goal}")
        print(f"Шести: {poles}")
        main(n - 1, helper, goal, start, poles)


if __name__ == "__main__":
    try:
        n = int(input("Введіть кількість дисків: "))
        poles = {
            "A": [x for x in range(n, 0, -1)],
            "B": [],
            "C": []
        }
        print(f"\nПочаткове положення: {poles}\n")
        main(n, 'A', "C", "B", poles)
    except ValueError:
        print("Будь ласка, введіть ціле число.")
