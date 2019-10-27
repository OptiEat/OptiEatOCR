import json

class Product:
    def __init__(self, id, description, quantity, quantityType, expiration, shortName):
        self.id = id
        self.description = description
        self.quantity = quantity
        self.quantityType = quantityType
        self.expiration = expiration
        self.shortName = shortName

    def toJSON(self):
        return json.dumps(self.__dict__)
