import sys
from datetime import datetime, timedelta

def generate_date_list(input_date):
    try:
        input_date = datetime.strptime(input_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD' format.")
        return
    
    date_list = [input_date - timedelta(days=i) for i in range(10)]
    date_list = [date.strftime('%Y-%m-%d') for date in date_list]
    return date_list

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python code.py 'YYYY-MM-DD'")
    else:
        input_date = sys.argv[1]
        date_list = generate_date_list(input_date)
        if date_list:
            print(date_list)
