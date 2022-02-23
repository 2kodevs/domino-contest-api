# domino-contest-api

Project template for a Dominoes python player implementing an API required to interact with a Manager like program.

## How to run

This player is implemented using [FastApi](https://fastapi.tiangolo.com). To set it up execute from the project root:
```bash
$ uvicorn api:app --reload --port X
```
where `X` is an open and valid port

## Docker

The docker image can be built running:
```bash
$ docker build --build-arg GIT_HASH=${GIT_HASH::7} -t <TAG> .
```
replace  `<TAG>` with the desired image tag

After building the image, run the container with the following command:
```bash
$ docker run --rm <TAG>
```