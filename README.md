<div align="center">

# SHOPEE VOUCHER AUTOMATION

_Automate your savings, seize every voucher opportunity!_

![last-commit](https://img.shields.io/github/last-commit/Danni4421/shopee-voucher-automation?style=flat&logo=git&logoColor=white&color=0080ff)
![repo-top-language](https://img.shields.io/github/languages/top/Danni4421/shopee-voucher-automation?style=flat&color=0080ff)
![repo-language-count](https://img.shields.io/github/languages/count/Danni4421/shopee-voucher-automation?style=flat&color=0080ff)

_Built with the tools and technologies:_

![Selenium](https://img.shields.io/badge/Selenium-43B02A.svg?style=flat&logo=Selenium&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Testing](#testing)

---

## Overview

**shopee-voucher-automation** is a developer-centric tool designed to automate the selection of vouchers in mobile applications, enhancing your shopping efficiency and experience.

**Why shopee-voucher-automation?**

This project aims to simplify the voucher application process while providing robust automation features. The core features include:

- 🎯 **Automated Voucher Selection:** Streamlines the process of selecting vouchers, saving time and reducing manual effort.
- ⏰ **Real-Time Clock Display:** Offers a dynamic view of the current time in WIB, ensuring timely actions.
- 🖥️ **User-Friendly GUI:** Intuitive interface built with Tkinter, accessible for users of all technical levels.
- 🛠️ **Flexible Environment Setup:** Dockerfile and Makefile ensure a consistent development environment, simplifying dependency management.
- 📱 **Integration with Appium:** Facilitates automated testing for mobile applications, improving testing efficiency and reliability.
- ⏳ **Countdown Timer:** Provides feedback on the timing of automation tasks, enhancing user experience.

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker

### Installation

Build shopee-voucher-automation from the source and install dependencies:

1. **Clone the repository:**

   ```sh
   ❯ git clone https://github.com/Danni4421/shopee-voucher-automation
   ```

2. **Navigate to the project directory:**

   ```sh
   ❯ cd shopee-voucher-automation
   ```

3. **Install the dependencies:**

**Using [docker](https://www.docker.com/):**

```sh
❯ docker build -t Danni4421/shopee-voucher-automation .
```

**Using [pip](https://pypi.org/project/pip/):**

```sh
❯ pip install -r requirements.txt
```

### Usage

Run the project with:

**Using [docker](https://www.docker.com/):**

```sh
❯ docker run -it danni4421/shopee-voucher-automation
```

**Using [pip](https://pypi.org/project/pip/):**

```sh
❯ python main.py
```

### Testing

Shopee-voucher-automation uses the **pytest** test framework. Run the test suite with:

**Using [docker](https://www.docker.com/):**

```sh
❯ docker run -it danni4421/shopee-voucher-automation pytest
```

**Using [pip](https://pypi.org/project/pip/):**

```sh
❯ pytest
```

---

[⬆ Return](#top)

---
