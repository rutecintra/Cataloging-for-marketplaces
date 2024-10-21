class Product:
    def __init__(self, sku, name, brand, image_url):
        self.sku = sku
        self.name = name
        self.brand = brand
        self.image_url = image_url
        self.estimated_weight_bestbuy = None
        self.estimated_weight_gpt = None
        self.average_weight = None

    def to_dict(self):
        return {
            "sku": self.sku,
            "productname": self.name,
            "productbrand": self.brand,
            "image_url": self.image_url,
            "estimated_weight_bestbuy": self.estimated_weight_bestbuy or "N/A",
            "estimated_weight_gpt": self.estimated_weight_gpt or "N/A",
            "average_weight": self.average_weight or "N/A"
        }