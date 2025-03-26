from .generator import Generator3D

def generate_3d_model(height=100, radius=50, pattern_type="smooth"):
    generator = Generator3D(height, radius, pattern_type)
    filename = generator.save_as_stl()
    return filename
