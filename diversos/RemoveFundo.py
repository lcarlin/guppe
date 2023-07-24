## pip install rembg
from rembg import remove
from PIL import Image
in_file_name = "bird.jpg"
out_file_name = in_file_name.replace("jpg","png")
input = Image.open(in_file_name)
output = remove(input)
output.save(out_file_name)