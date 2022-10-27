
import os
import sys
from datetime import datetime
from unittest.mock import MagicMock

import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from dibi import Database

# todo sparametryzowac
# CONST_DB_DILENAME = os.getenv('REACT_APP_CONST_DB_DILENAME')
CONST_DB_DILENAME = "backend/database.db"


@pytest.fixture(autouse=True)
def fixture():
    print("a")


def test_mock():
    thing = Database(CONST_DB_DILENAME)
    thing.method = MagicMock(return_value=3)
    thing.method(3, 4, 5, key='value')
    thing.method.assert_called_with(3, 4, 5, key='value')


def test_delete_all():
    db = Database(CONST_DB_DILENAME)
    db.delete_all()
    regs = db.get_registrations()
    assert len(regs) == 0

def test_should_get_one_element_bigger_dict_after_correct_insertion():
    db = Database(CONST_DB_DILENAME)
    before = db.get_registrations()
    date=datetime.now()
    new_reg ={'date_1':date,'date_2':date, 'who':'xd','what':'xdddd'}
    db.insert_registration(new_reg)
    after = db.get_registrations()
    assert len(before)+1==len(after)

def test_should_get_correct_record_for_correct_reading_parameter():
    db = Database(CONST_DB_DILENAME)
    currentRegistration = db.get_registration_by_id(1)
    assert currentRegistration['who'] == 'xd'
    assert currentRegistration['what'] == 'xdddd'

def test_should_get_one_element_smaller_dict_after_correct_deletion():
    db = Database(CONST_DB_DILENAME)
    before = db.get_registrations()
    db.delete_registration(1)
    after = db.get_registrations()
    assert len(before)-1==len(after)
