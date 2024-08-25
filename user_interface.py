from matplotlib.dates import YearLocator
from f1collect import *

class user_interface:
    import traceback
    import logging
    from datetime import datetime

    year: int
    race_number: int
    race_type: str
    driver: str
    current_year = datetime.now().year


    while True:
        try:
            year = int(input("Enter season Year (Ex = 2019)"))
            race_number = int(input("Number of race in the year"))
            race_type = input("Enter event (FP1 = free prac 1, Q1 = qualifying 1)")
            driver = input("First 3 letters of driver's last name (Ex: Hamilton = HAM)")


            print(f1collect.driver1_speed_time(year, race_number, race_type, driver))

        except Exception as e:
            if year > current_year:
                    print("Year is not possible")
            else:
                logging.error(traceback.format_exc())
    