

from codigo.bytebank import Funcionario


class TestClass:
    
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        
        entrada = '13/03/2000' # Given-Contexto
        
        esperado = 23
        
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        
        
        resultado = funcionario_teste.idade() # When-ação
        
        assert resultado == esperado # Then-desfecho
        
    def test_quando_sobrenome_recebe_Lucas_Silva_deve_retornar_apenas_Silva(self):
        
        entrada = 'Lucas Silva'
        esperado = 'Silva'
        
        funcionario_teste = Funcionario(entrada, '13/03/2000', 1111)
        
        
        resultado = funcionario_teste.sobrenome() # When-ação
        
        assert resultado == esperado # Then-desfecho
        
    def test_quando_decrescimo_salario_recebe_100_mil_deve_retornar_90000(self):
        entrada_salario = 100000 #given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        
        
        
        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() #when 
        resultado = funcionario_teste.salario 
        
        assert resultado ==  esperado
        
        
            