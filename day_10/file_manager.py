import os

"""
abspath(__file__) : Noas muestra la ruta exacta de donde se llama esta 
                    linea de codigo
dirname(this_file_path) : Nos retorna una ruta anterior a la que le
                          pasamos por parametro.
"""

this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)
ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)

email_txt = os.path.join(BASE_DIR, "templates", "email.txt")

content = ""

with open(email_txt, 'r') as f:
    content = f.read()


print(content.format(name='Tomas'))