import re

from flask import Flask, request
from tinydb import TinyDB
import phonenumbers
from datetime import datetime

app = Flask(__name__)

db = TinyDB('forms_db.json')


templates_table = db.table('form_templates')


@app.route('/get_form', methods=['POST'])
def get_form():
    form_data = request.form

    for template in templates_table.all():
        template_name = template.get('name')
        template_fields = set(template['fields'].keys())
        valid = True

        if template_fields.issubset(set(form_data.keys())):
            for field_name, field_type in template['fields'].items():
                value = form_data[field_name]
                if field_type == 'email' and not is_valid_email(value):
                    valid = False
                    break
                elif field_type == 'phone' and not is_valid_phone(value):
                    valid = False
                    break
                elif field_type == 'date' and not is_valid_date(value):
                    valid = False
                    break
            if valid:
                return {'template_name': template_name}

    missing_fields = {field: infer_field_type(form_data[field]) for field in form_data.keys()}
    return missing_fields


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def is_valid_phone(phone):
    try:
        parsed_phone = phonenumbers.parse(phone, None)
        return phonenumbers.is_valid_number(parsed_phone)
    except phonenumbers.NumberParseException:
        return False


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        pass
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def infer_field_type(field):

    if is_valid_date(field):
        return 'date'
    elif is_valid_phone(field):
        return 'phone'
    elif is_valid_email(field):
        return 'email'
    else:
        return 'text'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
