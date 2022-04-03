# Telegram Sticker Set

This is a repo for me to store the images/gifs for my telegram sticker pack, and to experiment with Github Actions. Hopefully, I would be able to setup Github Actions to automatically update the stickerpacks whenever the repo is pushed to Github.

Sticker Pack:

* [peepo_emotes](https://t.me/addstickers/peepo_by_jason_pa_bot)

## Converting files for Telegram Stickers

### Animated Sticker Requirements

* Sticker/canvas size must be 512х512 pixels.
* Sticker objects must not leave the canvas.
* Animation length must not exceed 3 seconds.
* All animations must be looped.
* Sticker size must not exceed 64 KB after rendering in Bodymovin.
* All animations must run at 60 Frames Per Second.
* You must not use the following Adobe After Effects functionality when animating your stickers: Auto-bezier keys, Expressions, Masks, Layer Effects, Images, Solids, Texts, 3D Layers, Merge Paths, Star Shapes, Gradient Strokes, Repeaters, Time Stretching, Time Remapping, Auto-Oriented Layers.

### Static Sticker Requirements

* One side of the sticker must be exactly 512 pixels in size – the other side can be 512 pixels or less.
* The image file must be in either .PNG or .WEBP format.

Usually animated files comes in .gif format. To convert into telegram compatible format:

1. [Convert .png file to .gif file if needed](https://www.onlineconverter.com/png-to-gif)

2. [Resize .gif file to 512x512 size](https://www.onlineconverter.com/resize-image)

3. [Convert .gif into .webm](https://www.onlineconverter.com/gif-to-webm)
