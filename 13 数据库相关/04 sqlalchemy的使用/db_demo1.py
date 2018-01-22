from flask import Flask
import sqlalchemy as orm

import config

app = Flask(__name__)

db = orm.create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
metadata = orm.MetaData(db)
# user = orm.Table('user', metadata,
#                  orm.Column('id', orm.Integer, primary_key=True),
#                  orm.Column('name', orm.String(20)),
#                  orm.Column('fullname', orm.String(40)),
#                  )
# address_table = orm.Table('address', metadata,
#                           orm.Column('id', orm.Integer, primary_key=True),
#                           orm.Column('user_id', None, orm.ForeignKey('user.id')),
#                           orm.Column('email', orm.String(128), nullable=False)
#                           )
#
metadata.create_all()



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
