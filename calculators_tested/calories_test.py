from calculators.index import CaloriesCalculator, Record

records = [Record(amount=145, comment='кофе'), 
          Record(amount=300, comment='Серёге за обед'), 
          Record(amount=3000,comment='бар в Танин др',date='08.11.2019')]

def test_calories():
  cash_calc = CaloriesCalculator()
  for r in records:
    cash_calc.add_record(r)

  assert cash_calc.get_calories_remained() == "На сегодня осталось 445 rub"

test_calories()
