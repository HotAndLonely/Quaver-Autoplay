<h1>Click this image to see the video!</h1>

[![Watch the video](https://i.ibb.co/DCQZ8rT/image.png)](https://youtu.be/aDZ5MkhPbc8?si=Sztgu2GsCBawEZLt)
> [!CAUTION]
> Please don't use this code to gain an advantage in the game. It ruins the experience for the rest of the players,
>  and you'll get caught because it's very obvious. <b>If you still want to try it, play offline.</b>

# Quaver-Autoplay 🎵 🤖
Quaver rhythm game simple autoplay script.

Prerequisites:
<ul>
<li>git</li>
<li>Python</li>
<li>AutoHotKey</li>
</ul>

<h1>Install</h1>

<h2>Source code</h2>

Clone repository
```
git clone https://github.com/HotAndLonely/Quaver-Autoplay
```
```
cd .\Quaver-Autoplay\
```
Pip install requirements
```
pip install -r .\requirements.txt
```
Run coords script and 4k note slots position coords and background rgb color.
```
python .\show_coords_color.py
```
Modify the autoplay script variables
```
# CHANGE THIS (EXAMPLE)
bg_color      = (20, 20, 20)            # Color of note slot without notes
coords_x      = [770, 900, 1015, 1140]  # X coords of every note slot horizontal left to right 4k mode
coords_y      = 900                     # Y coord of note slots vertical
game_controls = ['w', 'e', 'i', 'o']    # Game controls left to right 4k mode
```
Run when song starts
```
python .\autoplay.py
```
