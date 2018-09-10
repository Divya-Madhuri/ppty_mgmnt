from Configs.app_config import db


class AssetsData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column( db.String, primary_key=True)  # Get details from people table
    location = db.Column(db.String)
    dimensions = db.Column( db.String)
    history_data = db.Column('history_id', db.Integer)  # Get details from history table
    status = db.Column(db.String)  # Store this while  of asset
    Actual_Value = db.Column(db.Integer)
    Selling_price = db.Column(db.Integer)
    Payment_mode = db.Column(db.String)
    Pay_duration = db.Column( db.Integer)
    Mideater_comission = db.Column(db.String)

    def __init__(self, asset_id, cust_name, location, dimensions, hist_id, status, tp, sp):
        self.id = asset_id
        self.name = cust_name
        self.location = location
        self.dimensions = dimensions
        self.history_data = hist_id
        self.Actual_Value = tp

