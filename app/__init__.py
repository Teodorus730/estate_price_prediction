from flask import Flask, render_template
from app.model import Model

import pandas as pd

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

model = Model()

from app import routes, forms