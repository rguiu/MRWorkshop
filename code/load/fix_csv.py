with open('data/premier/12-13/e0.csv', 'w') as outfile, open('data/premier/12-13/e0.csv.original', 'r') as infile:
        for line in infile:
            line_as_list = line.split(',')
            line_as_list.insert(10,'') # inserting the referee referee
            outfile.write(','.join(line_as_list))

with open('data/premier/13-14/e0.csv', 'w') as outfile, open('data/premier/13-14/e0.csv.original', 'r') as infile:
        for line in infile:
            line_as_list = line.split(',')
            for i in range(3):
                line_as_list.insert(29,'') 
            for i in range(3):
                line_as_list.insert(50,'') 

            outfile.write(','.join(line_as_list))

