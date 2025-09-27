from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Integer)
    image_url = Column(String)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    rating = Column(Float)
    is_active = Column(Boolean, default=True)
    category = relationship('Category', back_populates='products', uselist=False)


## Imperative way:

# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
#
# engine = create_engine('sqlite:///mydatabase.db')
# metadata = MetaData()
#
# authors_table = Table('authors', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String)
# )
#
# books_table = Table('books', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('title', String),
# )
