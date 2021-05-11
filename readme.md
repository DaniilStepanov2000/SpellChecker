# Система распознавания текста: спеллчекер

## Проект

Данная система предназначена для дальнейшего внедрения в структуру чат-ботов. <br> 
__Основная задача__: распознавание введенного пользователем текста и вывод слов, в которых присутствуют ошибки. <br>
__Основная концепция__: в проекте реализован парсер, который проходится по странице википедии и читает весь HTML-текст из страницы. Парсер работает рекурсивно: сначала задается начальная страница для парсинга, 
после чего идет поиск всех ссылок на данной странице, случайным образом выбирается одна из станиц и алгоритм повторяется. 
Текст страницы сохраняется в папку ```/data```. В процессе парсинга происходит обработка текста и составление финального словаря, 
который называется ```dictionary.txt``` и находится в папке ```/data```.

## Технические детали

__Стек, который используется для разработки:__ requests(для отправления на сервер википедии), BeautifulSoup(для парсинга страниц), nltk(для работы с текстом).<br>
Весь список библиотек можно посмотреть в файле _requirements.txt_.

## Структура проекта

1. Файл ```create_data.py``` - данный скрипт выполняет: парсинг страницы википедии, сохранение статей в папку ```/data```, обработку текста, создание словаря с названием ```dictionary.txt``` и сохранение его в папку ```/data```.<br>
2. Файл ```check_sentence.py``` - отвечает за взаимодействие с пользователем. Консольная программа.

## Развертывание проекта

1. Перейти в директорию ```/SpellChecker```. 
2. Создать виртуальную среду. 
   ```
    python3 -m venv env_name
   ```
3. Активировать виртуальную среду, используя команду:<br>
   _Windows:_
   ``` 
   env_name/Scripts/activate
   ```
   _Mac OS / Linux:_
   ``` 
   source mypython/bin/activate
   ```
   
4. Установить все пакеты, которые перечислены в файле _requirements.txt_. Для этого использовать команду:
   ```
   pip install -r requirements.txt
   ```
5. Создать файл config.json.

6. В файле config.json создать переменные:<br>
   ```BASE_number_articles``` - содержит количество статей для парсинга. __Тип:__ _int_.<br>
   ```BASE_start_URL``` - содержит стартовую ссылку на статью в википедии. С данной ссылки начинается парсинг статей. __Тип:__ _str_.
   ```json
      {
     "BASE_number_articles": 50,
     "BASE_start_URL": "https://ru.wikipedia.org/wiki/%D0%94%D0%B8%D1%81%D0%BA%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F_%D0%9A%D1%8D%D1%82%D0%B8_%D0%9F%D0%B5%D1%80%D1%80%D0%B8"
      }
   ```
   
7. Запустить скрипт ```create_data.py```, используя команду:<br>
   ```
   python create_data.py
   ```
8. Запустить скрипт ```check_sentence.py```, используя команду:<br>
   ```
   python check_sentence.py
   ```
***
## Пример работы проекта

__Шаг 1:__ Запускаем скрипт ```create_data.py```, используя команду: ```python create_data.py```<br><br>
![image](https://user-images.githubusercontent.com/73431786/117779794-b1c79000-b247-11eb-8f03-179926245877.png)<br><br>
__Шаг 2:__ Запускаем скрипт ```check_sentence.py```, используя команду: ```python check_sentence.py```<br><br>
![image](https://user-images.githubusercontent.com/73431786/117780408-45995c00-b248-11eb-92b2-f7ecb87aa245.png)<br><br>
__Шаг 3:__ Вводим значение.<br><br>
![image](https://user-images.githubusercontent.com/73431786/117780602-75486400-b248-11eb-9e34-c59b47e58642.png)<br><br>
__Шаг 4:__ Вводим предложение для проверки правильности написания слов и получаем список слов, в которых присутствует ошибка.<br><br>
![image](https://user-images.githubusercontent.com/73431786/117780835-a9238980-b248-11eb-80b0-155245127aa2.png)<br><br>
__Шаг 5:__ Вводим значение '2' и завершаем работу с программой.<br><br>
![image](https://user-images.githubusercontent.com/73431786/117781122-f869ba00-b248-11eb-954d-34e9197d115f.png)<br><br>

# Ответы на вопросы
1. В чем недостатки этого способа построения спеллчекера? <br>
   Я считаю, что один из недостатков заключается в том, что данный спеллчекер не учитываем контекст, в котором находится слово. Так,
   например, в предложении _'Я дал зелье маны магу.'_ в слове _'магу'_ будет ошибка, если в словаре нет такого слова.
   
2. Быстро ли работает ваш спеллчекер? Можно ли его ускорить и если да, то как? <br>
   Разработанный спеллчекер работает достаточно быстро, но это все зависит от количества статей, которые надо спарсить и от количества слов в словаре.
   Для того, чтобы найти слово в файле ```dictionary.txt```, было принято решение хранить все слове в такой структуре данных, как множество, потому что поиск по множеству осуществляется быстрее, чем поиск по списку.
   Так же один из плюсов множество заключается в том, что оно гарантирует уникальность входящих в нее элементов.
   
3. Приведите интересные примеры правильных слов, которые этот спеллчекер считает ошибочными и наоборот, слов с опечаткой, которые считаются им правильными.
   