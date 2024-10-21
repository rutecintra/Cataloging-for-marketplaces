from src.models.product_model import Product
from src.drivers.bestbuy_driver import BestBuyAPI
from src.drivers.gpt_driver import GPTAPI
from src.utils.weight_utils import calculate_average_weight, convert_weight_to_kg
from collections import OrderedDict

class ProductWeightController:
    def __init__(self):
        self.bestbuy_api = BestBuyAPI()
        self.gpt_api = GPTAPI()

    def process_product_weight(self, data):
        weight_search_channel = data.get('weight_search_channel', 'all')
        products = data.get('products', [])

        results = []

        for product_data in products:

            product = Product(
                sku=product_data['sku'],
                name=product_data['productname'],
                brand=product_data['productbrand'],
                image_url=product_data['image_url']
            )

            weight_bestbuy = None

            if weight_search_channel in ['bestbuy', 'all']:

                weight_bestbuy = self.bestbuy_api.product_weight_bestbuy(product.sku, product.name)

                if weight_bestbuy:

                    product.estimated_weight_bestbuy = convert_weight_to_kg(weight_bestbuy)
                    print(convert_weight_to_kg(weight_bestbuy))

            weight_gpt = None

            if weight_search_channel in ['gpt', 'all']:

                weight_gpt = self.gpt_api.product_weight_gpt(product['image_url'], product['product_name'], product['product_brand'])

                if weight_gpt:

                    product.estimated_weight_gpt = convert_weight_to_kg(weight_gpt)

            product.average_weight = calculate_average_weight(weight_gpt, weight_bestbuy)

            product_dict = OrderedDict([
                ("sku", product.sku),
                ("productname", product.name),
                ("productbrand", product.brand),
                ("image_url", product.image_url),
                ("estimated_weight_bestbuy", product.estimated_weight_bestbuy),
                ("estimated_weight_gpt", product.estimated_weight_gpt),
                ("average_weight", product.average_weight)
            ])

            results.append(product_dict)

        return results