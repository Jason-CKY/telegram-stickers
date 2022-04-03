from PIL import Image

IMG_SIZE = (512, 512)

def png_to_webm(fpath):
    img = Image.open(fpath)
    img = img.resize(IMG_SIZE)
    save_path = f"{fpath.split('.')[0]}512.png"
    img.save(save_path)

def jpg_to_webm():
    pass

def gif_to_webm():
    pass