from Create_db_table import Users2
from app_config import app
from Create_db_table import db


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    insert_user1 = Users2('Srikanth', 33, 'H-No : 9-1-150 and etc')
    insert_user2 = Users2('Samanvisri', 1, 'H-No : 9-1-150 and etc')
    insert_user3 = Users2('Some random', 26, 'H-No : 9-1-150 and etc')

    db.session.add(insert_user1)
    db.session.add(insert_user2)
    db.session.add(insert_user3)
    db.session.commit()
    return 'data entered into table'


@app.route('/delete')
def delete():
    del_user1 = Users2.query.filter_by(id=5).first()
    db.session.delete(del_user1)
    db.session.commit()
    return 'data deleted from table'


if __name__ == '__main__':
    app.run(debug=True)

