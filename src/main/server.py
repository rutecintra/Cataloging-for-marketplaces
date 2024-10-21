from flask import Flask
from src.main.routes.productweight_route import productweight_bp

app = Flask(__name__)

app.register_blueprint(productweight_bp)

def start_server(host='0.0.0.0', port=8080):
    app.run(host=host, port=port, debug=True)