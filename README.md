# Raycast Game v1.1
This is the seccond version of the my pseudo 3D game based in raycast method, made with python and pygame and a lot of math!

# Instructions
Different from the first version, this game counts with two different windows. The first one'll have the 2D scene, and the seccond one'll have the 3D projection.

To play, you can move with W, S and turn arround with A, D.

# How to run the code
First of all, this code was tested on Windows, but problaby work on Linux.
You need to have Python installed and added to PATH.
You can download the files and run the code in git bash/linux terminal with the following sequence of commands:

```bash
# Clone the repository
git clone https://github.com/Zastetic/Raycast-game-v1.1.git

# Move to the game directory
cd Raycast-game-v1.1

# Create the virtual envirolment
python -m venv venv

# Enter in the virtual envirolment
source venv/Scripts/activate

# Install dependences
pip install -r requirements.txt
```

This game has two windows. One is the 2D version of the game, and the seccond one is the 3D projection of that scene.
In your first terminal, just run:

```bash
# To iniciate the 2D scene.
python raycastScene.py
```

Open another terminal, go to the directory of the project, activate the virtual envirolment with the previous steps, and run:
```bash
# To iniciate the 3D projection scene
python 3D_scene.py


