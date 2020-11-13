# Parking_Lot_System

Problem Statement:

We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.


To run the code you will need python 3.7
## Install python in mac:
```bash
brew install pipenv
```
```bash
pyenv install 3.7.3
```

## Install python in ubuntu:
```bash
sudo apt update
```
```bash
sudo apt install python3.7
```

## How to run:
If we are inside the ParkingLot folder
```bash
python3 parking_lot.py
```
Otherwise pass the whole path till parking_lot.py file.

## Description:

The parking_lot.py file reads the input file and parse the commands and executes them according to commands.
The parking.py file contains the logic of all the different operations, like parking & unparking car. Fetching out car details from driver age etc. It has collection of ParkingLot objects.
The lot.py file contains ParkingLot entity, having a unique slot id, empty boolean variable and a car entity.
The car.py file contains Car entity, having unique registration number and driver age.
