from numpy import character


class speed_time:
    
    @staticmethod
    def driver1(year: int, race_number: int, race_type: str, driver: str):
        import json
        import plotly.express as px
        import plotly.express as px
        import fastf1
        import fastf1.plotting

        session = fastf1.get_session(year, race_number, race_type)
        session.load()
        

        session.load()
        fast_driver = session.laps.pick_driver(driver).pick_fastest()
        driver_car_data = fast_driver.get_car_data()
        t = driver_car_data['Time']
        vCar = driver_car_data['Speed']

        
       
        
        
        fig = px.line(x = t, y= vCar, title=f"{driver} speed in race {race_number} of {year}")
        fig.show()
        
        
    


    



    
    






