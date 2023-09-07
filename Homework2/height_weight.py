import csv
height_inches = []
weight_pounds = []
with open('hw.csv') as csvfile:

    reader = csv.DictReader(csvfile)
    for row in reader:
        height_inches.append(row[' "Height(Inches)"'])
        weight_pounds.append(row[' "Weight(Pounds)"'])

height_inches_redacted = []
weight_pounds_redacted = []


def height_inches_func():
    for i in height_inches:
        i_split = i.replace(' ', '')
        i_split = int(float(i_split))
        height_inches_redacted.append(i_split)
    return height_inches_redacted


def weight_pounds_func():
    for i in weight_pounds:
        i_split = i.replace(' ', '')
        i_split = int(float(i_split))
        weight_pounds_redacted.append(i_split)
    return weight_pounds_redacted


weight_kg = f'Average Weight, kg: {(sum(weight_pounds_func())/ 25000) * 0.453592}'
height_cm = f'Average Height, cm: {(sum(height_inches_func())/ 25000) * 2.54}'

def weight_height_kg_cm():
    return weight_kg, height_cm

with open('templates/weight_height.txt', 'w') as file:
  for i in weight_height_kg_cm():
    file.write(i)



