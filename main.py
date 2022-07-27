from application.salary import calculate_salary
from application.db.get_employees import get_employees
from application.current_date_time import current_time

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    current_time()
