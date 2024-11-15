import random

class MatrixProcessor:
    def __init__(self):
        self.matrix = []

    def input_matrix(self):
        """Ввод матрицы вручную."""
        try:
            rows = int(input("Введите количество строк: "))
            self.matrix = []
            
            for i in range(rows):
                row = list(map(int, input(f"Введите элементы строки {i + 1} (через пробел): ").split()))
                self.matrix.append(row)
        except ValueError:
            print("Ошибка: Пожалуйста, введите целые числа.")

    def generate_matrix(self):
        """Генерация случайной матрицы."""
        rows = random.randint(2, 5)
        cols = random.randint(2, 5)
        self.matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
        
        print("Сгенерированная матрица:")
        self.output_matrix()

    def process_matrix(self):
        """Обработка матрицы: сортировка и добавление столбца с суммами модулей."""
        if not self.matrix:
            print("Ошибка: Матрица не введена. Пожалуйста, введите данные или сгенерируйте их.")
            return []

        sums = [sum(abs(x) for x in row) for row in self.matrix]
        
        new_matrix = [row + [sums[i]] for i, row in enumerate(self.matrix)]
        
        new_matrix.sort(key=lambda x: x[-1], reverse=True)
        
        return new_matrix

    def output_matrix(self):
        """Вывод матрицы."""
        if not self.matrix:
            print("Матрица пуста.")
            return
        
        for row in self.matrix:
            print("\t".join(map(str, row)))

    def menu(self):
        """Основное меню приложения."""
        while True:
            print("\nМеню:")
            print("1) Ввод матрицы вручную")
            print("2) Генерация случайной матрицы")
            print("3) Обработка матрицы")
            print("4) Вывод результата")
            print("0) Завершение работы")

            choice = input("Выберите пункт меню: ")

            if choice == '1':
                self.input_matrix()
            elif choice == '2':
                self.generate_matrix()
            elif choice == '3':
                result = self.process_matrix()
                if result:
                    self.matrix = result
                    print("Матрица обработана.")
            elif choice == '4':
                self.output_matrix()
            elif choice == '0':
                print("Завершение работы программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    processor = MatrixProcessor()  # Создание объекта класса вызовет метод menu
