import random

# Функция для заполнения случайных позиций в матрице бактериями
def fill_random_positions(matrix, age_matrix, num_positions):
    all_positions = [(i, j) for i in range(6) for j in range(6) if matrix[i][j] == 0]
    num_to_fill = min(num_positions, len(all_positions))
    positions_to_fill = random.sample(all_positions, num_to_fill)
    for pos in positions_to_fill:
        matrix[pos[0]][pos[1]] = 1
        age_matrix[pos[0]][pos[1]] = 1  # Начальный возраст бактерий

# Функция для распространения бактерий
def spread_bacteria(matrix, age_matrix, probability=0.05):
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
                        if random.random() < probability:
                            new_positions.append((ni, nj))
    for pos in new_positions:
        matrix[pos[0]][pos[1]] = 1
        age_matrix[pos[0]][pos[1]] = 1  # Возраст новых бактерий

# Функция для обновления возраста бактерий и проверки на смерть
def update_bacteria(matrix, age_matrix, N, death_probability=0.02):
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == 1:
                age_matrix[i][j] += 1
                if age_matrix[i][j] > N / 2 and random.random() < death_probability:
                    matrix[i][j] = -1  # Бактерия умирает, но ячейка не освобождается

# Функция для заполнения матрицы и обновления состояния в течение N дней
def fill_matrix_n_times(matrix, age_matrix, N):
    for day in range(N):
        num_positions = random.randint(1, 20)
        fill_random_positions(matrix, age_matrix, num_positions)
        spread_bacteria(matrix, age_matrix)
        update_bacteria(matrix, age_matrix, N)
        print(f"Day {day + 1}:")
        for row in matrix:
            print(row)
        print()

# Инициализация матрицы 6x6
matrix = [[0 for _ in range(6)] for _ in range(6)]
age_matrix = [[0 for _ in range(6)] for _ in range(6)]

# Запуск симуляции на N дней
N = 7
fill_matrix_n_times(matrix, age_matrix, N)
