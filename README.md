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
Here is a gif made in ezgif of me moving the sensor up and down with the light responding.
![ezgif com-video-to-gif (1)](https://github.com/lwimber39/engr3/assets/143545399/e00f213b-2d1e-4775-8699-0219576597cb)

I used [ezgif](https://ezgif.com/) to make the gif.

### Wiring
Here is a wiring diagram of my circuit.

![image](https://github.com/lwimber39/engr3/assets/143545399/a0c640d0-751c-4baf-9519-c79843a69126)

I used [Tinkercad](https://www.tinkercad.com/) to make the diagram.

### Reflection
This assignment was particilarly challenging due to some technical difficulties which I still cannot explain. I got help from the teachers and my classmates with fixing the problem however it was Joshua who ended up fixing it somehow. I also had some problems regarding the neopixel itself as mine is unable to display green so I had to change it from going from red to green with blue in between to going from red to blue with violet in between. This assignment helped me get more used to CircuitPython and reminded me that I need to be very careful on how I do everything.

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

## Onshape_Assignment_Multi-Part_Cylinder

### Assignment Description

In this assignment I followed instructions to create multiple parts that all fit together in a specific way. After that I had to change certain parts of it to test if I had created the parts in an acceptable way.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/a6c20807-ff55-435d-bf5b-df98b557ac43)

This is the final studio from one of the top corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/3bad8ec6-6ad7-4953-ba16-aca97f4a3ea0)

This is the final studio from one of the bottom corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/805e6c49-7a2c-43b7-8421-27c28aa4f600)

This is a sketch that I used to make a revolve cut in the top cap.

### Part Link 

[Link to my Onshape document](https://cvilleschools.onshape.com/documents/61ad1ade7aa47242eb881324/w/200fe19712c06dc9ed2e4c11/e/6c05e63ae34996a2fdeb11c1?renderMode=0&uiState=653abe0bdaecb51902d29313).

### Reflection

This assignment was somewhat tricky because it has multiple interacting parts however most of them were relatively simple. One obstacle that seemed difficult but really wan't was making the bolts always stick out from the top and bottom caps by 15 millimeters because all it took was using an up to face extrude and two ofsets. One thing that I missed was at the end when the cylinder switched materials and I didn't notice so making sure to check anything that may have changed from one diagram to the next is important.

&nbsp;

## Onshape_Assignment_Single-Part_V-Block

### Assignment Description

In this assignment I followed instructions to create a V-block and edit some dimensions to see if I made it properly.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/d36213ba-8a8b-41c2-8fca-ae3e6824c295)

This is the final version of the V-block from one of the top corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/2a3541bc-b6e5-4499-9d4f-5fac085a1c28)

This is the final version of the V-block from one of the bottom corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/7d5d241b-5438-4962-9ede-57fcee3804d2)

This is the initial sketch I used to design the main outline of the V-block.

### Part Link 

[Link to my Onshape document](https://cvilleschools.onshape.com/documents/d9ddee7dac063bd730464108/w/e18bb8e7b271bf53d49d30fa/e/8faf3f2c078c19e059fec293?renderMode=0&uiState=6543f9c8b9ea18220db39906) (link may lead to 403 forbidden error. If so just copy the link adress).

### Reflection

This assignment was really not very hard considering I have already done things similar to it and it had no confusing angles or section views. I did learn something from it, although it didn't end up being useful in this assignment, which is that you can make versions for anything that has more than one question where you have to change variables, so you can easily go back if anything fails.

&nbsp;

## Onshape_CAD_Challenge_Alignment_Plate

### Assignment Description

In this assignment I used the CAD challenges Onshape app to use a diagram to create an alignment plate. I was also judged on time taken to complete the part and how many features I used to create it, and compared to how others performed.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/7c944fab-974e-485f-b83d-45f4d06eb9d7)

This is the alignment plate from one of the top corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/7c2b8b65-f264-4b2a-b6c9-c90187ed8f72)

This is the alignment plate from one of the bottom corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/65268799-301c-450d-9bc0-b37d5451b452)

This is the only sketch I used.

### Part Link 

