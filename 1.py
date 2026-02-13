
from collections import defaultdict

class Fitness:
    def __init__(self, client_code, year, month, exercise_length):
        self._client_code = client_code
        self._year = year
        self._month = month
        self._exercise_length = exercise_length

first_exercise = Fitness(34443, 2025, 2, 65)
second_exercise = Fitness(435456, 2025, 12, 23)
third_exercise = Fitness(3232422, 2025, 1, 64)
fourth_exercise = Fitness(45343, 2025, 9, 34)
fifth_exercise = Fitness(352131235, 2025, 8, 43)
sixth_exercise = Fitness(564645, 2025, 4, 15)
seventh_exercise = Fitness(234234, 2025, 7, 14)
eighth_exercise = Fitness(2132123, 2025, 10, 17)
ninth_exercise = Fitness(546456, 2025, 6, 32)
tenth_exercise = Fitness(324242, 2025, 3, 39)

exercises = [first_exercise, second_exercise, third_exercise, fourth_exercise, fifth_exercise,
             sixth_exercise, seventh_exercise, eighth_exercise, ninth_exercise, tenth_exercise]

year_table = defaultdict(int)

for exercise in exercises:
    year_table[exercise._year] += exercise._exercise_length

max_year = max(year_table, key=year_table.get)
print(max_year, year_table[max_year])