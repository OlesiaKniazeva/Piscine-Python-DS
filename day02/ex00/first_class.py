class MustRead:
        f = open('data.csv', 'r')
        data = f.read()
        print(data)
        f.close()


if __name__ == '__main__':
    MustRead()

