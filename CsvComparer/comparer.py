from CSVFile import *
import click
import pandas as pd
import datetime
import glob

files_dir = "./files/"
def getFiles(pattern):
    return glob.glob(pattern)

input_files = getFiles(files_dir + "*.csv")
file_count = len(input_files)

# Read .csv files and add significant columns
def restructure_file():

    table = []
    data = []

    for i in range(0,file_count):
        file = input_files[i]
        data.append(file)
        csv = pd.read_csv(data[i])
        df = pd.DataFrame(csv)
        df = df[["worked_data_count","machine_used_memory","cpu_usage_rate","time"]]
        table.append(df)
    
    return table

# Each .csv file has it's own line
def get_file_line_count():

    table = restructure_file()

    file_line_number = []

    for i in range(0, file_count): 
        line_number = len(table[i])
        file_line_number.append(line_number)

    return file_line_number

def alter_tables():

    files_csv = []
    table = restructure_file()
    file_line_number = get_file_line_count()

    for i in range(0, file_count):
        maxPq = max(table[i]["worked_data_count"])
        minPq = min(table[i]["worked_data_count"])
        avgPq = (maxPq-minPq) / file_line_number[i]
        table[i].drop("worked_data_count",axis=1,inplace=False)
        table[i]["worked_data_count"] = avgPq

        table[i].drop("machine_used_memory",axis=1,inplace=False)
        table[i]["machine_used_memory"] = sum(table[i]["machine_used_memory"]) / file_line_number[i]

        memory_value = (sum(table[i]["machine_used_memory"]) / file_line_number[i] ) / (1024 * 1024 * 1024)
        table[i]["memory_as_GB"] = str(memory_value)[:7]

        cpu_value = sum(table[i]["cpu_usage_rate"]) / file_line_number[i]
        table[i].drop("cpu_usage_rate",axis=1,inplace=False)
        table[i]["cpu_usage_rate"] = cpu_value

        datetimeFormat = "%H:%M:%S"
        max_time = max(table[i]["time"])
        min_time = min(table[i]["time"])
        diff = datetime.datetime.strptime(max_time, datetimeFormat) - datetime.datetime.strptime(min_time, datetimeFormat)
        table[i].drop("time",axis=1,inplace=False)
        table[i]["time"] = diff

        file_values = table[i][:1]
        files_csv.append(file_values)

    return files_csv

# n should be 0 and 1
# 0 for the first and 1 for the second file.
def getCSVResults(n):

    files_csv = alter_tables()

    file_name = input_files[n].split("\\")[-1] 
    file_csv = files_csv[n]

    csv = CSVFile()
    csv.set_worked_data(file_csv["worked_data_count"].get(0))
    csv.set_used_memory(file_csv["machine_used_memory"].get(0))
    csv.set_total_memory(file_csv["memory_as_GB"].get(0))
    csv.set_cpu_usage(file_csv["cpu_usage_rate"].get(0))
    csv.set_time(file_csv["time"].get(0).total_seconds())
    return csv


@click.command()
@click.option('--compare', help = 'Will compare specific .csv files')
def cli():

    first_file = getCSVResults(0)
    second_file = getCSVResults(1)
    
    click.echo('''
        ||||||||||||||||||||||||||||||||||||||| CSV FILE 1 |||||||||||||||||||||||||||||||||||||||||
        || worked_data_count || machine_used_memory || total_memory || cpu_usage_rate ||   time   ||    
        ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        ||        {0}        ||          {1}        ||      {3}     ||       {4}      ||    {5}   ||
        ||||||||||||||||||||||||||||||||||||||| CSV FILE 2 |||||||||||||||||||||||||||||||||||||||||
        || worked_data_count || machine_used_memory || total_memory || cpu_usage_rate || time ||||||
        ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        ||        {6}        ||          {7}        ||      {8}     ||       {9}      ||    {10}  ||
        ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    '''.format(first_file.get_worked_data, first_file.get_used_memory, first_file.get_total_memory, first_file.get_cpu_usage, first_file.get_time,
    second_file.get_worked_data, second_file.get_used_memory, second_file.get_total_memory, second_file.get_cpu_usage, second_file.get_time))

