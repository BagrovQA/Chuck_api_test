import requests


class New_joke_test():
    """Создание новой шутки"""


    def __init__(self):
        pass


    def test_create_new_random_joke(self):
        """Создание случайной шутки"""

        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Статус код :" + str(result.status_code))
        assert 200 == result.status_code
        print("Успешно!!! Мы получили новую шутку")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        # check_info = check.get("categories")
        # print(check_info)
        # assert check_info == []
        # print("Категория верна!!!")
        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
           print("Chuck присутствует!!!")
        else:
            print("Chuck отсутствует!!!")

random_joke = New_joke_test()
random_joke.test_create_new_random_joke()
