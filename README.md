# GalleryDL Social Media Post Downloader

A simple Python script that uses `gallery-dl` to download images and videos from various social media and image hosting websites.

## About

This project provides a straightforward command-line interface to download content from URLs supported by `gallery-dl`. It is designed for users who want a simple script to handle downloads without needing to remember the specific `gallery-dl` command-line options.

## Features

-   Easy to use: Just run the script with a URL.
-   Powered by `gallery-dl`: Supports all websites that `gallery-dl` supports.
-   Lightweight: A simple wrapper script around a powerful tool.

## Prerequisites

Before you begin, ensure you have the following installed:
-   [Python 3](https://www.python.org/downloads/)
-   [gallery-dl](https://github.com/gallery-dl/gallery-dl#installation): You can install it via pip:
    ```bash
    pip install gallery-dl
    ```

## Installation

1.  Clone this repository to your local machine:
    ```bash
    git clone https://github.com/murtaza550/GalleryDL-Social-Media-Post-Downloader.git
    ```
2.  Navigate to the cloned directory:
    ```bash
    cd GalleryDL-Social-Media-Post-Downloader
    ```

## Usage

Run the main script with the URL of the social media post you want to download:

```bash
python main.py <URL>
```

Replace `<URL>` with the actual URL of the post. The downloaded files will be saved in a folder named after the website and user/author within the script's directory.

## Supported Websites

This script supports all websites that `gallery-dl` supports. For a full list, please see the [official list of supported sites](https://github.com/gallery-dl/gallery-dl/blob/master/docs/supported-sites.md) on the `gallery-dl` GitHub repository.

## License

This project is open source and available under the [MIT License](LICENSE).
