from numpy import character


class f1collect:
    import requests
   
    @staticmethod
    def driver1(year: int, track: character, race_type: character, driver: character):
        import fastf1
        import json

        session = fastf1.get_session(year, track, race_type)
        session.load(telemetry=False, laps = False, weather = False)
        driver = session.get_driver(driver)
        return "Pronto {driver['FirstName']}?"

    @staticmethod
    def driver2(year: int, track: character, race_type: character, driver: character):
        import fastf1
        import json

        session = fastf1.get_session(year, track, race_type)
        session.load(telemetry=False, laps = False, weather = False)
        driver = session.get_driver(driver)
        return "Pronto {driver['FirstName']}?"

    



    
    






