import pandas as pd
from pandas import DataFrame, Series
import numpy as np
from datetime import datetime

xlsfile = pd.ExcelFile('C:\Players_DB\Torres.xlsx')

torres = xlsfile.parse('Sheet1')

total_points = 0
iterator = 0

on_2002 = 0
on_2003 = 0
on_2004 = 0
on_2005 = 0
on_2006 = 0
on_2007 = 0
on_2008 = 0
on_2009 = 0
on_2010 = 0
on_2011 = 0
on_2012 = 0
on_2013 = 0
on_2014 = 0
on_2015 = 0

off_2002 = 0
off_2003 = 0
off_2004 = 0
off_2005 = 0
off_2006 = 0
off_2007 = 0
off_2008 = 0
off_2009 = 0
off_2010 = 0
off_2011 = 0
off_2012 = 0
off_2013 = 0
off_2014 = 0
off_2015 = 0

assists_2002 = 0
assists_2003 = 0
assists_2004 = 0
assists_2005 = 0
assists_2006 = 0
assists_2007 = 0
assists_2008 = 0
assists_2009 = 0
assists_2010 = 0
assists_2011 = 0
assists_2012 = 0
assists_2013 = 0
assists_2014 = 0
assists_2015 = 0

time_2002 = 0
time_2003 = 0
time_2004 = 0
time_2005 = 0
time_2006 = 0
time_2007 = 0
time_2008 = 0
time_2009 = 0
time_2010 = 0
time_2011 = 0
time_2012 = 0
time_2013 = 0
time_2014 = 0
time_2015 = 0

points_2015 = 0
points_2014 = 0
points_2013 = 0
points_2012 = 0
points_2011 = 0
points_2010 = 0
points_2009 = 0
points_2008 = 0
points_2007 = 0
points_2006 = 0
points_2005 = 0
points_2004 = 0
points_2003 = 0
points_2002 = 0

goals_2015 = 0
goals_2014 = 0
goals_2013 = 0
goals_2012 = 0
goals_2011 = 0
goals_2010 = 0
goals_2009 = 0
goals_2008 = 0
goals_2007 = 0
goals_2006 = 0
goals_2005 = 0
goals_2004 = 0
goals_2003 = 0
goals_2002 = 0

Season_2002_start = datetime(2002, 8, 1)
Season_2002_end = datetime(2003, 6, 30)

Season_2003_start = datetime(2003, 8, 1)
Season_2003_end = datetime(2004, 6, 30)

Season_2004_start = datetime(2004, 8, 1)
Season_2004_end = datetime(2005, 6, 30)

Season_2005_start = datetime(2005, 10, 1)
Season_2005_end = datetime(2006, 6, 30)

Season_2006_start = datetime(2006, 8, 1)
Season_2006_end = datetime(2007, 6, 30)

Season_2007_start = datetime(2007, 8, 1)
Season_2007_end = datetime(2008, 6, 30)

Season_2008_start = datetime(2008, 8, 1)
Season_2008_end = datetime(2009, 6, 30)

Season_2009_start = datetime(2009, 10, 1)
Season_2009_end = datetime(2010, 6, 30)

Season_2010_start = datetime(2010, 8, 1)
Season_2010_end = datetime(2011, 6, 30)

Season_2011_start = datetime(2011, 8, 1)
Season_2011_end = datetime(2012, 6, 30)

Season_2012_start = datetime(2012, 8, 1)
Season_2012_end = datetime(2013, 6, 30)

Season_2013_start = datetime(2013, 10, 1)
Season_2013_end = datetime(2014, 6, 30)

Season_2014_start = datetime(2014, 8, 1)
Season_2014_end = datetime(2015, 6, 30)

Season_2015_start = datetime(2015, 8, 1)
Season_2015_end = datetime(2016, 6, 30)

Seasons = ['2002/03', '2003/04', '2004/05', '2005/06', '2006/07', '2007/08', '2008/09', '2009/10', '2010/11', '2011/12', '2012/13', '2013/14', '2014/15', '2015/16']

Total_Time_Played = []

Goals = []

Assists = []

Off_Target = []

On_Target = []

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2015_start and torres['DATA'][iterator] <= Season_2015_end:
       goals_2015 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2014_start and torres['DATA'][iterator] <= Season_2014_end:
       goals_2014 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2013_start and torres['DATA'][iterator] <= Season_2013_end:
       goals_2013 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2012_start and torres['DATA'][iterator] <= Season_2012_end:
       goals_2012 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2011_start and torres['DATA'][iterator] <= Season_2011_end:
       goals_2011 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2010_start and torres['DATA'][iterator] <= Season_2010_end:
       goals_2010 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2009_start and torres['DATA'][iterator] <= Season_2009_end:
       goals_2009 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2008_start and torres['DATA'][iterator] <= Season_2008_end:
       goals_2008 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2007_start and torres['DATA'][iterator] <= Season_2007_end:
       goals_2007 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2006_start and torres['DATA'][iterator] <= Season_2006_end:
       goals_2006 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2005_start and torres['DATA'][iterator] <= Season_2005_end:
       goals_2005 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2004_start and torres['DATA'][iterator] <= Season_2004_end:
       goals_2004 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2003_start and torres['DATA'][iterator] <= Season_2003_end:
       goals_2003 += goals
    iterator += 1

