import datetime

def show_current_datetime():
    current_datetime = datetime.datetime.now()
    print("Current Date and Time:", current_datetime)

if __name__ == "__main__":
    show_current_datetime()

import datetime

def show_current_datetime():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted Date and Time:", formatted_datetime)

if __name__ == "__main__":
    show_current_datetime()
