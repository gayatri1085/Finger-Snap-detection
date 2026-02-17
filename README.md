# Finger Snap Detection

## Overview
Detects finger snaps through audio input and toggles media playback (e.g., Spotify, YouTube, Apple Music) using simulated key presses.

## Motivation
Gesture-based media control adds a touchless way to interact with apps using a simple snap.

## How It Works
- Captures microphone audio using PyAudio.
- Computes amplitude to detect when a snap occurs.
- Uses PyAutoGUI to send `playpause` key events.

## Demo
Add screenshots or a GIF here.

## Requirements
See `requirements.txt`

## Installation
```bash
pip install -r requirements.txt
