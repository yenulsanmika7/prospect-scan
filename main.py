from bose.launch_tasks import launch_tasks

from src.config import queries
from src import tasks_to_be_run
import csv
from flask import Flask, send_from_directory, request
from flask_cors import CORS
import pydash

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST"], "headers": "Content-Type"}})

@app.route('/api/generate', methods=['GET'])
def generate():

    keyword = request.args.get('keyword')
    maxResults = request.args.get('maxResults')
    
    queries[0]['keyword'] = keyword
    queries[0]['max_results'] = maxResults
    launch_tasks(*tasks_to_be_run)
    
    filename = pydash.kebab_case(keyword) + '.csv' 
    directory = 'output'  
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == "__main__":

    app.run(debug=True)
