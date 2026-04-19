import os
from icrawler.builtin import BingImageCrawler
from PIL import Image
import hashlib

POKEMONS = [
    "venonat", "paras", "nidoking", "vulpix",
    "ninetales", "golbat", "psyduck", "persian",
    "golduck", "primeape"
]

IMAGENS_POR_POKEMON = 120
DATASET_PATH = "dataset"

os.makedirs(DATASET_PATH, exist_ok=True)


def baixar_pokemon(nome):
    pasta = os.path.join(DATASET_PATH, nome)
    os.makedirs(pasta, exist_ok=True)

    print(f"\n📥 Baixando {nome}...")

    crawler = BingImageCrawler(storage={'root_dir': pasta})
    crawler.crawl(
        keyword=f"{nome} pokemon official artwork",
        max_num=IMAGENS_POR_POKEMON
    )


def limpar_imagens(pasta):
    print(f"🧹 Limpando {pasta}...")

    for img_nome in os.listdir(pasta):
        caminho = os.path.join(pasta, img_nome)

        try:
            with Image.open(caminho) as img:
                img.verify()
        except:
            os.remove(caminho)


def remover_duplicadas(pasta):
    print(f"🔁 Removendo duplicadas em {pasta}...")
    hashes = set()

    for img_nome in os.listdir(pasta):
        caminho = os.path.join(pasta, img_nome)

        try:
            with open(caminho, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            if file_hash in hashes:
                os.remove(caminho)
            else:
                hashes.add(file_hash)
        except:
            pass


def redimensionar(pasta, tamanho=(224, 224)):
    print(f"📏 Redimensionando {pasta}...")

    for img_nome in os.listdir(pasta):
        caminho = os.path.join(pasta, img_nome)

        try:
            with Image.open(caminho) as img:
                img = img.convert("RGB")
                img = img.resize(tamanho)
                img.save(caminho)
        except:
            pass


for pokemon in POKEMONS:
    baixar_pokemon(pokemon)
    pasta = os.path.join(DATASET_PATH, pokemon)

    limpar_imagens(pasta)
    remover_duplicadas(pasta)
    redimensionar(pasta)