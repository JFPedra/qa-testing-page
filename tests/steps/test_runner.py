from pytest_bdd import scenarios
from tests.steps.test_company_steps import *
from tests.steps.test_top_bar_steps_steps import  *
from tests.steps.test_property_steps import *

scenarios('./Company_Management.feature')
scenarios('./Property_Management.feature')