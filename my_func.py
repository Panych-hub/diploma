import re
def my_processing(text):
    marks_div = ['\n', '-']
    marks = [',', '>', '<', '\'', ';', '/', ':', '[', ']', '"', "'", '(', ')']
    marks_end = ['!', '?']
    text_main = text
    for i in marks_div:
        text_main = text_main.replace(i, ' ')
    for i in marks:
        text_main = text_main.replace(i, '')
    for i in marks_end:
        text_main = text_main.replace(i, '.')
    text_main = re.sub('[A-Za-z]\.[A-Za-z]', '', text_main)
    return text_main.lower()
    
def my_save_file(file_name, text):
    f = open(file_name, "w", encoding='utf-8')
    f.write(text.lower().replace('.', ' .PERIOD').replace(',', ' .PERIOD')\
            .replace('?', ' .PERIOD').replace('!', ' .PERIOD').replace('-', ' '))
    f.close()