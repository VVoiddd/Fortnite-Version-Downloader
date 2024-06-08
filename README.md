# Fortnite Version Downloader

Coded with ❤ by Void.

## 🌌 Overview

The **Fortnite Version Downloader** is a streamlined command-line utility designed to facilitate the downloading and archiving of various Fortnite versions spanning multiple seasons. Tailored for enthusiasts, historians, and gamers alike, this tool aims to provide an interactive experience, enabling users to dive into any version of Fortnite they desire.

## 🚀 Features

- **Intuitive Command-line Interface**: Navigate through options with ease.
- **Expansive Version Support**: From pre-Battle Royale to the latest season, we've got it all.
- **Integrated Download Manager**: Keep track of your downloads with a built-in progress bar.
- **Cosmic Purple Theme**: A space-themed design for those who love the cosmos.

## 🖥️ Usage

1. **Start**: Navigate to the directory containing the tool and run it using `python Launcher.py`.
2. **Select**: Choose your desired Fortnite season and its specific version from the given options.
3. **Destination**: Determine where you'd like to save the downloaded files.
4. **Download**: Sit back and watch as the selected version is downloaded.

## 🙏 Acknowledgements

A big thank you to the Fortnite community and everyone who supports the preservation of gaming history.

## Updates on 6/7/2024

### Enhancements

- **Improved User Experience**: Reduced lag when moving the window and added semi-transparency when resizing or moving the window for a smoother experience.

### Code Changes

- **Transparency Control**: Implemented functions to control window transparency during resizing and moving:
  - Added `make_transparent` function to make the window semi-transparent when resizing or moving.
  - Modified `make_opaque` function to remove the `event` parameter and adjusted the call inside `make_transparent` to use `after` correctly.

### README.md Update

- Added a section detailing the enhancements and code changes made on 6/7/2024.
- Updated the project description to reflect the latest improvements in user experience.
- Included acknowledgements to the Fortnite community and supporters of gaming history preservation.
