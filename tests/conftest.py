import pytest
from mathematic.math_func2 import StudentDB
import os


db = None


@pytest.fixture(scope='session')
def db():
    print("---------------setup---------------")
    global db
    db = StudentDB()
    db.connect(os.getcwd()+'/tests/data.json')
    yield db
    print("---------------teardown---------------")
    db.close()
