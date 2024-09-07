from matplotlib.dates import YearLocator
from driver_data_plot import *

class user_interface:
    import traceback
    import logging
    import driver_data
    import driver_data_plot
    from datetime import datetime

    year: int
    race_number: int
    race_type: str
    driver: str
    current_year = datetime.now().year


    while True:
        try:
            year = int(input("Enter season Year (Ex = 2019): "))
            race_number = int(input("Number of race in the year: "))
            race_type = input("Enter event (FP1 = free prac 1, Q1 = qualifying 1): ")
            driver = input("First 3 letters of driver's last name (Ex: Hamilton = HAM): ")


            driver1 = driver_data.driver_data(year, race_number, race_type, driver)
            
            driver2 = driver_data.driver_data(2019, 2, "R", "LEC")
            
            plot1 = driver_data_plot.driver_data_plot(driver1)
            
            plot1.speed_time_compare(driver2)

        except Exception as e:
            if year > current_year:
                    print("Year is not possible")
            else:
                logging.error(traceback.format_exc())
    