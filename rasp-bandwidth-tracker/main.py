import psutil
import time
import os
import csv

UPDATE_DELAY = 5 # in seconds
DATA_PRECISION = 3 # Round to decimals

lapsed_time = 0

csv_path = 'data.csv'
header = ['Time (s)', 'Upload (MB)', 'Download (MB)']

def main():
    while True:
        time.sleep(UPDATE_DELAY)
        update_network_stats()
        append_data_to_csv(csv_path)

def append_data_to_csv(path):
    file_exists = os.path.isfile(csv_path)

    with open(csv_path, 'a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(header)

        writer.writerow(get_data())

def get_data():
    return [lapsed_time, mbytes_recv, mbytes_sent]

def update_network_stats():
    global mbytes_sent, mbytes_recv, lapsed_time

    io = psutil.net_io_counters()

    mbytes_sent = convert_bytes_to_mb(io.bytes_sent)
    mbytes_recv = convert_bytes_to_mb(io.bytes_recv)

    lapsed_time += UPDATE_DELAY

def convert_bytes_to_mb(bytes):
    return round(bytes / (1024**2), DATA_PRECISION)

if __name__ == "__main__":
    main()


