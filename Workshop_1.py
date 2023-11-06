import re 
file_name = 'example.html'
with open(file_name, 'r', encoding='utf-8') as file:
    html_content = file.read()
print(re.findall(r'\b[A-Za-z0-9._%+-]{3,30}+@[A-Za-z0-9-]{1,12}+\.[A-Z|a-z]{2,5}\b', html_content)) 