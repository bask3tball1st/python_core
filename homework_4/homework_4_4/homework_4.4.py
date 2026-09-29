try:
    with open("image_4.4.1.jpg", 'rb') as image1, open("image_4.4.2.jpg", 'rb') as image2:
        image_buffer1 = image1.read()
        image_buffer2 = image2.read()
    with open("image_4.4.1.jpg", 'wb') as image1, open("image_4.4.2.jpg", 'wb') as image2:
        image1.write(image_buffer2)
        image2.write(image_buffer1)
        print("Файлы успешно поменяны местами!")
except FileNotFoundError:
    print("Файл не найден!")