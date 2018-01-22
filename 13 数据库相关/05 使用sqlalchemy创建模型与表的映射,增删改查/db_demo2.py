from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
import config


app = Flask(__name__)

# 创建对象的基类:
Base = declarative_base()

global engine


# 建立数据库表
def create_all_tables(DB_type):
    global engine
    if DB_type.upper() == "MYSQL":
        DB_URI = config.SQLALCHEMY_DATABASE_URI
        engine = create_engine(DB_URI, echo=True)
        # 寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
        Base.metadata.create_all(engine)


# 返回数据库会话
def loadSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


# # 正常的SQL语句。
# article表：
# create table article(
#     id int primary key autoincrement,
#     title varchar(100) not null,
#     content text not null,
# )
# article = Table('article', metadata,
#                     orm.Column('id', orm.Integer, primary_key=True, autoincrement=True),
#                     orm.Column('title', orm.String(20), nullable=False),
#                     orm.Column('content', orm.String(40), nullable=False),
#                     )
class article(Base):
    __tablename__ = "article"
    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    gender = Column(String(1), nullable=True, default=None)

    def __init__(self, title, content, gender=None):
        self.title = title
        self.content = content
        self.gender = gender


@app.route('/')
def hello_world():
    # 查询
    # 查第一行
    create_all_tables("mysql")
    session = loadSession()

    first = session.query(article.id, article.title, article.content).first()
    # 查所有行
    all = session.query(article.id, article.title, article.content).all()
    # 根据id倒序并取前两行
    limit = session.query(article).order_by(article.id.desc()).limit(2)
    print(first)
    print(all)
    print(limit)
    return render_template('index.html')


if __name__ == '__main__':
    # # 建表
    # create_all_tables("mysql")
    #
    # # 获取数据库会话
    # session = loadSession()
    #
    # # 增加
    # u1 = article(title="Rose", content="aaaa", gender="F")
    # u2 = article(title="Joe", content="bbbb", gender="M")
    # u3 = article(title="jack", content="bbbb", gender="M")
    # u4 = article(title="Billy", content="cccc")
    # session.add(u1)
    # session.add(u2)
    # session.add(u3)
    # session.add(u4)
    # session.commit()
    #
    # # 删除
    # session.query(article).filter(article.id > 2, article.gender == None).delete()
    # session.commit()
    #
    # # 修改
    # session.query(article).filter(article.title == "jack").update({article.content: "xxxx"})
    # session.commit()
    app.run(debug=True)
