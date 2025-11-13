from flask import Flask
 
application = Flask(__name__)
 
@application.route("/")
def home():
    return "Hello from Elastic Beanstalk! Your Python app is working 🚀"
 
if __name__ == "__main__":
    application.run()
