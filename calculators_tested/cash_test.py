from calculators.index import CashCalculator, Record

records = [Record(amount=145, comment='кофе'), 
          Record(amount=300, comment='Серёге за обед'), 
          Record(amount=3000,comment='бар в Танин др',date='08.11.2019')]

def test_cash():
  cash_calc = CashCalculator()
  for r in records:
    cash_calc.add_record(r)

  assert cash_calc.get_today_cash_remained('rub')

test_cash()