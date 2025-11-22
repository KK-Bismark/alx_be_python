# A script that performs specified operations with dates and times.


from datetime import datetime, date, timedelta


def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")


def calculate_future_date():
    n_days = int(input("Enter the number of days to add to the current date: "))
    today = date.today()
    future_date = today + timedelta(days=n_days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")


def main():
    display_current_datetime()
    calculate_future_date()



if __name__ == "__main__":
    main()
