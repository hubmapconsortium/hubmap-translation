This repository relies on the Search-API as a submodule to function. The file `.gitmodules` contains the configuration
for the URL and specific branch of the Search-API that is to be used. After modifying this file or in order to pull
changes from the Search-API repository, run the following command from the base directory:

```
git submodule update --init --force --remote
```