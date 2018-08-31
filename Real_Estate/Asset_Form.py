from Configs.app_config import app, db
from flask import render_template, request, flash
from Classes.Asset_Class import AssetsData


All_Assets=AssetsData.query.all()

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')


@app.route('/Add', methods=['GET', 'POST'])
def add_assets():
    #return render_template('AddAsset.html')
    #Asset = AssetsData(2, 'Name Two ', ' Loc', ' dime',1, ' Status',789, 987, ' mode', 4, 'Some charge')
    #db.session.add(Asset)
    #db.session.commit()

    if request.method == 'POST':
        if not request.form['id'] or not request.form['name'] or not request.form['location']:
            flash('Please enter all the fields', 'error')
        else:
            assets = AssetsData(request.form['id'], request.form['name'],
                                request.form['location'], request.form['dimensions'], request.form['history_id'],
                                request.form['status'],request.form['Actual_Value'], request.form['Selling_price'],
                                request.form['Payment_mode'], request.form['Pay_duration'],
                                request.form['Broker_charges'])

            db.session.add(assets)
            db.session.commit()
            flash('Record was successfully added')
    return render_template('AddAsset.html')


@app.route('/All', methods=['GET', 'POST'])
def all_assets():
   # return AssetsData.query.all()
    return render_template('AllAsset.html', All_Assets=All_Assets)


if __name__ == '__main__':
   app.run(debug=True)