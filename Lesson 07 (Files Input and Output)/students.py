import csv
from pathlib import Path


CSV_FILE = Path(__file__).with_name("students.csv")


def get_students():
    students = []

    while True:
        name = input("Nome do aluno (ou Enter para terminar): ").strip()
        if not name:
            return students

        home = input("Residência do aluno: ").strip()
        students.append([name, home])


def create_students_file():
    try:
        with CSV_FILE.open("x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(get_students())
    except FileExistsError:
        print("O arquivo students.csv já existe; ele não foi alterado.")
    else:
        print("Arquivo students.csv criado.")


def rewrite_students_file():
    with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(get_students())

    print("Arquivo students.csv reescrito.")


def read_students_file():
    students = []

    with CSV_FILE.open(newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                name, home = row
                students.append({"name": name, "home": home})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")


def main():
    print("1. Criar students.csv (sem substituir se já existir)")
    print("2. Reescrever students.csv")
    print("3. Ler students.csv")

    choice = input("Escolha uma opção: ").strip()

    if choice == "1":
        create_students_file()
    elif choice == "2":
        rewrite_students_file()
    elif choice == "3":
        read_students_file()
    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
