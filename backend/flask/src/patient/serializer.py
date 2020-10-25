from .models import Country
from tuberculosis.app import ma, db

class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Country
        sqla_session = db.session