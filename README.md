# pdf-to-img-example

Example to use this module 

A python (3.7+) module that wraps to convert PDF to a PIL Image object

## How to install

```sh
pip install pdf2image
```

for external lib reference named [poppler](https://github.com/oschwartz10612/poppler-windows/releases/).

### On Windows
add the bin/ folder to PATH or use poppler_path = r"C:\path\to\poppler-xx\bin" as an argument in convert_from_path.

### On MacOS

Mac users will have to install [poppler](https://poppler.freedesktop.org/).

Installing using [Brew](https://brew.sh/):

```sh
brew install poppler
```

### On Linux

Most distros ship with pdftoppm and pdftocairo. If they are not installed, refer to your package manager to install poppler-utils

#### Platform-independant (Using conda)
1. Install poppler: conda install -c conda-forge poppler
2. Install pdf2image: pip install pdf2image



reference : https://github.com/Belval/pdf2image

