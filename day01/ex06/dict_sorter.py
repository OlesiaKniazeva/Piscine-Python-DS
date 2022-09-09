def get_tuple():
    tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return tuples


def sort_dict():
    tuples = get_tuple()
    di = {}
    for x, y in tuples:
        di.setdefault(x, int(y))
    sort_by_key = dict(sorted(di.items(), key=lambda item: item[0]))
    sort = dict(sorted(sort_by_key.items(), reverse=True,  key=lambda item: item[1]))
    for k in sort.keys():
        print(k)


if __name__ == '__main__':
    sort_dict()