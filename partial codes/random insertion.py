import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, relationship
from faker import Faker
import random
from sqlalchemy.ext.automap import automap_base

engine = db.create_engine('sqlite:///Smart_Parking.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def generate_random_coordinates():
    latitude = round(random.uniform(8,38), 6)
    longitude = round(random.uniform(68,98), 6)
    return latitude, longitude

def generate_random_vehicle_number():
    state_code = fake.random_element(elements=('TS', 'AP', 'KA', 'MH', 'TN'))
    district_code = fake.random_int(min=10, max=99)
    series = fake.random_element(elements=('EV', 'EZ', 'XY', 'AB', 'CD'))
    number = fake.random_int(min=1000, max=9999)
    return f"{state_code} {district_code} {series} {number}"

def insert_random_customer_details(num_entries):
    for _ in range(num_entries):
        name = fake.name()
        mobile_number = fake.phone_number()
        
        customer_data = {
            'name': name,
            'mobile_number': mobile_number
        }
        
        new_customer = Base.classes.customer_details(**customer_data)
        session.add(new_customer)
    session.commit()

def insert_random_vehicle_details(num_entries):
    for _ in range(num_entries):
        vehicle_number = generate_random_vehicle_number()
        customer_id = random.randint(1, num_entries)
        
        vehicle_data = {
            'vehicle_number': vehicle_number,
            'customer_id': customer_id
        }
        
        new_vehicle = Base.classes.vehicle_details(**vehicle_data)
        session.add(new_vehicle)
    session.commit()

def insert_random_provider_details(num_entries):
    for _ in range(num_entries):
        provider_id = fake.unique.random_int(min=1, max=num_entries)
        name = fake.company()
        address = fake.address()
        spot_id = fake.unique.random_int(min=1, max=num_entries)
        
        provider_data = {
            'provider_id': provider_id,
            'name': name,
            'address': address,
            'spot_id': spot_id
        }
        
        new_provider = Base.classes.provider_details(**provider_data)
        session.add(new_provider)
    session.commit()

def insert_random_spot_details(num_entries, max_slot_id):
    for _ in range(num_entries):
        slot_id = random.randint(1, max_slot_id)
        latitude, longitude = generate_random_coordinates()
        price = round(random.uniform(1, 20), 2)
        monitoring = random.choice([True, False])
        
        spot_data = {
            'slot_id': slot_id,
            'latitude': latitude,
            'longitude': longitude,
            'price': price,
            'monitoring': monitoring
        }
        
        new_spot = Base.classes.spot_details(**spot_data)
        session.add(new_spot)
    session.commit()

def insert_random_availability(num_entries):
    for _ in range(num_entries):
        spot_id = random.randint(1, num_entries)
        
        existing_slot_ids = session.query(availability.c.slot_id).distinct().all()
        slot_id = random.choice(existing_slot_ids)[0]
        
        available = random.choice([True, False])
        
        availability_data = {
            'spot_id': spot_id,
            'slot_id': slot_id,
            'available': available
        }
        
        new_availability = Base.classes.availability(**availability_data)
        session.add(new_availability)
    session.commit()

def insert_random_needs(num_entries):
    for _ in range(num_entries):
        vehicle_number = generate_random_vehicle_number()
        latitude, longitude = generate_random_coordinates()
        
        needs_data = {
            'vehicle_number': vehicle_number,
            'latitude': latitude,
            'longitude': longitude
        }
        
        new_needs = Base.classes.needs(**needs_data)
        session.add(new_needs)
    session.commit()

def insert_random_schedule(num_entries):
    for _ in range(num_entries):
        vehicle_number = generate_random_vehicle_number()
        start_time = fake.date_time_between(start_date='-1y', end_date='now')
        end_time = fake.date_time_between(start_date=start_time, end_date='now')
        surge = round(random.uniform(1, 2), 2)
        amount = round(random.uniform(10, 50), 2)
        
        schedule_data = {
            'vehicle_number': vehicle_number,
            'start_time': start_time,
            'end_time': end_time,
            'surge': surge,
            'amount': amount
        }
        
        new_schedule = Base.classes.schedule(**schedule_data)
        session.add(new_schedule)
    session.commit()

def insert_random_extensions(num_entries):
    for _ in range(num_entries):
        vehicle_number = generate_random_vehicle_number()
        time = fake.date_time_between(start_date='now', end_date='+1y')
        
        extensions_data = {
            'vehicle_number': vehicle_number,
            'time': time
        }
        
        new_extensions = Base.classes.extensions(**extensions_data)
        session.add(new_extensions)
    session.commit()

num_entries_to_generate = 10

Base = automap_base()
Base.prepare(engine, reflect=True)

insert_random_customer_details(num_entries_to_generate)
insert_random_vehicle_details(num_entries_to_generate)
insert_random_provider_details(num_entries_to_generate)
insert_random_spot_details(num_entries_to_generate, num_entries_to_generate)
insert_random_availability(num_entries_to_generate)
insert_random_needs(num_entries_to_generate)
insert_random_schedule(num_entries_to_generate)
insert_random_extensions(num_entries_to_generate)

session.close()

print(f"Inserted {num_entries_to_generate} random entries into all tables.")
