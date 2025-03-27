from __init__ import CURSOR, CONN

# 
class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Department instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """Drop the table that persists Department instances"""
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    # The save() method takes the attributes that characterize the Python object and saves them in a new row in the database "departments" table.
    def save(self):
        """Insert a new row with the same name and location values of the current Department instance. Update object id attribute using the primary key value of new row."""
        sql = """
            INSERT INTO departments (name, location)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid

    # The create() method creates a new object that is an instance of cls and save its attributes as a new table row.
    @classmethod
    def create(cls, name, location):
        """Initialize a new Department instance and save the object to the database"""
        department = cls(name, location)
        department.save()
        return department
    
    def update(self):
        """Update the table row corresponding to the current Department instance."""
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Department instance"""
        sql = """
            DELETE FROM departments
            WHERE id = ?
        """
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        
