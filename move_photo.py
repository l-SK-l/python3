from pathlib import Path

# Создаем папку images/ в папке practice_files/
images_dir = Path.home() / "practice_files" / "images"
images_dir.mkdir(parents=True, exist_ok=True)

practice_files = Path.home() / "practice_files" / "documents"
# Перебираем файлы в папке documents/
for file in practice_files.glob("*"):
    # Проверяем, что файл имеет расширение .png, .gif или .jpg
    if file.suffix in [".png", ".gif", ".jpg"]:
        # Показываем что нашли
        print(file)
        # Перемещаем файл в папку images/
        file.rename(images_dir / file.name)
