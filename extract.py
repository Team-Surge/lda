import csv

f = open('training.csv')


csv_f = csv.reader(f)

corpus = ""
for row in csv_f:
    corpus +='\n'
    corpus += row[3]

text_file = open("Output.txt", "w")
text_file.write(corpus)
text_file.close()

f.close()
