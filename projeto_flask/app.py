from flask import Flask,render_template, request, redirect, url_for

lista_produtos = [

    {"nome": "cocacola", "descricao": "veneno", "preco": "10pau", "imagem": "https://www.ze.delivery/_next/image?url=https%3A%2F%2Fcourier-images-prod.imgix.net%2Fproduc_variant%2F00011026_aa6c4325-5b4f-4b81-ab2a-7b757a58a025.jpg%3Fauto%3Dcompress%2Cformat%26fit%3Dmax%26w%3D540%26h%3D540%26dpr%3D2&w=3840&q=75" },
    {"nome": "doritos", "descricao": "suja mao", "preco": "20pau", "imagem": "https://superprix.vteximg.com.br/arquivos/ids/221097-600-600/7892840820060---Salgadinho-Doritos-Rock-in-Rio-Pizza-78G---1.jpg?v=638399962297430000" },
    {"nome": "agua", "descricao": "limpa mao", "preco": "30pau", "imagem": "https://images.tcdn.com.br/img/img_prod/1115696/agua_crystal_com_gas_pet_500ml_65_1_164e21ae3236fbad2542f59153aec538.png"}
   
]


app = Flask(__name__)

@app.route("/")
def home ():
    return render_template("home.html")


@app.route("/contato")
def contato ():
    return "<h1>Contato</h1>"


@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos = lista_produtos )

@app.route ("/produtos/<nome>")
def produto (nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return render_template ("produto.html" , produto=produto)
        

    return "Produto nao encontrado"


#GET
@app.route ("/produtos/cadastro")
def cadastro_produto():
    return render_template ("cadastro_produto.html")

#POST

#Aqui vamos pegar os dados que o usuario vai digitar (nome,descricao) e criar um novo produto na lista de produtos (em forma de dicionario)

@app.route ("/produtos" , methods=["POST"])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form ['descricao']
    preco = request.form['preco']
    imagem = request.form['imagem']
    produto = {"nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem }
    
    lista_produtos.append(produto)

    return redirect(url_for("produtos"))