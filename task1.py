#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Решение 1
test = "Привет! идем три гулять."
words = test.split(" ")
words = [word for word in words if not "три" in word]
answer = " ".join(words)
print(words)
print(answer)
# Решение 2
#my_str = 'Мороз ТРИ и холод, веретри зима!'
#new_str = ' '.join(list(filter(lambda elem: 'три' not in elem.lower(), my_str.split())))
#print(new_str)