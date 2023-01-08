import pathlib

lines_of_text = [
"Discovery\n",
"Enterprise\n",
"Defiant\n",
"Voyager\n",
]

path = pathlib.Path.home() / "starships.txt"  # Определяем пусть файла
path.touch()  # Создаём файл
with path.open(mode="w", encoding="utf-8") as file:  # Открываем с перезаписью
    file.writelines(lines_of_text)  # Пишем список

with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines(): 
        print(line, end="")

with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        if line.startswith("D"):  # Выводим строки начинающиеся с D
            print(line, end="")

