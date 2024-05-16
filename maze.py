import random

# Функция для заполнения случайных позиций в матрице бактериями
def fill_random_positions(matrix, num_positions):
    all_positions = [(i, j) for i in range(6) for j in range(6) if matrix[i][j] == 0]
    num_to_fill = min(num_positions, len(all_positions))
    positions_to_fill = random.sample(all_positions, num_to_fill)
    for pos in positions_to_fill:
        matrix[pos[0]][pos[1]] = 1

# Функция для распространения бактерий
def spread_bacteria(matrix, probability=0.05):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    new_positions = []
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == 1:
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < 6 and 0 <= nj < 6 and matrix[ni][nj] == 0:
                        new_positions.append((ni, nj))
    for pos in new_positions:
        if random.random() < probability:
            matrix[pos[0]][pos[1]] = 1

# Функция для обновления состояния бактерий
def update_bacteria(matrix, age_matrix, T):
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == 1:
                age_matrix[i][j] += 1
                if age_matrix[i][j] >= T / 2:
                    matrix[i][j] = -1  # Бактерия умирает, но ячейка не освобождается

# Функция для заполнения матрицы и обновления состояния в течение T дней
def simulate_days(matrix, T):
    age_matrix = [[0 for _ in range(6)] for _ in range(6)]
    for day in range(T):
        num_positions = random.randint(0, 2) if day < 7 else 0
        fill_random_positions(matrix, num_positions)
        if day >= 1:
            spread_bacteria(matrix)
        update_bacteria(matrix, age_matrix, T)
        print(f"Day {day + 1}:")
        for row in matrix:
            print(row)
        print()

# Инициализация матрицы 6x6
matrix = [[0 for _ in range(6)] for _ in range(6)]

# Запуск симуляции на T дней
T = 14
simulate_days(matrix, T)
