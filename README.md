# Async CLI Image Downloader

A high-performance command-line tool written in Python, designed for concurrent image downloading from URL lists using asynchronous programming.

## Tech Stack
* Python 3
* Asyncio
* Aiohttp

## Key Features
* **Non-blocking CLI:** Implemented asynchronous user input in the console, allowing continuous URL entry without interrupting ongoing downloads.
* **High Concurrency:** Utilized `asyncio` and `aiohttp` for efficient parallel downloading and minimizing I/O bottlenecks.
* **Fault Tolerance:** Built-in resilience against network errors and timeouts to prevent execution crashes.
* **Summary Statistics:** Displays real-time download status and comprehensive final execution reports.

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the project directory:
   ```bash
   cd Async-CLI-Image-Downloader
   ```
3. Run the script:
   ```bash
   python main.py
   ```
