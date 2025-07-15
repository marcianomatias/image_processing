import os
from image_processing import to_grayscale

def test_to_grayscale(tmp_path):
    input_path = "tests/sample.jpg"
    output_path = tmp_path / "output.jpg"
    to_grayscale(input_path, output_path)
    assert os.path.exists(output_path)
