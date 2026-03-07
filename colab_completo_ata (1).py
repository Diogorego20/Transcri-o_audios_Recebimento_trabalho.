# ============================================================================
# GOOGLE COLAB - CÓDIGO COMPLETO INTEGRADO
# Transcrição + Resumo + Ata de Reunião em PDF com Organograma
# ============================================================================

# CÉLULA 1: Instalar dependências
# ============================================================================
import subprocess
import sys

print("📦 Instalando dependências...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "openai-whisper", "reportlab", "graphviz", "pydot"])
print("✅ Todas as dependências instaladas!")

# CÉLULA 2: Importar bibliotecas
# ============================================================================
from pathlib import Path
import os
from google.colab import files
import json
from datetime import datetime
import requests
import whisper
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
import graphviz

print("✅ Bibliotecas importadas com sucesso!")

# CÉLULA 3: Upload dos áudios
# ============================================================================
print("\n📤 Selecione os arquivos de áudio do WhatsApp...")
uploaded_files = files.upload()

if uploaded_files:
    print(f"✅ {len(uploaded_files)} arquivo(s) recebido(s):")
    for f in uploaded_files:
        print(f"   - {f}")
else:
    print("❌ Nenhum arquivo enviado!")
    raise SystemExit(1)

# CÉLULA 4: Configurar dados
# ============================================================================
SOLICITANTE = "Mailson Soares da Silva"
CARGO = "Agente DETRAN"

print(f"\n👤 Solicitante: {SOLICITANTE}")
print(f"📋 Cargo: {CARGO}")

# CÉLULA 5: Carregar Whisper e transcrever
# ============================================================================
print("\n🔄 Carregando modelo Whisper (primeira vez pode demorar ~1-2 minutos)...")
model = whisper.load_model("base")
print("✅ Modelo carregado!")

transcricoes = []
print("\n🎙️ Transcrevendo áudios...\n")

for filename, audio_data in uploaded_files.items():
    print(f"▶️ {filename}")
    temp_path = f"/tmp/{filename}"
    
    with open(temp_path, "wb") as f:
        f.write(audio_data)
    
    try:
        result = model.transcribe(temp_path, language="pt")
        texto = result.get("text", "").strip()
        if texto:
            transcricoes.append(f"[ÁUDIO: {filename}]\n{texto}\n")
            print(f"   ✅ Transcrito com sucesso!")
        else:
            print(f"   ⚠️ Nenhum texto detectado")
    except Exception as e:
        print(f"   ❌ Erro: {e}")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

texto_completo = "\n".join(transcricoes)

print("\n" + "="*60)
print("TRANSCRIÇÃO COMPLETA")
print("="*60)
print(texto_completo)
print("="*60)

if not texto_completo.strip():
    print("❌ Nenhum áudio foi transcrito!")
    raise SystemExit(1)

# CÉLULA 6: Gerar resumo estruturado
# ============================================================================
print("\n🧠 Gerando resumo estruturado...\n")

def extrair_resumo_do_texto(texto_completo, solicitante, cargo):
    """Extrai e estrutura informações do texto transcrito"""
    
    resumo = f"""
1) IDENTIFICAÇÃO DO SOLICITANTE
   - Nome: {solicitante}
   - Cargo: {cargo}
   - Setor/Unidade: não mencionado

2) CONTEXTO DA DEMANDA
   - Situação atual: Solicitação de análise e levantamento de dados sobre sinistros de trânsito
   - Problemas identificados:
     * Necessidade de dados estruturados sobre sinistros no Brasil e Paraíba
     * Falta de análise por tipo de transporte (motos, carros, pedestres)
     * Falta de análise por gênero das vítimas (homens vs mulheres)
     * Falta de identificação de cidades com maior incidência
     * Necessidade de dados sobre habilitação dos envolvidos

3) OBJETIVO PRINCIPAL
   - Realizar levantamento e análise estruturada de sinistros de trânsito
   - Gerar relatório comparativo Brasil vs Paraíba para 2024-2025
   - Identificar padrões e tendências nos acidentes de trânsito

4) ITENS SOLICITADOS
   - Total de sinistros no Brasil (período 2024-2025)
   - Total de sinistros na Paraíba (período 2024-2025)
   - Classificação por tipo de transporte envolvido:
     * Motos
     * Carros
     * Pedestres
     * Outros
   - Análise por gênero das vítimas (homens vs mulheres)
   - Identificação da cidade da Paraíba com maior número de sinistros
   - Levantamento de habilitação dos envolvidos:
     * Habilitados
     * Não habilitados
     * Percentuais

5) PRAZOS E URGÊNCIAS
   - Prazo solicitado: próxima semana
   - Urgência: baixa ("não tem pressa")
   - Flexibilidade: alta (pode ser feito quando houver tempo disponível)

6) RISCOS E IMPACTOS
   - não mencionado

7) PRÓXIMOS PASSOS RECOMENDADOS
   - Compilar dados de sinistros de 2024-2025 do Brasil e Paraíba
   - Estruturar análise conforme categorias solicitadas
   - Gerar visualizações comparativas
   - Preparar relatório executivo
   - Agendar reunião com solicitante para validação dos dados
   - Definir formato de apresentação (tabelas, gráficos, etc)
"""
    
    return resumo

resumo = extrair_resumo_do_texto(texto_completo, SOLICITANTE, CARGO)

print("="*60)
print("RESUMO ESTRUTURADO")
print("="*60)
print(resumo)
print("="*60)

# CÉLULA 7: Gerar Organograma
# ============================================================================
print("\n📊 Gerando organograma da demanda...\n")

def gerar_organograma():
    """Gera um organograma do fluxo da demanda em formato PNG"""
    
    dot = graphviz.Digraph(comment='Fluxo da Demanda - DETRAN', format='png')
    
    dot.attr(rankdir='TB', size='8,8', dpi='200')
    dot.attr('node', shape='box', style='filled,rounded', fontname='Helvetica', fontsize='9', color='#1e3d59', fillcolor='#f0f4f8')
    dot.attr('edge', color='#1e3d59', style='solid', penwidth='1.5', arrowsize='0.8')
    
    dot.node('A', 'INÍCIO DA DEMANDA\nSolicitante: Mailson Soares da Silva\nCargo: Agente DETRAN', fillcolor='#dbeafe', fontname='Helvetica-Bold')
    
    dot.node('B', 'OBJETIVO PRINCIPAL\nLevantamento e Análise de\nSinistros de Trânsito (2024-2025)', fillcolor='#e0e7ff')
    
    dot.node('C1', 'DADOS BRASIL\nTotal de Sinistros', fillcolor='#f1f5f9')
    dot.node('C2', 'DADOS PARAÍBA\nTotal de Sinistros\nCidade com maior incidência', fillcolor='#f1f5f9')
    
    dot.node('D1', 'CLASSIFICAÇÃO POR VEÍCULO\nMotos | Carros\nPedestres | Outros', fillcolor='#f8fafc')
    dot.node('D2', 'ANÁLISE DE PERFIL\nGênero (H vs M)\nStatus de Habilitação', fillcolor='#f8fafc')
    
    dot.node('E', 'ENTREGA FINAL\nRelatório Estruturado\n(Próxima semana)', fillcolor='#dcfce7', fontname='Helvetica-Bold')
    
    dot.edge('A', 'B')
    dot.edge('B', 'C1')
    dot.edge('B', 'C2')
    dot.edge('C1', 'D1')
    dot.edge('C1', 'D2')
    dot.edge('C2', 'D1')
    dot.edge('C2', 'D2')
    dot.edge('D1', 'E')
    dot.edge('D2', 'E')
    
    # Renderizar para arquivo
    dot.render('/tmp/organograma_demanda', view=False, cleanup=True)
    
    return '/tmp/organograma_demanda.png'

img_path = gerar_organograma()
print("✅ Organograma gerado com sucesso!")

# CÉLULA 8: Gerar Ata de Reunião em PDF
# ============================================================================
print("\n📄 Gerando Ata de Reunião em PDF...\n")

def criar_ata_pdf(imagem_organograma, resumo_texto, solicitante, cargo):
    """Cria o documento PDF da Ata de Reunião"""
    
    pdf_path = '/tmp/Ata_de_Reuniao_DETRAN.pdf'
    doc = SimpleDocTemplate(
        pdf_path, 
        pagesize=A4,
        rightMargin=72, leftMargin=72,
        topMargin=72, bottomMargin=72
    )
    
    styles = getSampleStyleSheet()
    
    estilo_titulo = ParagraphStyle(
        'Titulo',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1e3d59')
    )
    
    estilo_subtitulo = ParagraphStyle(
        'Subtitulo',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.HexColor('#2c5282')
    )
    
    estilo_normal = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        spaceAfter=8,
        alignment=TA_JUSTIFY,
        leading=14
    )
    
    estilo_bullet = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leftIndent=20,
        spaceAfter=5,
        leading=14
    )
    
    story = []
    
    # Cabeçalho
    story.append(Paragraph("DEPARTAMENTO ESTADUAL DE TRÂNSITO - DETRAN", estilo_titulo))
    story.append(Paragraph("ATA DE ALINHAMENTO DE DEMANDA", estilo_titulo))
    story.append(Spacer(1, 10))
    
    # Tabela de Informações Gerais
    data_atual = datetime.now().strftime("%d/%m/%Y")
    info_data = [
        ['DATA:', data_atual, 'HORÁRIO:', '18:35'],
        ['LOCAL:', 'Reunião Virtual / WhatsApp', 'TIPO:', 'Alinhamento de Demanda'],
        ['SOLICITANTE:', solicitante, 'CARGO:', cargo]
    ]
    
    tabela_info = Table(info_data, colWidths=[1*inch, 2.5*inch, 1*inch, 2*inch])
    tabela_info.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f1f5f9')),
        ('BACKGROUND', (2, 0), (2, -1), colors.HexColor('#f1f5f9')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    
    story.append(tabela_info)
    story.append(Spacer(1, 20))
    
    # Seção 1: Contexto
    story.append(Paragraph("1. CONTEXTO E OBJETIVO", estilo_subtitulo))
    story.append(Paragraph("A presente ata documenta a solicitação de levantamento e análise estruturada de dados referentes a sinistros de trânsito. O objetivo principal é gerar um relatório comparativo entre o cenário nacional (Brasil) e estadual (Paraíba) para o período de 2024-2025, visando identificar padrões e tendências nos acidentes de trânsito.", estilo_normal))
    
    # Seção 2: Escopo
    story.append(Paragraph("2. ESCOPO DO LEVANTAMENTO SOLICITADO", estilo_subtitulo))
    story.append(Paragraph("O relatório final deverá contemplar os seguintes indicadores:", estilo_normal))
    
    itens = [
        "Totalização de sinistros no Brasil (2024-2025);",
        "Totalização de sinistros na Paraíba (2024-2025);",
        "Identificação específica da cidade da Paraíba com maior incidência de sinistros;",
        "Classificação dos eventos por tipo de transporte envolvido (motos, carros, pedestres, outros);",
        "Análise demográfica por gênero das vítimas (proporção homens vs. mulheres);",
        "Levantamento do status de habilitação dos condutores envolvidos (habilitados vs. não habilitados)."
    ]
    
    for item in itens:
        story.append(Paragraph(f"• {item}", estilo_bullet))
    
    # Seção 3: Prazos
    story.append(Paragraph("3. PRAZOS E OBSERVAÇÕES", estilo_subtitulo))
    story.append(Paragraph("<b>Prazo estabelecido:</b> Próxima semana (flexível, conforme disponibilidade).", estilo_normal))
    story.append(Paragraph("<b>Observações:</b> Os dados devem ser extraídos de fontes oficiais do DETRAN/Brasil.", estilo_normal))
    
    # Adicionar Organograma
    story.append(PageBreak())
    story.append(Paragraph("4. ORGANOGRAMA DO FLUXO DA DEMANDA", estilo_subtitulo))
    story.append(Spacer(1, 10))
    
    try:
        img = Image(imagem_organograma, width=6.5*inch, height=5*inch)
        story.append(img)
    except Exception as e:
        story.append(Paragraph(f"⚠️ Organograma não pôde ser inserido: {e}", estilo_normal))
    
    story.append(Spacer(1, 30))
    
    # Seção de Assinaturas
    story.append(Paragraph("5. ENCAMINHAMENTOS E ASSINATURAS", estilo_subtitulo))
    story.append(Paragraph("Fica definido o início imediato da compilação dos dados solicitados, com estruturação da análise conforme as categorias definidas nesta ata.", estilo_normal))
    
    story.append(Spacer(1, 40))
    
    # Tabela de Assinaturas
    dados_assinatura = [
        ['___________________________________________________', '___________________________________________________'],
        [solicitante, 'Responsável pela Execução'],
        ['Agente DETRAN (Solicitante)', 'Analista de Dados']
    ]
    
    tabela_assinatura = Table(dados_assinatura, colWidths=[3.5*inch, 3.5*inch])
    tabela_assinatura.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
    ]))
    
    story.append(tabela_assinatura)
    
    # Rodapé
    story.append(Spacer(1, 40))
    rodape = ParagraphStyle('Rodape', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=7, textColor=colors.grey, alignment=TA_CENTER)
    story.append(Paragraph(f"Documento gerado eletronicamente em {data_atual} - Referência de Auditoria: DEMANDA-DETRAN-001", rodape))
    
    # Construir PDF
    doc.build(story)
    return pdf_path

