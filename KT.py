def get_books(file_name):
  result = []
  with open(file_name, 'r', encoding='utf8') as f:
    str_list = list(map(lambda line: line.split('|'), f))
    clear_list = list(map(lambda row: list(map(lambda elem: elem.replace('\n', '').strip(), row)), str_list))
    result = list(map(lambda row: list(map(lambda elem: 
    int(elem) 
    if elem.isdigit()
    else float(elem) if elem.replace('.', '', 1).isdigit()
    else elem, row)), clear_list))
    f.close()
  return result

def filtered_books(books, query):
  result = []
  result = list(filter(lambda row: query.lower() in str(row[1]).lower(), books))
  result = list(map(lambda row: [row[0], row[1] + ', ' + row[2]] + row[3:], result))
  return result

def turpleFunc(books):
  result = []
  result = list(map(lambda row: (row[0], row[2] * row[3]), books))
  return result
books = get_books('books.csv')

books2 = filtered_books(books, 'python')

turpleFunc(books2)
