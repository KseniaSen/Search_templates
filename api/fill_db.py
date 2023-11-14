from tinydb import TinyDB

db = TinyDB('forms_db.json')
templates_table = db.table('form_templates')


templates_table.insert({
    'name': 'OrderForm',
    'fields': {
        'user_name': 'text',
        'user_email': 'email',
        'user_phone': 'phone',
        'createdAt': 'date',
        'address': 'text',
    }
})

templates_table.insert({
    'name': 'UserForm',
    'fields': {
        'fullName': 'text',
        'phone': 'phone',
        'email': 'email',
        'address': 'text',
    }
})
