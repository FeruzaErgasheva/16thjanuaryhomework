from problem1 import Transport
import csv
class Car(Transport):
    def __init__(self, brand:str, model:str, color:str,speed:int,seatCount:int,manufactureDate:str):
        assert speed>0, f"speed can be at least 1 m/h {speed}"
        assert seatCount>=2, f'seat count can be at least 2:{seatCount}'
        
        
        super().__init__(brand, model, color)
        self.speed=speed
        self.seatCount=seatCount
        self.manufactureDate=manufactureDate
    @classmethod
    def csv_objects(self):
        with open("Transport.csv","r") as ftransport:
            reader=csv.DictReader(ftransport)
            transports=list(reader)
            for transport in transports:
                Car(
                    brand=transport.get("brand"),
                    model=transport.get("model"),
                    color=transport.get("color"),
                    speed=int(transport.get("speed")),
                    seatCount=int(transport.get("seatCount")),
                    manufactureDate=transport.get("manufactureDate")
                )
    def getinfo(self):
        information=super().getinfo()+f" speed:{self.speed} seat_count:{self.seatCount} manufacture_date:{self.manufactureDate}"
        print(information)
    def __repr__(self) -> str:
        representatiton=super().__repr__()[:-1]+f",{self.speed}, {self.seatCount}, '{self.manufactureDate}')\n"
        return representatiton

Car.csv_objects()
print(Car.all)