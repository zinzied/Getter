# Request Tester Application

## Overview

The Request Tester Application is a PyQt5-based GUI tool designed to facilitate the testing of HTTP GET and POST requests. This application allows users to send multiple requests to a specified URL, with configurable delay and optional port settings. It also provides real-time logging, progress tracking, and the ability to save logs to a file.

## Features

- **Send Multiple GET Requests**: Configure the number of GET requests and the delay between each request.
- **Send Multiple POST Requests**: Configure the number of POST requests, the delay between each request, and specify the POST body and headers.
- **Real-Time Logging**: View real-time logs of each request's status and response.
- **Progress Tracking**: Track the progress of the requests with a progress bar.
- **Save Logs**: Save the log output to a text file.
- **Clear All Fields**: Clear all input fields and logs with a single button click.
- **Dark Theme**: The application comes with a dark theme for better readability.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/zinzied/Getter.git
    cd Getter
    ```

2. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

    Ensure that `requirements.txt` includes:
    ```txt
    PyQt5
    requests
    ```

3. **Run the application**:
    ```sh
    python get.py
    ```

## Usage

1. **URL**: Enter the URL to which the requests will be sent.
2. **Number of Requests**: Specify the number of requests to be sent.
3. **Delay (ms)**: Enter the delay between each request in milliseconds.
4. **Port (optional)**: Optionally, specify a port number.
5. **POST Body**: Enter the body content for POST requests.
6. **POST Headers**: Enter the headers for POST requests in the format `key:value` per line.
7. **Start GET Requests**: Click this button to start sending GET requests.
8. **Start POST Requests**: Click this button to start sending POST requests.
9. **Stop Requests**: Click this button to stop the ongoing requests.
10. **Save Log**: Click this button to save the log output to a text file.
11. **Clear All**: Click this button to clear all input fields and logs.

## Screenshots

![image](https://github.com/user-attachments/assets/c887f054-eb61-4e25-a7a5-5b5bec1e4d2d)


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Credit

This project is Forked From joe-shenouda/Getter Thanks to him for let me pull requests and make some changes on it . 
---
