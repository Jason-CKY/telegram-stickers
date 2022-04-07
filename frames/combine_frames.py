from io import BytesIO
from PIL import Image, ImageSequence
from glob import glob

def separate_gif(fpath, output_path):
    im = Image.open(fpath)
    i = 0
    for frame in ImageSequence.Iterator(im):
        frame.save(f"{output_path.split('.')[0]}-{str(i)}.png", lossless=True)
        i += 1

def combine_gif(dirname: str, output_path):
    fnames = glob(f"{dirname}/*.png")
    frames = []
    for i in range(len(fnames)):
        fname = f"{dirname}/{dirname}-{i}.png"
        print(fname)
        img = Image.open(fname)
        byte = BytesIO()
        frames.append(byte)
        img.save(byte, format='GIF')
        # img = Image.open(fname)
        # frames.append(img.convert('P', palette=Image.ADAPTIVE))
    gifs = [Image.open(frame) for frame in frames]    
    gifs[0].save(output_path, format='GIF', save_all=True, append_images=gifs[1:], duration=40, loop=0, disposal=3)
    

if __name__ == '__main__':
    combine_gif('sadpeepoclap', 'sadpeepoclap.gif')

