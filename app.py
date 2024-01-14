from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, url_for, flash, redirect
import json
import secrets
import string
import pymongo

app = Flask(__name__)

# Check if a field is empty
def is_field_empty(field_value):
    return field_value is None or field_value == ''

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        print("Entro")
        owner = request.form['name']
        print(owner)
        email = request.form['email']
        print(email)
        server = request.form['server']
        print(server)
        tags = request.form['tags']
        print(tags)
        intent1 = request.form['intent1']
        print(intent1)

        param1_name = request.form['param1_name']
        print(param1_name)
        param1_des = request.form['param1_desc']
        print(param1_des)
        param1_req = request.form['param1_req']
        print(param1_req)
        param1_type = request.form['param1_type']
        print(param1_type)
        param1_q = request.form['param1_q']
        print(param1_q)

        param2_name = request.form['param2_name']
        if (not is_field_empty(param2_name)):
            print(param2_name)
            param2_des = request.form['param2_desc']
            print(param2_des)
            param2_req = request.form['param2_req']
            print(param2_req)
            param2_type = request.form['param2_type']
            print(param2_type)
            param2_q = request.form['param2_q']
            print(param2_q)

        param3_name = request.form['param3_name']
        if (not is_field_empty(param3_name)):
            print(param3_name)
            param3_des = request.form['param3_desc']
            print(param3_des)
            param3_req = request.form['param3_req']
            print(param3_req)
            param3_type = request.form['param3_type']
            print(param3_type)
            param3_q = request.form['param3_q']
            print(param3_q)

        param4_name = request.form['param4_name']
        if (not is_field_empty(param4_name)):
            print(param4_name)
            param4_des = request.form['param4_desc']
            print(param4_des)
            param4_req = request.form['param4_req']
            print(param4_req)
            param4_type = request.form['param4_type']
            print(param4_type)
            param4_q = request.form['param4_q']
            print(param4_q)

        param5_name = request.form['param5_name']
        if (not is_field_empty(param5_name)):
            print(param5_name)
            param5_des = request.form['param5_desc']
            print(param5_des)
            param5_req = request.form['param5_req']
            print(param5_req)
            param5_type = request.form['param5_type']
            print(param5_type)
            param5_q = request.form['param5_q']
            print(param5_q)

        """
        intent2 = request.form['intent2']

        if intent2:
            param1_i2_name = request.form['param1_i2_name']
            param1_i2_des = request.form['param1_i2_desc']
            param1_i2_req = request.form['param1_i2_req']
            param1_i2_type = request.form['param1_i2_type']
            param1_i2_q = request.form['param1_i2_q']

            param2_i2_name = request.form['param2_i2_name']
            param2_i2_des = request.form['param2_i2_desc']
            param2_i2_req = request.form['param2_i2_req']
            param2_i2_type = request.form['param2_i2_type']
            param2_i2_q = request.form['param2_i2_q']

            param3_i2_name = request.form['param3_i2_name']
            param3_i2_des = request.form['param3_i2_desc']
            param3_i2_req = request.form['param3_i2_req']
            param3_i2_type = request.form['param3_i2_type']
            param3_i2_q = request.form['param3_i2_q']

            param4_i2_name = request.form['param4_i2_name']
            param4_i2_des = request.form['param4_i2_desc']
            param4_i2_req = request.form['param4_i2_req']
            param4_i2_type = request.form['param4_i2_type']
            param4_i2_q = request.form['param4_i2_q']

            param5_i2_name = request.form['param5_i2_name']
            param5_i2_des = request.form['param5_i2_desc']
            param5_i2_req = request.form['param5_i2_req']
            param5_i2_type = request.form['param5_i2_type']
            param5_i2_q = request.form['param5_i2_q']

        intent3 = request.form['intent3']

        if intent3:
            param1_i3_name = request.form['param1_i3_name']
            param1_i3_des = request.form['param1_i3_desc']
            param1_i3_req = request.form['param1_i3_req']
            param1_i3_type = request.form['param1_i3_type']
            param1_i3_q = request.form['param1_i3_q']

            param2_i3_name = request.form['param2_i3_name']
            param2_i3_des = request.form['param2_i3_desc']
            param2_i3_req = request.form['param2_i3_req']
            param2_i3_type = request.form['param2_i3_type']
            param2_i3_q = request.form['param2_i3_q']

            param3_i3_name = request.form['param3_i3_name']
            param3_i3_des = request.form['param3_i3_desc']
            param3_i3_req = request.form['param3_i3_req']
            param3_i3_type = request.form['param3_i3_type']
            param3_i3_q = request.form['param3_i3_q']

            param4_i3_name = request.form['param4_i3_name']
            param4_i3_des = request.form['param4_i3_desc']
            param4_i3_req = request.form['param4_i3_req']
            param4_i3_type = request.form['param4_i3_type']
            param4_i3_q = request.form['param4_i3_q']

            param5_i3_name = request.form['param5_i3_name']
            param5_i3_des = request.form['param5_i3_desc']
            param5_i3_req = request.form['param5_i3_req']
            param5_i3_type = request.form['param5_i3_type']
            param5_i3_q = request.form['param5_i3_q']
        """

        print("Creo el JSON")
        #CREAR EL JSON
        service = {
            "openapi": "3.0.0",
            "info": {
                "title": "Restaurant Booking API",
                "description": "Restaurant information for IA slot filling",
                "termsOfService": "http://miapp.com/terms.php",
                "contact": {
                    "name": owner,
                    "url": "https://directorio.ugr.es/static/PersonalUGR/*/show/8cbe900fb866f9ac9f399915a132dad3",
                    "email": email
                },
                "license": {
                    "name": "Apache 2.0",
                    "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
                },
                "version": "1.0"
            },
            "servers": [
                {
                    "url": server,
                    "description": "Server for the app"
                }
            ],
            "tags": [
                {
                    "name": tags
                }
            ],
            "paths": {
                "/"+intent1: {
                    "get": {
                        "description": "Make the restaurant reservation",
                        "operationId": intent1,
                        "parameters": [
                            {
                                "name": param1_name,
                                "in": "query",
                                "description": param1_des,
                                "required": param1_req,
                                "style": "form",
                                "schema": {
                                    "type": param1_type
                                },
                                "x-custom-question": param1_q
                            }
                        ],
                        "responses": {
                            "200": {
                                "description": "Successful request",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "type": "string",
                                            "example": "{\"message\":\"The phone number is: 675151146\"}"
                                        }
                                    }
                                }
                            },
                            "404": {
                                "description": "url not found",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "type": "string",
                                            "example": "{\"message\":\"Error: The url or request is not found\"}"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "components": {}
        }

        if not is_field_empty(param2_name):
            service["paths"]["/" + intent1]["get"]["parameters"].append({
                "name": param2_name,
                "in": "query",
                "description": param2_des,
                "required": param2_req,
                "style": "form",
                "schema": {
                    "type": param2_type,
                },
                "x-custom-question": param2_q
            })

        if not is_field_empty(param3_name):
            service["paths"]["/" + intent1]["get"]["parameters"].append({
                "name": param3_name,
                "in": "query",
                "description": param3_des,
                "required": param3_req,
                "style": "form",
                "schema": {
                    "type": param3_type,
                },
                "x-custom-question": param3_q
            })

        if not is_field_empty(param4_name):
            service["paths"]["/" + intent1]["get"]["parameters"].append({
                "name": param4_name,
                "in": "query",
                "description": param4_des,
                "required": param4_req,
                "style": "form",
                "schema": {
                    "type": param4_type,
                },
                "x-custom-question": param4_q
            })

        if not is_field_empty(param5_name):
            service["paths"]["/" + intent1]["get"]["parameters"].append({
                "name": param5_name,
                "in": "query",
                "description": param5_des,
                "required": param5_req,
                "style": "form",
                "schema": {
                    "type": param5_type,
                },
                "x-custom-question": param5_q
            })

        # MongoDB connection details
        mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

        # Choose or create a database and collection
        database_name = "services"
        collection_name = "restaurant"

        # Access or create the database and collection
        db = mongo_client[database_name]
        collection = db[collection_name]

        # Insert the JSON data into the collection
        collection.insert_one(service)

        return redirect(url_for('index'))

    return render_template('create.html')


if __name__ == '__main__':
    """
    from flask_cors import CORS
    import ssl

    context = ssl.SSLContext()
    context.load_cert_chain("/home/mariajesus/certificados/conversational_ugr_es.pem",
                            "/home/mariajesus/certificados/conversational_ugr_es.key")
    CORS(app)
    app.run(host='0.0.0.0', port=5050, ssl_context=context, debug=False)
    """

    app.run()
