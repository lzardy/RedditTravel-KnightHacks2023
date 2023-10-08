from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/receive_input', methods=['POST'])
def receive_input():
    # Receive user input from the client
    user_input = request.json  # Assuming the client sends data in JSON format

    # Send the user input to the external API
    external_api_url = 'https://external-api.com/process_data'
    response = requests.post(external_api_url, json=user_input)

    # Process the response from the external API
    if response.status_code == 200:
        result_data = response.json()
        # Return the result data to the client
        return jsonify(result_data)
    else:
        return jsonify({"error": "Failed to process data with the external API"})

if __name__ == '__main__':
    app.run(debug=True)
