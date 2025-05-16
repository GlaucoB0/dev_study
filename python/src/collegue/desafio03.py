temperaturas = (29.4, 30.2, 28.9, 31.0, 30.2, 29.7, 28.9)
media = 0

for temperatura in temperaturas:
    media += temperatura
media = media/len(temperaturas)

sem_repeticao = set(temperaturas)
sem_repeticao = tuple(sem_repeticao)

print(f"tupla: {temperaturas}")
print(f"media: {media}")
print(f"Sem repetição: {sem_repeticao}")