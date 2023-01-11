from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)  # Открываем страницу
html = page.read().decode("utf-8")  # Извлекаем HTML код и декодируем в utf-8
# Находим заголок и индекс самого заголовка
start_index_name = html.find("Name: ") + len("Name: ")
end_index_name = html.find("</h2>")  # Находим индекс закрывающего тега
name = html[start_index_name:end_index_name]  # Извлекаем текст с помощаю среза
start_index_color = html.find("Favorite Color: ") + len("Favorite Color: ")
end_index_color = html.find("\n</center>")
color = html[start_index_color:end_index_color]
print(name)
print(color)
