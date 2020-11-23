from flask import Flask
import os

app =  Flask(__name__)

app.run(host="0.0.0.0", port=os.getenv('PORT', "5002"))
