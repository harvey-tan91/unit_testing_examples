import requests
class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fulllname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def month_schedule(self, month):
        ro = requests.get(f'http://company.com/{self.last}/{month}')
        if ro.ok:
            return ro.text
        else:
            return f'Bad Response.'

