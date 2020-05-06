import csv

mantis_file = open("mantis.csv","r")
r = csv.reader(mantis_file, delimiter=",", quotechar='"')
# on lit la première ligne avec le noms des colonnes pour la passer 
next(r)

result_file = open("backlog.csv","w")
w = csv.writer(result_file, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

for row in r:
    newrow = [row[0], row[2], row[3], row[1]]
    w.writerow(newrow)