# Flask Law Management API

A simple Flask application for managing county laws with CRUD operations. This project uses Flask, Flask-SQLAlchemy, and Flask-Marshmallow for API creation and data validation.

## Features

- **Create County Law**: Add a new county law.
- **Update County Law**: Modify an existing county law.
- **Read All Laws**: Retrieve a list of all county laws.
- **Error Handling**: Includes custom error handling for 404 and 500 errors.

## Requirements

- Python 3.6+
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- marshmallow
- logging

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure the application**:
    - Create a `config.py` file in the root directory with the following content:
      ```python
      class Config:
          SQLALCHEMY_DATABASE_URI = 'sqlite:///yourdatabase.db'
          SQLALCHEMY_TRACK_MODIFICATIONS = False
      ```

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Endpoints**:

    - **Create a County Law**:
      - **URL**: `/law/county/create`
      - **Method**: `POST`
      - **Request Body**:
        ```json
        {
          "title": "Law Title",
          "description": "Law Description",
          "content": "Law Content"
        }
        ```

    - **Update a County Law**:
      - **URL**: `/law/county/update/<int:law_id>`
      - **Method**: `PUT`
      - **Request Body** (fields are optional):
        ```json
        {
          "title": "Updated Title",
          "description": "Updated Description",
          "content": "Updated Content"
        }
        ```

    - **Read All County Laws**:
      - **URL**: `/law/county/read`
      - **Method**: `GET`
      - **Response**: 
        ```json
        [
          {
            "id": 1,
            "title": "Law Title",
            "description": "Law Description",
            "content": "Law Content",
            "law_type": "county",
            "status": "pending"
          }
        ]
        ```

## Error Handling

- **404 Not Found**: If the endpoint or resource is not found.
- **500 Internal Server Error**: For unexpected server issues.

## Contributing

Feel free to open an issue or submit a pull request if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
