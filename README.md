# PL Player and Stats

A full-stack web application to track Premier League player stats.  
The backend is built with **Spring Boot** and **PostgreSQL**, and the frontend uses **React**.

## Features

- View all players
- Filter players by team, position, nation, or name
- Add, update, and delete players via the API
- Fully connected frontend for live data display

## Backend

- Java 17, Spring Boot 3.1.2
- JPA / Hibernate
- PostgreSQL database
- API base URL: `http://localhost:8080/api/v1/player`

### Run Backend

```bash
cd Backend
mvn spring-boot:run
npm start