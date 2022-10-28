
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


def test_should_get_zero_registrations_after_total_deletion():
    #arrange
    db = Database(CONST_DB_DILENAME)
    
    #act
    db.delete_all()
    regs = db.get_registrations()
    
    #assert
    assert len(regs) == 0

def test_delete_all_for_10_reg():
    #arrange
    db = Database(CONST_DB_DILENAME)
    date=datetime.now()
    
    #act
    for i in range(10):
        new_reg ={'date_1':date,'date_2':date, 'who':'Jan Nowak','what':f'{i}'}
        db.insert_registration(new_reg)
    db.delete_all()
    regs = db.get_registrations()
    
    #assert
    assert len(regs) == 0

def test_should_get_one_element_bigger_dict_after_correct_insertion():
    #arrange
    db = Database(CONST_DB_DILENAME)
    before = db.get_registrations()
    date=datetime.now()
    
    #act
    new_reg ={'date_1':date,'date_2':date, 'who':'Marek Nowakowski','what':'Awaria 1'}
    db.insert_registration(new_reg)
    after = db.get_registrations()
    
    #assert
    assert len(before)+1==len(after)

def test_should_get_10_element_bigger_dict_after_10_correct_insertions():
    #arrange
    db = Database(CONST_DB_DILENAME)
    before = db.get_registrations()
    date=datetime.now()
    
    #act
    for i in range(10):
        new_reg ={'date_1':date,'date_2':date, 'who':'Jan Nowak','what':f'{i}'}
        db.insert_registration(new_reg)
    after = db.get_registrations()
    
    #assert
    assert len(before)+10==len(after)

def test_should_get_correct_record_for_correct_id_parameter():
    #arrange
    db = Database(CONST_DB_DILENAME)
    
    #act
    cur_reg = db.get_registration_by_id(1)

    #assert
    assert cur_reg['who'] == 'Marek Nowakowski'
    assert cur_reg['what'] == 'Awaria 1'

def test_should_get_KeyError_for_incorrect_id_parameter():
    #arrange
    db = Database(CONST_DB_DILENAME)
    
    #act
    with pytest.raises(KeyError):   
        cur_reg = db.get_registration_by_id(100)
    #assert
        assert cur_reg['who'] == 'Marek Nowakowski'
        assert cur_reg['what'] == 'Awaria 1'

def test_should_get_KeyError_for_incorrect_type_of_id_parameter():
    #arrange
    db = Database(CONST_DB_DILENAME)
    
    #act
    with pytest.raises(KeyError):   
        cur_reg = db.get_registration_by_id("Marek Nowakowski")
    #assert
        assert cur_reg['who'] == 'Marek Nowakowski'
        assert cur_reg['what'] == 'Awaria 1'

def test_should_get_correct_record_for_correct_name_parameter():
    #arrange
    db = Database(CONST_DB_DILENAME)

    #act
    cur_regs = db.get_registartions_by_name('Marek Nowakowski')
    cur_reg = cur_regs[0]

    #assert
    assert cur_reg['who'] == 'Marek Nowakowski'
    assert cur_reg['what'] == 'Awaria 1'

def test_should_get_IndexError_for_incorrect_type_name_parameter():
    #arrange
    db = Database(CONST_DB_DILENAME)

    #act
    with pytest.raises(IndexError):  
        cur_regs = db.get_registartions_by_name(1)
        cur_reg = cur_regs[0]

def test_should_get_empty_list_of_records_for_incorrect_name_parameter():
    #arrange
    db = Database(CONST_DB_DILENAME)

    #act
    cur_regs = db.get_registartions_by_name('Andrzej Wirowski')

    #assert
    assert len(cur_regs)== 0

def test_should_update_record_for_correct_update_parameters():
    #arrange﻿
    db = Database(CONST_DB_DILENAME)

    #act
    cur_reg = db.get_registration_by_id(1)
    assert cur_reg['who'] == 'Marek Nowakowski'
    assert cur_reg['what'] == 'Awaria 1'
    new_reg = {'date_1':cur_reg['date_1'],'date_2':cur_reg['date_2'], 'who':'Jan Kowalski','what':'Awaria 2'}
    
    db.update_registration(new_reg, 1)
    cur_reg = db.get_registration_by_id(1)
    
    #assert
    assert cur_reg['who'] == 'Jan Kowalski'
    assert cur_reg['what'] == 'Awaria 2'

def test_should_not_update_record_for_incorrect_id_type_update_parameter():
    #arrange﻿
    db = Database(CONST_DB_DILENAME)

    #act
    cur_reg = db.get_registration_by_id(1)
    assert cur_reg['who'] == 'Jan Kowalski'
    assert cur_reg['what'] == 'Awaria 2'
    new_reg = {'date_1':cur_reg['date_1'],'date_2':cur_reg['date_2'], 'who':'Marek Nowakowski','what':'Awaria 1'}
    
    db.update_registration(new_reg, 'Marek Nowakowski')
    cur_reg = db.get_registration_by_id(1)
    
    #assert
    assert cur_reg['who'] == 'Jan Kowalski'
    assert cur_reg['what'] == 'Awaria 2'

def test_update_record_for_not_existng_id_update_parameter():
    #arrange﻿
    db = Database(CONST_DB_DILENAME)
    regs = db.get_registrations()
    before = len(regs)

    #act
    cur_reg = db.get_registration_by_id(1)
    new_reg = {'date_1':cur_reg['date_1'],'date_2':cur_reg['date_2'], 'who':'Marek Nowakowski','what':'Awaria 3'}
    
    db.update_registration(new_reg, 100)
    regs = db.get_registrations()
    after = len(regs)
    
    #assert
    assert after == before

def test_should_get_one_element_smaller_dict_after_correct_deletion():
    #arrange
    db = Database(CONST_DB_DILENAME)
    before = db.get_registrations()
    
    #act
    db.delete_registration(1)
    after = db.get_registrations()
    
    #assert
    assert len(before)-1==len(after)

def test_should_get_10_element_smaller_dict_after_10_correct_deletions():
    #arrange
    db = Database(CONST_DB_DILENAME)
    date=datetime.now()
    for i in range(10):
        new_reg ={'date_1':date,'date_2':date, 'who':'Adam Nowak','what':f'{i}'}
        db.insert_registration(new_reg)
    before = db.get_registrations()
    
    #act
    for i in range(10):
        db.delete_registration(2+i)
    after = db.get_registrations()
    
    #assert
    assert len(before)-10==len(after)

def test_should_get_0_elements_after_trying_to_delete_from_empty_regdb():
    #arrange
    db = Database(CONST_DB_DILENAME)
    db.delete_all()
    
    #act
    db.delete_registration(1)
    after = db.get_registrations()
    
    #assert
    assert 0==len(after)