[Link to my Onshape document](https://cvilleschools.onshape.com/documents/5e20a104017bfa7c51f03cc3/w/66a58d9fedb3d3ea308eb65a/e/5ea22348d5bb8b2427847207?renderMode=0&uiState=654d43deceb0b07951fbdc4c).

### Reflection

This assignment was extremely easy since it only took 3 features (could be 2 if you made the chamfer lines in the sketch) and I completed it in 7 minutes and 24 seconds even while looking over my work. I didn't really learn anything since I only used a sketch, extrude, and chamfer, but I don't use chamfers much so some practice couldn't hurt. 

&nbsp;

## Onshape_Assignment_Multi-Part_Mic_Stand

### Assignment Description

In this assignment I followed instructions to create a mic stand with multiple versions and an assembly to insert a screw.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/446f3657-da8f-498c-8fe4-7cadae880deb)

This is the final version of the mic stand from one of the top corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/3948b59c-6107-4933-a4fa-8782f554843f)

This is the final version of the mic stand from one of the bottom corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/ad2af5ce-b3e0-4aa4-9fb9-6a4970c7e3c7)

This is the sketch I used to make part of the mic holder.

### Part Link 

[Link to my Onshape document](https://cvilleschools.onshape.com/documents/26ba9313acc0d872aa5ccbe5/w/2a44363d6219e183d5812431/e/4411ac9dd478d07ed325a1b9?renderMode=0&uiState=654e92975ca28861232480af).

### Reflection

This assignment was somewhat difficult because it contained multiple parts, however none of them were super complicated. I did come across some trouble when trying to make a curve in the mic holder the same thickness all the way. To solve this you have to subtract the thickness you want from the outer curve's radius to get the inner curve's radius.

&nbsp;

## Onshape_Assignment_Assemblies_Locking_Pliers

### Assignment Description

In this assignment I followed instructions to put together pliers in an assemblies with multiple orientations to gather measurements.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/d237dd6b-61ad-4c78-b25e-b59c906599ba)

These are the pliers from one of the top corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/ef0f0ddf-3eaf-4cc1-ac5b-eaed99507bb6)

These are the pliers from one of the bottom corners.

![image](https://github.com/lwimber39/engr3/assets/143545399/5cd14cb7-b8a6-4dc4-ac94-e3eb773b0da1)

This shows the offset I used for the mate between the top handle and the screw.

### Part Link 

[Link to my Onshape document](https://cvilleschools.onshape.com/documents/33f3ba19a5a1d50c2eb84db9/w/c9efc5b03be6e90789bf88df/e/7c4e5a729625516c68c3b841?renderMode=0&uiState=656a45fedb4dd143170b2751).

### Reflection

This assignment was pretty easy overall because it was only in an assembly. It was a little difficult because I am not super used to the types of mates but it was nothing very complicated. One issue was with the parallel mate because some things can be parallel in multiple positions so you should keep in mind that you may have to move the parts to be in a position close to where you want it before you do the mate.

&nbsp;

## CircuitPython_Rotary_Encoder

### Description & Code Snippets
  The goal of this assignment was to get a LCD screen to display a menu with options that can be scrolled through and selected with a rotary encoder and have the neopixel react to it.

Make sure to print blank lines inbetween readings to clear the display like this:
```python
 lcd.set_cursor_pos(0,0)
    lcd.print("Push For: ")
    lcd.set_cursor_pos(1,0)
    lcd.print("          ")
    lcd.set_cursor_pos(1,0)
    lcd.print(menu[menu_index_lcd])

```

[**Link to my code**](https://github.com/lwimber39/engr3/blob/main/RotaryEncoder?scrlybrkr=8b87b4e9)


### Evidence!
Here is a gif made of me scrolling through each menu and selecting them.
![ezgif com-video-to-gif-converter](https://github.com/lwimber39/engr3/assets/143545399/309f3dbd-c531-4eb4-8839-1640a45115be)

I used [ezgif](https://ezgif.com/) to make the gif.

### Wiring
Here is a wiring diagram of my circuit.
![Screenshot (1)](https://github.com/lwimber39/engr3/assets/143545399/de4af623-85b3-48fd-94f8-48b164612fab)

I used [Tinkercad](https://www.tinkercad.com/) to make the diagram.

### Reflection
This assignment was pretty troublesome because I had so technical difficulties which made me have to start from scratch after getting some progress and I was still new to Circuitpython. I mainly used examples that I found online fron GitHub and the resources provided to me to learn how to code and wire the servo and buttons. This assignment has taught me how to run most basic functions in Circuitpython and how to use GitHub and find materials on it online. 
