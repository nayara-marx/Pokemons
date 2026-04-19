from flask import Flask, request
import torch
from torchvision import transforms, models, datasets
from PIL import Image
import os

app = Flask(__name__)

# ========================
# CLASSES
# ========================
dataset = datasets.ImageFolder("dataset")
class_names = dataset.classes

# ========================
# MODELO
# ========================
model = models.resnet18(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))
model.load_state_dict(torch.load("modelo_pokemon.pth", map_location="cpu"))
model.eval()

# ========================
# TRANSFORMAÇÃO
# ========================
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# ========================
# DESCRIÇÕES
# ========================
descricoes = {
    "golbat": "Voa silenciosamente na escuridão, drenando energia de suas presas com suas presas afiadas.",
    "golduck": "Nada com incrível velocidade e usa poderes psíquicos misteriosos quando enfrenta grandes desafios.",
    "nidoking": "Um Pokémon extremamente poderoso que combina força bruta com ataques venenosos devastadores.",
    "ninetales": "Diz-se que cada uma de suas nove caudas possui um poder místico e que pode viver por mil anos.",
    "paras": "Controlado por um fungo parasita que cresce em suas costas, influenciando suas ações.",
    "persian": "Elegante e ágil, mas pode se tornar feroz e imprevisível quando provocado.",
    "primeape": "Sempre irritado, entra em fúria facilmente e persegue qualquer alvo até perder completamente o controle.",
    "psyduck": "Sofre de dores de cabeça constantes que liberam poderes psíquicos extraordinários quando ficam intensas.",
    "venonat": "Seus grandes olhos permitem enxergar no escuro, ajudando-o a detectar movimentos com precisão.",
    "vulpix": "Possui várias caudas encantadoras que crescem e se tornam mais elegantes à medida que envelhece."
}

# ========================
# ROTA
# ========================
@app.route("/", methods=["GET", "POST"])
def index():

    # ========================
    # QUANDO ENVIA IMAGEM
    # ========================
    if request.method == "POST":
        file = request.files.get("imagem")

        if not file:
            return "Envie uma imagem!"

        if not os.path.exists("static"):
            os.makedirs("static")

        caminho = "static/upload.jpg"
        file.save(caminho)

        img = Image.open(caminho).convert("RGB")
        img = transform(img).unsqueeze(0)

        with torch.no_grad():
            output = model(img)
            pred = torch.argmax(output, 1).item()

        classe = class_names[pred]
        descricao = descricoes.get(classe, "")

        # ========================
        # TELA RESULTADO
        # ========================
        return f"""
        <html>
        <head>
        <style>
        body {{
            background: #111;
            font-family: Arial;
            color: white;
            text-align: center;
        }}

        .pokedex {{
            background: #e3350d;
            width: 350px;
            margin: 50px auto;
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 0 30px rgba(0,0,0,0.8);
        }}

        .screen {{
            background: #222;
            padding: 15px;
            border-radius: 10px;
        }}

        img {{
            width: 200px;
            border-radius: 10px;
        }}

        h2 {{
            margin-top: 10px;
            font-size: 26px;
        }}

        p {{
            font-size: 16px;
            opacity: 0.9;
        }}

        a {{
            display: inline-block;
            margin-top: 15px;
            padding: 8px 15px;
            background: black;
            color: white;
            border-radius: 10px;
            text-decoration: none;
        }}
        </style>
        </head>

        <body>

        <div class="pokedex">
            <div class="screen">
                <img src="/static/upload.jpg">
                <h2>{classe.upper()}</h2>
                <p>{descricao}</p>
            </div>
            <a href="/">⬅ Voltar</a>
        </div>

        </body>
        </html>
        """

    # ========================
    # TELA INICIAL
    # ========================
    return """
    <html>
    <head>
    <style>
    body {
        background: linear-gradient(90deg, #6db3f2, #56ab2f);
        font-family: Arial;
        text-align: center;
    }

    .pokedex {
        width: 350px;
        background: #e6002e;
        margin: 100px auto;
        padding: 20px;
        border-radius: 25px;
        box-shadow: 0 0 25px rgba(0,0,0,0.5);
        color: white;
    }

    input {
        width: 100%;
        padding: 8px;
        margin-top: 10px;
        border-radius: 5px;
        border: none;
    }

    button {
        padding: 10px;
        margin-top: 10px;
        border: none;
        border-radius: 5px;
        background: black;
        color: white;
        cursor: pointer;
    }
    </style>
    </head>

    <body>

    <div class="pokedex">
        <h2>📟 Pokédex IA</h2>

        <form method="post" enctype="multipart/form-data">
            <input type="file" name="imagem">
            <button type="submit">Analisar</button>
        </form>
    </div>

    </body>
    </html>
    """

# ========================
# RUN
# ========================
if __name__ == "__main__":
    app.run(debug=True)