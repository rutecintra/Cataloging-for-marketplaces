from src.services.image_service import download_image, get_image_description
import openai
import os

class GPTAPI:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key


    def product_weight_gpt(self, image_url, product_name, product_brand):

        image_path = download_image(image_url)
        
        if not image_path:

            return None

        description = get_image_description(image_path)

        try:

            response = openai.ChatCompletion.create(

                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente especializado em estimar pesos de produtos com base na descrição de imagens."},
                    {"role": "user", "content": f"Com base na descrição: '{description}', no nome do produto: '{product_name}' e na marca do produto: '{product_brand}', estime um peso específico do produto e responda com um número seguido da unidade de medida (g ou kg)."}
                ],

                max_tokens=10
            )

            return response.choices[0].message['content'].strip()
        
        except Exception as e:
            print(f"Error getting product weight: {e}")
            return None