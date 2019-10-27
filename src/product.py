import json


class Product:
    """
    Models a product from the receipt
    """

    def __init__(self, id, description, quantity, quantity_type, expiration, short_name):
        """
        Init method
        :param id: the product id
        :param description: the product description
        :param quantity: the product quantity
        :param quantity_type: the product quantity type (oz, fl oz, ....)
        :param expiration: the product expiration days
        :param short_name: the product short name
        """
        self.id = id
        self.description = description
        self.quantity = quantity
        self.quantityType = quantity_type
        self.expiration = expiration
        self.shortName = short_name

    def to_json(self):
        """
        :return: a product element as json
        """
        return json.dumps(self.__dict__)
