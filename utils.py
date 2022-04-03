import os
import ffmpeg
from PIL import Image
from pathlib import Path

IMG_SIZE = (512, 512)

def png_to_webm(fpath: Path):
    img = Image.open(fpath)
    img = img.resize(IMG_SIZE)
    img.save(fpath.with_suffix('.gif'))
    gif_to_webm(fpath.with_suffix('.gif'))
    os.remove(fpath.with_suffix('.gif'))

def gif_to_webm(fpath: Path):
    job = ffmpeg.input(fpath).filter('fps', fps=30)
    info = ffmpeg.probe(fpath)
    stream = info['streams'][0]
    fmt = info['format']
    # Try to scale to 512px
    if stream['width'] >= stream['height']:
        job = job.filter('scale', 512, -1)
    else:
        job = job.filter('scale', -1, 512)
    if 'duration' in fmt:
        duration = float(fmt['duration'])

        # Try speed up video if it's over 3 seconds
        if duration > 3.0:
            job = job.filter('setpts', f"(2.9/{duration})*PTS")
    else:
        job = job.filter('setpts', f"1.0*PTS")

    job.output(str(fpath.with_suffix('.webm')),
            pix_fmt='yuva420p',
            vcodec='libvpx-vp9',
            an=None,  # Remove Audio
            ).overwrite_output().run()
        