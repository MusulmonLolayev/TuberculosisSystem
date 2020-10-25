from common.models import Base
from tuberculosis.app import db

class Country(Base):
    __tablename__ = "Country"

    def __str__(self):
        return self.name