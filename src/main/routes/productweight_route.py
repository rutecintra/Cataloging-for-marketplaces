from flask import Blueprint, request, jsonify
from src.controllers.productweight_controller import ProductWeightController

productweight_bp = Blueprint('productweight', __name__)

controller = ProductWeightController()

@productweight_bp.route('/productweight', methods=['POST'])
def product_weight_api():

    data = request.get_json()

    if 'weight_search_channel' not in data:
        return jsonify({"error": "The 'weight_search_channel' field is required"}), 400
    
    result = controller.process_product_weight(data)
    return jsonify(result)
