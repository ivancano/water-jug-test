# Water Jug Test

This repository contains a Flask web application that is containerized using Docker and orchestrated with Docker Compose. It provides a basic structure for building and running a Flask app in a containerized environment.

## Prerequisites

Before you can run Water Jug Test, make sure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ivancano/water-jug-test
   ```

2. Navigate to the project directory and run the command below

   ```bash
   docker-compose up
   ```

3. Open your web browser and visit http://localhost:5000 to access the application.

4. In order to use the API endpoint, use the url and parameters below:

GET http://localhost:5000?x={x}&y={y}&z={z}

Example: http://localhost:5000/api?x=5&y=4&z=3


5. To run tests using pytest, you must run command below in the root folder:

    ```bash
    pytest
    ```