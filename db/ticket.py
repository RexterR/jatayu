from db.db import connect
from db.employee import Employee
from bson.objectid import ObjectId
employee_instance = Employee()


class Ticket():
    def __init__(self):
        self._ticket = connect('ticket')

    def create_ticket(self, job):
        try:

            employees = employee_instance.getAll()
            target = {}
            for employee in employees:
                if not employee.get('tickets'):
                    target = str(employee['_id'])
                elif len(employee.get('tickets')) <= 5:
                    target = str(employee['_id'])
                else:
                    target = {}
            res = self._ticket.insert_one({'job': job, 'assigned_employee': target})
            print(res)
            return True
        except Exception as e:
            print(e)
            return False
    def getTicketbyEmploee(self,id):
        try:
            ticket = self._ticket.find_one({'assigned_employee':id},{'_id':0})
    
            if not ticket:
                raise Exception("Ticket not found")
            return ticket
        except Exception as e:
            print(e)
            return False