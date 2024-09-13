def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()
    inside_tag = False
    cleaned_text = ''
    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            cleaned_text += char
    cleaned_lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]
    with open(result_file, 'w', encoding='utf-8') as output_file:
        output_file.write("\n".join(cleaned_lines))
delete_html_tags('draft.html', 'cleaned.txt')
