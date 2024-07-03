# Euro 2024 Highlights Downloader

This is a very simple program that can be run on your machine to automatically download the latest Euro 2024 Highlights. Made due to the inavailability of proper Euro 2024 highlights in certain regions

## What does it do

### The Python Script

- The Python script scrapes YouTube using the `scrapetube` library to find the 20 latest videos from the Fox Soccer channel. It filters these videos to find all available highlights, cross-checks whether each video has been downloaded by checking a JSON file, and uses `pytube` to download any videos that have not yet been downloaded.

### The HTML Viewer

- The HTML file provides a simple interface to view downloaded videos. It reads the JSON file to list all the videos that have been downloaded so far and displays them in a user-friendly format accessible through a web browser.

## How to use it

### Python Script

1. **VPN Connection:**
    - If you are in a location where the highlights are unavailable, connect to a Japan-based VPN. You can obtain one from [VPN Gate](https://www.vpngate.net/EN/) and use [OpenVPN Connect](https://openvpn.net/client/) to connect to a Japan VPN server for free.
2. **Clone the Repository:**
    - Clone the repository to your desired directory using:
        
        ```bash
        git clone <repository_url>
        ```
        
3. **Set Up Virtual Environment:**
    
    **For Windows:**
    
    - Open Command Prompt or PowerShell and navigate to the project directory.
    - Create a virtual environment:
        
        ```bash
        python -m venv env
        ```
        
    - Activate the virtual environment:
        
        ```bash
        .\env\Scripts\activate
        ```
        
    
    **For Linux:**
    
    - Open Terminal and navigate to the project directory.
    - Create a virtual environment:
        
        ```bash
        python3 -m venv env
        ```
        
    - Activate the virtual environment:
        
        ```bash
        source env/bin/activate
        
        ```
        
4. **Install Dependencies:**
    - Once the virtual environment is activated, install the required dependencies:
        
        ```bash
        pip install -r requirements.txt
        ```
        
5. **Run the Python Script:**
    - Execute the Python script to download the videos:
        
        ```bash
        python download_videos.py
        ```
        

### HTML Viewer

1. **Run Python Live Server:**
    
    **For Windows:**
    
    - You can use the built-in `http.server` module to start a simple HTTP server. Navigate to the directory containing your HTML file and run:
        
        ```bash
        python -m http.server 8000
        ```
        
    
    **For Linux:**
    
    - Similarly, navigate to the directory containing your HTML file and run:
        
        ```bash
        python3 -m http.server 8000
        ```
        
2. **Access the Viewer:**
    - Open your web browser and go to http://localhost:8000 to view the downloaded highlights.

## Future Plans

- **Automation Script:**
    - Create a `.sh` script to automate the launching of the Python file every few hours. This can be done using a cron job on Linux or Task Scheduler on Windows.
