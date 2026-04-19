<h1 align="center">
  🔴 Pokédex com Inteligência Artificial
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
</p>

<p align="center">
  Uma Pokédex inteligente capaz de identificar Pokémons a partir de imagens utilizando <strong>Inteligência Artificial</strong> e <strong>Visão Computacional</strong>.
</p>

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Tecnologias](#-tecnologias)
- [Funcionalidades](#-funcionalidades)
- [Pokémons Suportados](#-pokémons-suportados)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Modelo de IA](#-modelo-de-ia)
- [Interface](#-interface)
- [Aprendizados](#-aprendizados)

---

## 🎯 Sobre o Projeto

Este projeto é uma **Pokédex com IA** — uma aplicação web que utiliza uma rede neural convolucional treinada com PyTorch para identificar Pokémons a partir de imagens enviadas pelo usuário.

O sistema combina:
- 🤖 **Inteligência Artificial** — modelo ResNet18 adaptado e treinado do zero
- 👁️ **Visão Computacional** — reconhecimento de padrões visuais em imagens
- 🌐 **Desenvolvimento Web** — interface com Flask, HTML e CSS

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python | Linguagem principal |
| PyTorch | Treinamento do modelo de IA |
| ResNet18 | Arquitetura da rede neural (transfer learning) |
| Flask | Backend e servidor web |
| HTML/CSS | Interface inspirada na Pokédex |

---

## ✨ Funcionalidades

- 📤 Upload de imagem pelo usuário
- 🔍 Identificação do Pokémon via IA
- 📝 Exibição do nome e descrição do Pokémon identificado
- 🖼️ Visualização da imagem enviada com o resultado
- 🎨 Interface temática inspirada na Pokédex clássica

---

## 🎮 Pokémons Suportados

O modelo foi treinado para identificar **10 Pokémons diferentes**, organizados em um dataset de imagens por classe.

> 💡 *Liste aqui os 10 Pokémons do seu dataset!*
> Exemplo: Pikachu, Charmander, Bulbasaur, Squirtle, Mewtwo...

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.8+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/nayara-marx/agendamento.git
cd agendamento

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Executando a aplicação

```bash
python app.py
```

Acesse no navegador: `http://localhost:5000`

### Como identificar um Pokémon

1. Abra a aplicação no navegador
2. Clique em **"Enviar Imagem"**
3. Selecione uma foto de um Pokémon
4. Aguarde o processamento
5. Veja o resultado com o nome e descrição do Pokémon identificado! ✅

---

## 📁 Estrutura do Projeto

```
📦 pokedex-ia/
├── 📂 dataset/          # Imagens organizadas por classe (Pokémon)
│   ├── pikachu/
│   ├── charmander/
│   └── ...
├── 📂 static/           # Arquivos CSS e imagens da interface
├── 📂 templates/        # Templates HTML
├── 📄 app.py            # Aplicação Flask
├── 📄 model.py          # Definição e carregamento do modelo
├── 📄 train.py          # Script de treinamento
├── 📄 requirements.txt  # Dependências
└── 📄 README.md
```

---

## 🧠 Modelo de IA

O modelo utiliza **Transfer Learning** com a arquitetura **ResNet18**, uma rede neural convolucional (CNN) pré-treinada no dataset ImageNet.

**Pipeline de treinamento:**
1. Coleta e organização do dataset por classes
2. Pré-processamento e augmentação das imagens
3. Fine-tuning da ResNet18 para as 10 classes de Pokémons
4. Avaliação e exportação do modelo treinado

```
Imagem → Pré-processamento → ResNet18 → Classificação → Pokémon identificado
```

---

## 🎨 Interface

A interface foi desenvolvida com visual temático da Pokédex clássica, com:
- Layout responsivo em HTML e CSS
- Exibição da imagem enviada pelo usuário
- Resultado da classificação com nome e descrição do Pokémon
- Design inspirado no universo Pokémon 🔴

---

## 📌 Aprendizados

Este projeto proporcionou experiência prática em:

- ✅ Machine Learning aplicado a imagens
- ✅ Treinamento de modelos com PyTorch
- ✅ Transfer Learning com ResNet18
- ✅ Integração entre IA, backend (Flask) e frontend
- ✅ Organização de projeto e versionamento com Git/GitHub

---

## 👩‍💻 Participantes:

- Hugo Batista
- João
-Nayara
-Stela
-Thiago

```bash

