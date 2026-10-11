# ascii-art_HackClub
a program to turn an images pixels into ASCII (letters, numbers, & symbols)

The program takes an image (default or given) and then converts each pixel into a tuple of it r, g and b.               
Then each tuple gets converted to one integer either through brightness (average), lightness (min-max),                 
or luminosity (brightness accounted for human perception). There is also an option to invert the image  
so the dark parts will be light and vice versa.

## EXAMPLE

Starting Image     
<img src="https://imgur.com/PjBnJQ3.jpg" width="700" alt="pineapple">

After program (average brightness, no invert)    
###### (The image might look weird and have large spots, but that goes away if you zoom in)
<img src="https://imgur.com/Iv0keBm.jpg" width="700" alt="Pineapple after program">


Top of pineapple     
<img src="https://imgur.com/oMqgJ2J.jpg" width="700" alt="Top of pineapple">

## How to Run
#### (This has only been tested on a Mac so instructions are only for mac)

1. make sure to have the library [pillow](https://pillow.readthedocs.io/en/stable/index.html) installed
2. Clone repository or compy main.py (when using only main.py only the default image option won't work)
3. cd into repository folder through terminal
4. run 'python3 ./main.py'
5. make sure to zoom out with cmd + '-' to fully see your image