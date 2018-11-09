import csv


def get_ave(lst):
    if len(lst) > 0:
        total = 0
        for x in lst:
            total += x
        return round(total / len(lst), 2)


with open('crawl_result.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    nano = []
    micro = []
    macro = []
    celebrity = []
    below_100 = []
    engagements = []

    for row in csv_reader:
        if line_count == 0:
            pass
        else:
            followers = int(row[2])
            avg_engagements = float(row[6])

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

            if avg_engagements > 0:
                engagements.append(avg_engagements)

        line_count += 1

    print(f'Total number = {line_count}')
    print(f'Average engagement = average:{get_ave(engagements)}  total: {len(engagements)}')
    print(f'Nano =  average:{get_ave(nano)}, total: {len(nano)}')
    print(f'Micro = average:{get_ave(micro)}  total: {len(micro)}')
    print(f'Macro = average:{get_ave(macro)}  total: {len(macro)}')
    print(f'Celebrity = average:{get_ave(celebrity)}  total: {len(celebrity)}')
    print(f'Below 100 = average:{get_ave(below_100)}  total: {len(below_100)}')
