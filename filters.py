from PIL import Image

def to_grayscale(input_path, output_path):
    image = Image.open(input_path).convert('L')
    image.save(output_path)