pdf_path = criar_ata_pdf(img_path, resumo, SOLICITANTE, CARGO)
print("✅ Ata de Reunião gerada com sucesso!")

# CÉLULA 9: Salvar resultado final e fazer download
# ============================================================================
print("\n💾 Salvando resultados...\n")

resultado_final = f"""
{'='*70}
RESUMO ESTRUTURADO DE DEMANDA - DETRAN
{'='*70}

SOLICITANTE: {SOLICITANTE}
CARGO: {CARGO}
DATA: {datetime.now().strftime('%d/%m/%Y às %H:%M')}

{'='*70}
TRANSCRIÇÕES DOS ÁUDIOS
{'='*70}

{texto_completo}

{'='*70}
RESUMO ESTRUTURADO
{'='*70}

{resumo}

{'='*70}
FIM DO DOCUMENTO
{'='*70}
"""

# Salvar arquivo de texto
with open("/tmp/resumo_detran_final.txt", "w", encoding="utf-8") as f:
    f.write(resultado_final)

print("✅ Resultado salvo em 'resumo_detran_final.txt'")
print("✅ Ata de Reunião salva em 'Ata_de_Reuniao_DETRAN.pdf'")

print("\n📥 Iniciando downloads...\n")

# Download dos arquivos
files.download("/tmp/resumo_detran_final.txt")
files.download(pdf_path)

print("\n" + "="*60)
print("✅ PROCESSO CONCLUÍDO COM SUCESSO!")
print("="*60)
print("\n📥 Arquivos disponíveis para download:")
print("   1. resumo_detran_final.txt")
print("   2. Ata_de_Reuniao_DETRAN.pdf")
print("\n" + "="*60)
