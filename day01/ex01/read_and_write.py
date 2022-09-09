def change_delimeter():
    f = open('ds.csv', 'r')
    f_out = open('ds.tsv', 'w')
    for line in f:
        copy = line
        flag = True
        for index, ch in enumerate(line):
            if ch == '"' and flag:
                flag = False
                continue
            if ch == ',' and flag:
                copy = copy[:index] + '\t' + copy[index + 1:]
            if ch == '"' and flag != True:
                flag = True
        f_out.write(copy)
    f.close()
    f_out.close()


if __name__ == '__main__':
    change_delimeter()
