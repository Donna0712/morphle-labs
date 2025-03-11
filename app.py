from flask import Flask, jsonify
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
   
    full_name = "Donna S Sebastian"
    
    # Get the system username
    username = os.getlogin()
    
    # Get the current server time in IST
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    
    # Get the top output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    # Prepare the response
    response = f"""
    <html>
        <head>
            <title>HTop Info</title>
        </head>
        <body>
            <h1>HTop Information</h1>
            <p><strong>Full Name:</strong> {Donna_S_Sebastian}</p>
            <p><strong>Username:</strong> {Donna}</p>
            <p><strong>Server Time (IST):</strong> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
            <h2>Top Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return response

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)
