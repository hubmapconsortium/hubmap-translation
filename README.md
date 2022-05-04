# hubmap-translation

## Working with submodule

This repository relies on the Search-API as a submodule to function. The file `.gitmodules` contains the configuration
for the URL and specific branch of the Search-API that is to be used. Once you already have cloned this repository and switched to the target branch, to load the latest `search-api` submodule:

```
git submodule update --init --remote
```

## Docker build for development

```
cd docker
./docker-development.sh [check|config|build|start|stop|down]
```

## Docker build for deployment

```
cd docker
./docker-deployment.sh [start|stop|down]
```