iterator = 0

for goals in torres['GOALS'].dropna():
    if torres['DATA'][iterator] >= Season_2002_start and torres['DATA'][iterator] <= Season_2002_end:
       goals_2002 += goals
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2002_start and torres['DATA'][iterator] <= Season_2002_end:
       time_2002 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2003_start and torres['DATA'][iterator] <= Season_2003_end:
       time_2003 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2004_start and torres['DATA'][iterator] <= Season_2004_end:
       time_2004 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2005_start and torres['DATA'][iterator] <= Season_2005_end:
       time_2005 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2006_start and torres['DATA'][iterator] <= Season_2006_end:
       time_2006 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2007_start and torres['DATA'][iterator] <= Season_2007_end:
       time_2007 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2008_start and torres['DATA'][iterator] <= Season_2009_end:
       time_2008 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2009_start and torres['DATA'][iterator] <= Season_2009_end:
       time_2009 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2010_start and torres['DATA'][iterator] <= Season_2010_end:
       time_2010 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2011_start and torres['DATA'][iterator] <= Season_2011_end:
       time_2011 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2012_start and torres['DATA'][iterator] <= Season_2012_end:
       time_2012 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2013_start and torres['DATA'][iterator] <= Season_2013_end:
       time_2013 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2014_start and torres['DATA'][iterator] <= Season_2014_end and type(time) == 'int':
        time_2014 += time
    iterator += 1

iterator = 0

for time in torres['APPEAR'].dropna():
    if torres['DATA'][iterator] >= Season_2015_start and torres['DATA'][iterator] <= Season_2015_end:
       time_2015 += time
    iterator += 1

iterator = 0

# ASSISTS

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2015_start and torres['DATA'][iterator] <= Season_2015_end:
       assists_2015 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2014_start and torres['DATA'][iterator] <= Season_2014_end:
       assists_2014 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2013_start and torres['DATA'][iterator] <= Season_2013_end:
       assists_2013 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2012_start and torres['DATA'][iterator] <= Season_2012_end:
       assists_2012 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2011_start and torres['DATA'][iterator] <= Season_2011_end:
       assists_2011 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2010_start and torres['DATA'][iterator] <= Season_2010_end:
       assists_2010 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2009_start and torres['DATA'][iterator] <= Season_2009_end:
       assists_2009 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2008_start and torres['DATA'][iterator] <= Season_2008_end:
       assists_2008 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2007_start and torres['DATA'][iterator] <= Season_2007_end:
       assists_2007 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2006_start and torres['DATA'][iterator] <= Season_2006_end:
       assists_2006 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2005_start and torres['DATA'][iterator] <= Season_2005_end:
       assists_2005 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2004_start and torres['DATA'][iterator] <= Season_2004_end:
       assists_2004 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2003_start and torres['DATA'][iterator] <= Season_2003_end:
       assists_2003 += assists
    iterator += 1

iterator = 0

for assists in torres['A'].dropna():
    if torres['DATA'][iterator] >= Season_2002_start and torres['DATA'][iterator] <= Season_2002_end:
       assists_2002 += assists
    iterator += 1

iterator = 0

# SHOT OFF TARGET

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2015_start and torres['DATA'][iterator] <= Season_2015_end:
       off_2015 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2014_start and torres['DATA'][iterator] <= Season_2014_end:
       off_2014 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2013_start and torres['DATA'][iterator] <= Season_2013_end:
       off_2013 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2012_start and torres['DATA'][iterator] <= Season_2012_end:
       off_2012 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2011_start and torres['DATA'][iterator] <= Season_2011_end:
       off_2011 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2010_start and torres['DATA'][iterator] <= Season_2010_end:
       off_2010 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2009_start and torres['DATA'][iterator] <= Season_2009_end:
       off_2009 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2008_start and torres['DATA'][iterator] <= Season_2008_end:
       off_2008 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2007_start and torres['DATA'][iterator] <= Season_2007_end:
       off_2007 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2006_start and torres['DATA'][iterator] <= Season_2006_end:
       off_2006 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2005_start and torres['DATA'][iterator] <= Season_2005_end:
       off_2005 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2004_start and torres['DATA'][iterator] <= Season_2004_end:
       off_2004 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2003_start and torres['DATA'][iterator] <= Season_2003_end:
       off_2003 += off
    iterator += 1

