import numpy as np
import trimesh

class Generator3D:
    def __init__(self, height=100, radius=50, pattern_type="smooth"):
        self.height = height
        self.radius = radius
        self.pattern_type = pattern_type

    def generate(self):
        """
        Генерирует 3D-модель абажура в формате STL.
        """
        # Создаем цилиндр (основу абажура)
        mesh = trimesh.creation.cylinder(radius=self.radius, height=self.height, sections=64)

        # Можно добавить узоры, вырезы и прочие элементы, используя numpy и триангуляцию.

        return mesh

    def save_as_stl(self, filename="lampshade.stl"):
        """
        Сохранение модели в файл STL.
        """
        mesh = self.generate()
        mesh.export(filename)
        return filename
