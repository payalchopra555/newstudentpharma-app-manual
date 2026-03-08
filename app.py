from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
   return "I am Taking classes from Maninder sir for Devops Cloud Computing is running with the help of Webhook🚀"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5005)
