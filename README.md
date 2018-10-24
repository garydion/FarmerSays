![](https://github.com/garydion/FarmerSays/blob/master/art/praw.jpg)

# The Other End

Be sure to see the "entagled" page here for more supporting information of the twin unit:
https://github.com/topherCantrell/FarmerSays

# The Farmer Says

The first order of business I attacked was removing some of the mechanical hardware in the toy and installing a motor to spin the dial electrically.
![](https://github.com/garydion/FarmerSays/blob/master/art/IMG_0860.JPG)
Then I removed the control board and drilled small holes in order to bring sense/control wires out the back.
![](https://github.com/garydion/FarmerSays/blob/master/art/IMG_0862.JPG)
Here I'm showing how I mounted the Adafruit Feather HUZZAH with ESP8266 board at the edge of the case so I could plug in the USB mini connector for programming/charging.  This is the board I purchased:
https://www.adafruit.com/product/2821
![](https://github.com/garydion/FarmerSays/blob/master/art/IMG_0872.JPG)
The wires I soldered onto the board are shown here connected to a socket which holds an MCP23017.  You can get one here:
https://www.adafruit.com/product/732
![](https://github.com/garydion/FarmerSays/blob/master/art/IMG_0876.JPG)
Just another picture showing how I needed to bend the pins on the chip a little, as space was tight.
![](https://github.com/garydion/FarmerSays/blob/master/art/IMG_0877.JPG)
I followed the Adafruit guide on wiring the port expander to the Huzzah.  The guide is found here: https://learn.adafruit.com/using-mcp23008-mcp23017-with-circuitpython?view=all
![](https://github.com/garydion/FarmerSays/blob/master/art/IMG_0882.JPG)
The toy's mechanical construction is really quite inspiring to see.  I'm sure the designers had a blast coming up with the unique solotion.  I had to do a little creative reconstruction using string, super glue, and hot glue to mimic the behavior so that board would still work.
![](https://github.com/garydion/FarmerSays/blob/master/art/IMG_0885.JPG)
Showing the original return string re-purposed to pull the red arm back when the string is released.
![](https://github.com/garydion/FarmerSays/blob/master/art/IMG_0886.JPG)
And finally... It's hard to see here, but I installed an 18650 battery and a mosfet to control power to the motor.
![](https://github.com/garydion/FarmerSays/blob/master/art/IMG_0890.JPG)
