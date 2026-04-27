from flask import Flask, jsonify


def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')

    from app.config import Config
    app.config.from_object(Config)

    from app.routes.main_routes import main_bp
    from app.routes.api_routes import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    @app.errorhandler(404)
    def not_found(_):
        return jsonify({'success': False, 'error': 'Endpoint not found'}), 404

    @app.errorhandler(500)
    def internal_error(_):
        return jsonify({'success': False, 'error': 'Internal server error'}), 500

    return app
