import sqlalchemy as db
engine=db.create_engine('sqlite:///Smart_Parking.db',echo=True)
metaobject=db.MetaData()
customer_details=db.Table(
    'customer_details',
    metaobject,
    db.Column('customer_id',db.Integer,primary_key=True),
    db.Column('name',db.String),
    db.Column('mobile_number',db.Integer)
)
vehicle_details=db.Table(
    'vehicle_details',
    metaobject,
    db.Column('vehicle_number',db.String,primary_key=True),
    db.Column('customer_id',db.Integer)
    
)
provider_details=db.Table(
    'provider_details',
    metaobject,
    db.Column('id',db.Integer,primary_key=True),
    db.Column('provider_id',db.Integer),
    db.Column('name',db.String),
    db.Column('address',db.String),
    db.Column('spot_id',db.Integer)
)
spot_details=db.Table(
    'spot_details',
    metaobject,
    db.Column('spot_id',db.Integer,primary_key=True),
    db.Column('slot_id',db.Integer),
    db.Column('latitude',db.Float),
    db.Column('longitude',db.Float),
    db.Column('price',db.Float),
    db.Column('monitoring',db.Boolean)
)
availability=db.Table(
    'availability',
    metaobject,
    db.Column('spot_id',db.Integer,nullable=False),
    db.Column('slot_id',db.Integer,nullable=False),
    db.Column('available',db.Boolean)
)
needs=db.Table(
    'needs',
    metaobject,
    db.Column('vehicle_number',db.String),
    db.Column('latitude',db.Float),
    db.Column('longitude',db.Float)
    
)
schedule=db.Table(
    'schedule',
    metaobject,
    db.Column('vehicle_number',db.String),
    db.Column('id',db.Integer),
    db.Column('start_time',db.DateTime),
    db.Column('end_time',db.DateTime),
    db.Column('surge',db.Float),    
    db.Column('amount',db.Float)
)
extensions=db.Table(
    'extensions',
    metaobject,
    db.Column('vehicle_number',db.String),
    db.Column('time',db.DateTime)
)

metaobject.create_all(engine)