"""
Script de teste manual sem pytest
Útil para testar rapidamente sem dependências
"""
from cnab_converter.conversor import ConversorCNAB
from cnab_converter.models import (
    PagamentoPix, EmpresaInfo, TipoChavePix,
    TipoDocumento, TipoConta
)


def teste_01_pagamento_email():
    """Teste 1: Pagamento com Pix por Email"""
    print("\n" + "="*70)
    print("TESTE 1: Pagamento com Pix por Email")
    print("="*70)
    
    pagamento = PagamentoPix(
        tipo_chave_pix=TipoChavePix.EMAIL,
        chave_pix="usuario@email.com",
        nome_beneficiario="JOAO SILVA",
        cpf_cnpj_beneficiario="12345678901",
        tipo_documento_beneficiario=TipoDocumento.CPF,
        tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
        ispb_beneficiario="12345678",
        valor=1000.50,
        data_pagamento="20022026"
    )
    
    valido, mensagem = pagamento.validar()
    status = "✅ PASSOU" if valido else "❌ FALHOU"
    print(f"{status}: {mensagem}")
    return valido


def teste_02_pagamento_telefone():
    """Teste 2: Pagamento com Pix por Telefone"""
    print("\n" + "="*70)
    print("TESTE 2: Pagamento com Pix por Telefone")
    print("="*70)
    
    pagamento = PagamentoPix(
        tipo_chave_pix=TipoChavePix.TELEFONE,
        chave_pix="+5511987654321",
        nome_beneficiario="MARIA SANTOS",
        cpf_cnpj_beneficiario="98765432100",
        tipo_documento_beneficiario=TipoDocumento.CPF,
        tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
        ispb_beneficiario="87654321",
        valor=2500.00,
        data_pagamento="20022026"
    )
    
    valido, mensagem = pagamento.validar()
    status = "✅ PASSOU" if valido else "❌ FALHOU"
    print(f"{status}: {mensagem}")
    return valido


def teste_03_pagamento_cpf():
    """Teste 3: Pagamento com Pix por CPF"""
    print("\n" + "="*70)
    print("TESTE 3: Pagamento com Pix por CPF")
    print("="*70)
    
    pagamento = PagamentoPix(
        tipo_chave_pix=TipoChavePix.CPF_CNPJ,
        chave_pix="12345678901",
        nome_beneficiario="PEDRO OLIVEIRA",
        cpf_cnpj_beneficiario="12345678901",
        tipo_documento_beneficiario=TipoDocumento.CPF,
        tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
        ispb_beneficiario="12345678",
        valor=750.25,
        data_pagamento="20022026"
    )
    
    valido, mensagem = pagamento.validar()
    status = "✅ PASSOU" if valido else "❌ FALHOU"
    print(f"{status}: {mensagem}")
    return valido


def teste_04_pagamento_uuid():
    """Teste 4: Pagamento com Chave Aleatória (UUID)"""
    print("\n" + "="*70)
    print("TESTE 4: Pagamento com Chave Aleatória (UUID)")
    print("="*70)
    
    pagamento = PagamentoPix(
        tipo_chave_pix=TipoChavePix.ALEATORIA,
        chave_pix="12345678-1234-1234-1234-123456789012",
        nome_beneficiario="CARLOS FERREIRA",
        cpf_cnpj_beneficiario="55555555555",
        tipo_documento_beneficiario=TipoDocumento.CPF,
        tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
        ispb_beneficiario="11111111",
        valor=3200.75,
        data_pagamento="20022026"
    )
    
    valido, mensagem = pagamento.validar()
    status = "✅ PASSOU" if valido else "❌ FALHOU"
    print(f"{status}: {mensagem}")
    return valido


def teste_05_email_invalido():
    """Teste 5: Rejeita Email Inválido"""
    print("\n" + "="*70)
    print("TESTE 5: Rejeita Email Inválido")
    print("="*70)
    
    pagamento = PagamentoPix(
        tipo_chave_pix=TipoChavePix.EMAIL,
        chave_pix="email_invalido",
        nome_beneficiario="JOAO SILVA",
        cpf_cnpj_beneficiario="12345678901",
        tipo_documento_beneficiario=TipoDocumento.CPF,
        tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
        ispb_beneficiario="12345678",
        valor=1000.50,
        data_pagamento="20022026"
    )
    
    valido, mensagem = pagamento.validar()
    status = "✅ PASSOU" if not valido else "❌ FALHOU"
    print(f"{status}: Esperado falha - recebido: {mensagem}")
    return not valido


def teste_06_valor_negativo():
    """Teste 6: Rejeita Valor Negativo"""
    print("\n" + "="*70)
    print("TESTE 6: Rejeita Valor Negativo")
    print("="*70)
    
    pagamento = PagamentoPix(
        tipo_chave_pix=TipoChavePix.EMAIL,
        chave_pix="usuario@email.com",
        nome_beneficiario="JOAO SILVA",
        cpf_cnpj_beneficiario="12345678901",
        tipo_documento_beneficiario=TipoDocumento.CPF,
        tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
        ispb_beneficiario="12345678",
        valor=-100.50,
        data_pagamento="20022026"
    )
    
    valido, mensagem = pagamento.validar()
    status = "✅ PASSOU" if not valido else "❌ FALHOU"
    print(f"{status}: Esperado falha - recebido: {mensagem}")
    return not valido


