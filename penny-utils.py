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
  setfishlist = set(fishlist)
  return setfishlist

def get_dates_by_fish(dates_d, fish):
  totallist = []
  totallist = dates_d[fish]
  dateslist = set(totallist)

  return dateslist

def get_fishes_by_datelist(fish_d, datelist):

  # return a list of those fish that were eaten on the dates
  # given in ‘datelist’, which is a list of dates

  big_fishlist = []
  i = 0
  while i < len(datelist):
    current = datelist[i]
#    print 'current', current
    day_fishlist = fish_d.get(datelist[i], [])
#    print 'day fishlist', day_fishlist
    for line in day_fishlist:
      big_fishlist.append(line)
#    print i, 'big_fishlist', big_fishlist
    i += 1
  return big_fishlist

def get_dates_by_fishlist(dates_d, fishlist):

  # return a list of those dates on which the fish given
  # in ‘fishlist’ (a list of fish) were eaten.

  big_datelist = []
  i = 0
  while i < len(fishlist):
    current = fishlist[i]
#    print 'current', current
    fish_daylist = dates_d.get(fishlist[i], [])
#    print 'fish daylist', fish_daylist
    for line in fish_daylist:
      big_datelist.append(line)
#    print i, 'big_datelist', big_datelist
    i += 1
  final = set(big_datelist)
  return final


# this code is outside the functions and USES the functions to
# load data and ask questions of the data.

fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
#print fish_d
dates_d = make_dates_dict(fish_d)
#print dates_d


print get_fishes_by_date(fish_d, '1/1')
print get_dates_by_fish(dates_d, 'ahi')

# test 1
x = get_fishes_by_date(fish_d, '1/1')
assert 'salmon' in x

###

# test 2
x = get_dates_by_fish(dates_d, 'salmon')
assert '1/1' in x
assert '1/2' in x

###

# test 3
x = get_fishes_by_datelist(fish_d, ['1/1'])
assert 'salmon' in x, x

###

# test 4
x = get_dates_by_fishlist(dates_d, ['salmon'])
assert '1/1' in x
