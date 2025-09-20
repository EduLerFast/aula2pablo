"""
Você recebeu duas listas:​
funcionariosParaCadastrar → contém vários dicionários, onde cada um guarda as informações de uma pessoa (nome, sobrenome, idade, altura e se possui habilitação).​
cadastrosParaEnviarParaOBanco → começa vazia e será usada para armazenar os objetos criados a partir dos dicionários.​


funcionariosParaCadastrar = [​

    {"nome": "Pablo", "sobrenome": "Araujo", "idade": 34, "altura": 1.71, "temHabilitacao": True},​
    {"nome": "Ana", "sobrenome": "Silva", "idade": 28, "altura": 1.65, "temHabilitacao": False},​
    {"nome": "Carlos", "sobrenome": "Souza", "idade": 40, "altura": 1.80, "temHabilitacao": True}​

]​

cadastrosParaEnviarParaOBanco = []​

​

Seu objetivo:​

Criar uma classe Pessoa que represente cada funcionário.​
Criar uma função de cadastro que percorra a lista funcionariosParaCadastrar, crie objetos da classe Pessoa e adicione-os na lista cadastrosParaEnviarParaOBanco.​
Criar uma função de salvar, que percorra a lista cadastrosParaEnviarParaOBanco e exiba a mensagem:​
“O usuário <nome> <sobrenome> foi salvo com sucesso.”​
"""






class funcionariosParaCadastrar:
    def __init__ (self,nome,sobrenome,idade,altura,TemHabilitacao)
        self.nome=nome
        self.sobrenome=sobrenome
        self.idade=idade
        self.altura=altura
        self.TemHabilitacao=TemHabilitacao

funcinario1=funcionariosParaCadastrar ('Pablo','Araujo','34','1.71',True)
funcinario2=funcionariosParaCadastrar ('ana','silva',28,1.65,False)
funcinario3=funcionariosParaCadastrar ('carlos','souza',40,1.81,True)


cadastrosParaEnviarParaOBanco = []