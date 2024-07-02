# Документация по RestAPI запросам

<hr>

### URLs
  GET   /submitData/    
  POST  /submitData/    
* Просмотр и добавление новых записей: http://127.0.0.1:8000/submitData/    
> *Пример запроса:* http://127.0.0.1:8000/submitData/   

<img src="samples/sample_1.jpg" width="800" />
 

<hr>

### /submitData/{id}

  GET  /submitData/{id}    
  POST /submitData/{id}    
* Просмотр и редактирования конкретной записи: http://127.0.0.1:8000/submitData/<int:pk>

> *Пример запроса:* http://127.0.0.1:8000/submitData/1

<img src="samples/sample_2.jpg" width="800" />

<hr>

### /submitData/{id}/status

#### GET /submitData/{id}/status
Получение статуса записи: http://127.0.0.1:8000/submitData/<int:pk>/status

>*Пример запроса:* http://127.0.0.1:8000/submitData/1/status

<img src="samples/sample_3.jpg" width="800" />


### COMMANDS:
#### Запуск сервера
    python manage.py runserver
  