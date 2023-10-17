# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence
Pictures / Gifs of your finished work should go here.  You need to communicate what your thing does.
For making a GIF, I recommend [ezgif.com](https://www.ezgif.com) Remember you can insert pictures using Markdown or HTML to insert an image.

![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your Google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**



## CircuitPython_Servo

### Description & Code Snippets
  The goal of this assignment was to get a servo to sweep back and forth by pressing buttons. I accomplished this by use of my prior code knowledge, asking for help, and using libraries online.

Make sure to constrain your servo angle like this:
```python
while True:
    if btn.value:
        angle = angle + 2
        if angle > 180:
            angle = 180
        print(angle)
        servo.angle = angle
        time.sleep(0.01)

```

[**Link to my code**](https://github.com/lwimber39/engr3/blob/main/ServoButton.py)


### Evidence
Here is a gif made in ezgif of me sweeping the servo back and forth.
![ezgif com-video-to-gif](https://github.com/lwimber39/engr3/assets/143545399/11d9bf3a-7880-44f8-b4ad-d20da4ec89c7)

I used [ezgif](https://ezgif.com/) to make the gif.

### Wiring
Here is a wiring diagram of my circuit.
![Screenshot (1)](https://github.com/lwimber39/engr3/assets/143545399/de4af623-85b3-48fd-94f8-48b164612fab)

I used [Tinkercad](https://www.tinkercad.com/) to make the diagram.

### Reflection
This assignment was pretty troublesome because I had so technical difficulties which made me have to start from scratch after getting some progress and I was still new to Circuitpython. I mainly used examples that I found online fron GitHub and the resources provided to me to learn how to code and wire the servo and buttons. This assignment has taught me how to run most basic functions in Circuitpython and how to use GitHub and find materials on it online. 

## CircuitPython_Distance_Sensor

### Description & Code Snippets
This assignment has a distance sensor and depending on the distance read it changes color from red to blue. I did this by use of help from teachers and my peers as well as previous knowledge.

Make sure to use else ifs as shown here:

```python
        if dist < 5:
            pixels.fill((255, 0,0))
            pixels.show()
        elif dist > 5 and dist < 20:
            pixels.fill((255, 0, (dist - 5 / 15 * 255)))
            pixels.show()
        elif dist > 20 and dist < 35:
            pixels.fill((255-(dist - 5 / 15 * 255), 0, 255))
            pixels.show()
        elif dist > 35:
            print(">35")
            pixels.fill((0, 0, 255))
            pixels.show()   

```

[**Link to my code**](https://github.com/lwimber39/engr3/blob/main/TEst)

### Evidence

### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)
### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**

## Onshape_Assignment_Hanger

### Assignment Description

In this assignment I made a hanger part based on schematics. I had to precisely follow the directions in order to get the proper mass.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/ce5983fb-655b-4a6b-b306-6174b6d01190)
This is the hanger from one of the top corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/70e56e66-c97b-43f6-a1c6-fcf38bda4551)
This is the hanger from one of the bottom corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/31d20660-9db0-4682-b315-2c64af9c8277)
This is the original sketch of the part.

### Part Link 

[Link to my Onshape document](https://cvilleschools.onshape.com/documents/111df3ee3bbfcd71a657e772/w/fd37c28187c700c133386fe5/e/a8050e2f6efa20835f3a326c?renderMode=0&uiState=65259f9358b9cc41d101bcc4).

### Reflection

This assignment was overall not very difficult however there were some slight struggles. One simple struggle was just the fact that I had not used Onshape in some time so I had to get back into it. Something important I learned is that when mirroring it does not continue mirroring things after the mirror is created. This means that if you part is symmetrical you should mirror as late as possible so that it mirrors most if not all of the part.

&nbsp;

## Onshape_Assignment_Swing_Arm

### Assignment Description

In this assignment I made a swing arm based on schematics. I had to make two variants and get the correct mass for each.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/ee4a2d19-9fce-410e-bc7d-96fd450b8d00)

This is the swing arm from one of the top corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/3fca4e4e-fd96-4572-a596-f195812ce659)

This is the swing arm from one of the bottom corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/656bb1ed-999a-435c-b56d-aaaf5f6d1653)

This is the original sketch of the part.

### Part Link 

[Link to my Onshape document](https://cvilleschools.onshape.com/documents/a75db3b22fd9a12045b6c124/w/990fe5e1c0ae326054140db8/e/a8963720870de959ef2da54c?renderMode=0&uiState=6525a65839441a63fa082bf4).

### Reflection

This assignment was much harder that the hanger for multiple reasons. Firstly the instructions were much more complicated with multiple confusing cross sections. It also has two variants with variable that could break your whole part. Something important I learned is to make sure you thoroughly look at the instructions to make sure you don't miss any nkey parts such as how in the swing are the middle is actually extruded and not a hole.

&nbsp;
