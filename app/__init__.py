from flask import Flask, render_template
from app.model import Model

import pandas as pd

from config import load_config

app = Flask(__name__)
app.config.from_object(load_config())

model = Model()

from app import routes, forms