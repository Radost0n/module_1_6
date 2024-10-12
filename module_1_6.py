my_dict = {'Слава': 2006, 'Максим': 2004}
print("По списку:", *my_dict.items())
print("Год рождения Славы:", my_dict.get("Слава"))
print("Год рождения:", my_dict.get("Кабан", "Не найдено"))
my_dict["Сеня"] = 2007
my_dict["Дима"] = 2007
print("Обновленный список my_dict:", *my_dict.items())
remov_value = my_dict.pop("Максим", "Не найдено")
print("Удалено значение для Максим:", remov_value)
print("Обновлённый список my_dict:", *my_dict.items())

my_set = {1, 2, 3, 4, 5, 6, 4, 5, 6, "Слава", True, 2, "кабанчик", "Слава"}
print("Варики:", *my_set)
my_set.add(7)
my_set.add("кабаня")
my_set.remove(1)
print("Измененный список:", *my_set)