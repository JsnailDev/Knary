# Knary

This is a web application project that uses FastAPI as the backend and React as the frontend. The project aims to provide a simple and user-friendly interface for managing expenses.

## How to Fork and Contribute

If you want to fork this project and work on your own version, or contribute to this project and improve it, you can follow these steps:

1. Click on the Fork button on the top-right corner of this page. This will create a copy of this repository in your GitHub account.
2. Clone your forked repository to your local machine. You can use the command git clone https://github.com/<your-username>/<your-fork>.git or use a GUI tool like GitKraken or GitHub Desktop.
3. Create a new branch for your feature or bug fix. You can use the command git checkout -b <branch-name> or use a GUI tool.
4. Make your changes and commit them to your branch. You can use the command git commit -m "<commit-message>" or use a GUI tool.
5. Push your branch to your remote repository. You can use the command git push origin <branch-name> or use a GUI tool.
6. Create a pull request from your branch to the develop branch of this repository if you want to contribute, or to the main branch of this repository if you want to work on your own version. You can do this from the GitHub website or use a GUI tool.
7. Wait for your pull request to be reviewed and merged by the project maintainers if you are contributing, or enjoy your own version of the project if you are forking.

## How to Launch the Docker Compose

If you want to launch the project using Docker Compose, you can follow these steps:

1. Make sure you have Docker and Docker Compose installed on your machine. You can check the installation instructions [here](https://docs.docker.com/get-docker/) and [here](https://docs.docker.com/compose/install/).
2. Navigate to the root directory of the project where the docker-compose.yml file is located.
3. Run the command docker-compose up -d to build and run the containers for the backend, frontend, database, mail server, and cache services.
4. Wait for the containers to start and then visit http://localhost:3000 in your browser to see the frontend application.
5. You can also visit http://localhost:8000/docs in your browser to see the backend API documentation.
6. You can access the PostgreSQL database using any client tool with the following credentials: host: localhost, port: 5432, user: postgres, password: postgres, database: fastapi_react_project.
7. You can access the Maildev mail server using any web browser with the following URL: http://localhost:1080.
8. You can access the Redis cache using any client tool with the following credentials: host: localhost, port: 6379.
