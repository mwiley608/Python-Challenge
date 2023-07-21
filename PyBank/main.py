#store file path of CSV
file = '../Resources/budget_data.csv'
#open, read, and store contents
with open(file, 'r') as text:
    #store text in variable
    lines = text.read()
    
