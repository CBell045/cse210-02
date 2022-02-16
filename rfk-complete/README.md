# Greed
A game in which a player gets points by catching gems and looses points by hitting rocks. 

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 rfk 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- rfk                 (source code for game)
  +-- data              (data files for game)
  +-- game              (specific game classes)
    +-- casting         
      +-- actor         (Keeps track of appearences)
      +-- artifact      (Provides information about itself)
      +-- cast          (Keeps track of actors)
    +-- directing
      +-- director      
    +-- services
      +-- keyboard_service
      +-- video_service
    +-- shared
      +-- color
      +-- point
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* # TODO: Tyler Elms elmsy43@gmail.com
          Chad Bell bel19006@byui.edu
          Jonathan Mardo 
