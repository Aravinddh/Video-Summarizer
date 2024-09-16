from flask import Flask, render_template, request, jsonify
from core1 import process_youtube_video  

app = Flask(__name__)

# First homepage route
@app.route('/')
def index():
    return render_template('index.html')

# New homepage route
@app.route('/homepage2')
def homepage2():
    return render_template('homepage2.html')

@app.route('/process', methods=['POST'])
def process_video():
    youtube_url = request.form['youtube_url']
    results = process_youtube_video(youtube_url)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=False)