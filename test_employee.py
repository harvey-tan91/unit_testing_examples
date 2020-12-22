from employee import Employee # we are employing the class

import unittest
from unittest.mock import patch 
# we can use patch as a decorator or as a context manager
# it allow us to mock an object during a text and the object is automatically restored after the test is run

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('================================')
        print('This is the setup class - this will be executed before the start')
        print('================================')
        print()

    @classmethod
    def tearDownClass(cls):
        print('================================')
        print('this is the end')
        print('================================')

##################### Setups for each Method/Function ########################
# the below will be executed for each round of execution of the method/function
    def setUp(self): # the setUp is a standard Python class so take note of teh camel case
        # the setUp class allow us to store all the static variables for testing all the different scenarios
        # in order to access it from tests, WE WILL NEED TO STORE THEM INSTANCES's ATTRIBUTES
        print('setUp')
        self.emp_1 = Employee('Harvey', 'Tan', 60000)

    def tearDown(self): # the tearDown is a standard Python class so take note of teh camel case
        print('tearDown\n')
        pass

##################### Methods/Functions for Test Scripts ########################

    def test_email(self):
        print('test_email')

        self.assertEqual(self.emp_1.email, 'Harvey.Tan@gmail.com')
        self.emp_1.first = 'Jason'
        self.assertEqual(self.emp_1.email, 'Jason.Tan@gmail.com')

    def test_fullname(self):
        print('test_fullname')

        self.assertEqual(self.emp_1.fulllname, 'Harvey Tan')
        self.emp_1.first = 'Jason'
        self.assertEqual(self.emp_1.fulllname, 'Jason Tan')

    def test_apply_raise(self):
        print('test_apply_raise')
        
        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.pay , 63000)

# we only want our test to fail if our code failed and not because some website is down or if the link is incorrect
# we can do something called mocking
    def test_month_schedule(self):
        print('test_month_schedule')
        with patch('employee.requests.get') as mocked_get:
            
            ####################### testing a success response ##
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            # we are creating the mock results of request.get of the employee module

            schedule = self.emp_1.month_schedule('May')
            # we are creating the mock request object

            mocked_get.assert_called_with('http://company.com/Tan/May')
            # assert_called_with is a method of the mocked object
            # we are testing the request.get call

            self.assertEqual(schedule, 'Success')
            # we are testing if the mocked result is equal to the result of the mock request object
            
            ####################### testing a FAILED response ##
            mocked_get.return_value.ok = False

            schedule = self.emp_1.month_schedule('May')

            mocked_get.assert_called_with('http://company.com/Tan/May')

            self.assertEqual(schedule, 'Bad Response.')

if __name__ == '__main__':
    unittest.main()