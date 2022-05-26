from datetime import datetime

"""Возвращает дату с нужным типом в зависимости от типа аргумента"""
def make_date(date):
  if type(date) == str:
    return datetime.strptime(date, '%d.%m.%Y')
  elif isinstance(date, datetime):
    return date
  return None

class Record:
  def __init__(self, amount, comment, date=datetime.now()):
      self.amount = amount
      self.comment = comment
      self.date = make_date(date)
    

class Calculator:
  def __init__(self, limit=0):
    self.records = []
    self.today = datetime.now()
    self.limit = limit


  """Добавляет запись в массив записей, проверяя на тип"""
  def add_record(self, record):
    if not isinstance(record, Record):
      raise TypeError('Wrong record format')    
    self.records.append(record)

  """Возвращает количество потраченных единиц за сегодня"""
  def get_today_stats(self):
    count = 0
    for record in self.records:
      if record.date.day == self.today.day:
        count = count + record.amount
    return count

  """Возвращает количество потраченных единиц за неделю"""
  def get_weel_state():
    count = 0
    for record in self.records:
      if self.today.week - 7 < record.date.week <= self.today.week:
        count = count + record.amount
    return count


class CashCalculator(Calculator):
  def __init__(self, limit=0, *args, **kwargs):
    super().__init__(limit=limit)
    self.USD_RATE = 90
    self.EURO_RATE = 100
    
  """Возвращает статус баланса относительно потраченных денег за сегодня и лимита на траты"""
  def get_today_cash_remained(self, currency):
    coef = 1
    if currency == 'usd':
      coef = self.USD_RATE
    elif currency == 'eur':
      coef = self.EURO_RATE

    wasted = self.get_today_stats()
    if wasted < self.limit:
      return f"На сегодня осталось {wasted * coef - self.limit} {currency}"
    elif wasted == self.limit:
      return "Денег нет, держись"
    elif wasted > self.limit:
      return f"Денег нет, держись: твой долг - {wasted * coef - self.limit} {currency}"


class CaloriesCalculator(Calculator):
  """Возвращает статус поглощенных калорий относительно поглощенных калорий за сегодня и лимита на калории"""
  def get_calories_remained(self):
    wasted = self.get_today_stats()
    if wasted < self.limit:
      return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {wasted - self.limit} кКал"
    elif wasted >= self.limit:
      return "Хватит есть!"
    

cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000,comment='бар в Танин др',date='08.11.2019'))

print(cash_calculator.get_today_cash_remained('rub'))
