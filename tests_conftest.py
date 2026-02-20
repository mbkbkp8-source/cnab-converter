"""
Configuração de fixtures para testes
"""
import pytest


@pytest.fixture(scope="session")
def dados_teste():
    """Fixture com dados padrão para testes"""
    return {
        "cpf_valido": "12345678901",
        "cnpj_valido": "12345678000190",
        "email_valido": "usuario@email.com",
        "telefone_valido": "+5511987654321",
        "uuid_valido": "12345678-1234-1234-1234-123456789012",
    }