from app import app
from app import model

from flask import render_template
from app.forms import DataForm

from app.utils import DataRowModel, to_row

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = DataForm()

    if form.validate_on_submit():
        row = to_row(form.data)
        data_row = DataRowModel(row).prep()
        price = int(model.predict(data_row)[0])
        return render_template('output.html', price=price)
    return render_template('index.html', form=form)