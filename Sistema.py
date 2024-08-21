# 1 - Pessoa fisica / 2 - Pessoa juridica / 3 - Sair
# 1 - Cadastrar Pessoa Física / 2 -  Listar Pessoa Física / 3 - Sair 
# 1 - Cadastrar Pessoa Juridica / 2 -  Listar Pessoa Juridica / 3 - Sair


from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica, PessoaJuridica
  

def main():

  lista_pf = []
  lista_pj = []

  while True:
    opcao = input('Escolha uma opção:\n1 - Pessoa Física\n2 - Pessoa Jurídica\n0 - Sair\n\nInsira aqui: ')
    if opcao == '1':
      while True: 
        opcao_pf = input('Escolha uma opção:\n1 - Cadastrar Pessoa Física\n2 - Listar Pessoa Física\n3 - Remover pessoa física\n4 - Atualizar Pessoa Física\n0 - Voltar\n\nInsira aqui: ')
        # 1 - Cadastrar uma Pessoa Física
        if opcao_pf == '1':
          nova_pf = PessoaFisica()
          novo_end_pf = Endereco()

          nova_pf.nome = input('Digite o nome da pessoa física: ')
          nova_pf.cpf = input('Digite o cpf da pessoa física: ').strip()
          nova_pf.rendimento = float(input('Digite o rendimento da pessoa física (somente números): '))

          data_nascimento = input('Digite a data de nascimento da pessoa física (dd/MM/aaaa): ')
          nova_pf.data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
          idade = (date.today() - nova_pf.data_nascimento).days // 365

          if idade >= 18:
            print('A pessoa tem mais de 18 anos')
          else:
            print('A pessoa tem menos de 18 anos. Retornando ao menu...')
            continue # Retorna ao inicio do loop

          novo_end_pf.logradouro = input('Digite o logradouro: ')
          novo_end_pf.numero = input('Digite o número: ')
          end_comercial = input('Este endereço é comercial? S/N: ').strip().upper()
          novo_end_pf.endereco_comercial = end_comercial == 'S'

          nova_pf.endereco = novo_end_pf

          lista_pf.append(nova_pf)

          print('Cadastro de pessoa física realizada!')

        # Listar pessoa física
        elif opcao_pf == '2':
          if lista_pf:
            for cada_pf in lista_pf:
              print(f'Nome: {cada_pf.nome}')
              print(f'CPF: {cada_pf.cpf}')
              print(f'Endereço: {cada_pf.endereco.logradouro} {cada_pf.endereco.numero}')
              print(f'Data Nascimento: {cada_pf.data_nascimento.strftime('%d/%m/%Y')}')
              print(f'Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}')
              print()
              print('Digite 0 para continuar')
              input()
          else:
            print('Não há pessoas fisicas cadastradas')
        
        elif opcao_pf == '3':
          if lista_pf:

            cpf_remover = input('Digite o cpf da pessoa desejada para remove-la da lista: ').strip()
            pessoa_encontrada = False

            for pf in lista_pf:
              if pf.cpf == cpf_remover:
                lista_pf.remove(pf)
                pessoa_encontrada = True
                print('Pessoa física removida com sucesso! Pressione qualquer tecla para voltar.')
                break

            if not pessoa_encontrada:
              print('Pessoa não encontrada. Pressione qualquer tecla para voltar.\n')

            input()
          else:
            print('Impossível realizar ação. Não há pessoas físicas registradas.\n')
        
        elif opcao_pf == '4':
          if lista_pf:

            cpf_atualizar = input('Digite o cpf da pessoa desejada para remove-la da lista: ').strip()
            pessoa_encontrada = False

            for pf in lista_pf:
              if pf.cpf == cpf_atualizar:
                pessoa_encontrada = True
                print('Pessoa Encontra! Selecione a informação que deseja atualizar:\n')
                print('1 - Nome\n2 - CPF\n3 - Data de nascimento\n4 - Rendimento\n5 - Logradouro\n6 - Número Logradouro\n7 - Endereco comercial\n0 - Cancelar Ação\n')

                opcao_pf_alt = input('Insira sua opção: ')

                if opcao_pf_alt == '1':
                  pf.nome = input('Digite o nome da pessoa física: ')
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pf_alt == '2':
                  pf.cpf = input('Digite o cpf da pessoa física: ').strip()
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pf_alt == '3':
                  try:
                    data_nascimento = datetime.strptime(input('Digite a data de nascimento da pessoa física (dd/MM/aaaa): ').strip(), '%d/%m/%Y').date()
                    idade = (date.today() - data_nascimento).days // 365

                    if idade >= 18:
                      pf.data_nascimento = data_nascimento
                      print('A pessoa tem mais de 18 anos. Continuando as alterações...')
                    else:
                      print('A pessoa tem menos de 18 anos. Impossivel continuar. Retornando...')
                      break # Retorna ao menu de pessoa fisica

                  except:
                    print('Um erro ocorreu com a idade. Retornando ao menu...')
                    break

                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pf_alt == '4':
                  pf.rendimento = float(input('Digite o rendimento da pessoa física (somente números): '))
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pf_alt == '5':
                  pf.endereco.logradouro = input('Digite o logradouro: ')
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pf_alt == '6':
                  pf.endereco.numero = input('Digite o número: ')
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pf_alt == '7':
                  end_comercial = input('Este endereço é comercial? S/N: ').strip().upper()
                  pf.endereco.endereco_comercial = end_comercial == 'S'
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pf_alt == '0':
                  print('Operação cancelada. Pressione qualquer tecla para voltar.')
                  break

                else:
                  print('Opção invalida. Pressione qualquer tecla para voltar.')
                  break

            if not pessoa_encontrada:
              print('Pessoa não encontrada. Pressione qualquer tecla para voltar.\n')

            input()
          else:
            print('Impossível realizar ação. Não há pessoas físicas registradas.\n')
          
        elif opcao_pf == '0':
          print('Voltando ao menu anterior')
          break

        else:
          print('Opção inválida, por favor digite uma das opções indicadas:')
    
    elif opcao == '2':
      while True: 
        opcao_pj = input('Escolha uma opção:\n1 - Cadastrar Pessoa Jurídica\n2 - Listar Pessoa Jurídica\n3 - Remover Pessoa Jurídica\n0 - Voltar\n\nInsira aqui: ')
        # 1 - Cadastrar uma Pessoa Jurídica
        if opcao_pj == '1':
          nova_pj = PessoaJuridica()
          novo_end_pj = Endereco()

          nova_pj.nome = input('Digite o nome da pessoa jurídica: ')
          nova_pj.cnpj = input('Digite o cnpj da pessoa jurídica: ')
          nova_pj.rendimento = float(input('Digite o rendimento da pessoa jurídica (somente números): '))
          nova_pj.nome_empresa = input('Digite o nome empresa da pessoa: ')

          novo_end_pj.logradouro = input('Digite o logradouro: ')
          novo_end_pj.numero = input('Digite o número: ')
          end_comercial = input('Este endereço é comercial? S/N: ').strip().upper()
          novo_end_pj.endereco_comercial = end_comercial == 'S'

          nova_pj.endereco = novo_end_pj

          lista_pj.append(nova_pj)

          print('Cadastro de pessoa jurídica realizada!')

        # Listar pessoa juridica
        elif opcao_pj == '2':
          if lista_pj:
            for cada_pj in lista_pj:
              print(f'Nome: {cada_pj.nome}')
              print(f'CNPJ: {cada_pj.cnpj}')
              print(f'Endereço: {cada_pj.endereco.logradouro} {cada_pj.endereco.numero}')
              print(f'Nome empresa: {cada_pj.nome_empresa}')
              print(f'Imposto a ser pago: {cada_pj.calcular_imposto(cada_pj.rendimento)}')
              print('Digite 0 para sair')
              input()
          else:
            print('Não há pessoas jurídicas cadastradas')

        elif opcao_pj == '3':
          if lista_pj:

            cnpj_remover = input('Digite o cnpj da pessoa desejada para remove-la da lista: ').strip()
            pj_encontrado = False

            for pj in lista_pj:
              if pj.cnpj == cnpj_remover:
                lista_pj.remove(pj)
                pj_encontrado = True
                print('Pessoa jurídica removida com sucesso! Pressione qualquer tecla para voltar.')
                break

            if not pj_encontrado:
              print('Pessoa não encontrada. Pressione qualquer tecla para voltar.\n')

            input()
          else:
            print('Impossível realizar ação. Não há pessoas jurídicas registradas.\n')
        
        elif opcao_pj == '4':
          if lista_pj:

            cnpj_atualizar = input('Digite o cnpj da pessoa desejada para remove-la da lista: ').strip()
            pj_encontrada = False

            for pj in lista_pj:
              if pj.cpj == cnpj_atualizar:
                pj_encontrada = True
                print('Pessoa Encontra! Selecione a informação que deseja atualizar:\n')
                print('1 - Nome\n2 - CNPJ\n3 - Data de nascimento\n4 - Rendimento\n5 - Logradouro\n6 - Número Logradouro\n7 - Endereco comercial\n0 - Cancelar Ação\n')

                opcao_pj_alt = input('Insira sua opção: ')

                if opcao_pj_alt == '1':
                  pj.nome = input('Digite o nome da pessoa física: ')
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pj_alt == '2':
                  pj.cpj = input('Digite o cnpj da pessoa física: ').strip()
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pj_alt == '3':

                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pj_alt == '4':
                  pj.rendimento = float(input('Digite o rendimento da pessoa física (somente números): '))
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pj_alt == '5':
                  pj.endereco.logradouro = input('Digite o logradouro: ')
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pj_alt == '6':
                  pj.endereco.numero = input('Digite o número: ')
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pj_alt == '7':
                  end_comercial = input('Este endereço é comercial? S/N: ').strip().upper()
                  pf.endereco.endereco_comercial = end_comercial == 'S'
                  print('Pessoa física atualizada com sucesso! Pressione qualquer tecla para voltar.')
                  break

                elif opcao_pf_alt == '0':
                  print('Operação cancelada. Pressione qualquer tecla para voltar.')
                  break

                else:
                  print('Opção invalida. Pressione qualquer tecla para voltar.')
                  break

            if not pj_encontrada:
              print('Pessoa não encontrada. Pressione qualquer tecla para voltar.\n')

            input()
          else:
            print('Impossível realizar ação. Não há pessoas físicas registradas.\n')
        
        elif opcao_pj == '0':
          print('Voltando ao menu anterior')
          break

        else:
          print('Opção inválida, por favor digite uma das opções indicadas:')

    elif opcao == '0':
      print('Programa encerrado. Obrigado por utilizar o sistema!')
      break

    else:
      print('Opção inválida, por favor digite uma das opções indicadas:')


if __name__ == '__main__':
  main() # Chama a função principal
