from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>Skill Match</title></head>
    <body style="font-family: Arial; max-width: 600px; margin: 50px auto; text-align: center;">
        <h1>Skill Match</h1>
        <p>A Resume Matcher and Skill Recommender built with Python & Flask.</p>
        <p>Running inside a Docker container!</p>
        <ul style="text-align: left;">
            <li>Upload your resume</li>
            <li>Paste a job description</li>
            <li>Get matched skills instantly</li>
        </ul>
        <p><b>Status:</b> Running ✅</p>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'ok', 'app': 'Skill Match', 'version': '1.0'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)