from PyPDF2 import PdfReader

reader = PdfReader("dados/livreto_33_1_appai_clinicas.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[2]
text = page.extract_text()

list = [{
    'municipio': '',
    'especializacao': '',
    'nome': '',
    'endereco': '',
    'telefone': ''
}]

list2 = {}
municipios = ['ANGRA DOS REIS', 'ARARUAMA', 'BELFORD ROXO'
              , 'CABO FRIO', 'DUQUE DE CAXIAS', 'IGUABA GRANDE'
              , 'ITABORAI', 'ITAGUAI', 'MARICA'
              , 'MAGE', 'NILOPOLIS', 'MESQUITA'
              , 'NITEROI', 'NOVA FRIBURGO', 'NOVA IGUACU'
              , 'PATY DO ALFERES', 'PETROPOLIS', 'PARACAMBI'
              , 'QUEIMADOS', 'RIO BONITO', 'RIO DE JANEIRO'
              , 'SAO JOAO DE MERITI', 'SãO PEDRO DA ALDEIA', 'SAQUAREMA'
              , 'SEROPEDICA']

especializacao = ['CLINICA MEDICA', 'GERIATRIA', 'Radiologia',
                  'PATOLOGIA CLÍNICA', 'GINECOLOGIA', 'DOPPLER COLORIDO DE VASOS CERVICAIS ARTERIAIS BILATERAL (CARÓTIDAS E VERTEBRAS)',
                  'ALERGOLOGIA', 'NUTRIÇÃO', 'MAMOGRAFIA',
                  'ECOCARDIOGRAMA', 'ELETROCARDIOGRAMA', '',
                  'CARDIOLOGIA', 'OFTALMOLOGIA', 'HOLTER DE 24 HORAS 2 OU MAIS CANAIS ANALOGICO', 'ORTOPEDIA', 'MONITORIZACAO MAPA 24 HORAS', 'DENSITOMETRIA OSSEA'
                  , 'OTORRINOLARINGOLOGIA', 'DERMATOLOGIA', 'PEDIATRIA'
                  , 'ENDOCRINOLOGIA', 'FISIOTERAPIA', 'PSICOLOGIA'
                  , 'RADIOLOGISTA', 'GASTROENTEROLOGIA'
                  , 'UROLOGIA', 'REUMATOLOGIA', 'FONOAUDIOLOGIA'
                  , 'PNEUMOLOGIA', 'NEUROLOGIA', 'ULTRASSONOGRAFIA'
                  , 'ANGIOLOGIA', 'US – ARTICULAR (POR ARTICULAÇÃO)', 'AUDIOMETRIA TONAL LIMIAR COM TESTES DE DISCRIMINAÇÃO'
                  ,'MASTOLOGIA', 'VIDEO FARINGO-LARINSGOSCOPIA COM ENDOSCOPIO FLEXIVEL']  

def get_text_from_pdf():
    for x in range(0, number_of_pages):
        page = reader.pages[x]
        text = page.extract_text()
        list2[''] = text.split('\n')
        for municipio in municipios:
            list.append({
                'municipio': municipio,
                'especializacao': '',
                'nome': '',
                'endereco': '',
                'telefone': ''
            })
    return list2

get_text_from_pdf()
print(list2)