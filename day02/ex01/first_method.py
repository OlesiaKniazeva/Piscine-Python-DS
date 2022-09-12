class Research:
    def file_reader(self):
        f = open('data.csv', 'r')
        data = f.read()
        f.close()
        return data


if __name__ == '__main__':
    r = Research()
    print(r.file_reader())

