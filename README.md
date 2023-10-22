# Bewise Test

## Installation

1. Клонируйте репозиторий:

```bash
git clone https://github.com/codingoleg/Bewise_Test.git
```

2. Перейдите в папку проекта:

```bash
cd .\Bewise_Test\
```

+ Если в Windows используется Hyper-V вместо WSL, для создания volumes нужно добавить путь проекта в Docker по
  инструкции: https://stackoverflow.com/questions/62215781/docker-compose-failed-to-build-filesharing-has-been-cancelled-eshoponcontain
+ Запустите docker-compose:

```bash
docker-compose up
```

## Usage

Примеры запросов:
```bash
curl --location 'http://127.0.0.1:5000/api/v1/question' \
--header 'Content-Type: application/json' \
--data '{"questions_num": 5}'
```
Получает и записывает 5 вопросов в БД. Возвращает предыдущие вопросы, если таковые были.
Если БД пуста, возвращает пустой объект.
```bash
curl --location 'http://127.0.0.1:5000/api/v1/question' \
--header 'Content-Type: application/json' \
--data '{"questions_num": 3}'
```
Получает и записывает 3 вопроса в БД. Возвращает 5 вопросов, записанные в БД при первом запросе.

## License

GNU GPLv3 