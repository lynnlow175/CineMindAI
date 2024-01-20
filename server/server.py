from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Members API route
CORS(app, origins=["http://localhost:5173"], methods=["GET", "POST"], allow_headers=["Content-Type"])

@app.route('/members')
def members():  
  return {
    "members": [
      "Member 1",
      "Member 2",
      "Member 3",
    ]
  }

if __name__ == "__main__":
  app.run(debug=True)