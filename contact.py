from flask import Flask, jsonify, request

contacts = [
    {
        'id': 1,
        'name': 'Tom',
        'number': '123413290',
        'done': False,
    },

    {
        'id': 2,
        'name': 'Cruise',
        'number': '2930485754',
        'done': False,
    }
]

app = Flask('__name__')

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": contacts
    })


@app.route('/add-data', methods=['POST'])
def add_contact():
    if not request.json:
        return jsonify({'status': 'error', 'message': 'Please provide the Data!'}, 400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['name'],
        'number': request.json.get('number', ''),
        'done': False
    }
    contacts.append(contact)

    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug = True)
