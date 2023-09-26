import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base


engine = db.create_engine('sqlite:///Smart_Parking.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


Base = automap_base()
Base.prepare(engine, reflect=True)

def interact_with_table(table_name):

    TableClass = getattr(Base.classes, table_name)


    print(f"Attributes of table '{table_name}':")
    for column in TableClass.__table__.columns:
        print(f"{column.name}: {column.type}")


    values = {}
    for column in TableClass.__table__.columns:
        user_input = input(f"Enter value for {column.name}: ")
        values[column.name] = user_input


    try:
        new_row = TableClass(**values)
        session.add(new_row)
        session.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        session.close()


table_name = input("Enter the name of the table you want to interact with: ")
interact_with_table(table_name)
