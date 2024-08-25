from numpy import character


class f1collect:
    import requests
   
    @staticmethod
    def driver1_graph(year: int, race_number: int, race_type: str, driver: str):
        from matplotlib import pyplot as plt
        import fastf1
        import fastf1.plotting
        import json

        session = fastf1.get_session(year, race_number, race_type)
        session.load()
        

        session.load()
        fast_driver = session.laps.pick_driver(driver).pick_fastest()
        driver_car_data = fast_driver.get_car_data()
        t = driver_car_data['Time']
        vCar = driver_car_data['Speed']

        
        fig, ax = plt.subplots()
        ax.plot(t, vCar, label='Fast')
        ax.set_xlabel('Time')
        ax.set_ylabel('Speed [Km/h]')
        ax.set_title(f"{driver} speed in race {race_number} of {year}")
        ax.legend()
        plt.show()
        


    



    
    






