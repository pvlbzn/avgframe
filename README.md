# Average Frame

Produce one frame from a sequence of frames such that resulting
frame represents an average of a sequence.


## Algorithm

<img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;\large&space;(\sum_{i=1}^{|&space;\,&space;\chi|&space;\,&space;}&space;\chi_i)&space;\;&space;/&space;\;&space;|\,&space;\chi\,&space;|" title="\large (\sum_{i=1}^{| \, \chi| \, } \chi_i) \; / \; |\, \chi\, |" />

<img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;\large&space;\chi&space;=&space;\left&space;\{&space;x_1,&space;x_2,&space;...&space;,&space;x_n\right&space;\}&space;|&space;x_i&space;\in&space;\mathbb{R}^m^^\times&space;n" title="\large \chi = \left \{ x_1, x_2, ... , x_n\right \} | x_i \in \mathbb{R}^m^^\times n" />

Where _X_ is a set of frames, x is a particular frame.


## Usage

From terminal:

```
python3 path/to/video/file.mp4 frames_to_skip frames_to_grab
```

From REPL:

```
from src import averanger as a

# Path to your video file
path = 'data/video.mp4'

# Frames to skip
skip = 2000

# Frames to grab
grab = 25

a.averengify(path, skip, grab)
```


## Outcomes

There is no one unique recepi besides basic video analisys. General rules are the following:

* The more video is centered on some object and more this object 'still' the bigger grab value can be taken

* The more video intense (change of the background, absense of central or 'still' object) the smaller grab value should be


#### 5 frames

![5 frames](https://github.com/pvlbzn/avgframe/raw/master/outcomes/5.jpeg "5 frames")


#### 10 frames

![10 frames](https://github.com/pvlbzn/avgframe/raw/master/outcomes/10.jpeg "10 frames")


#### 25 frames

![25 frames](https://github.com/pvlbzn/avgframe/raw/master/outcomes/25.jpeg "25 frames")


#### 50 frames

![50 frames](https://github.com/pvlbzn/avgframe/raw/master/outcomes/50.jpeg "50 frames")
