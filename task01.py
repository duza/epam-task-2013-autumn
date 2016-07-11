# -*- coding: utf-8 -*-
''' Python 2.7.3'''

'''Функция для смены кодировки в utf-8 возможности вывода кириллицы в консоли'''
def dec(e):
    return e.decode('utf-8')

'''Объявляем класс покупок (главный или супер-класс)'''
class buy:                                                                 
    def __init__(self,a1=0,a2=1,a3=1):  #   Создаем метод-конструктор класса
        self.name = "Обычная"   #   Тип покупки                                           
        self.price = a1         #   Цена покупки
        self.day = a2           #   День покупки 
        self.number = a3        #   Количество единиц товара (штук)
        self.cost = self.price * self.number    #   Общая стоимость
    def out(self):  #   Метод для вывода атрибутов нашего класса
        print '|','%24s'%self.name.decode('utf-8') ,'|', '%12d'%self.price,'|', '%12d'%self.day,'|', '%24d'%self.number,'|', '%15d'%self.cost,'|','%32s'%dec('нет'),'|'  
        print '-'*138
        
'''Создаем класс покупок со скидкой по проценту (подкласс по отношению к классу buy)'''        
class buysale(buy):
    def __init__(self,a1=0,a2=1,a3=1,a4=15):    #   Переопределяем метод-конструктор и делаем его расширение
        buy.__init__(self,a1,a2,a3)
        self.name = "Со скидкой по проценту"
        self.sale = a4
        self.cost = self.cost*(1-self.sale/100)
    def out(self):  #   Переопределяем метод т.к. появился атрибут скидок который нужно вывести
        print '|','%24s'%dec(self.name) ,'|', '%12d'%self.price,'|', '%12d'%self.day,'|', '%24d'%self.number,'|', '%15d'%self.cost,'|','%32d'%self.sale,'|'  
        print '-'*138

class buyfix(buysale):
    def __init__(self,a1=0,a2=1,a3=1,a4 = 40000):
        buysale.__init__(self,a1,a2,a3,a4)
        self.name = "Со скидкой по транспорту"
        self.cost = self.price * self.number - a4

class buybonus(buyfix):
    def __init__(self,a1=0,a2=1,a3=1,a4 = 50000):
        buyfix.__init__(self,a1,a2,a3,a4)
        self.name = "Со скидкой-бонусом"

'''Функция вывода всех покупок в виде таблицы'''        
def output():
    print '-'*138
    print dec('|         Тип покупки      | Цена покупки | День покупки | Количество единиц товара | Общая стоимость | Скидка (зависит от типа покупки) |')
    print '-'*138
    i=0
    while i<len(lst):
        lst[i].out()
        i=i+1
        
'''Функция, определяющая была ли покупка десятого дня'''
def dozen():
    y=0
    for z in lst:
        if z.day == 10:
            y = y + 1
    if y > 0:
        print dec('Да, покупка 10-го числа была совершена')
    else:
        print dec('Нет, покупки 10-го числа не было')

'''Инициализируем список покупок разных классов используя метод __init__'''        
lst = [buy(50000,12,23),buysale(120000,17,8,20),buyfix(200000,3,20,45000),buybonus(30000,1,5,75000),buy(160000,27,15),buysale(225000,29,11,12),
       buyfix(197000,13,20,25000),buybonus(241000,10,13,32000),buy(55000,14,4),buysale(132000,2,8,8),buyfix(302000,16,4,16000),buybonus(17000,13,25,32000)]
print dec('Отсортированные покупки по атрибуту "день покупки":')
lst = sorted(lst, key=lambda x: x.day)  #   Сортируем список объектов по возрастанию атрибута day, используя неявную функцию lambda и функцию sorted()
output()
dozen()
print "\n"
print dec('Отсортированные покупки по атрибуту "тип покупки":')
lst.sort(key=lambda x: x.name)  #   Сортируем список объектов по name используя метод списка sort()
output()
