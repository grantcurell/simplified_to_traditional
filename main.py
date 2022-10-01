# Simplified to Traditional
from time import sleep
from googletrans import Translator
import argparse
import os

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-f', '--filename', dest='filename', help='Name of the file containing simplified characters that '
                                                              'you want to translate to traditional.')
args = parser.parse_args()

translator = Translator()

with open(args.filename, "r", encoding="utf-8") as file:
    data = file.read()
    file.close()

# Google limits how many characters you can send per translation. This is designed to split the inbound file up into
# reasonable chunks and then translate them.
CHARACTER_COUNT_LIMIT = 5000
split_data = [data[i:i + CHARACTER_COUNT_LIMIT] for i in range(0, len(data), CHARACTER_COUNT_LIMIT)]

translations = []
for item in split_data:
    translations.append(translator.translate(item, src="zh-cn", dest='zh-tw').text)
    sleep(30)

# this will return a tuple of root and extension
split_tup = os.path.splitext(args.filename)

with open(split_tup[0] + "_traditional" + split_tup[1], "w", encoding="utf-8") as file:
    file.writelines(translations)
    file.close()

