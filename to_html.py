import mammoth

with open('test.docx','rb') as f:
    html = mammoth.convert_to_html(f)
    
    with open('result.html','w') as fw:
        fw.write(html.value)