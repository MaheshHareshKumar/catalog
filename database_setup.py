from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
import datetime
Base = declarative_base()



class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    item = relationship("Item", order_by="Item.id", backref="Category")

    @property
    def serialize(self):
        
        return {
            'name': self.name,
            'id': self.id,
            
       }



class Item(Base):
    __tablename__ = 'item'

    def _get_date():
        return datetime.datetime.now()
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    date_time = Column(Date, default=_get_date)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
        }


engine = create_engine('sqlite:///categorywithusers.db')


Base.metadata.create_all(engine)