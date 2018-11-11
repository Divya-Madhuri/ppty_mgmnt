from Create_db_and_table import db
from Create_db_and_table import Family

delete_row = Family.query.filter_by(id=6).first()
db.session.delete(delete_row)
db.session.commit()