# Validador de CPF e CNPJ
from validador import Documento

exemplo_cpf = "15316264754"
exemplo_cnpj = "35379838000112"
documento = Documento.cria_documento(exemplo_cpf)
# print(documento)

# Validador de Telefone
from TelefonesBr import TelefonesBr

telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
# print(telefone_objeto)

# Buscador de Data
from data import DatasBr

cadastro = DatasBr()
# print(cadastro.dia_semana())
hoje = DatasBr()
# print(hoje.tempo_cadastro())

# Buscador de Endereco
from CEP import BuscaEndereco

cep = "21380010"
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)
