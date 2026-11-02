# PSET 0: Ready Player One (The Dot)

**Course:** Computer Games Programming  
**Student:** Nicole Shekinah  

## Overview
This project is an introduction to Python 2D game development using the **Arcade** framework. It demonstrates frame updating, persistent state management, user input handling, time-aware movement, and boundary collision rules.

## Controls
- **WASD** or **Arrow Keys**: Move the player dot (Blue).

## Implementation Details
- **Persistent State**: Window class tracks player position `(x, y)` and target velocity `(target_dx, target_dy)`.
- **Time-Aware Movement**: Velocity is scaled by `delta_time` in `on_update` so object speed remains independent of display refresh rate.
- **Boundary Behavior**: Player is clamped to screen dimensions; the target dot bounces off screen edges by inverting velocity.

## How to Run
1. Ensure Python 3.12 is installed.
2. Activate the virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install arcade

   Run the application:
   ```bash
   python main.py

3. Commit and push the README to GitHub:
```powershell
git add README.md
git commit -m "Add project documentation in README"
git push