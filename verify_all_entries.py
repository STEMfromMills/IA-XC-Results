"""
Yet again, ChatGPT FTW!
"""

import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def main():
    csv_file1 = '2022-10-20-1A Regina.csv'  # Change this to the first CSV file's name
    csv_file2 = 'all_players.csv'  # Change this to the second CSV file's name

    data_file1 = read_csv(csv_file1)
    data_file2 = read_csv(csv_file2)

    for row in data_file1:
        for cell in row:
            found = False
            for row2 in data_file2:
                if cell in row2:
                    found = True
                    break
            if not found:
                print(f"Cell not found in {csv_file2}: {cell}")
            #else:
            #    print("Verified!")

if __name__ == "__main__":
    main()
