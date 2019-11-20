import csv

def parse(filename):
    data = []
    print('[+] Reading the file...')
    with open(filename, 'r') as file:
        print('[+] File opened.')

        # open csv and store headers, move on to the next line
        csv_file = csv.reader(file)
        headers = next(csv_file)
        
        # display headers
        print('\nHeaders\n| ', end ='')
        for title in headers:
            print(title, end = ' | ')
        print()

        # append each line in the data as a discionary with each row corresponding to the title
        for row in csv_file:
            data.append(dict(zip(headers, row)))

    # return the data
    return data

data = parse('car.csv')