import csv

def get_ave(lst):
    if len(lst) > 0:
        total = 0
        for x in lst:
            total += x
        return round(total / len(lst))


with open('crawl_result.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    nano = []
    micro = []
    macro = []
    celebrity = []
    below_100 = []

    for row in csv_reader:
        if line_count == 0:
            pass
        else:
            followers = int(row[2])

            if followers > 100 < 200:
                nano.append(followers)
            elif followers > 201 < 5000:
                micro.append(followers)
            elif followers > 5001 < 50000:
                macro.append(followers)
            elif followers > 50001:
                celebrity.append(followers)
            else:
                below_100.append(followers)

        line_count += 1

    print(f'Total number = {line_count}.')
    print('Nano = ' + str(get_ave(nano)))
    print('Micro = ' + str(get_ave(micro)))
    print('Macro = ' + str(get_ave(macro)))
    print('Celebrity = ' + str(get_ave(celebrity)))
    print('Below 100 = ' + str(get_ave(below_100)))
