from flask import Blueprint, request, jsonify

user_input_bp = Blueprint('user_input', __name__)

@user_input_bp.route('/submit', methods=['POST'])
def submit_data():
    if request.method == 'POST':
        try:
            data = request.get_json()
            # Process the data (for now, we'll just print it)
            print(data)
            # Simulate storing data
            response = {
                'status': 'success',
                'message': 'Data received successfully',
                'received_data': data
            }
            return jsonify(response), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 400
    else:
        return jsonify({'status': 'error', 'message': 'Invalid request method'}), 405
