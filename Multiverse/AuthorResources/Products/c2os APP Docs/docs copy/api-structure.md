# API Structure

This document outlines the API structure for the Cadence Cornerstone OS application.

## API Versioning

All API endpoints are versioned using path-based versioning, with the current version being `v1`. This ensures backward compatibility as the API evolves.

Example: `/api/v1/tasks`

## Authentication

All API endpoints (except public endpoints and webhooks) require authentication using Supabase Auth. The authentication is handled by cookies that are set during the login process.

## Core API Endpoints

### Health Check

- **GET** `/api/v1/health`
  - Returns the status of the API
  - Does not require authentication

### Tasks

- **GET** `/api/v1/tasks`
  - Retrieves all tasks for the authenticated user
  - Supports filtering by status, due date, etc.

- **POST** `/api/v1/tasks`
  - Creates a new task
  - Required fields: `title`
  - Optional fields: `description`, `due_date`, `status`, etc.

- **GET** `/api/v1/tasks/:id`
  - Retrieves a specific task by ID

- **PUT** `/api/v1/tasks/:id`
  - Updates a specific task
  
- **DELETE** `/api/v1/tasks/:id`
  - Deletes a specific task

### Projects (Planned)

- **GET** `/api/v1/projects`
- **POST** `/api/v1/projects`
- **GET** `/api/v1/projects/:id`
- **PUT** `/api/v1/projects/:id`
- **DELETE** `/api/v1/projects/:id`

### Goals (Planned)

- **GET** `/api/v1/goals`
- **POST** `/api/v1/goals`
- **GET** `/api/v1/goals/:id`
- **PUT** `/api/v1/goals/:id`
- **DELETE** `/api/v1/goals/:id`

## Webhook Endpoints

### GoHighLevel

- **POST** `/api/webhooks/ghl`
  - Receives webhook events from GoHighLevel
  - Does not require user authentication, but validates using a webhook secret
  - Handles events like `location.subscription.created`, `location.subscription.updated`, etc.

## Response Format

All API responses follow a standard format:

### Success Response

```json
{
  "data": {
    // Response data here
  },
  "message": "Optional success message"
}
```

### Error Response

```json
{
  "error": "Error message",
  "code": "Optional error code"
}
```

## Error Codes

- `401` - Unauthorized (authentication required)
- `403` - Forbidden (insufficient permissions)
- `404` - Resource not found
- `422` - Validation error
- `500` - Internal server error 