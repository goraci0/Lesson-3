#Считать текст из файла
f=open('text.txt')
text=list(f.read())
#Очистить текст от знаков препинания
pr={',','.','!','?','»','«','—',':','(',')'}
str=""
for i in range(len(text)):
if text[i] in pr:
text[i] = ' '
str+=text[i]
#Cформировать list со словами (split)
str.split()
#Привести все слова к нижнему регистру,
#получить из list dict, ключами которого являются слова,
#а значениями их количество появлений в тексте;
str.lower()
slov = {}
for word in set(str.split()):
slov[word]=str.count(word)
#Вывести 5 наиболее часто встречающихся слов (sort),
#вывести количество разных слов в тексте (set)
list_txt=list(slov.items())
list_txt.sort(key=lambda i: i[1])
list_txt.reverse()

print(list_txt[:5])
print(len(list_txt)) 
