#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def info(first_name, second_name, birth, city, email, number):
    return ' '.join([first_name, second_name, birth, city, email, number])
print(info(first_name = "Nikita", second_name = "Koromyslov", birth = "10.12.2001", city = "Moscow", email = "nkws2020@gmail.com", number = "88005553535"))