iterator = 0

for off in torres['SH'].dropna():
    if torres['DATA'][iterator] >= Season_2002_start and torres['DATA'][iterator] <= Season_2002_end:
       off_2002 += off
    iterator += 1

iterator = 0

# SHOT ON TARGET

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2015_start and torres['DATA'][iterator] <= Season_2015_end:
       on_2015 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2014_start and torres['DATA'][iterator] <= Season_2014_end:
       on_2014 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2013_start and torres['DATA'][iterator] <= Season_2013_end:
       on_2013 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2012_start and torres['DATA'][iterator] <= Season_2012_end:
       on_2012 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2011_start and torres['DATA'][iterator] <= Season_2011_end:
       on_2011 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2010_start and torres['DATA'][iterator] <= Season_2010_end:
       on_2010 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2009_start and torres['DATA'][iterator] <= Season_2009_end:
       on_2009 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2008_start and torres['DATA'][iterator] <= Season_2008_end:
       on_2008 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2007_start and torres['DATA'][iterator] <= Season_2007_end:
       on_2007 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2006_start and torres['DATA'][iterator] <= Season_2006_end:
       on_2006 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2005_start and torres['DATA'][iterator] <= Season_2005_end:
       on_2005 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2004_start and torres['DATA'][iterator] <= Season_2004_end:
       on_2004 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2003_start and torres['DATA'][iterator] <= Season_2003_end:
       on_2003 += on
    iterator += 1

iterator = 0

for on in torres['SG'].dropna():
    if torres['DATA'][iterator] >= Season_2002_start and torres['DATA'][iterator] <= Season_2002_end:
       on_2002 += on
    iterator += 1

iterator = 0

Total_Time_Played.append(time_2002)
Total_Time_Played.append(time_2003)
Total_Time_Played.append(time_2004)
Total_Time_Played.append(time_2005)
Total_Time_Played.append(time_2006)
Total_Time_Played.append(time_2007)
Total_Time_Played.append(time_2008)
Total_Time_Played.append(time_2009)
Total_Time_Played.append(time_2010)
Total_Time_Played.append(time_2011)
Total_Time_Played.append(time_2012)
Total_Time_Played.append(time_2013)
Total_Time_Played.append(time_2014)
Total_Time_Played.append(time_2015)


Goals.append(goals_2002)
Goals.append(goals_2003)
Goals.append(goals_2004)
Goals.append(goals_2005)
Goals.append(goals_2006)
Goals.append(goals_2007)
Goals.append(goals_2008)
Goals.append(goals_2009)
Goals.append(goals_2010)
Goals.append(goals_2011)
Goals.append(goals_2012)
Goals.append(goals_2013)
Goals.append(goals_2014)
Goals.append(goals_2015)

Assists.append(assists_2002)
Assists.append(assists_2003)
Assists.append(assists_2004)
Assists.append(assists_2005)
Assists.append(assists_2006)
Assists.append(assists_2007)
Assists.append(assists_2008)
Assists.append(assists_2009)
Assists.append(assists_2010)
Assists.append(assists_2011)
Assists.append(assists_2012)
Assists.append(assists_2013)
Assists.append(assists_2014)
Assists.append(assists_2015)

Off_Target.append(off_2002)
Off_Target.append(off_2003)
Off_Target.append(off_2004)
Off_Target.append(off_2005)
Off_Target.append(off_2006)
Off_Target.append(off_2007)
Off_Target.append(off_2008)
Off_Target.append(off_2009)
Off_Target.append(off_2010)
Off_Target.append(off_2011)
Off_Target.append(off_2012)
Off_Target.append(off_2013)
Off_Target.append(off_2014)
Off_Target.append(off_2015)

On_Target.append(on_2002)
On_Target.append(on_2003)
On_Target.append(on_2004)
On_Target.append(on_2005)
On_Target.append(on_2006)
On_Target.append(on_2007)
On_Target.append(on_2008)
On_Target.append(on_2009)
On_Target.append(on_2010)
On_Target.append(on_2011)
On_Target.append(on_2012)
On_Target.append(on_2013)
On_Target.append(on_2014)
On_Target.append(on_2015)


t = {'Season' : Series(Seasons), 'Total Time Played' : Series(Total_Time_Played), 'Goals' : Series(Goals), 'Assists' : Series(Assists), 'Off Target' : Series(Off_Target), 'On Target' : Series(On_Target)}

table = DataFrame(t)

factors = table[['Goals', 'Assists', 'On Target', 'Off Target']]

table['Points'] = np.dot(factors, [50, 20, 4, 1])

print(table)

#print(total_points)

#print(type(torres['DATA'][2]))

#print(torres.dropna())
