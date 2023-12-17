from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import dash

if __name__ == '__main__':
    print(f'Сегодня {datetime.date.today()}')
    calculate_salary()
    get_employees()