from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError
from flask_marshmallow import Marshmallow
import config
import logging

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Define the schemas for validation
class LawSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(required=True, validate=validate.Length(min=1))
    content = fields.Str(required=True, validate=validate.Length(min=1))


# Define the models
class Law(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    law_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)



# Create the database tables if they do not exist
with app.app_context():
    db.create_all()


@app.route('/law/county/create', methods=['POST'])
def create_county_law():
    schema = LawSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_law = Law(title=data['title'], description=data['description'], content=data['content'], law_type='county',
                  status='pending')
    db.session.add(new_law)
    db.session.commit()

    logger.info(f"Created new county law with ID {new_law.id}")
    return jsonify({'message': 'County law created successfully!'}), 201


@app.route('/law/county/update/<int:law_id>', methods=['PUT'])
def update_county_law(law_id):
    schema = LawSchema(partial=True)
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    law = Law.query.get(law_id)
    if not law:
        abort(404, description=f"Law with ID {law_id} not found")
    law.title = data.get('title', law.title)
    law.description = data.get('description', law.description)
    law.content = data.get('content', law.content)
    db.session.commit()

    logger.info(f"Updated county law with ID {law_id}")
    return jsonify({'message': 'County law updated successfully!'}), 200


@app.route('/law/county/read', methods=['GET'])
def get_all_laws():
    laws = Law.query.all()
    law_list = []

    for law in laws:
        law_data = {
            'id': law.id,
            'title': law.title,
            'description': law.description,
            'content': law.content,
            'law_type': law.law_type,
            'status': law.status
        }
        law_list.append(law_data)

    return jsonify(law_list), 200

@app.errorhandler(404)
def not_found(error):
    logger.error(f"404 Not Found: {error}")
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {error}")
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True)
