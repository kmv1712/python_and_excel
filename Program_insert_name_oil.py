import os
path = input("Input path:")
print (path)
name_file = [
"Виз В 110 Искра 2 ф  «С» 27.06.18",
"Виз В 110 Искра 2 ф  «В» 27.06.18",
"Виз В 110 Искра 2 ф  «А» 27.06.18",
"Виз В 110 Искра 1 ф  «С» 27.06.18",
"Виз В 110 Искра 1 ф  «В» 27.06.18",
"Виз В 110 Искра 1 ф  «А» 27.06.18",
"Виз В 110 Петрищевская2 ф «С» 27.06.18",
"Виз В 110 Петрищевская2 ф «В» 27.06.18",
"Виз В 110 Петрищевская2 ф «А» 27.06.18",
"Виз В 110 Петрищевская1 ф «С» 27.06.18",
"Виз В 110 Петрищевская1 ф «В» 27.06.18",
"Виз В 110 Петрищевская1 ф «А» 27.06.18",
"Виз В 110 ШСВ ф «С» 26.06.18",
"Виз В 110 ШCB ф «В» 26.06.18",
"Виз В 110 ШСВ ф «А» 26.06.18",
"Виз В 110 Т3 ф «С» 26.06.18",
"Виз В 110 Т3 ф «В» 26.06.18",
"Парниковая РПН Т2 22.06.18",
"Парниковая РПН Т1 22.06.18",
"Космическая РПН Т2 22.06.18",
"Космическая РПН Т1 22.06.18"
]
for i, filename in enumerate(os.listdir(path)):
    print (os.listdir(path))
    os.chdir(path)
    os.rename(filename, '{0}.jpg'.format(name_file[i]))