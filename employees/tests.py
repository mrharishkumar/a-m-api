from django.test import TestCase, Client
from .models import *

# Create your tests here.


class EmployeeTest(TestCase):

    # def setUp(self):
    #    Employee.objects.create(branch_id="USA")

    def test_employee(self):
        user = ['rahul.katoch@impressico.com']

        obj = User.objects.create(
            username=user
        )
        self.assertEquals(user, obj.username)

    def test_get_all_employee(self):
        c = Client()
        response = c.get('')
        print(response)

        self.assertEquals(response, Employee.objects.all())

    def test_get_employee_detail(self):
        pass
