from Create_db_and_table import db
from Create_db_and_table import Family

update_row = Family.query.filter_by(id=2).first()

update_row.name = 'Naga Jyothi'
update_row.age = 52
db.session.commit()

print('data updated successfully')

