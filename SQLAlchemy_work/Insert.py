from Create_db_and_table import Family
from Create_db_and_table import db

insert1 = Family(1, 'rao', 53)
insert2 = Family(1, 'rao', 53)

db.session.add(insert1)
db.session.add(insert2)
db.session.commit()

print('end of inserting rows in table')

all_family = Family.query.all()

print(all_family)
