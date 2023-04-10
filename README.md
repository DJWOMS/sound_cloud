# Sound Cloud

Проект Sound Cloud - это аудио платформа, которая позволяет людям находить, слушать и скачивать музыку. Музыканты могут загружать музыку для бесплатного использования.
### Функционал
- Авторизация через Google и Spotify
- Редактирование профиля пользователя
- Создать, редактировать и удалять 
  - Альбомы
  - Плейлисты
  - Треки
  - Лицензии
- Загрузка, воспроизведение и скачивание музыки
- Добавление исполнителя в избранное
- Комментарии к треку

### Интересное
- Кастомная модель пользователя
- Аутентификация пользователя с использованием JWT
- Валидаторы для загружаемых файлов
- Проверка прав, перед тем как nginx отдаст файл пользователю

**Ссылки**:
- [Сайт](https://collabteam.dev)
- [YouTube](https://youtube.com/playlist?list=PLF-NY6ldwAWosy6hAyKMwZozmEyq1J2fg)
- [Telegram](https://t.me/trueDjangoChannel)

### Инструменты

- Python >= 3.9
- Django Rest Framework
- Docker
- Postgres
- Nginx

## Старт

#### 1) В корне проекта создать переименовать .env.example в .env.dev и прописать свои настройки

#### 2) Создать образ и запустить контейнер

    docker-compose up --build
    
##### 3) Перейти по адресу

    http://localhost/api/v1/swagger/

##### 4) Создать супер юзера

    docker exec -it sound_cloud_web bash
    python manage.py createsuperuser
                                                        
##### 0) Если нужно очистить БД

    docker-compose down -v
 
## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2021-present, DJWOMS - Omelchenko Michael




