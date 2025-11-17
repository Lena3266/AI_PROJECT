from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/allocate', methods=['POST'])
def allocate():
    data = request.json or {}
    students = data.get('students', [])
    rooms = data.get('rooms', [])
    allocations = []
    for i, s in enumerate(students):
        room = rooms[i % len(rooms)] if rooms else None
        allocations.append({ 'studentId': s.get('id'), 'roomId': room.get('id') if room else None, 'score': 0.5 })
    return jsonify({ 'allocations': allocations })

@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
