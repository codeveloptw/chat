def read_file(filename):
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    new_lines = []
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        chat = ''.join(s[2:])  # 把 list 接起來成 str ，中間用 '?' 隔開
        new_lines.append([time, name, chat])   
        if name == 'Allen':
            print(f'A: {chat}')
            if chat == '貼圖':
                allen_sticker_count += 1
            elif chat == '圖片':
                allen_image_count += 1
            else:
                allen_word_count += len(chat)
        elif name == 'Viki':
            print(f'V: {chat}')
            if chat == '貼圖':
                viki_sticker_count += 1
            elif chat == '圖片':
                viki_image_count += 1
            else:
                viki_word_count += len(chat)
    print(f'Allen 字數 : {allen_word_count}')
    print(f'Allen 貼圖 : {allen_sticker_count}')
    print(f'Allen 圖片 : {allen_image_count}')
    print(f'Viki  字數 : {viki_word_count}')
    print(f'Viki  貼圖 : {viki_sticker_count}')
    print(f'Viki  圖片 : {viki_image_count}')
    return new_lines


def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line[1] + ',' +line[2] +'\n')


def main():
    lines = read_file('LINE-Viki.txt')
    new_lines = convert(lines)
    write_file('output.txt', new_lines)


if __name__ == '__main__':
    main()
