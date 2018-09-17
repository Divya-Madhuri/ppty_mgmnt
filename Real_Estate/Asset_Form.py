from Configs.app_config import app, db
from flask import render_template, request, flash, redirect
from Classes.Asset_Class import AssetsData
from Classes.People_Class import People
from Classes.Roles import Roles


All_Assets=AssetsData.query.all()
customer_name= AssetsData.query.filter_by(name = 'test').all()


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')


@app.route('/All', methods=['GET', 'POST'])
def all_assets():
    return render_template('AllAsset.html', All_Assets=All_Assets)


@app.route('/Back', methods=['GET', 'POST'])
def back():
    return render_template('welcome.html')


@app.route('/BackAsset', methods=['GET', 'POST'])
def backasset():
    return render_template('AllAsset.html', All_Assets=All_Assets)


@app.route('/Add', methods=['GET', 'POST'])
def add_assets():

    if request.form:
        print(request.form)

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


@app.route('/add_people', methods=['GET', 'POST'])
def add_people():

    if request.method == 'POST':
        if not request.form['id'] or not request.form['name']:
            flash('Please enter all the fields', 'error')
        else:
            people = People(request.form['id'], request.form['name'], request.form['role'],
                                request.form['gender'], request.form['age'], request.form['mobile_num'],
                                request.form['alternate_num'], request.form['address'])

            db.session.add(people)
            db.session.commit()
            flash('Record was successfully added')
    return render_template('AddPeople.html')


@app.route('/update/<update_id>', methods=['GET', 'POST'])
def update(update_id):

    update_asset = AssetsData.query.filter_by(id=update_id).first()

    if request.method == 'GET' :
        return render_template('UpdateAsset.html', update_id=update_id, update_asset=update_asset)

    elif request.method == 'POST':
        if not request.form['id'] or not request.form['name']:
            flash('Please enter all the fields', 'error')
        else:
            update_assets = AssetsData(request.form['id'], request.form['name'],
                                request.form['location'], request.form['dimensions'], request.form['history_id'],
                                request.form['status'],request.form['Actual_Value'], request.form['Selling_price'],
                                request.form['Payment_mode'], request.form['Pay_duration'],
                                request.form['Broker_charges'])
            update_asset.name = update_assets.name
            update_asset.location = update_assets.location
            update_asset.dimensions = update_assets.dimensions
            update_asset.status = update_assets.status
            update_asset.Actual_Value = update_assets.Actual_Value
            update_asset.Selling_price = update_assets.Selling_price
            update_asset.Payment_mode = update_assets.Payment_mode
            update_asset.Pay_duration = update_assets.Pay_duration
            update_asset.Broker_charges = update_assets.Broker_charges

            db.session.commit()
            flash('Record was successfully updated')

    return redirect("All")


if __name__ == '__main__':
   app.run(debug=True)