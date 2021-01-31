from db.db import connect
from bson.objectid import ObjectId


class Employee():
    def __init__(self):
        self._employee = connect('employee')
    def getAll(self):
        try:
            all = []
            for employee in self._employee.find():
                all.append(employee)
            return all
        except Exception as e:
            print(e)
            return []
            