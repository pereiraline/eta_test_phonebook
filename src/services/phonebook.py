class Phonebook:
    invalid_chars = ['#', '@', '!', '$', '%']
    invalid_name = 'Nome invalido'

    def __init__(self):
        self.entries = {'POLICIA': '190', 'SAMU': '192', 'BOMBEIRO': '193'}

    def is_valid_name(self, name):
        return all(char not in name for char in self.invalid_chars)

    #Melhoria - Novo metodo criado e reutilizado em metodos posteriores

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado' or
        'Impossívél adicionair. Contato já existe na lista!'
        """

        if not self.is_valid_name(name):
            return self.invalid_name

        """
        Para limpar o código e remover a quantidade exacerbada de IFs do código,
        eu declarei uma variavel invalid_char e atribui os caracteres não aceito
        ao adicionar um nome. Utilizei esta variavel dentro de um método
        def is_invalid_name e chamei este dentro do metodo def add para validar
        a adição de nomes invalidos.
        """

        if number <= 0:
            return 'Numero invalido'

    #Removir o len, validando apenas se o numero recebido é menor que 0

        if name not in self.entries:
            self.entries[name] = number

            return 'Contato adicionado!'
        else:
            return 'Impossívél adicionair. Contato já existe na lista!' #Melhoria no codigo, caso o contato já exista na lista

    #Correção ortografica das mensagens de retorno

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name or 'Nome invalido' or 'Contato não cadastrado'
        """
        if not self.is_valid_name(name):
            return self.invalid_name

        if name in self.entries.keys():
            return f'O contato é = {name} e o NUMERO = {self.entries[name]}'

        else:
            return 'Contato não cadastrado'

    #Melhoria - no ultimo return inseri um if e um else com mais uma validação com o resultado 'Contato não cadastrado'


    def get_names(self):
        """
        :return: return all names in phonebook
        """

        return list(self.entries.keys())


    #Converter dictionary para lista


    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """
        return list(self.entries.values())


    #Converter dictionary para lista


    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
                return result
        else:
            return "Não localizado"

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        return sorted(self.entries.items())

    #Inseri um sorted

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        """
        return sorted(self.entries.items(), reverse=True)

    #Inseri um sorted e um reverse = True

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        if name not in self.entries:
            return 'Numero não existe!'

        else:
            return 'Numero deletado'

    #Melhoria de codigo - dicionado um else para verificar se o numero buscado encontra-se na lista de contatos.
