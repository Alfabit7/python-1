# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

text = 'Забвение — угасание памяти о каком-либо явлении, событии или человеке. АБВГДе́йка — советская и российская детская образовательная телевизионная программа для дошкольников и младших школьников.'
letters = 'абв'
def word_remover(text, letters):
    text = text.lower().split()
    for item in text:
        if letters.lower() in item:
            text.pop(text.index(item))
    text = ' '.join(text)
    return text

print(f'Исходный текст: {text}')
print(f'Измененный текст: {word_remover(text, letters)}')
