# UV-Flask User Management API

A simple Flask-based REST API for managing users with CRUD operations.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Project Structure](#project-structure)

## Overview

This project is a lightweight Flask application that provides a RESTful API for user management. It allows you to create, retrieve, and delete users with a simple in-memory storage system.

## Features

- Create new users with custom data
- Retrieve user information by ID
- Delete users by ID
- In-memory storage (data resets on server restart)
- Simple and clean REST API design
- Comprehensive test suite

## Requirements

- Python 3.13 or higher
- Flask 3.1.2 or higher
- pytest 8.4.2 or higher
- requests 2.32.5 or higher
- pytest-html 4.1.1 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd uv-flask
   ```

2. Install dependencies using [uv](https://github.com/astral-sh/uv):
   ```bash
   uv sync
   ```

## Usage

1. Start the Flask server:
   ```bash
   python main.py
   ```
   The server will start on `http://127.0.0.1:5000` in debug mode.

2. The API is now ready to accept requests.

## API Endpoints

### Create a User
- **URL**: `/users`
- **Method**: `POST`
- **Request Body**: JSON object with user data
- **Success Response**: `201 Created`
- **Example**:
  ```bash
  curl -X POST http://127.0.0.1:5000/users \
       -H "Content-Type: application/json" \
       -d '{"name": "John Doe", "email": "john@example.com"}'
  ```

### Get a User
- **URL**: `/users/<user_id>`
- **Method**: `GET`
- **Success Response**: `200 OK`
- **Error Response**: `404 Not Found`
- **Example**:
  ```bash
  curl -X GET http://127.0.0.1:5000/users/1
  ```

### Delete a User
- **URL**: `/users/<user_id>`
- **Method**: `DELETE`
- **Success Response**: `204 No Content`
- **Error Response**: `404 Not Found`
- **Example**:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/users/1
  ```

## Testing

The project includes a test suite using pytest:

1. Run the tests:
   ```bash
   pytest test.py
   ```

2. Generate an HTML report:
   ```bash
   pytest --html=report.html --self-contained-html
   ```

## Project Structure

```
uv-flask/
├── main.py              # Main Flask application
├── test.py              # Test suite for the API
├── mock_test.py         # Alternative tests using mock API
├── pyproject.toml       # Project configuration and dependencies
├── README.md            # This file
├── report.html          # Test report (generated)
└── assets/
    └── style.css        # CSS for test reports
```