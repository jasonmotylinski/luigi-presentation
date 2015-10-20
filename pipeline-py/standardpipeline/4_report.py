import json

report = {}

for category in ['KICK_RETURNS', 'KICKING', 'PASSING', 'PUNTING', 'RECEIVING', 'RUSHING', 'SACKS', 'SCORING', 'TACKLES', 'TOUCHDOWNS']:
    with open('../output/{0}.json'.format(category), 'r') as f:
        data = json.loads(f.read())
        report[category] = data[:-10]


with open('../output/report.json', 'wt') as f:
    for k in report.keys():
        for el in report[k]:
            f.write(el.values()[0] + "," + el.values()[1] + "," + el.values()[2] + "," + el.values()[3] + '\n')

print 'Complete!'
