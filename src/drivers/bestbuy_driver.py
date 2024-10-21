import requests
import time
import os

class BestBuyAPI:
    def __init__(self):
        self.api_key = os.getenv("BESTBUY_API_KEY")
        self.base_url = "https://api.bestbuy.com/v1/products"

    def product_weight_bestbuy(self, product_sku, product_name):

        request_url = f'{self.base_url}/{product_sku}.json?show=name,shippingWeight&apiKey={self.api_key}'

        max_retries = 5
        backoff_factor = 2
        wait_time = 1 
        connect_timeout = 10 
        read_timeout = 20 

        for attempt in range(max_retries):

            try:
                response = requests.get(request_url, timeout=(connect_timeout, read_timeout))

                if response.status_code == 200:
                    product_data = response.json()
                    if product_data.get('shippingWeight'):
                        return f"{product_data['shippingWeight']} pounds"
                    else:
                        print(f"No products found for: {product_name}")
                        return None
                    
                elif response.status_code in [429, 403]:
                    print(f"Too Many Requests - Attempt {attempt + 1}. Waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                    wait_time *= backoff_factor

                else:
                    print(f"Error fetching information from Best Buy (status {response.status_code}): {product_name}")
                    return None

            except requests.exceptions.RequestException as e:
                print(f"Error fetching information from Best Buy: {e}")
                return None
            
        print(f"Failed to get information after {max_retries} attempts.")
        return None