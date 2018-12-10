#!/usr/bin/env python

import datetime as dt
import pandas as pd

def parse_guard_activity(raw_guard_activity):
    df = pd.read_csv(
        raw_guard_activity,
        sep=' ',
        names=[ 'date', 'time', 'action', 'what', 'starts', 'shift']
    )
    df = df.apply(lambda x: x.str.strip("[]"))
    df['date'] = df['date'].apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%d"))
    df['time'] = pd.to_datetime(df['time'], format='%H:%M')
    df.sort_values(by=['date', 'time'], inplace=True)
    return df

def create_grid(guard_activity):
    gdf = pd.DataFrame(columns=['date', 'guard']+[i for i in range(0, 60)])
    gdf.set_index(['date', 'guard'], inplace=True)
    sleep_start = wake_start = 0
    current_date = None
    current_guard = None
    for index, row in guard_activity.iterrows():
        if row['action'] == "Guard":
            current_date = row['date']
            if row['time'].hour == 23:
                current_date = current_date + dt.timedelta(days=1)
            current_guard = int(row['what'].strip('#'))
            gdf.at[(current_date, current_guard), range(0, 60)] = [0]*60
            continue
        elif row['action'] == "falls":
            sleep_start = row['time'].minute
        elif row['action'] == "wakes":
            wake_start = row['time'].minute
            for i in range(sleep_start, wake_start):
                gdf.at[(current_date, current_guard), i] += 1
    return gdf

def strategy1(guard_activity):
    gdf = create_grid(guard_activity)
    sleepiest_guard = gdf.sum(axis=1).groupby(by=['guard']).sum().idxmax()
    gdf_sum = gdf.groupby(by=['guard']).sum()
    sleepy_minute = int(gdf_sum.loc[sleepiest_guard].idxmax())
    return sleepiest_guard, sleepy_minute, sleepiest_guard * sleepy_minute

def main(guard_activity_input):
    guard_activity = parse_guard_activity(guard_activity_input)
    sleepiest_guard, sleepy_minute, s1 = strategy1(guard_activity)
    print('Strategy 1 Sleepiest Guard: ', sleepiest_guard, 'Sleepy Minute: ', sleepy_minute)
    print('Strategy 1 calculation: ', s1)

if __name__ == '__main__':
    guard_activity = "input_test.txt"
    main(guard_activity)

    guard_activity = "input.txt"
    main(guard_activity)
