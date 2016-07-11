﻿#Тестовое задание на курсы epam'а осень 2013

##Условие задачи

Определить класс, описывающий покупку одного и того же штучного 
товара по одной и той же цене (в белорусских рублях) в течение 
одного месяца и содержащий сведения о дне покупки и количестве 
приобретенных единиц.
Допускаются еще три варианта покупок:
1. со скидкой, задаваемой процентом от стоимости 
`(стоимость покупки = стоимость партии товара * (1 – процент скидки/100))`; 
2. с фиксированной (постоянной) скидкой за транспортные расходы 
на доставку товара 
`(стоимость покупки = стоимость партии товара – транспортные расходы)`;
3. с бонусом в виде другого товара в единичном количестве 
`(стоимость покупки = стоимость партии товара – цена бонусного товара)`. 


####Создать консольное приложение, в котором выполнить следующие задания: 
– определить набор покупок различного вида (не менее 10); 
– отсортировать покупки по возрастанию дня покупки; 
– вывести на консоль в табличном виде (можно без границ) 
набор покупок (полный состав атрибутов и стоимость); 
– определить, была ли покупка в десятый день месяца; 
– отсортировать покупки по категориям (обычная, со скидкой по проценту, 
со скидкой за транспорт, с бонусной скидкой) и вывести их на консоль. 

 
####Требования: 
– Использовать объектно-ориентированный подход для описания сущностей 
предметной области. 
– Массив или коллекцию покупок инициализировать в коде с помощью конструктора 
или метода, не используя внешние источники данных: консоль (т.е. ввод с 
клавиатуры), файлы, СУБД, XML и т.п. 
– Инициализацию выполнить без датчика случайных чисел. Передавать в 
конструктор корректные константные значения. 
– Приложение должно быть консольным. Не использовать графический интерфейс! 
Таким образом, приложение ничего не должно вводить, а только выводить 
результаты на консоль. 

 
####Предпочтения по выбору: 
– языка программирования: 
  * Java; 
  * C++; 
  * другой ООП язык. 
– реализации сортировки и поиска: 
  * интерфейс библиотек (например, метод sort() подходящего класса); 
  * собственный код.