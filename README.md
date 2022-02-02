# Project Astrios
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
<img src="https://img.shields.io/badge/version-v1.0-red">

A Virtual Assistant that is capable of doing some basic things.

## Installation

- Download [`Chrome`](https://www.google.com/chrome/)/[`Chromium`](https://www.chromium.org/getting-involved/download-chromium/) and [`Chromedriver`](https://chromedriver.chromium.org/home).
    - Make sure the version of Chromedriver and Chrome/Chromedriver supports each other.
- Download the latest release from [here](https://github.com/Indominus-Rexian/Project-Astrios/releases).
- Install the dependencies using pip.
    - ```bash
         pip install -r requirements.txt
      ```   
- Run `ai.py`.
    - ```bash
         python ai.py
      ``` 
## Working

The Assistant uses Brainshop to reply. But there are some fields where it does specific work.

- ## Fields
    - Showing Google Results
        - If you say something that starts from `search google` for ex. `search google meaning of hello` it will automatically search and open the first URL.
        - The opening URL feature is somewhat dangerous considering it can sometime open malicious website, I might change this feature in the following updates.
    - Showing Youtube Content
        - You can view YouTube content by saying something that starts from `search youtube for` or `search on youtube`. For ex., `search youtube for minecraft memes` or `search on youtube minecraft memes`- It will download the first video and open a new Window(Custom Video Player) where you can view your video.
    - Shutdown
        - If you just say `close` or `shutdown`, It will automatically close itself after 3 seconds.
                

