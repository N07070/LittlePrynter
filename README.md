# Little Prynter
---

> Print out shit from the cloud.

## About

This project started when I got a Thermal Printer from a friend. I don't really know if you can do anything more, but I guess it's fun.


## Installation

To make this project work, you will need :
- [A Thermal Printer]( https://www.adafruit.com/product/597 )
- A Raspberry Pi
- Some electric wires.

Start by following the guide [here](https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi) to install the CUPS software needed to print images. You can also get some information from [here](https://learn.adafruit.com/mini-thermal-receipt-printer) and [here](https://learn.adafruit.com/instant-camera-using-raspberry-pi-and-thermal-printer) if you're stuck.

Then, setup the project :
```
git clone https://github.com/N07070/LittlePrynter
cd LittlePrynter
pip install -r requirements.txt
```
Now, edit `the users.json` and add a user. **Don't forget to remove the test user.**

You can now start the web server with

```
export FLASK_APP=littleprynter.py
flask run
```

Voilà !

## More
If you liked this project, feel free to support my work !

BTC : `1GYEiFSS7vbZXxDjKQavdaGsAEtvGjNWqb`

## Licence

```
LittlePrynter
   Copyright (C) 2018  N07070

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
