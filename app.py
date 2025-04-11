from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import numpy as np



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ =='__main__':
    app.run(port=8000,debug=True)