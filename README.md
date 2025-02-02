# SnipBox - Note Management API

SnipBox is a Django REST Framework-based API that allows users to save and manage short notes (snippets) with tags. The system features JWT authentication and provides comprehensive CRUD operations for managing snippets and tags.

## Features

- JWT Authentication
- CRUD operations for snippets
- Tag management with automatic deduplication
- Docker support for easy deployment

## Prerequisites

- Docker and Docker Compose
- Postman (for testing APIs)

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/Harikrishnanvc/SnipBox.git
cd snipbox
```

2. Create .env file:
```bash
cp .env.example .env
# Edit .env file with your configuration
```

3. Build and run using Docker Compose:
```bash
docker-compose up --build
```
## Create Super Admin
```
docker exec -it snipbox-web-1 python manage.py createsuperuser
```


The API will be available at `http://localhost:8000`

## API Documentation

Complete API documentation with examples, request/response formats is available in the Postman collection:
- Import `SnipBox.postman_collection.json` into Postman to access the full documentation
  or you can access through a public link : https://documenter.getpostman.com/view/19961502/2sAYX3riWR
- The collection includes environment setup, authentication flow, and detailed API examples

## Database Schema
The database schema diagram can be found in docs/schema.png

## Environment Variables

Create a `.env` file with the following variables:

```
DEBUG=True
SECRET_KEY=django-insecure-xy&jzx6q89(@y(ik5w7w@405^&6#_s4u+#50p3wtbxe=&tqv)g
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.