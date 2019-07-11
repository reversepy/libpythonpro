import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_emai():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'rnixonaf@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'richardnixon@posteo.org',
        'Cursos python pro',
        'Primeira turma aberta'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','rnixonaf']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'richardnixon@posteo.org',
            'Cursos python pro',
            'Primeira turma aberta'
        )
        
