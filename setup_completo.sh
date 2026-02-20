#!/bin/bash

echo "=========================================="
echo "CNAB Converter - Setup Completo"
echo "=========================================="
echo ""

# Criar estrutura de diretórios
mkdir -p cnab_converter
mkdir -p tests

# Criar arquivos Python principais
echo "Criando arquivos Python..."

# 1. cnab_converter/__init__.py
cat > cnab_converter/__init__.py << 'EOF'
"""
CNAB Converter - Conversão de CNAB 240 Banco do Brasil para Banco Inter
Suporte a transferências via Pix com todos os tipos de chaves
"""

__version__ = "1.0.0"
__author__ = "CNAB Converter Team"
EOF

# 2. tests/__init__.py
touch tests/__init__.py

echo "✅ Estrutura de pastas criada"
echo ""
echo "Próximos passos:"
echo "1. Copie os arquivos .py do projeto para as pastas correspondentes"
echo "2. Execute: git add ."
echo "3. Execute: git commit -m 'Add: CNAB Converter completo'"
echo "4. Execute: git push"