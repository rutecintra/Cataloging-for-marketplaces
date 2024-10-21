from flask import Blueprint, request, jsonify, Response
from src.controllers.productweight_controller import ProductWeightController
# from src.models.product_model import Product
import json
from collections import OrderedDict

productweight_bp = Blueprint('productweight', __name__)

controller = ProductWeightController()

@productweight_bp.route('/productweight', methods=['POST'])
def product_weight_api():

    data = request.get_json()

    if 'weight_search_channel' not in data:
        return jsonify({"error": "The 'weight_search_channel' field is required"}), 400
    
    result = controller.process_product_weight(data)
    return Response(
        response=json.dumps(result, ensure_ascii=False, sort_keys=False),
        mimetype='application/json'
    )

# @productweight_bp.route('/test_product', methods=['GET'])
# def test_product_api():
#     # Simula um produto
#     product = Product(
#         sku="6321794",
#         name="Logitech - C920s Pro 1080 Video Conferencing, Streaming, and Gaming Webcam with Privacy Shutter - Black-960-001257",
#         brand="Logitech",
#         image_url="https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6321/6321794_sd.jpg"
#     )

#     # Definindo os valores de peso
#     product.estimated_weight_bestbuy = "181.44 kg"
#     product.estimated_weight_gpt = "N/A"
#     product.average_weight = "0.18 kg"

#     response_data = OrderedDict([
#         ("sku", product.sku),
#         ("productname", product.name),
#         ("productbrand", product.brand),
#         ("image_url", product.image_url),
#         ("estimated_weight_bestbuy", product.estimated_weight_bestbuy),
#         ("estimated_weight_gpt", product.estimated_weight_gpt),
#         ("average_weight", product.average_weight)
#     ])

#     return Response(
#         response=json.dumps(response_data, ensure_ascii=False, sort_keys=False),
#         mimetype='application/json'
#     )