## Куда пойти

### Описание

Проект сайта "[Куда пойти](http://redbor.pythonanywhere.com/)" позволяет ознакомится с интересными местами.
Сайт представляет собой интерактивную карту, на которой отмечены места с описаниями и фотографиями.

### Установка
`Python3` должен быть установлен. Используйте `pip` (или `pip3`, если есть конфликт с `Python2`) 
для установки зависимостей:
```bash
pip install -r requirements.txt
```

### Первоначальная настройка

Скопируйте файл `.env.Example` из папки `short_links` и переименуйте его в `.env`.  

Заполните переменные окружения в файле `.env`:
- `ALLOWED_HOSTS` - Разрешенные хосты. Указываются через запятую, например: `127.0.0.1,localhost`;
- `SECRET_KEY` - Секретный ключ Django;
- `DEBUG` - Если нужно включить режим отладки web-сервера, установите значение в `True`.

### Запуск 
```bash
python manage.py runserver localhost:80
```

### Управление контентом
Для управления контентом сайта требуется суперпользователь-администратор и админка сайта.

#### Создание суперпользователя
```bash
python manage.py createsuperuser
```
Введите в консоли имя пользователя, email и пароль дважды.

#### Админка
Для управления контентом сайта откройте [панель администрирования](http://localhost/admin)
и введите логин и пароль суперпользователя.

### Загрузка данных из формата GeoJSON  

Описание места, куда можно пойти, состоит из [нескольких элементов](http://localhost/admin/places/place/1/change/).
Их можно вводить вручную через панель администрирования сайта. Но когда мест много, то проще воспользоваться
механизмом загрузки этих данных в формате [GeoJSON](https://ru.wikipedia.org/wiki/GeoJSON) из консоли.

Набор данных об интересных местах Москвы можно взять [здесь](https://github.com/devmanorg/where-to-go-places/tree/master/places).

Для загрузки данных о месте в формате [GeoJSON](https://ru.wikipedia.org/wiki/GeoJSON), 
выполните в консоли следующую команду:
```bash
python manage.py load_place <geojson_url>
```

где ```geojson_url``` ссылка на файл в формате [GeoJSON](https://ru.wikipedia.org/wiki/GeoJSON).

Пример файла в формате [GeoJSON](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json):  
```json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

Описание формата GeoJSON в [Википедии](https://ru.wikipedia.org/wiki/GeoJSON).

### Демо сервер  

В демонстрационных целях сайт доступен по адресу 
[redbor.pythonanywhere.com](http://redbor.pythonanywhere.com/).

Его [админка](http://redbor.pythonanywhere.com/admin/). Данные для входа: admin - 111.

