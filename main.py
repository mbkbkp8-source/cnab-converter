"""
Script principal para conversão de CNAB 240 BB para Banco Inter Pix
"""
import sys
from cnab_converter.conversor import ConversorCNAB
from cnab_converter.models import (
    PagamentoPix, EmpresaInfo, TipoChavePix, TipoDocumento, TipoConta
)


def exemplo_conversao_manual():
    """Exemplo de uso: conversão com dados inseridos manualmente"""
    print("=" * 70)
    print("EXEMPLO 1: Conversão Manual de Pagamentos Pix")
    print("=" * 70)
    
    # Definir informações da empresa
    empresa = EmpresaInfo(
        tipo_documento=TipoDocumento.CNPJ,
        cpf_cnpj="12345678000190",
        nome="EMPRESA TESTE LTDA",
        agencia="00001",
        dv_agencia="9",
        conta="0000000001",
        dv_conta="2",
        logradouro="RUA DAS FLORES",
        numero="123",
        complemento="SALA 10",
        cidade="SAO PAULO",
        cep="01234",
        cep_complemento="567",
        estado="SP"
    )
    
    # Criar pagamentos Pix
    pagamentos = [
        # Pagamento com Pix por CPF
        PagamentoPix(
            tipo_chave_pix=TipoChavePix.CPF_CNPJ,
            chave_pix="12345678901",
            nome_beneficiario="JOAO DA SILVA",
            cpf_cnpj_beneficiario="12345678901",
            tipo_documento_beneficiario=TipoDocumento.CPF,
            tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
            ispb_beneficiario="12345678",
            valor=1000.50,
            data_pagamento="20022026"
        ),
        # Pagamento com Pix por Email
        PagamentoPix(
            tipo_chave_pix=TipoChavePix.EMAIL,
            chave_pix="maria@email.com",
            nome_beneficiario="MARIA DOS SANTOS",
            cpf_cnpj_beneficiario="98765432100",
            tipo_documento_beneficiario=TipoDocumento.CPF,
            tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
            ispb_beneficiario="87654321",
            valor=2500.00,
            data_pagamento="20022026"
        ),
        # Pagamento com Pix por Telefone
        PagamentoPix(
            tipo_chave_pix=TipoChavePix.TELEFONE,
            chave_pix="+5511987654321",
            nome_beneficiario="PEDRO OLIVEIRA",
            cpf_cnpj_beneficiario="55555555555",
            tipo_documento_beneficiario=TipoDocumento.CPF,
            tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
            ispb_beneficiario="11111111",
            valor=750.25,
            data_pagamento="20022026"
        ),
        # Pagamento com Chave Aleatória
        PagamentoPix(
            tipo_chave_pix=TipoChavePix.ALEATORIA,
            chave_pix="12345678-1234-1234-1234-123456789012",
            nome_beneficiario="CARLOS FERREIRA",
            cpf_cnpj_beneficiario="11111111111",
            tipo_documento_beneficiario=TipoDocumento.CPF,
            tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
            ispb_beneficiario="99999999",
            valor=3200.75,
            data_pagamento="20022026"
        ),
        # Pagamento com Dados Bancários
        PagamentoPix(
            tipo_chave_pix=TipoChavePix.DADOS_BANCARIOS,
            chave_pix="",  # Não usado neste tipo
            nome_beneficiario="EMPRESA XYZ LTDA",
            cpf_cnpj_beneficiario="99999999000100",
            tipo_documento_beneficiario=TipoDocumento.CNPJ,
            tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
            ispb_beneficiario="22222222",
            valor=5000.00,
            data_pagamento="20022026"
        ),
    ]
    
    # Criar conversor
    conversor = ConversorCNAB()
    conversor.definir_empresa(empresa)
    conversor.definir_numero_sequencial("000001")
    conversor.adicionar_pagamentos(pagamentos)
    
    # Validar pagamentos
    print("\n1. Validando pagamentos...")
    if conversor.validar():
        print("   ✓ Todos os pagamentos são válidos!")
    else:
        print("   ✗ Existem erros na validação")
    
    # Gerar arquivo CNAB
    print("\n2. Gerando arquivo CNAB para Banco Inter...")
    arquivo = conversor.gerar_arquivo_inter("remessa_inter.REM")
    
    # Gerar relatórios
    print("\n3. Gerando relatórios...")
    conversor.gerar_relatorio("csv", "relatorio_pagamentos.csv")
    conversor.gerar_relatorio("json", "relatorio_pagamentos.json")
    conversor.gerar_relatorio("html", "relatorio_pagamentos.html")
    
    print("\n✓ Conversão concluída com sucesso!")
    print("\nArquivos gerados:")
    print("  - remessa_inter.REM (arquivo CNAB para envio ao Banco Inter)")
    print("  - relatorio_pagamentos.csv")
    print("  - relatorio_pagamentos.json")
    print("  - relatorio_pagamentos.html")


def exemplo_validacao_erros():
    """Exemplo com validações de erro"""
    print("\n" + "=" * 70)
    print("EXEMPLO 2: Validações de Erro")
    print("=" * 70)
    
    pagamentos_com_erro = [
        # Email inválido
        PagamentoPix(
            tipo_chave_pix=TipoChavePix.EMAIL,
            chave_pix="email_invalido",
            nome_beneficiario="TESTE",
            cpf_cnpj_beneficiario="12345678901",
            tipo_documento_beneficiario=TipoDocumento.CPF,
            tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
            ispb_beneficiario="12345678",
            valor=100.00,
            data_pagamento="20022026"
        ),
        # Valor negativo
        PagamentoPix(
            tipo_chave_pix=TipoChavePix.CPF_CNPJ,
            chave_pix="12345678901",
            nome_beneficiario="TESTE 2",
            cpf_cnpj_beneficiario="98765432100",
            tipo_documento_beneficiario=TipoDocumento.CPF,
            tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
            ispb_beneficiario="87654321",
            valor=-500.00,
            data_pagamento="20022026"
        ),
    ]
    
    print("\nTestando validações com dados inválidos:")
    for i, pag in enumerate(pagamentos_com_erro, 1):
        valido, mensagem = pag.validar()
        status = "✓" if valido else "✗"
        print(f"  {status} Pagamento {i}: {mensagem}")


if __name__ == "__main__":
    try:
        exemplo_conversao_manual()
        exemplo_validacao_erros()
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)