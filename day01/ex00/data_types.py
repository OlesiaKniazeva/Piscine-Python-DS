def data_types():
    integer = 1
    string = "hi"
    float_type = 1.3
    boolean = True
    list_type = ["one", "two", "three", "one"]
    dictionary = {'cat': 'Molly', 'dog': 'Brian'}
    tuple_type = tuple()
    set_type = {12, 13, 45}

    res = [type(integer).__name__, type(string).__name__, type(float_type).__name__,
           type(boolean).__name__, type(list_type).__name__, type(dictionary).__name__,
           type(tuple_type).__name__, type(set_type).__name__]

    print(str(res).replace('\'', ''))


if __name__ == '__main__':
    data_types()
