from project import deposition
from project import withdrawal
from project import correct_user
from project import editor

def test_deposition():
    user_1={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"}
    assert deposition(user_1,"400")=={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1400.00"}

    user_2={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"}
    assert deposition(user_2,"3000")=={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "4000.00"}

    user_3={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"}
    assert deposition(user_3,"3000.90")=={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "4000.90"}

    user_4={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"}
    assert deposition(user_4,"-3000")=={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"}


def test_withdrawl():
    user_1={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"}
    assert withdrawal(user_1,"400")=={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "600.00"}

    user_2={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"}
    assert withdrawal(user_2,"1100")=={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"}

    user_3={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"}
    assert withdrawal(user_3,"100.30")=={"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "899.70"}


def test_editor():
    database=[{"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"},{"first": "Katie", "last": "Bell", "username": "dell_katie", "pin": "8564", "money": "6000.00"}]
    result=[{"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"},{"first": "Katie", "last": "Bell", "username": "dell_katie", "pin": "8564", "money": "4000.00"}]
    assert editor(database,{"first": "Katie", "last": "Bell", "username": "dell_katie", "pin": "8564", "money": "4000.00"})==result

def test_correct_user():
    database=[{"first": "Hannah", "last": "Abbott", "username": "Habb", "pin": "5496", "money": "1000.00"},{"first": "Katie", "last": "Bell", "username": "dell_katie", "pin": "8564", "money": "6000.00"}]
    assert correct_user(database,"dell_katie")==True
    assert correct_user(database,"Invalid_name")==False
