import glob
import os
import math
from PIL import Image
from pathlib import Path


def open_file(filename: str):
    """После создания или изменения открываем файл автоматически"""
    try:
        print(f'Открываем файл {filename}')
        os.startfile(filename)
    except: print(f'Файл {filename} невозможно открыть')


def create_file(image_list: list, new_image: Image, image_size: tuple, grid_size: int):
    """Заполняем TIFF файл изображениями и сохраняем его"""
    width = 0
    height = 0
    for index, elem in enumerate(image_list):
        if index % grid_size == 0 and index != 0:
            width = 0
            height += image_size[1]
        elem.thumbnail(image_size, Image.Resampling.LANCZOS)
        new_image.paste(elem, (width, height))
        width += elem.width
    filename = 'Result.tiff'
    new_image.save(filename, 'TIFF')
    open_file(filename)


def main():
    """Главная функция программы с извлечением изображенией"""
    list_to_find = ['1369_12_Наклейки 3-D_3', '1388_2_Наклейки 3-D_1']
    new_image = Image.new('RGB', (1000, 1000), (255, 255, 255))
    image_list = []
    for directory in list_to_find:
        current_path = str(Path(__file__).parent.absolute()) + '/' + directory

        for filename in glob.glob(current_path + '\\*'):
            image = Image.open(filename)
            image_list.append(image)

    # В зависимости от количества картинок делаем разные размеры
    image_count = len(image_list)
    if image_count <= 9:
        grid_size = 3
    elif image_count <= 16:
        grid_size = 4
    elif image_count <= 36:
        grid_size = 6
    else:
        grid_size = 10

    side_size = math.floor(1000 / grid_size)
    image_size = side_size, side_size
    create_file(image_list, new_image, image_size, grid_size)
    return image_list

if __name__ == '__main__':
    main()