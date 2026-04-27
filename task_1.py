import datetime


class OnlineSalesRegisterCollector:
    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items    
    @property
    def number_items(self):
        return self.__number_items
    
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price.keys():
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__number_items += 1
            self.__name_items.append(name)

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__number_items -= 1
            self.__name_items.remove(name)
    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        return sum(total) * 0.9 if len(total) > 10 else sum(total)
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])
        return sum(total) * 0.9 * 0.2 if self.__number_items > 10 else sum(total) * 0.2
    
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])
        return sum(total) * 0.9 * 0.1 if self.__number_items > 10 else sum(total) * 0.1
    
    def total_tax(self):
        tax_20 = self.twenty_percent_tax_calculation()
        tax_10 = self.ten_percent_tax_calculation()
        return tax_20 + tax_10
    
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'
        
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year],
        ]
        now = datetime.datetime.now()
        for time in date:
            date_and_time.append(f'{time[0]}: {time[1](now)}')
        return date_and_time

if __name__ == '__main__':
    cheque = OnlineSalesRegisterCollector()

    cheque.add_item_to_cheque('чипсы')      # 50  (20%)
    cheque.add_item_to_cheque('кола')       # 100 (20%)
    cheque.add_item_to_cheque('печенье')    # 45  (20%)
    cheque.add_item_to_cheque('молоко')     # 55  (10%)
    cheque.add_item_to_cheque('кефир')      # 70  (10%)

    print('Товары в чеке:', cheque.name_items)
    print('Количество товаров:', cheque.number_items)
    print('Общая сумма:', cheque.check_amount())
    print('НДС 20%:', cheque.twenty_percent_tax_calculation())
    print('НДС 10%:', cheque.ten_percent_tax_calculation())
    print('Общий НДС:', cheque.total_tax())

    cheque.delete_item_from_check('кефир')
    print('После удаления "кефир":', cheque.name_items, '| кол-во:', cheque.number_items)

    print('Телефон:', OnlineSalesRegisterCollector.get_telephone_number(9001234567))
    print('Дата/время:', OnlineSalesRegisterCollector.get_date_and_time())
