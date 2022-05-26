# Toy Robot

### Requirements

Just docker :)

## Installation

The Toy Robot CLI is run from a Docker container. To build the Docker image run:

```bash
docker build . -t toy_robot
```

## Running Toy Robot

To run the Toy Robot CLI simply run:

```bash
docker run -it toy_robot
```

To change the board size:

```bash
docker run -it -e CONFIG_FORCE_x_size=7 -e CONFIG_FORCE_y_size=8 toy_robot
```

## Testing

To run unit and integration tests inside the docker container run:

```bash
docker run --entrypoint=python toy_robot -m unittest -v tests/integration_tests/* tests/unit_tests/*
```

## Help

Help is provided in the application by typing the HELP command.