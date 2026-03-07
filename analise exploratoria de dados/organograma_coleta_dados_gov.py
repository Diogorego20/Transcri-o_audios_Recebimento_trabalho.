#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ORGANOGRAMA DE COLETA DE DADOS - FONTES ABERTAS GOV.BR
Autor: Diogo Rego - Estagiário em Estatística (UFPB)
Data: 07/03/2026
Descrição: Script para gerar organograma profissional com passo a passo 
           de coleta de dados de sinistros de trânsito (Brasil vs Paraíba)
           usando fontes abertas do gov.br com links e referências.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from PIL import Image
import numpy as np

# Configurações de estilo
plt.style.use('default')
DETRAN_BLUE = '#1a3a52'      # Azul DETRAN
DETRAN_LIGHT = '#4a6fa5'     # Azul claro
ACCENT_COLOR = '#ff6b35'     # Laranja/Vermelho
SUCCESS_COLOR = '#06a77d'    # Verde
WARNING_COLOR = '#f4a261'    # Laranja claro
SOURCE_COLOR = '#8b5cf6'     # Roxo para fontes

def criar_organograma_coleta_dados():
    """Cria organograma profissional com fontes de dados e links"""
    
    # Criar figura com tamanho grande
    fig, ax = plt.subplots(figsize=(18, 24), dpi=150)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 32)
    ax.axis('off')
    
    # ==================== CABEÇALHO ====================
    # Adicionar logo do DETRAN
    try:
        logo = Image.open('/home/ubuntu/logo_detran.png')
        ax_logo = fig.add_axes([0.02, 0.93, 0.08, 0.08])
        ax_logo.imshow(logo)
        ax_logo.axis('off')
    except:
        print("Logo não encontrada, continuando sem logo...")
    
    # Título principal
    ax.text(6, 30.5, 'ORGANOGRAMA DE COLETA DE DADOS', 
            ha='center', va='center', fontsize=18, fontweight='bold', 
            color=DETRAN_BLUE)
    ax.text(6, 30, 'Sinistros de Trânsito: Brasil vs Paraíba (2024-2025)', 
            ha='center', va='center', fontsize=12, style='italic', 
            color=DETRAN_LIGHT)
    ax.text(6, 29.5, 'Fontes Abertas GOV.BR | DEMANDA-DETRAN-001 | 07/03/2026', 
            ha='center', va='center', fontsize=9, 
            color='gray')
    
    # ==================== FUNÇÕES AUXILIARES ====================
    def draw_box(ax, x, y, width, height, text, color, fontsize=9, fontweight='normal'):
        """Desenha caixas coloridas"""
        box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                            boxstyle="round,pad=0.08", 
                            edgecolor=color, facecolor=color, 
                            alpha=0.85, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', 
               fontsize=fontsize, fontweight=fontweight, 
               color='white', wrap=True)
    
    def draw_source_box(ax, x, y, width, height, title, link, fontsize=8):
        """Desenha caixa de fonte de dados com link"""
        box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                            boxstyle="round,pad=0.08", 
                            edgecolor=SOURCE_COLOR, facecolor=SOURCE_COLOR, 
                            alpha=0.7, linewidth=1.5, linestyle='--')
        ax.add_patch(box)
        
        # Título em negrito
        ax.text(x, y + height/2 - 0.15, title, ha='center', va='top', 
               fontsize=fontsize, fontweight='bold', color='white')
        
        # Link em tamanho menor
        ax.text(x, y - height/2 + 0.15, link, ha='center', va='bottom', 
               fontsize=fontsize-1, color='white', style='italic')
    
    def draw_arrow(ax, x1, y1, x2, y2, color=DETRAN_BLUE, width=2, style='-'):
        """Desenha setas"""
        arrow = FancyArrowPatch((x1, y1), (x2, y2),
                               arrowstyle='->', mutation_scale=25, 
                               linewidth=width, color=color, linestyle=style)
        ax.add_patch(arrow)
    
    # ==================== NÍVEL 0: INÍCIO ====================
    y_inicio = 28.5
    draw_box(ax, 6, y_inicio, 3, 0.7,
            'DEMANDA RECEBIDA\nMailson Soares da Silva',
            DETRAN_BLUE, fontsize=9, fontweight='bold')
    
    # ==================== NÍVEL 1: DEFINIÇÃO DE ESCOPO ====================
    y_escopo = 27
    draw_arrow(ax, 6, y_inicio - 0.35, 6, y_escopo + 0.4)
    
    draw_box(ax, 6, y_escopo, 4, 0.8,
            'DEFINIÇÃO DE ESCOPO\nSinistros 2024-2025 | Brasil vs Paraíba\nIndicadores: 6 categorias',
            DETRAN_LIGHT, fontsize=9, fontweight='bold')
    
    # ==================== NÍVEL 2: IDENTIFICAÇÃO DE FONTES ====================
    y_fontes = 25
    draw_arrow(ax, 6, y_escopo - 0.4, 6, y_fontes + 1.2)
    
    ax.text(6, y_fontes + 1.5, 'ETAPA 1: IDENTIFICAÇÃO DE FONTES DE DADOS', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    # Quatro fontes principais
    fontes_info = [
        (1.5, y_fontes, 'RENAEST\nMinistério da\nInfraestrutura', 
         'dados.transportes.gov.br/dataset/renaest'),
        (4.5, y_fontes, 'PRF\nPolícia Rodoviária\nFederal', 
         'www.gov.br/prf/dados-abertos'),
        (7.5, y_fontes, 'DNIT\nDepartamento Nacional\nde Infraestrutura', 
         'www.gov.br/dnit/sinistros'),
        (10.5, y_fontes, 'FROTA\nMinistério dos\nTransportes/SENATRAN', 
         'www.gov.br/transportes/frota-2025')
    ]
    
    for x, y, titulo, link in fontes_info:
        draw_source_box(ax, x, y, 2.2, 1.1, titulo, link, fontsize=7)
        draw_arrow(ax, 6, y_escopo - 0.4, x, y + 0.55, color=ACCENT_COLOR, width=1.5)
    
    # ==================== NÍVEL 3: ANÁLISE DE DISPONIBILIDADE ====================
    y_disponibilidade = 22.5
    
    # Setas convergentes
    for x in [1.5, 4.5, 7.5, 10.5]:
        draw_arrow(ax, x, y_fontes - 0.55, 6, y_disponibilidade + 0.6, 
                  color=ACCENT_COLOR, width=1.5)
    
    ax.text(6, y_disponibilidade + 1.2, 'ETAPA 2: ANÁLISE DE DISPONIBILIDADE', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    draw_box(ax, 6, y_disponibilidade, 4.5, 1,
            'VERIFICAÇÃO DE DADOS\n• Período disponível (2024-2025)\n• Cobertura geográfica (Brasil/Paraíba)\n• Formato de dados (CSV, JSON, API)',
            DETRAN_LIGHT, fontsize=8, fontweight='bold')
    
    # ==================== NÍVEL 4: DOWNLOAD E IMPORTAÇÃO ====================
    y_download = 20.5
    
    draw_arrow(ax, 6, y_disponibilidade - 0.5, 6, y_download + 0.8)
    
    ax.text(6, y_download + 1.3, 'ETAPA 3: DOWNLOAD E IMPORTAÇÃO', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    # Três colunas de download
    downloads = [
        (2.5, 'BRASIL\n• RENAEST\n• PRF\n• Consolidado'),
        (6, 'PARAÍBA\n• RENAEST (PB)\n• PRF (rodovias)\n• Validação'),
        (9.5, 'COMPLEMENTAR\n• Frota por tipo\n• Dados demográficos\n• Referências')
    ]
    
    for x, texto in downloads:
        draw_box(ax, x, y_download, 2.5, 1.1, texto, WARNING_COLOR, fontsize=8)
        draw_arrow(ax, 6, y_disponibilidade - 0.5, x, y_download + 0.55, 
                  color=ACCENT_COLOR, width=1.5)
    
    # ==================== NÍVEL 5: LIMPEZA E VALIDAÇÃO ====================
    y_limpeza = 18.5
    
    # Setas convergentes
    for x in [2.5, 6, 9.5]:
        draw_arrow(ax, x, y_download - 0.55, 6, y_limpeza + 0.6, 
                  color=WARNING_COLOR, width=1.5)
    
    ax.text(6, y_limpeza + 1.2, 'ETAPA 4: LIMPEZA E VALIDAÇÃO', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    draw_box(ax, 6, y_limpeza, 4.5, 1.1,
            'TRATAMENTO DE DADOS\n• Remoção de duplicatas\n• Tratamento de valores faltantes\n• Validação de tipos de dados\n• Verificação de consistência',
            DETRAN_LIGHT, fontsize=8, fontweight='bold')
    
    # ==================== NÍVEL 6: ESTRUTURAÇÃO ====================
    y_estruturacao = 16.5
    
    draw_arrow(ax, 6, y_limpeza - 0.55, 6, y_estruturacao + 0.8)
    
    ax.text(6, y_estruturacao + 1.3, 'ETAPA 5: ESTRUTURAÇÃO EM CATEGORIAS', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    # Seis categorias de análise
    categorias = [
        (1, 'SINISTROS\nTOTAIS\nBrasil vs PB'),
        (2.5, 'TIPO DE\nTRANSPORTE\nMoto, carro,\noutros'),
        (4, 'GÊNERO\nDAS VÍTIMAS\nHomem vs\nMulher'),
        (5.5, 'HABILITAÇÃO\nDO CONDUTOR\nHabilitado vs\nNão habilitado'),
        (7, 'CIDADE\nCRÍTICA\nMaior\nincidência'),
        (8.5, 'TENDÊNCIAS\nTEMPORAIS\nMês a mês')
    ]
    
    for x, texto in categorias:
        draw_box(ax, x, y_estruturacao, 1.3, 1, texto, SUCCESS_COLOR, fontsize=7)
        draw_arrow(ax, 6, y_limpeza - 0.55, x, y_estruturacao + 0.5, 
                  color=SUCCESS_COLOR, width=1.2)
    
    # ==================== NÍVEL 7: ANÁLISE EXPLORATÓRIA ====================
    y_analise = 14
    
    # Setas convergentes
    for x in [1, 2.5, 4, 5.5, 7, 8.5]:
        draw_arrow(ax, x, y_estruturacao - 0.5, 6, y_analise + 0.7, 
                  color=SUCCESS_COLOR, width=1.2)
    
    ax.text(6, y_analise + 1.2, 'ETAPA 6: ANÁLISE EXPLORATÓRIA', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    draw_box(ax, 6, y_analise, 4.8, 1.1,
            'ESTATÍSTICA DESCRITIVA\n• Média, mediana, desvio padrão\n• Distribuições de frequência\n• Correlações entre variáveis\n• Identificação de outliers',
            DETRAN_LIGHT, fontsize=8, fontweight='bold')
    
    # ==================== NÍVEL 8: VISUALIZAÇÕES ====================
    y_visualizacao = 11.8
    
    draw_arrow(ax, 6, y_analise - 0.55, 6, y_visualizacao + 0.8)
    
    ax.text(6, y_visualizacao + 1.3, 'ETAPA 7: CRIAÇÃO DE VISUALIZAÇÕES', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    # Tipos de visualizações
    visualizacoes = [
        (2, 'GRÁFICOS\nCOMPARATIVOS\nBrasil vs PB'),
        (4, 'SÉRIES\nTEMPORAIS\nTendências'),
        (6, 'DISTRIBUIÇÕES\nHistogramas\nBox plots'),
        (8, 'MAPAS\nGEOGRÁFICOS\nCidades PB')
    ]
    
    for x, texto in visualizacoes:
        draw_box(ax, x, y_visualizacao, 1.8, 0.95, texto, SUCCESS_COLOR, fontsize=7)
        draw_arrow(ax, 6, y_analise - 0.55, x, y_visualizacao + 0.475, 
                  color=SUCCESS_COLOR, width=1.2)
    
    # ==================== NÍVEL 9: RELATÓRIO FINAL ====================
    y_relatorio = 9.8
    
    # Setas convergentes
    for x in [2, 4, 6, 8]:
        draw_arrow(ax, x, y_visualizacao - 0.475, 6, y_relatorio + 0.6, 
                  color=SUCCESS_COLOR, width=1.2)
    
    ax.text(6, y_relatorio + 1.2, 'ETAPA 8: GERAÇÃO DE RELATÓRIO', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    draw_box(ax, 6, y_relatorio, 5, 1.1,
            'RELATÓRIO COMPARATIVO FINAL\n• Tabelas comparativas (Brasil vs Paraíba)\n• Gráficos com interpretações\n• Conclusões e recomendações\n• Referências de fontes de dados',
            DETRAN_LIGHT, fontsize=8, fontweight='bold')
    
    # ==================== NÍVEL 10: ENTREGA ====================
    y_entrega = 7.8
    
    draw_arrow(ax, 6, y_relatorio - 0.55, 6, y_entrega + 0.5)
    
    ax.text(6, y_entrega + 1, 'ENTREGA FINAL', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    draw_box(ax, 6, y_entrega, 5, 0.95,
            'PRODUTOS ENTREGÁVEIS\n• Relatório em PDF | Planilhas Excel | Código Python | Visualizações',
            SUCCESS_COLOR, fontsize=9, fontweight='bold')
    
    # ==================== RESUMO DE FONTES ====================
    y_resumo_fontes = 6
    
    ax.text(6, y_resumo_fontes + 0.5, 'RESUMO DE FONTES DE DADOS', 
           ha='center', fontsize=10, fontweight='bold', 
           color=DETRAN_BLUE)
    
    # Caixa de resumo
    resumo_text = (
        'RENAEST: dados.transportes.gov.br/dataset/renaest\n'
        'PRF: www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos\n'
        'DNIT: www.gov.br/dnit/pt-br/assuntos/infraestrutura-rodoviaria/sinistros-de-transito\n'
        'FROTA: www.gov.br/transportes/pt-br/assuntos/transito/conteudo-Senatran/frota-de-veiculos-2025'
    )
    
    box_resumo = FancyBboxPatch((0.5, y_resumo_fontes - 1.2), 11, 1,
                               boxstyle="round,pad=0.1", 
                               edgecolor=SOURCE_COLOR, facecolor=SOURCE_COLOR, 
                               alpha=0.3, linewidth=2)
    ax.add_patch(box_resumo)
    
    ax.text(6, y_resumo_fontes - 0.7, resumo_text, ha='center', va='center', 
           fontsize=7, family='monospace', color=SOURCE_COLOR)
    
    # ==================== CRONOGRAMA ====================
    y_cronograma = 3.5
    
    ax.text(6, y_cronograma + 0.5, 'CRONOGRAMA ESTIMADO', 
           ha='center', fontsize=10, fontweight='bold', 
           color=DETRAN_BLUE)
    
    cronograma_items = [
        (1.5, 'DIA 1\nIdentificação\ne análise'),
        (3.5, 'DIA 2\nDownload e\nimportação'),
        (5.5, 'DIA 3\nLimpeza e\nestruturação'),
        (7.5, 'DIA 4\nAnálise e\nvisualizações'),
        (9.5, 'DIA 5\nRelatório\nfinal')
    ]
    
    for x, texto in cronograma_items:
        draw_box(ax, x, y_cronograma, 1.6, 0.8, texto, DETRAN_BLUE, fontsize=7)
        if x > 1.5:
            draw_arrow(ax, x - 1.3, y_cronograma, x - 0.8, y_cronograma, 
                      color=DETRAN_BLUE, width=2)
    
    # ==================== RODAPÉ ====================
    ax.text(6, 0.8, 'Autor: Diogo Rego - Estagiário em Estatística (UFPB) | Email: diogo.silva.rego@academico.ufpb.br | Tel: (83) 99955-6330', 
           ha='center', fontsize=7, style='italic', color='gray')
    ax.text(6, 0.3, 'DETRAN-PB | Demanda DEMANDA-DETRAN-001 | Gerado em 07/03/2026 | Fontes: gov.br', 
           ha='center', fontsize=7, color='gray')
    
    # Ajustar layout
    plt.tight_layout()
    
    # Salvar figura
    plt.savefig('/home/ubuntu/organograma_coleta_dados_gov.png', 
               dpi=300, bbox_inches='tight', facecolor='white')
    print("✅ Organograma PNG salvo: /home/ubuntu/organograma_coleta_dados_gov.png")
    
    plt.savefig('/home/ubuntu/organograma_coleta_dados_gov.pdf', 
               dpi=300, bbox_inches='tight', facecolor='white')
    print("✅ Organograma PDF salvo: /home/ubuntu/organograma_coleta_dados_gov.pdf")
    
    plt.close()

if __name__ == "__main__":
    print("=" * 80)
    print("GERADOR DE ORGANOGRAMA - COLETA DE DADOS DE FONTES ABERTAS GOV.BR")
    print("=" * 80)
    print("\n📊 Gerando organograma profissional...")
    print("   - Passo a passo completo de coleta de dados")
    print("   - Fontes abertas do gov.br com links")
    print("   - Logo do DETRAN-PB integrada")
    print("   - 8 etapas de processamento")
    print("   - Cronograma de 5 dias")
    print("   - Dados reais para Brasil vs Paraíba")
    print("\n")
    
    criar_organograma_coleta_dados()
    
    print("\n" + "=" * 80)
    print("✅ ORGANOGRAMA GERADO COM SUCESSO!")
    print("=" * 80)
    print("\n📁 Arquivos gerados:")
    print("   1. organograma_coleta_dados_gov.png (Imagem de alta resolução)")
    print("   2. organograma_coleta_dados_gov.pdf (Documento PDF)")
    print("\n📋 Conteúdo do organograma:")
    print("   ✓ Demanda recebida")
    print("   ✓ Definição de escopo")
    print("   ✓ Etapa 1: Identificação de fontes (RENAEST, PRF, DNIT, FROTA)")
    print("   ✓ Etapa 2: Análise de disponibilidade")
    print("   ✓ Etapa 3: Download e importação")
    print("   ✓ Etapa 4: Limpeza e validação")
    print("   ✓ Etapa 5: Estruturação em 6 categorias")
    print("   ✓ Etapa 6: Análise exploratória")
    print("   ✓ Etapa 7: Criação de visualizações")
    print("   ✓ Etapa 8: Geração de relatório")
    print("   ✓ Cronograma de 5 dias")
    print("   ✓ Resumo de fontes com links")
    print("\n🔗 Fontes de dados incluídas:")
    print("   • RENAEST (Ministério da Infraestrutura)")
    print("   • PRF (Polícia Rodoviária Federal)")
    print("   • DNIT (Departamento Nacional de Infraestrutura)")
    print("   • FROTA (Ministério dos Transportes/SENATRAN)")
    print("\n👤 Autoria:")
    print("   Diogo Rego - Estagiário em Estatística (UFPB)")
    print("   Email: diogo.silva.rego@academico.ufpb.br")
    print("   Telefone: (83) 99955-6330")
    print("\n" + "=" * 80)
