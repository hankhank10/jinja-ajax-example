from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    item_list = [
        {'unique_id': 1, 'name': 'First Item', 'price': '$1.99'},
        {'unique_id': 2, 'name': 'Second Item', 'price': '$2.99'},
        {'unique_id': 3, 'name': 'Third Item', 'price': '$3.99'}
    ]
    
    return render_template('example.html', item_list = item_list)


@app.route('/your_endpoint/<unique_id>')
def ajax_endpoint(unique_id):

    print ("Received item id " + str(unique_id) + " via AJAX.")
    return jsonify({
        'status': 'ok'}
    )


app.run(host='0.0.0.0', port=8899, debug=True)