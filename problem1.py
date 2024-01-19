import csv
class Transport:
    all=[]
    def __init__(self,brand,model,color): #setmetodlari hammasi bittada
        self.brand=brand
        self.model=model
        self.color=color
        Transport.all.append(self)
    @classmethod
    def csv_objects(self):
        with open("Transport.csv","r") as ftransport:
            reader=csv.DictReader(ftransport)
            transports=list(reader)
            for transport in transports:
                Transport(
                    brand=transport.get("brand"),
                    model=transport.get("model"),
                    color=transport.get("color")
                )
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.brand}','{self.model}','{self.color}')"
    def getinfo(self): #Transportning csv listdagi indexi boyica selfga berish kerak->Listning 1 ta elementi haqida malumot qaytaradi
        return f'''brand:{self.brand}  model:{self.model}  color:{self.color}'''
#print(Transport.all)->Listdagi hamma elementlarning malumotlarini chiqaradi
        