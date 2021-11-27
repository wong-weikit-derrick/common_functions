from common_functions import lib

def test_num_func():
    num_test_func = len([x for x in dir(lib) if not x.startswith('__')])
    
    with open('common_functions/lib.py', 'r') as file:
        data = file.readlines()
    
    num_func = len([x for x in data if x.startswith('def')])

    assert num_func == num_test_func