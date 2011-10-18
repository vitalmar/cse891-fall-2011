import csv, urllib

def load_csv(url):
  d = {}
  fp = urllib.urlopen(url)
  for row in csv.DictReader(fp):
     key = row['date']
     value = row['fish']

     x = d.get(key, [])
     x.append(value)
     d[key] = x

  return d

def make_dates_dict(fish_d):
  dates_d = {}

  for date, fish in fish_d.iteritems():
    values = fish_d[date]
    i = 0
    while i < len(values):
        key = values[i]
        fish_list = dates_d.get(key, [])
        fish_list.append(date)
        dates_d[key] = fish_list
        i += 1

  return dates_d

def get_fishes_by_date(fish_d, date):
  fishlist = []
  fishlist = fish_d[date]

  return fishlist

def get_dates_by_fish(dates_d, fish):
  totallist = []
  totallist = dates_d[fish]
  dateslist = set(totallist)

  return dateslist

# this code is outside the functions and USES the functions to
# load data and ask questions of the data.

fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
#print fish_d
dates_d = make_dates_dict(fish_d)
#print dates_d


print get_fishes_by_date(fish_d, '1/1')
print get_dates_by_fish(dates_d, 'cod')
