# My Test App Instructions

## Setup

1. **Prepare the Environment:**
   - Create a `.env` file inside the `backend/backend` folder.
   - Add your PostgreSQL database details to this file.

2. **Configuration:**
   - In the HOST parameter, replace `localhost` with `my-postgres` before running your app in the container.

## Running the App

- Execute the following command to build and run the app:
  ```bash
  docker compose up --build

Frontend
Current Status:
The frontend does not have full implementation.
An authentication system is fully implemented.
All necessary Axios code to connect with backend endpoints for notes is written.

Backend

Complete Functionality:

The backend includes all required functionalities with API endpoints.
Testing:

Comprehensive tests are in place to ensure the backend operates correctly.

Containerization

I decided to use nginx to containerize my application in order to see it go 
to localhost:80 to see my application.