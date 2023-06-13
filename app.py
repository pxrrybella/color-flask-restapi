import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# Find the path of our Flask app, so we can create de database there
basedir = os.path.abspath(os.path.dirname(__file__))
# Setting the SQLALCHEMY_DATABASE_URI to the database created previously
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'colors.db')

# Initializing database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Creating terminal commands for Flask
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')


@app.cli.command('db_seed')
def db_seed():
    light_coral = Color(color_name="Light Coral",
                        hex_code="#F08080")
    lemon_green = Color(color_name="Lemon Green",
                        hex_code="#AEFF16")
    light_cyan = Color(color_name="Light Cyan",
                       hex_code="#64FFEC")

    # Adding colors created before to the db
    db.session.add(light_coral)
    db.session.add(lemon_green)
    db.session.add(light_cyan)
    # Commiting changes
    db.session.commit()
    print('Database seeded!')


@app.route('/add_color', methods=['POST'])
def add_color():
    color_name = request.form['color_name']
    hex_code = request.form['hex_code']
    test = Color.query.filter_by(hex_code=hex_code).first()
    if test:
        return jsonify(message='That color already exists.'), 409
    else:
        new_color = Color(color_name=color_name, hex_code=hex_code)
        db.session.add(new_color)
        db.session.commit()
        return jsonify(message="Color added successfully."), 201


@app.route('/colors', methods=['GET'])
def colors():
    colors_list = Color.query.all()
    result = colors_schema.dump(colors_list)
    return jsonify(result)


@app.route('/update_color', methods=['PUT'])
def update_color():
    color_id = int(request.form['color_id'])
    color_name = request.form['color_name']
    hex_code = request.form['hex_code']
    color = Color.query.filter_by(color_id=color_id).first()
    if color:
        color.color_id = color_id
        color.color_name = color_name
        color.hex_code = hex_code
        db.session.commit()
        return jsonify(message="Color updated."), 202
    else:
        return jsonify(message="That color is not on the database."), 404


@app.route('/drop_color/<int:color_id>', methods=['DELETE'])
def drop_color(color_id: int):
    color = Color.query.filter_by(color_id=color_id).first()
    if color:
        db.session.delete(color)
        db.session.commit()
        return jsonify(message="Color deleted successfully.")
    else:
        return jsonify(message="That color is not on the database."), 404


class Color(db.Model):
    __tablename__ = 'colors'
    color_id = Column(Integer, primary_key=True)
    color_name = Column(String)
    hex_code = Column(String)


class ColorSchema(ma.Schema):
    class Meta:
        fields = ('color_id', 'color_name', 'hex_code')


color_schema = ColorSchema
colors_schema = ColorSchema(many=True)


if __name__ == '__main__':
    app.run()
