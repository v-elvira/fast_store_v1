import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
print(sys.path)


from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)  # New

    products = relationship("Product", back_populates="category", uselist=True)


if __name__ == '__main__':
    from sqlalchemy.schema import CreateTable
    from app.models.products import Product

    print(CreateTable(Category.__table__))
    print(CreateTable(Product.__table__))
