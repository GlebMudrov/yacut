# Проект Yacut

## Описание проекта
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Технологии
- Python 3.11
- Flask 2.0
- SQLAlchemy 1.4

## Запуск проекта
1. Клонировать репозиторий (по SSH)

```
git@github.com:GlebMudrov/yacut.git
```

2. Установить и активировать виртуальное окружение

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

3. Установить зависимости проекта

```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Примечание: с последней версией pip не все зависимости могут установиться автоматически.
При необходимости недостающие зависимости можно установить вручную:
```
pip install название_библиотеки
```
4. Создать и заполнить файл .env

```
touch .env
```
Пример заполнения:
```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=123456
```

5. Запустить сервер

```
flask run
```

## Автор проекта:  <a href= "https://github.com/GlebMudrov">__Мудров Глеб__<a/>