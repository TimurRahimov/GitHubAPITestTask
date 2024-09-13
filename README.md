# GitHub API

Автоматический тест для проверки работы с [GitHub API](https://docs.github.com/en/rest) на языке Python.

### ⚡ Быстрый старт

Чтобы запустить тесты, необходимо:

1. Установить [Python 3.12](https://www.python.org/downloads/);
2. Скачать данный репозиторий в виде zip-архива, нажав на зелёную кнопку "< > Code", после чего "Download ZIP";
3. Распаковать содержимое архива. Открыть папку GitHubAPITestTask-master;
4. Запустить командную строку, изменить текущую рабочую директорию на папку GitHubAPITestTask-master;
5. Создать виртуальное окружение: `python -m venv ./venv/`

6. Активировать виртуальное окружение:

- Для Windows (PowerShell): `.\venv\Scripts\activate.ps1`
- Для Windows (Командная строка): `.\venv\Scripts\activate.bat`
- Для Linux: `source ./venv/bin/activate`

7. Установить требуемые библиотеки:

- Для Windows: `.\venv\Scripts\python.exe -m pip install -r requirements.txt`
- Для Linux: `pip install -r requirements.txt`

8. Получить токен API:

- Для получения токена API необходимо перейти по ссылке https://github.com/settings/tokens?type=beta;
- Нажать кнопку "Generate new token";
- Ввести в поле "Token name" произвольное название токена;
- Установить для параметра "Repository access" значение "All repositories";
- Установить для параметра "Repository permissions" значение "Administration" = "Read and write";
- Нажать на зеленую кнопку "Generate token";

9. Установить переменные окружения:

- Для установки переменных окружения необходимо создать файл ".env" в корне рабочей папки;
- Прописать в данном файле имя пользователя GitHub, токен API и имя репозитория в формате:

```python
GH_API_USERNAME = "Имя пользователя GitHub"
GH_API_TOKEN = "Токен API"
GH_API_REPOSITORY_NAME = "Имя репозитория"
```

10. Запустить скрипт:

- Для Windows: `.\venv\Scripts\python.exe test_api.py`
- Для Linux: `python3 test_api.py`

11. По прохождении всех тестов в командной строке отобразится сообщение "Ran 1 tests in **.***s", под которым будет написано "OK"