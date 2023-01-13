def rle_encode(text):
    result = ''
    prev_char = ''
    count = 1

    for char in text:
        if char != prev_char:
            if prev_char:
                result += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count +=1
    else:
        result += str(count) + prev_char
        return result

def rle_decode(text):
    result = ''
    count = ''
    for char in text:
        if char.isdigit():
            count += char
        else:
            result += int(count) * char
            count = ''
    return result

text = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
encode = rle_encode(text)
decode = rle_decode(rle_encode(text))
print(f'Исходный текст: {text}')
print(f'Результат сжатия данных: {encode}')
print(f'Результат восстановления данных: {decode}')
print(f'Исходный и восстановленный результат одинаковы? {decode == text}')