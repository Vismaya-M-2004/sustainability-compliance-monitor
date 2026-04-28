from flask import Flask

# IMPORT BLUEPRINTS
from routes.describe import describe_bp
from routes.recommend import recommend_bp
from routes.report_routes import report_bp

# CREATE APP FIRST
app = Flask(__name__)

# REGISTER BLUEPRINTS AFTER app is created
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(report_bp)

# OPTIONAL: health check
@app.route('/health')
def health():
    return {"status": "ok"}

# RUN APP
if __name__ == "__main__":
    app.run(debug=True, port=5000)