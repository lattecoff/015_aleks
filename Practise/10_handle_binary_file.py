import os
import pickle
import platform

fp_content = ['На златом крыльце сидели\n, Царь, царевич, король, королевич\n, Сапожник, портной, Кто ты будешь такой?\n']

# Пишем данные в бинарный файл из заданной строки.
with open('rhyme_binary', 'wb') as bfp:
    pickle.dump(fp_content, bfp)

# Копируем файл и добавляем к копии расширение.
match (platform.system()):
    case 'Windows':
        os.system('copy rhyme_binary rhyme.log')
    case 'Linux':
        os.system('cp rhyme_binary rhyme.log')

# Удаляем оригинальный бинарник.
os.remove('rhyme_binary')

# Выводим содержимое копии.
with open('rhyme.log', 'r') as fp:
    print(fp.readlines())
