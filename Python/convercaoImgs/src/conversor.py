from PIL import Image, XbmImagePlugin

def converterImgs(inImg, outImg):    
    imgCmpx = ['webp', 'pdf', 'ppm', 'eps', 'pcx', 'tga',
           'xbm', 'xpm', 'hdr', 'hdr', 'psd']
    
    img = ['bmp', 'gif', 'ico', 'jpeg', 'jpg', 'png',
           'tiff']

    try:       
        sliceImg = inImg.split('.')
        sliceImgR = sliceImg[0].replace('in', 'out')

        if sliceImg[1] in img and outImg in img:
            img = Image.open(inImg)
            img.save(f'{sliceImgR}.{outImg}')
            return {'status': 200, 'msg': 'Imagem convertida com sucesso!'}
        else:
            return {'status': 400, 'msg': 'Formato do arquivo não suportado!'}  
    except:
        print('Erro ao converter imagem!')

converterImgs("src/data-imgs/in/gustavo_vieira.gif", "bmp")
