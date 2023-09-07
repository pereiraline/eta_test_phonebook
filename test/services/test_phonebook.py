from src.services.phonebook import Phonebook


class TestPhonebook:

    def test_add_invalid_name(self):
        #Setup
        service = Phonebook()
        invalid_name = 'Nome invalido'

        #Chamada
        resultado = service.add('POLICI!', 0)
        print(resultado)

        #Avaliação
        assert resultado == invalid_name

    def test_add_invalid_number(self):
        # Setup
        service = Phonebook()
        invalid_number = 'Numero invalido'

        # Chamada
        resultado = service.add('POLICIA', 0)

        # Avaliação
        assert resultado == invalid_number

    def test_add_contact(self):
        # Setup
        service = Phonebook()
        add_contato = 'Contato adicionado!'

        # Chamada
        resultado = service.add('DEFESA CIVIL', 199)

        # Avaliação
        assert resultado == add_contato

    def test_add_verify_name(self):
        # Setup
        service = Phonebook()
        verify_name = 'Impossívél adicionair. Contato já existe na lista!'
        service.add('SAMU', 192)

        # Chamada
        resultado = service.add('SAMU', 192)

        # Avaliação
        assert resultado == verify_name

    def test_lookup_invalid_name(self):
        service = Phonebook()
        invalid_name = 'Nome invalido'

        resultado = service.lookup('POLICI@')
        print(resultado)
        assert resultado == invalid_name

    def test_lookup_contact_exist(self):
        service = Phonebook()
        contact_exist = 'O contato é = POLICIA e o NUMERO = 190'

        resultado = service.lookup('POLICIA')
        print(resultado)

        assert resultado == contact_exist

    def test_lookup_contact_not_exist(self):
        service = Phonebook()
        contact_not_exist = 'Contato não cadastrado'

        resultado = service.lookup('BOMBEIRA')
        print(resultado)

        assert resultado == contact_not_exist

    def test_return_list_name(self):
        service = Phonebook()

        resultado = service.get_names()
        print(resultado)

    def test_return_list_number(self):
        service = Phonebook()

        resultado = service.get_numbers()
        print(resultado)

    def test_return_clear_phonebook(self):
        service = Phonebook()

        resultado = service.clear()
        print(resultado)

    def test_return_search_name(self):
        service = Phonebook()
        search_name = service.search('Pi')

        resultado = service.search('Pi')
        print(resultado)
        return resultado == search_name


    def test_get_phonebook_sorted(self):
        service = Phonebook()
        resultado = service.get_phonebook_sorted()
        print(resultado)

    def test_get_phonebook_reverse(self):
        service = Phonebook()
        resultado = service.get_phonebook_reverse()
        print(resultado)


    def test_delete_name_not_exist(self):
        service = Phonebook()
        not_delete_name = service.delete('Numero não existe!')
        service.add('Kassia', 123)

        resultado = service.delete('Kassi')
        print(resultado)

        assert resultado == not_delete_name

    def test_delete_name(self):
        service = Phonebook()
        delete_name = service.delete('Numero deletado')
        service.add('Kassia', 123)

        resultado = service.delete('Kassi')
        print(resultado)

        assert resultado == delete_name