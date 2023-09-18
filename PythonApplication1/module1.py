import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
#make sure to cd and start the development server before running
        # python module1.py


conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key1 TEXT,
        key2 TEXT
               )

''')                              
conn.commit()
conn.close()

@app.route('/store_data', methods=['POST'])
def store_data():
    try:
        data = request.get_json()
        data_str = json.dumps(data)
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO data (key1, key2) VALUES (?, ?)', (data['key1'], data['key2']))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "data stored successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute('SELECT key1, key2 FROM data')
        result = cursor.fetchall()
        conn.close()
        data = [{"key1": row[0], "key2": row[1]} for row in result]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/purge_data', methods=['DELETE'])
def purge_data():
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM data')
        conn.commit()
        conn.close()
        return jsonify({"message": "All data purged successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        

if __name__ == '__main__':
    app.run(debug=True)
    