def teste_07_geracao_arquivo():
    """Teste 7: Geração Completa de Arquivo"""
    print("\n" + "="*70)
    print("TESTE 7: Geração Completa de Arquivo CNAB")
    print("="*70)
    
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
    
    pagamentos = [
        PagamentoPix(
            tipo_chave_pix=TipoChavePix.EMAIL,
            chave_pix="usuario1@email.com",
            nome_beneficiario="USUARIO 1",
            cpf_cnpj_beneficiario="11111111111",
            tipo_documento_beneficiario=TipoDocumento.CPF,
            tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
            ispb_beneficiario="11111111",
            valor=1000.00,
            data_pagamento="20022026"
        ),
        PagamentoPix(
            tipo_chave_pix=TipoChavePix.TELEFONE,
            chave_pix="+5511987654321",
            nome_beneficiario="USUARIO 2",
            cpf_cnpj_beneficiario="22222222222",
            tipo_documento_beneficiario=TipoDocumento.CPF,
            tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
            ispb_beneficiario="22222222",
            valor=2000.00,
            data_pagamento="20022026"
        ),
    ]
    
    try:
        conversor = ConversorCNAB()
        conversor.definir_empresa(empresa)
        conversor.definir_numero_sequencial("000001")
        conversor.adicionar_pagamentos(pagamentos)
        
        # Validar
        if not conversor.validar():
            print("❌ FALHOU: Validação falhou")
            return False
        
        # Gerar arquivo
        arquivo = conversor.gerar_arquivo_inter("teste_cnab.REM")
        
        # Verificar
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            linhas = conteudo.split("\n")
            
            # Verificar número de linhas
            if len(linhas) != 9:
                print(f"❌ FALHOU: Esperado 9 linhas, recebido {len(linhas)}")
                return False
            
            # Verificar tamanho de cada linha
            for i, linha in enumerate(linhas):
                if len(linha) != 240:
                    print(f"❌ FALHOU: Linha {i} com tamanho {len(linha)}, esperado 240")
                    return False
        
        print("✅ PASSOU: Arquivo gerado com sucesso")
        print(f"   - Arquivo: {arquivo}")
        print(f"   - Linhas: {len(linhas)}")
        print(f"   - Tamanho por linha: 240 caracteres")
        return True
        
    except Exception as e:
        print(f"❌ FALHOU: {str(e)}")
        return False


def teste_08_relatorio():
    """Teste 8: Geração de Relatórios"""
    print("\n" + "="*70)
    print("TESTE 8: Geração de Relatórios")
    print("="*70)
    
    pagamentos = [
        PagamentoPix(
            tipo_chave_pix=TipoChavePix.EMAIL,
            chave_pix="usuario@email.com",
            nome_beneficiario="JOAO SILVA",
            cpf_cnpj_beneficiario="12345678901",
            tipo_documento_beneficiario=TipoDocumento.CPF,
            tipo_conta_beneficiario=TipoConta.CONTA_CORRENTE,
            ispb_beneficiario="12345678",
            valor=1000.50,
            data_pagamento="20022026"
        ),
    ]
    
    try:
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
        
        conversor = ConversorCNAB()
        conversor.definir_empresa(empresa)
        conversor.adicionar_pagamentos(pagamentos)
        
        # Gerar relatórios
        conversor.gerar_relatorio("csv", "relatorio_teste.csv")
        conversor.gerar_relatorio("json", "relatorio_teste.json")
        conversor.gerar_relatorio("html", "relatorio_teste.html")
        
        print("✅ PASSOU: Relatórios gerados com sucesso")
        print("   - relatorio_teste.csv")
        print("   - relatorio_teste.json")
        print("   - relatorio_teste.html")
        return True
        
    except Exception as e:
        print(f"❌ FALHOU: {str(e)}")
        return False


if __name__ == "__main__":
    print("\n" + "="*70)
    print("CNAB CONVERTER - TESTES MANUAIS")
    print("="*70)
    
    resultados = []
    
    resultados.append(("Pagamento Email", teste_01_pagamento_email()))
    resultados.append(("Pagamento Telefone", teste_02_pagamento_telefone()))
    resultados.append(("Pagamento CPF", teste_03_pagamento_cpf()))
    resultados.append(("Pagamento UUID", teste_04_pagamento_uuid()))
    resultados.append(("Email Inválido", teste_05_email_invalido()))
    resultados.append(("Valor Negativo", teste_06_valor_negativo()))
    resultados.append(("Geração Arquivo", teste_07_geracao_arquivo()))
    resultados.append(("Relatórios", teste_08_relatorio()))
    
    # Resumo
    print("\n" + "="*70)
    print("RESUMO DOS TESTES")
    print("="*70)
    
    passou = 0
    falhou = 0
    
    for nome, resultado in resultados:
        status = "✅" if resultado else "❌"
        print(f"{status} {nome}")
        if resultado:
            passou += 1
        else:
            falhou += 1
    
    print("="*70)
    print(f"Total: {passou} passou, {falhou} falhou de {len(resultados)} testes")
    print("="*70 + "\n")
    
    if falhou == 0:
        print("🎉 TODOS OS TESTES PASSARAM!")
    else:
        print(f"⚠️  {falhou} teste(s) falharam")