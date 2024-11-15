import random


class MatrixProcessor:
    def __init__(self):
        self.matrix = []

    def input_matrix(self):
        """Ввод матрицы вручную."""
        rows = int(input("Введите количество строк: "))
        self.matrix = []
        
        for i in range(rows):
            row = list(map(int, input(f"Введите элементы строки {i + 1} (через пробел): ").split()))
            self.matrix.append(row)

    def generate_matrix(self):
        """Генерация случайной матрицы."""
        rows = random.randint(2, 5)  # Случайное количество строк
        cols = random.randint(2, 5)  # Случайное количество столбцов
        self.matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
        
        print("Сгенерированная матрица:")
        self.output_matrix()

    def process_matrix(self):
        """Обработка матрицы: сортировка и добавление столбца с суммами модулей."""
        sums = [sum(abs(x) for x in row) for row in self.matrix]
        
        # Создаем новую матрицу с добавленным столбцом сумм
        new_matrix = [row + [sums[i]] for i, row in enumerate(self.matrix)]
        
        # Сортируем по убыванию суммы модулей
        new_matrix.sort(key=lambda x: x[-1], reverse=True)
        
        return new_matrix

    def output_matrix(self):
        """Вывод матрицы."""
        if not self.matrix:
            print("Матрица пуста.")
            return
        
        for row in self.matrix:
            print("\t".join(map(str, row)))

def main_menu():
    """Основное меню приложения."""
    processor = MatrixProcessor()

    while True:
        print("\nМеню:")
        print("1) Ввод матрицы вручную")
        print("2) Генерация случайной матрицы")
        print("3) Обработка матрицы")
        print("4) Вывод результата")
        print("0) Завершение работы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            processor.input_matrix()
        elif choice == '2':
            processor.generate_matrix()
        elif choice == '3':
            if not processor.matrix:
                print("Ошибка: матрица не введена. Пожалуйста, введите данные или сгенерируйте их.")
                continue
            result = processor.process_matrix()
            print("Матрица обработана.")
            processor.matrix = result  # Сохраняем результат в основной атрибут
        elif choice == '4':
            processor.output_matrix()
        elif choice == '0':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()
