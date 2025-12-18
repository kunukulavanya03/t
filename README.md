# t

Backend API for t

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Designecommerceproductui.git))

## Project Structure

```
t/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User registration
- User login
- Password reset
- Data creation
- Data updating
- Data deletion

## API Endpoints

- `POST /api/register` - Register a new user
- `POST /api/login` - Login an existing user
- `POST /api/password_reset` - Reset a user's password
- `GET /api/data` - Get a list of user's data
- `POST /api/data` - Create new data
- `PUT /api/data/{id}` - Update existing data
- `DELETE /api/data/{id}` - Delete existing data

## License

MIT
