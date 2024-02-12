
series_num = ''


with open('list_numbers.txt', 'r', encoding='utf-8') as fp_src:
    while True:
        s = fp_src.readline()
        s = s.rstrip('\n')

        if s == '':
            break
        elif int(s) < 0:
            with open('list_negative_numbers.txt', 'a', encoding='utf-8') as fp_dst:
                fp_dst.write(str(s) + '\n')






