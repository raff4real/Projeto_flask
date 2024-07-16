from flask import render_template, request, redirect, url_for
from validate_docbr import CPF, CNPJ
import random

cpf = CPF()
cnpj = CNPJ()

def generate_random_cpf():
    return cpf.generate()

def generate_random_cnpj():
    return cnpj.generate()

def validate_cpf(cpf_input):
    return cpf.validate(cpf_input)

def validate_cnpj(cnpj_input):
    return cnpj.validate(cnpj_input)

from . import create_app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_cpf')
def gerar_cpf():
    generated_cpf = generate_random_cpf()
    return render_template('resultado.html', documento=generated_cpf, tipo='CPF')

@app.route('/gerar_cnpj')
def gerar_cnpj():
    generated_cnpj = generate_random_cnpj()
    return render_template('resultado.html', documento=generated_cnpj, tipo='CNPJ')

@app.route('/validar_cpf', methods=['GET', 'POST'])
def validar_cpf():
    if request.method == 'POST':
        cpf_input = request.form['cpf']
        is_valid = validate_cpf(cpf_input)
        return render_template('resultado.html', documento=cpf_input, tipo='CPF', valido=is_valid)
    return render_template('validar_cpf.html')

@app.route('/validar_cnpj', methods=['GET', 'POST'])
def validar_cnpj():
    if request.method == 'POST':
        cnpj_input = request.form['cnpj']
        is_valid = validate_cnpj(cnpj_input)
        return render_template('resultado.html', documento=cnpj_input, tipo='CNPJ', valido=is_valid)
    return render_template('validar_cnpj.html')