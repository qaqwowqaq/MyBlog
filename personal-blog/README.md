# Personal Blog Project

This is a personal blog project built using Flask for the backend and Vue 3 with TypeScript for the frontend. The application allows users to create, read, update, and delete blog posts, as well as manage user authentication and comments.

## Technology Stack

- **Backend**: Flask, MySQL
- **Frontend**: Vue 3, TypeScript
- **Database**: MySQL
- **Deployment**: Docker, Cloud Server

## Project Structure

```
personal-blog
├── backend
│   ├── app.py                  # Flask application entry point
│   ├── config.py               # Configuration file
│   ├── models                  # Data models
│   ├── routes                  # API routes
│   ├── services                # Business logic layer
│   ├── utils                   # Utility functions
│   ├── migrations              # Database migrations
│   ├── requirements.txt        # Backend dependencies
│   └── tests                   # Test files
├── frontend
│   ├── public                  # Public resources
│   ├── src                     # Frontend source code
│   ├── package.json            # Frontend dependencies
│   ├── tsconfig.json           # TypeScript configuration
│   └── vite.config.ts          # Vite configuration
├── docs                        # Project documentation
├── scripts                     # Deployment scripts
├── docker-compose.yml          # Docker configuration
├── .env.example                # Environment variable example
├── .gitignore                  # Git ignore file
└── README.md                   # Project README
```

## Features

- User authentication (registration, login, logout)
- CRUD operations for blog posts
- Commenting system for blog posts
- Responsive design for mobile and desktop
- Admin dashboard for managing posts and users

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd personal-blog
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Configure the database connection in `config.py`.
   - Run migrations to set up the database:
     ```
     flask db upgrade
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install dependencies:
     ```
     npm install
     ```
   - Start the development server:
     ```
     npm run dev
     ```

4. Deploy the application using Docker:
   ```
   docker-compose up --build
   ```

## Documentation

- [Requirements Analysis](docs/requirements.md)
- [Architecture Design](docs/architecture.md)
- [API Documentation](docs/api.md)

## License

This project is licensed under the MIT License.