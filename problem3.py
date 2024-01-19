from problem1 import Transport
import csv
class Truck(Transport):
    def __init__(self, brand, model, color,weightCapacity):
        assert weightCapacity>0, f"weight_capacity can't be negative:{self.weightCapacity}"
        super().__init__(brand, model, color)
        self.weightCapacity=weightCapacity
    @classmethod
    def csv_objects(self):
        with open("Transport.csv","r") as ftransport:
            reader=csv.DictReader(ftransport)
            transports=list(reader)
            for transport in transports:
                Truck(
                    brand=transport.get("brand"),
                    model=transport.get("model"),
                    color=transport.get("color"),
                    weightCapacity=int(transport.get("weightCapacity")),
                )
    def getinfo(self):
       information= super().getinfo()+f" weight_capacity:{self.weightCapacity}"
       return information
    def __repr__(self) -> str:
        representation=super().__repr__()[:-1]+f", {self.weightCapacity})\n"
        return representation
Truck.csv_objects()
print(Truck.all)
print(Truck.getinfo(Truck.all[0]))