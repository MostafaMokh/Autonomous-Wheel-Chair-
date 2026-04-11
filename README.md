# Autonomous Wheelchair - Decision Module

This project is part of the Autonomous Wheelchair system.  
The purpose of this module is to make movement decisions based on obstacle distance detected by sensors.

## Features
- Stops wheelchair if obstacle is too close
- Slows down when obstacle is at medium range
- Moves normally when path is clear
- Handles invalid inputs safely

## Decision Logic
- Distance ≤ 20 cm → STOP
- Distance ≤ 50 cm → SLOW
- Distance > 50 cm → MOVE

## File Included
- `wheelchair_decision.py`

## Example Output
Input (cm) | Decision  
-----------|----------
15         | STOP  
35         | SLOW  
80         | MOVE  

## How to Run
```bash
python wheelchair_decision.py
```
