from numpy import character
import driver_data 
import fastf1

class driver_data_plot:
    
    driver: driver_data
    
    def __init__(self, driver: driver_data):
        self.driver = driver
    
    @classmethod    
    def event_string_builder(self, interpret):
        
        event_compare = ""
        
        match self:
            case _ if "FP" in self:
                event_compare = "Free Practice"
            case _ if "Q" in self:
                event_compare = "Qualifying"
            case _ if "R" in self:
                event_compare = "Race"
            case _ if "S" in self:
                event_compare = "Sprint"
    
        return event_compare
    

     
    def speed_time_plot(curr_driver, interpret):
        from matplotlib import pyplot as plt
        import fastf1
        import fastf1.plotting
       
       
        
        t1 = curr_driver.get_driver_car_data()['Time']
        vCar1 = curr_driver.get_driver_car_data()['Speed']
        
        event_data = curr_driver.get_race_type()
        
        event_type = driver_data_plot.event_string_builder(event_data, interpret)
        
        fig, ax = plt.subplots()
        ax.plot(t1, vCar1, label="speed")
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Speed (KM/H)')
        ax.set_title(f'{curr_driver.get_driver_name()} speed in {event_type} {curr_driver.get_race_number()} of {curr_driver.get_year()}')
        ax.legend()
        plt.show()
        
    def speed_time_compare(self, other_driver: driver_data):
        from matplotlib import pyplot as plt
        import fastf1
        import fastf1.plotting
    
        event_type = ""
               
        
        t1 = self.driver.get_driver_car_data()['Time']
        vCar1 = self.driver.get_driver_car_data()['Speed']
        
        t2 = other_driver.get_driver_car_data()['Time']
        vCar2 = other_driver.get_driver_car_data()['Speed']
        
        # event_data = self.driver.get_race_type()
        
        # event_type = self.event_string_builder(event_data)
        
        
        fig, ax = plt.subplots()
        ax.plot(t1, vCar1, label = self.driver.get_driver_name())
        ax.plot(t2, vCar2, label = other_driver.get_driver_name())
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Speed (KM/H)')
        ax.set_title(f'{self.driver.get_driver_name()} speed in {self.driver.get_race_type()} {self.driver.get_race_number()} of {self.driver.get_year()}')
        ax.legend()
        plt.show()
        
        



    
    






