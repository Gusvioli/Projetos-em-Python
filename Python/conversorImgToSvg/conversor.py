from PIL import Image

def converterImgs(rutaImg, rutaSvg):
    img = Image.open(rutaImg)
    img.save(rutaSvg)
    print("Imagen convertida con exito")

converterImgs("limpador.svg", "limpador.png")
