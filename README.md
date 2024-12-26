# Card Sides Unifier PDF

Card Sides Unifier merges the front and back sides of a card into a single PDF file. It’s ideal for ID cards, driver's licenses, business cards, and similar items. The file format is PDF and A4 paper size is recommended.

## Usage

1. Locate `front-side.pdf` and `back-side.pdf` into `/pdf` directory as below.
```
project-root/
 ├─ ...
 └─ pdf/
     ├─ front-side.pdf
     └─ back-side.pdf
```

2. Build docker image and run container.
```
$ docker build -t card-sides-unifier . && docker run --rm -v "$PWD/pdf":/app/pdf card-sides-unifier
```

3. Generated `both-sides.pdf` will be located into `/pdf` directory as below.
```
project-root/
 ├─ ...
 └─ pdf/
     ├─ front-side.pdf
     ├─ back-side.pdf
     └─ both-sides.pdf   <-- generated file
```