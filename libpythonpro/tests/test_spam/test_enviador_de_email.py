from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_email():
    enviador=Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'rnixonaf@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()

     resultado = enviador.enviar(
        destinatario,
        'rnixonaf123@gmail.com',
        'Curso PythonPro',
        'Turma Luciano Ramalho.'
    )

    assert destinatario in resultado
