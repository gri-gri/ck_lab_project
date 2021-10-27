# ITMO lab-DElivery Application (I.D.E.A.)
## Пользовательские кейсы
### Кейсы со стороны преподавателя:
#### Use-case 1. Добавление новой лабораторной работы.
1.	Пользователь нажимает кнопку “создать”.
2.	Вводит название работы. 
3.	Если работа с таким названием уже существует – пользователь получает предложение изменить название.
4.	Пользователь назначает дедлайн сдачи работы.
5.	Если назначенная дата уже прошла, пользователь получает предложение изменить дедлайн.
6.	Пользователь добавляет содержание работы.
7.	Прикрепляет необходимые файлы
8.	Выбирает из выпадающего списка группы, которым назначена работа.
9.	При корректных данных в полях “Название” и “Дедлайн” (при которых не выполняются шаги 3 и 5), пользователь может нажать кнопку “Сохранить”.
#### Use-case 2. Редактирование лабораторной работы.
1.	Пользователь нажимает на кнопку “Просмотр” рядом с названием работы.
2.	В открывшемся окне просмотра работы нажимает кнопку “Редактировать”.
3.	Повторяет шаги 2-7 Use-case 1.
#### Use-case 3. Удаление лабораторной работы.
1.	Пользователь нажимает на кнопку “Просмотр” рядом с названием работы.
2.	В открывшемся окне просмотра работы нажимает кнопку “Удалить”.
3.	Получает предупреждение о необратимости действия и просьбу подтвердить решение (“Вы действительно хотите удалить?”), нажимает “да”.
#### Use-case 4. Просмотр и проверка сданных работ.
1.	Пользователь нажимает на кнопку “Сданные работы” рядом с названием работы.
2.	Видит список ФИО студента + группа + сданный файл. Может отсортировать список так, чтобы непросмотренные работы показывались наверху.
3.	Выбирает нужный файл.
4.	При необходимости может пометить работу как “просмотренную”, нажав на кнопку в той же строке списка.

### Кейсы ученика
#### Use case 5. Сдача работы.
1.	Выбирает из выпадающего списка свою группу.
2.	Выбирает из списка работ нужную.
3.	Если дедлайн не просрочен, открывается окно сдачи работы.
4.	Вводит ФИО.
5.	Если человек с таким ФИО не состоит в выбранной группе или если человек с таким ФИО уже сдал эту работу, пользователь получает предупреждение об этом.
6.	Пользователь прикрепляет файл.
7.	Если ФИО корректно (не выполняется шаг 5), пользователь может нажать кнопку “отправить”.

