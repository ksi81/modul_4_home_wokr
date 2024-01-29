#Перше завдання

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total_salary = 0

        for line in lines:
            name, salary_str = line.strip().split(',')
            salary = int(salary_str)
            total_salary += salary

        if len(lines) > 0:
            average_salary = total_salary / len(lines)
        else:
            average_salary = 0

        return total_salary, average_salary

    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Приклад використання функції:
total, average = total_salary("path/to/salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
