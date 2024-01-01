import os
import sys
import time
sys.path.append('/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/arquivos_py')

import json

from utils.produc_encoder import ProductEncoder

dados = {
  "extensoes": [
    ".com",
    ".com.br",
    ".net",
    ".org",
    ".gov",
    ".app.br",
    ".art.br",
    ".com.br",
    ".dev.br",
    ".eco.br",
    ".emp.br",
    ".log.br",
    ".net.br",
    ".ong.br",
    ".seg.br",
    ".tec.br",
    ".edu.br",
    ".blog.br",
    ".flog.br",
    ".nom.br",
    ".vlog.br",
    ".wiki.br",
    ".adm.br",
    ".adv.br",
    ".arq.br",
    ".ato.br",
    ".bib.br",
    ".bio.br",
    ".bmd.br",
    ".cim.br",
    ".cng.br",
    ".cnt.br",
    ".coz.br",
    ".des.br",
    ".det.br",
    ".ecn.br",
    ".enf.br",
    ".eng.br",
    ".eti.br",
    ".fnd.br",
    ".fot.br",
    ".fst.br",
    ".geo.br",
    ".ggf.br",
    ".jor.br",
    ".lel.br",
    ".mat.br",
    ".med.br",
    ".mus.br",
    ".not.br",
    ".ntr.br",
    ".odo.br",
    ".ppg.br",
    ".pro.br",
    ".psc.br",
    ".qsl.br",
    ".rep.br",
    ".slg.br",
    ".taxi.br",
    ".teo.br",
    ".trd.br",
    ".vet.br",
    ".zlg.br",
    ".9guacu.br",
    ".abc.br",
    ".aju.br",
    ".anani.br",
    ".aparecida.br",
    ".barueri.br",
    ".belem.br",
    ".bhz.br",
    ".boavista.br",
    ".bsb.br",
    ".campinagrande.br",
    ".campinas.br",
    ".caxias.br",
    ".contagem.br",
    ".cuiaba.br",
    ".curitiba.br",
    ".feira.br",
    ".floripa.br",
    ".fortal.br",
    ".foz.br",
    ".goiania.br",
    ".gru.br",
    ".jab.br",
    ".jampa.br",
    ".jdf.br",
    ".joinville.br",
    ".londrina.br",
    ".macapa.br",
    ".maceio.br",
    ".manaus.br",
    ".maringa.br",
    ".morena.br",
    ".natal.br",
    ".niteroi.br",
    ".osasco.br",
    ".palmas.br",
    ".poa.br",
    ".pvh.br",
    ".recife.br",
    ".ribeirao.br",
    ".rio.br",
    ".riobranco.br",
    ".riopreto.br",
    ".salvador.br",
    ".sampa.br",
    ".santamaria.br",
    ".santoandre.br",
    ".saobernardo.br",
    ".saogonca.br",
    ".sjc.br",
    ".slz.br",
    ".sorocaba.br",
    ".the.br",
    ".udi.br",
    ".vix.br",
    ".agr.br",
    ".esp.br",
    ".etc.br",
    ".far.br",
    ".imb.br",
    ".ind.br",
    ".inf.br",
    ".radio.br",
    ".rec.br",
    ".srv.br",
    ".tmp.br",
    ".tur.br",
    ".tv.br",
    ".am.br",
    ".coop.br",
    ".fm.br",
    ".g12.br",
    ".gov.br",
    ".mil.br",
    ".org.br",
    ".psi.br",
    ".b.br",
    ".def.br",
    ".jus.br",
    ".leg.br",
    ".mp.br",
    ".tc.br"
  ]
}

def criar_dominios_mais_usados(dir, dados):
    with open(dir, 'w') as arquivo_json:
        json.dump(dados,
                arquivo_json,
                ensure_ascii=False,
                indent=2, cls=ProductEncoder
            )
    print("(OK!) Arquivo de dominios mais usados criado com sucesso!")

def criar_arquivo_json_dominios():
    dir = 'src/arquivos_jsons/dominios/'

    if not os.path.exists(dir):
        print("(OK!) Criando diretório...")
        time.sleep(3)
        os.makedirs(dir)
        print("(OK!) Diretório criado com sucesso!")
        criar_dominios_mais_usados(f'src/arquivos_jsons/dominios_mais_usados.json', dados)

    print("(OK!) Criando arquivos JSON...")
    time.sleep(3)
    for i in range(2, 27):
        with open(f'{dir}/dominios{i}.json', 'w') as json_file:
            json.dump(
                {"data_criacao": "", "dominios": []},
                json_file,
                ensure_ascii=False,
                indent=2, cls=ProductEncoder
            )
    print("(OK!) Arquivos JSON criados com sucesso!")


if __name__ == "__main__":
    criar_arquivo_json_dominios()
