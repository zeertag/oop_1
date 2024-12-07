import requests
import webbrowser


class Search:
    def __init__(self, search_request):
        self._api = f'https://ru.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srsearch="{search_request}"'
        self._url = 'https://ru.wikipedia.org/w/index.php?curid='
        self._articles = {}

    @property
    def get_size(self):
        return len(self._articles)

    def get_names(self):
        try:
            r = requests.get(self._api)
            r.raise_for_status()
        except:
            return 0
        data = r.json()
        j = 0
        for i in data['query']['search']:
            self._articles[j] = [i['title'], i['pageid']]
            j += 1
        return 1

    def variation(self):
        print(f"Количество найденных статей: {len(self._articles)}.")
        if len(self._articles) > 0:
            print("\nВыберите нужную:\n")
            for i in range(len(self._articles)):
                print(f"{i + 1}: {self._articles[i][0]}")
            return 1
        return 0

    def choice(self, variant):
        webbrowser.open(f"{self._url}{self._articles[variant - 1][1]}")


class User:
    def __init__(self):
        self._for_search = None

    def get_search(self):
        while True:
            self._for_search = input("Введите слово для поиска: ")
            if len(self._for_search.strip()) == 0:
                print("Некорректный ввод. Попробуйте снова\n")
            else:
                break
        return self._for_search

    def check_connection(self, ans: object) -> object:
        if not ans:
            print("Ошибка соединения")
            return 0
        return 1

    def choose_article(self, max_size):
        while True:
            try:
                num = int(input("Введите номер статьи: "))
            except:
                print("Введены некорректные данные. Повторите попытку\n")
                continue
            if num <= 0 or num > max_size:
                print("Введены некорректные данные. Повторите попытку\n")
            else:
                return num


user = User()
request = user.get_search()
search = Search(request)
answer = search.get_names()
if user.check_connection(answer):
    variants = search.variation()
    print('\n')
    if variants:
        found_size = search.get_size
        chosen = user.choose_article(found_size)
        search.choice(chosen)
