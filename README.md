# Flask Application with JWT Authentication

This Flask application provides an API for managing county laws and voting on them, with JWT authentication for secure access.

## Features

- **Law Management**: Create and update county laws.
- **Voting**: Allow users to vote on laws.
- **JWT Authentication**: Secure routes with JSON Web Tokens (JWT).

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Marshmallow

## Installation

```bash

1. **Clone the Repository**

      ```bash
      git clone https://github.com/yourusername/your-repo.git
      cd your-repo
   
   

2. **Create a Virtual Environment**

   `bash
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate 


3. Install Dependencies

      bash

      pip install -r requirements.txt

4. Set Up Configuration

   Copy config.example.py to config.py and update with your own configuration.

      bash

      cp config.example.py config.py

   Make sure to set SECRET_KEY and JWT_SECRET_KEY in config.py.


5. Create the Database

      bash

      flask shell
      >>> from app import db
      >>> db.create_all()

