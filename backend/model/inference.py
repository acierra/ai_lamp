# inference.py
import torch
import trimesh
import numpy as np
from .generator import Generator3D # Абсолютный импорт генератора 3D моделей

# Пример загрузки модели (предположим, что модель обучена)
def load_model(model_path="shade_model.pth"):
    """
    Загрузка предварительно обученной модели
    """
    model = Generator3D()  # Создание объекта генератора 3D моделей
    model.load_state_dict(torch.load(model_path))  # Загрузка параметров модели
    model.eval()  # Переводим модель в режим инференса
    return model

def generate_3d_model(model, input_params):
    """
    Генерация 3D модели с использованием обученной модели
    :param model: объект модели, использующий нейросеть для генерации
    :param input_params: входные параметры для генерации модели
    :return: 3D модель в виде объекта trimesh
    """
    # Генерация модели на основе входных параметров
    # Здесь используем модель для создания данных, но для примера будем генерировать примитивный куб
    model_output = model.generate(input_params)  # Пример вызова генератора модели

    # Преобразование результатов в формат trimesh (или другой формат для 3D)
    mesh = trimesh.Trimesh(vertices=model_output['vertices'], faces=model_output['faces'])
    return mesh

def save_3d_model(mesh, file_name="generated_model.stl"):
    """
    Сохранение 3D модели в файл .stl для 3D печати
    :param mesh: объект 3D модели
    :param file_name: имя файла для сохранения
    """
    mesh.export(file_name)  # Экспортируем модель в формате STL

# Пример использования
if __name__ == "__main__":
    model = load_model("shade_model.pth")  # Загрузка обученной модели
    input_params = {'diameter': 10, 'height': 20}  # Пример входных параметров для абажура
    mesh = generate_3d_model(model, input_params)  # Генерация 3D модели
    save_3d_model(mesh)  # Сохранение модели в файл STL
