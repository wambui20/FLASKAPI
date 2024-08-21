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
class RuleSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(required=True, validate=validate.Length(min=1))
    content = fields.Str(required=True, validate=validate.Length(min=1))


# Define the models
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    Rule_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)



# Create the database tables if they do not exist
with app.app_context():
    db.create_all()


@app.route('/Rule/county/create', methods=['POST'])
def create_county_rule():
    schema = RuleSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_rule = Rule(title=data['title'], description=data['description'], content=data['content'], rule_type='county',
                  status='pending')
    db.session.add(new_rule)
    db.session.commit()

    logger.info(f"Created new county Rule with ID {new_rule.id}")
    return jsonify({'message': 'County Rule created successfully!'}), 201


@app.route('/Rule/county/update/<int:rule_id>', methods=['PUT'])
def update_county_rule(rule_id):
    schema = RuleSchema(partial=True)
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    rule = Rule.query.get(rule_id)
    if not rule:
        abort(404, description=f"Rule with ID {rule_id} not found")
    rule.title = data.get('title', rule.title)
    rule.description = data.get('description', Rule.description)
    rule.content = data.get('content', Rule.content)
    db.session.commit()

    logger.info(f"Updated county Rule with ID {rule_id}")
    return jsonify({'message': 'County Rule updated successfully!'}), 200


@app.route('/Rule/county/read', methods=['GET'])
def get_all_rules():
    rules = Rule.query.all()
    rule_list = []

    for rule in rules:
        rule_data = {
            'id': rule.id,
            'title': rule.title,
            'description': rule.description,
            'content': rule.content,
            'Rule_type': rule.rule_type,
            'status': rule.status
        }
        rule_list.append(rule_data)

    return jsonify(rule_list), 200

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
