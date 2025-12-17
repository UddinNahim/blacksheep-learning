from piccolo.table import Table
from piccolo.columns import Serial, Varchar, Integer, Numeric

class Course(Table):
    id = Serial(primary_key=True)
    name = Varchar(length=255)
    description = Varchar(length=500)
    instructor = Varchar(length=255)
    price = Numeric(digits=(6, 2))   # Total of 6 digits, 2 after decimal
    rating = Numeric(digits=(3, 1))  # Total of 3 digits, 1 after decimal
