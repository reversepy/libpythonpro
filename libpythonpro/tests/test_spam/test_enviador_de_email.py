from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_email():
    enviador=Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado=enviador.enviar(
        'rnixonaf@gmail.com',
        'rnixonaf123@gmail.com',
        'Curso PythonPro',
        'Turma Luciano Ramalho.'
    )
    assert  'rnixonaf@gmail.com' in resultado
