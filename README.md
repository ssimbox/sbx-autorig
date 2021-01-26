# sbx-autorig
Welcome to my repo, first in my life.

I'm currently working on controllers and relationships maker of my own rigs and I would like to share my entire work, free for all.
Actually I developed a simple IKFK-builder for legs and arms and an auto hand maker (I really hate make fingers rigs, really tedious)

Actually there is a simple rule to remember using my tools **naming convention**. 
I use this type of joint naming: *side_jointName* ---> *l_upperleg* or *r_knee*. Suffixes are ok but I need this kind of prefix.

This is just a start, I want to build always better tools to help my own works and, hopefully, speed up yours.
These things is what I achieved in one full month of study, I'm totally new to coding, there's much more to do.
Any suggestion will be appreciated and, if you want to contribute feel free, I just want some of this in Maya world :)

# IKFK-Builder

![Alt Text](https://media.giphy.com/media/9oNiWOptNcUAJlf9cG/giphy.gif)
## Features

Oh well, you know...

* Support arm and leg chains.
    * Arm = 3 joint length
    * Leg = 5 joint length
* Create an _ik chain and _fk chain using, by your choice, blendColors node connections or orientConstraint + Set Driven Key
* Create fk controllers and ik-handles for legs and arms

## To-Do list

Lots of stuff

- [x] Better foot attributes
- [x] Clavicle support
- [x] Tweaks about pole vectors
- [x] More complex leg and arm chains
- [x] Add Squash and Stretch option
- [x] Color choice (by your own)
- [x] Better controllers
- [x] Auto hierarchy in outliner

## How to install
Save *IKFK_Builder* in your maya scripts folder with *ctrlUI_lib*
Then, write and save this lines into your shelf

```
import IKFK_Builder
IKFK_Builder.showUI()
```

# AutoHand
![Alt Text](https://media.giphy.com/media/NYyDRYhQClclSwf4Fh/giphy.gif)
## Features 

For now very simple stuff but it could be very useful to create an usable hand with fingers control.

* Various length fingers
* Fingers controller creation with attributes to control them

P.S. Another rule: if you use what I call _supportJoint_ (watch gif second shot) please use this hierarchy

- Hand
    - Thumb
    - SupportJoint
        - other fingers

## To-Do list

* IK Hand - Actually it started all for this, to create automatically an IK Hand. This is my main goal
* Various hand builds - My objective was to build the human hand (five fingers) but could be useful have three, four or six fingers.

## How to install
Save *Auto_Hand* in your maya scripts folder
Then, write and save this lines into your shelf

```
import Auto_Hand
Auto_Hand.showUI()
```