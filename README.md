# conan-libzip

Conan package for [libzip](https://libzip.org)

The packages generated with this **conanfile** can be found on [here](https://bintray.com/zimmerk/conan).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[ ![Download](https://api.bintray.com/packages/zimmerk/conan/libzip%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/libzip%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-libzip.svg?branch=release%2F1.5.1)](https://travis-ci.org/AtaLuZiK/conan-libzip)|[![Build status](https://ci.appveyor.com/api/projects/status/9sopts37dn0u350d/branch/release/1.5.1?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-libzip/branch/release/1.5.1)|

## Reuse the packages

### Basic setup

```
conan install libzip/1.5.1@zimmerk/stable
```

### Project setup

```
[requires]
libzip/1.5.1@zimmerk/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
