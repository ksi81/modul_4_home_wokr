#Перше завдання
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total_salary = 0
        for line in lines:
            try:
                name, salary_str = line.strip().split(',')
                salary = float(salary_str)
                total_salary += salary
            except ValueError:
                print(f"Помилка при читанні рядка: {line}. Неправильний формат даних.")

        if len(lines) == 0:
            print("Файл містить нульові дані.")

        average_salary = total_salary / len(lines)

        return total_salary, average_salary

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None

    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None, None

# Введення даних
input_data = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
Kokm, 500
"""

# Збереження даних у файл
file_path = "/Users/sleeper/Documents/GoIt-Python/HomeWork_4/modul_4_home_wokr/salary_file.txt"
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(input_data)

# Перевірка функції
total, average = total_salary(file_path)

# Виведення результату
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
