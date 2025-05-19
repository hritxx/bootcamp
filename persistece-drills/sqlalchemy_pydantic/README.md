# SQLAlchemy + Pydantic Practice

This project provides comprehensive examples of using SQLAlchemy with Pydantic, progressing from beginner to advanced levels.

## Project Structure

The project demonstrates the integration of SQLAlchemy (an ORM for database operations) with Pydantic (a data validation library) to create robust data models and APIs.

## Data Models

The project includes the following data models:

### User-related Models

- **User**: Basic user information including name and email
- **UserEmailHistory**: Tracks changes to user email addresses
- **ProfileImage**: Stores user profile image information

### Content Models

- **Post**: User-generated content with title and content fields

### Financial Models

- **Account**: User account with balance information
- **Transfer**: Represents fund transfers between accounts

### Product Models

- **Product**: Product information including name, description, and price

## Schema Structure

Each model typically has several schema classes:

- **Base**: Contains core fields
- **Create**: Used for creation operations
- **Schema**: Full model representation with IDs and timestamps
- **Update**: Optional fields for update operations (where applicable)

## Features Demonstrated

- Pydantic validation with Field constraints
- Email validation using EmailStr
- ORM mode configuration for SQLAlchemy integration
- Optional fields for flexible API requests
- Relationship handling (e.g., Users with Posts)
- Financial transaction modeling
