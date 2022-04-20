In order to clone this repository use the following command: 

```commandline
git clone --recurse-submodules https://github.com/hubmapconsortium/hubmap-translation.git
```

This repository relies on the Search-API as a submodule to function. The file `.gitmodules` contains the configuration
for the URL and specific branch of the Search-API that is to be used. After modifying this file or in order to pull
the latest changes from the Search-API repository, run the following command from the base directory:

```
git submodule update --init --force --remote
```