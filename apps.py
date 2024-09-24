from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


ads = {}
ad_id_counter = 1


@app.route('/ads', methods=['POST'])
def create_ad():
    global ad_id_counter
    data = request.get_json()

    if not data.get('title') or not data.get('description') or not data.get('owner'):
        return jsonify({'error': 'Invalid data'}), 400

    ad = {
        'id': ad_id_counter,
        'title': data['title'],
        'description': data['description'],
        'date_created': datetime.now().isoformat(),
        'owner': data['owner']
    }

    ads[ad_id_counter] = ad
    ad_id_counter += 1

    return jsonify(ad), 201



@app.route('/ads/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    ad = ads.get(ad_id)

    if not ad:
        return jsonify({'error': 'Ad not found'}), 404

    return jsonify(ad), 200



@app.route('/ads/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    ad = ads.pop(ad_id, None)

    if not ad:
        return jsonify({'error': 'Ad not found'}), 404

    return jsonify({'message': 'Ad deleted'}), 200


if __name__ == '__main__':
    app.run(debug=True)
