import json
x = open('data.json')
data = json.load(x)

print('''
1. Melatih Bot
2. Berbicara dengan Bot
''')


while True:
    input_pertama = input("Masukkan Kode: ")
    if input_pertama == "1":
        while True:
            a = input("User\t: ")
            if a == "Keluar":
                break
            else:
                b = input("Bot\t: ")
                data[a] = b
                b = open('D:\VSC\CODINGAN\PYTHON\BOT WA\data.json', "w")
                json.dump(data,b)
                b.close()


    elif input_pertama == "2":
        while True:
            a = input("User\t: ")
            if a == 'Keluar':
                break
            if a in data:
                print(f'Bot\t: {data[a]}')
            else:
                print('Bot\t: Itu kata baru')

    else:
        pass
