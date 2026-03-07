#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ORGANOGRAMA DE FLUXO DE DEMANDA - DETRAN-PB
Autor: Diogo Rego - Estagiário em Estatística (UFPB)
Data: 07/03/2026
Descrição: Script para gerar organograma profissional com passo a passo 
           para atender demanda de levantamento de sinistros de trânsito.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image
import numpy as np

# Configurações de estilo
plt.style.use('default')
DETRAN_BLUE = '#1a3a52'      # Azul DETRAN
DETRAN_LIGHT = '#4a6fa5'     # Azul claro
ACCENT_COLOR = '#ff6b35'     # Laranja/Vermelho
SUCCESS_COLOR = '#06a77d'    # Verde
WARNING_COLOR = '#f4a261'    # Laranja claro

def criar_organograma():
    """Cria organograma profissional com dados reais da demanda DETRAN"""
    
    # Criar figura com tamanho grande para melhor visualização
    fig, ax = plt.subplots(figsize=(16, 20), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 28)
    ax.axis('off')
    
    # ==================== CABEÇALHO ====================
    # Adicionar logo do DETRAN
    try:
        logo = Image.open('/home/ubuntu/logo_detran.png')
        ax_logo = fig.add_axes([0.02, 0.92, 0.08, 0.08])
        ax_logo.imshow(logo)
        ax_logo.axis('off')
    except:
        print("Logo não encontrada, continuando sem logo...")
    
    # Título principal
    ax.text(5, 26.5, 'ORGANOGRAMA DE FLUXO DE DEMANDA', 
            ha='center', va='center', fontsize=18, fontweight='bold', 
            color=DETRAN_BLUE)
    ax.text(5, 26, 'Levantamento de Sinistros de Trânsito - Brasil vs Paraíba', 
            ha='center', va='center', fontsize=12, style='italic', 
            color=DETRAN_LIGHT)
    ax.text(5, 25.5, 'DETRAN-PB | Demanda: DEMANDA-DETRAN-001 | Data: 07/03/2026', 
            ha='center', va='center', fontsize=9, 
            color='gray')
    
    # ==================== NÍVEL 1: SOLICITAÇÃO ====================
    def draw_box(ax, x, y, width, height, text, color, fontsize=10, fontweight='normal'):
        """Função auxiliar para desenhar caixas"""
        box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                            boxstyle="round,pad=0.1", 
                            edgecolor=color, facecolor=color, 
                            alpha=0.8, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', 
               fontsize=fontsize, fontweight=fontweight, 
               color='white', wrap=True)
    
    def draw_arrow(ax, x1, y1, x2, y2, color=DETRAN_BLUE, width=2):
        """Função auxiliar para desenhar setas"""
        arrow = FancyArrowPatch((x1, y1), (x2, y2),
                               arrowstyle='->', mutation_scale=30, 
                               linewidth=width, color=color)
        ax.add_patch(arrow)
    
    # Nível 1: Solicitação
    y_nivel1 = 24
    draw_box(ax, 5, y_nivel1, 3, 0.8, 
            'SOLICITAÇÃO RECEBIDA\nMailson Soares da Silva\nAgente DETRAN', 
            DETRAN_BLUE, fontsize=9, fontweight='bold')
    
    # ==================== NÍVEL 2: ANÁLISE INICIAL ====================
    y_nivel2 = 22.5
    
    # Seta para análise
    draw_arrow(ax, 5, y_nivel1 - 0.4, 5, y_nivel2 + 0.4)
    
    draw_box(ax, 5, y_nivel2, 3.5, 0.8,
            'ANÁLISE INICIAL DA DEMANDA\nEscopo: Sinistros 2024-2025\nGeografia: Brasil vs Paraíba',
            DETRAN_LIGHT, fontsize=9, fontweight='bold')
    
    # ==================== NÍVEL 3: ETAPAS DE COLETA ====================
    y_nivel3 = 20.5
    
    # Seta para coleta
    draw_arrow(ax, 5, y_nivel2 - 0.4, 5, y_nivel3 + 1.2)
    
    # Título da seção
    ax.text(5, y_nivel3 + 1.5, 'ETAPA 1: COLETA DE DADOS', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    # Três colunas de coleta
    coletas = [
        (2, 'DADOS BRASIL\n• Sinistros totais\n• Classificação por\n  tipo de transporte\n• Análise demográfica'),
        (5, 'DADOS PARAÍBA\n• Sinistros totais\n• Cidade com maior\n  incidência\n• Status de habilitação'),
        (8, 'DADOS COMPLEMENTARES\n• Fontes oficiais\n  DETRAN/Brasil\n• Validação cruzada\n• Tratamento de dados')
    ]
    
    for x, texto in coletas:
        draw_box(ax, x, y_nivel3, 2.5, 1.2, texto, WARNING_COLOR, fontsize=8)
        draw_arrow(ax, 5, y_nivel2 - 0.4, x, y_nivel3 + 0.6, color=ACCENT_COLOR)
    
    # ==================== NÍVEL 4: PROCESSAMENTO ====================
    y_nivel4 = 18
    
    # Setas convergentes
    for x in [2, 5, 8]:
        draw_arrow(ax, x, y_nivel3 - 0.6, 5, y_nivel4 + 0.5, color=ACCENT_COLOR)
    
    ax.text(5, y_nivel4 + 1, 'ETAPA 2: PROCESSAMENTO E ESTRUTURAÇÃO', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    draw_box(ax, 5, y_nivel4, 4, 1,
            'PROCESSAMENTO DE DADOS\n• Limpeza e validação\n• Estruturação em categorias\n• Análise comparativa Brasil vs Paraíba',
            DETRAN_LIGHT, fontsize=9, fontweight='bold')
    
    # ==================== NÍVEL 5: ANÁLISE ====================
    y_nivel5 = 16
    
    draw_arrow(ax, 5, y_nivel4 - 0.5, 5, y_nivel5 + 0.6)
    
    ax.text(5, y_nivel5 + 1, 'ETAPA 3: ANÁLISE E INDICADORES', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    # Indicadores
    indicadores = [
        (1.5, 'INDICADORES\nNACIONAIS\n• Total sinistros\n• Tendências'),
        (3.5, 'INDICADORES\nESTADUAIS\n• Total Paraíba\n• Cidade crítica'),
        (5.5, 'INDICADORES\nDEMOGRÁFICOS\n• Gênero\n• Habilitação'),
        (7.5, 'INDICADORES\nVEICULARES\n• Tipo transporte\n• Classificação')
    ]
    
    for x, texto in indicadores:
        draw_box(ax, x, y_nivel5, 1.8, 1, texto, SUCCESS_COLOR, fontsize=8)
        draw_arrow(ax, 5, y_nivel4 - 0.5, x, y_nivel5 + 0.5, color=SUCCESS_COLOR)
    
    # ==================== NÍVEL 6: RELATÓRIO ====================
    y_nivel6 = 13.5
    
    # Setas convergentes
    for x in [1.5, 3.5, 5.5, 7.5]:
        draw_arrow(ax, x, y_nivel5 - 0.5, 5, y_nivel6 + 0.5, color=SUCCESS_COLOR)
    
    ax.text(5, y_nivel6 + 1.2, 'ETAPA 4: GERAÇÃO DE RELATÓRIO', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    draw_box(ax, 5, y_nivel6, 4.5, 1.2,
            'RELATÓRIO COMPARATIVO\n• Tabelas comparativas Brasil vs Paraíba\n• Gráficos de tendências\n• Análise por categoria (transporte, gênero, habilitação)',
            DETRAN_LIGHT, fontsize=9, fontweight='bold')
    
    # ==================== NÍVEL 7: ENTREGA ====================
    y_nivel7 = 11.5
    
    draw_arrow(ax, 5, y_nivel6 - 0.6, 5, y_nivel7 + 0.5)
    
    ax.text(5, y_nivel7 + 1, 'ETAPA 5: ENTREGA E VALIDAÇÃO', 
           ha='center', fontsize=11, fontweight='bold', 
           color=ACCENT_COLOR)
    
    draw_box(ax, 5, y_nivel7, 4.5, 1,
            'PRODUTOS FINAIS\n• Relatório em PDF\n• Planilhas com dados estruturados\n• Apresentação executiva',
            SUCCESS_COLOR, fontsize=9, fontweight='bold')
    
    # ==================== TIMELINE ====================
    y_timeline = 9.5
    
    draw_arrow(ax, 5, y_nivel7 - 0.5, 5, y_timeline + 0.8)
    
    ax.text(5, y_timeline + 1.2, 'CRONOGRAMA DE EXECUÇÃO', 
           ha='center', fontsize=11, fontweight='bold', 
           color=DETRAN_BLUE)
    
    # Timeline
    timeline_items = [
        (1.5, 'DIA 1-2\nColeta de dados\nfonte oficial'),
        (3.5, 'DIA 2-3\nProcessamento\ne limpeza'),
        (5.5, 'DIA 3-4\nAnálise e\nindicadores'),
        (7.5, 'DIA 4-5\nRelatório e\nvalidação')
    ]
    
    for x, texto in timeline_items:
        draw_box(ax, x, y_timeline, 1.6, 0.9, texto, DETRAN_BLUE, fontsize=8)
        if x > 1.5:
            draw_arrow(ax, x - 1.2, y_timeline, x - 0.8, y_timeline, 
                      color=DETRAN_BLUE, width=2)
    
    # ==================== RESPONSABILIDADES ====================
    y_resp = 7
    
    ax.text(5, y_resp + 0.8, 'RESPONSABILIDADES E PAPÉIS', 
           ha='center', fontsize=11, fontweight='bold', 
           color=DETRAN_BLUE)
    
    responsabilidades = [
        (2, 'SOLICITANTE\nMailson Soares\n(Agente DETRAN)\n• Validar escopo\n• Revisar resultados'),
        (5, 'ANALISTA DE DADOS\nDiogo Rego\n(Estagiário UFPB)\n• Coletar dados\n• Processar\n• Gerar relatório'),
        (8, 'SUPERVISOR\nCoronel Valter Lins\n(DETRAN-PB)\n• Orientação\n• Aprovação final')
    ]
    
    for x, texto in responsabilidades:
        draw_box(ax, x, y_resp - 1.2, 2.5, 1.8, texto, DETRAN_LIGHT, fontsize=8)
    
    # ==================== INDICADORES DE QUALIDADE ====================
    y_qualidade = 3.5
    
    ax.text(5, y_qualidade + 0.8, 'INDICADORES DE QUALIDADE E CONFORMIDADE', 
           ha='center', fontsize=11, fontweight='bold', 
           color=DETRAN_BLUE)
    
    qualidade_items = [
        (1.5, '✓ Rastreabilidade\nCompleta'),
        (3.5, '✓ Dados de Fonte\nOficial'),
        (5.5, '✓ Validação\nCruzada'),
        (7.5, '✓ Documentação\nAuditável')
    ]
    
    for x, texto in qualidade_items:
        draw_box(ax, x, y_qualidade - 0.8, 1.8, 0.8, texto, SUCCESS_COLOR, fontsize=8)
    
    # ==================== RODAPÉ ====================
    ax.text(5, 0.5, 'Autor: Diogo Rego - Estagiário em Estatística (UFPB) | Contato: diogo.silva.rego@academico.ufpb.br | (83) 99955-6330', 
           ha='center', fontsize=8, style='italic', color='gray')
    ax.text(5, 0.1, 'DETRAN-PB | Demanda DEMANDA-DETRAN-001 | Gerado em 07/03/2026', 
           ha='center', fontsize=8, color='gray')
    
    # Ajustar layout
    plt.tight_layout()
    
    # Salvar figura
    plt.savefig('/home/ubuntu/organograma_demanda_detran.png', 
               dpi=300, bbox_inches='tight', facecolor='white')
    print("✅ Organograma salvo: /home/ubuntu/organograma_demanda_detran.png")
    
    plt.savefig('/home/ubuntu/organograma_demanda_detran.pdf', 
               dpi=300, bbox_inches='tight', facecolor='white')
    print("✅ Organograma salvo: /home/ubuntu/organograma_demanda_detran.pdf")
    
    plt.close()

if __name__ == "__main__":
    print("=" * 70)
    print("GERADOR DE ORGANOGRAMA - DEMANDA DETRAN-PB")
    print("=" * 70)
    print("\n📊 Gerando organograma profissional...")
    print("   - Dados reais da demanda de sinistros de trânsito")
    print("   - Logo do DETRAN-PB integrada")
    print("   - Passo a passo completo")
    print("   - Responsabilidades definidas")
    print("   - Cronograma de execução")
    print("\n")
    
    criar_organograma()
    
    print("\n" + "=" * 70)
    print("✅ ORGANOGRAMA GERADO COM SUCESSO!")
    print("=" * 70)
    print("\n📁 Arquivos gerados:")
    print("   1. organograma_demanda_detran.png (Imagem de alta resolução)")
    print("   2. organograma_demanda_detran.pdf (Documento PDF)")
    print("\n📋 Conteúdo do organograma:")
    print("   ✓ Solicitação inicial")
    print("   ✓ Análise da demanda")
    print("   ✓ Etapa 1: Coleta de dados (Brasil, Paraíba, Complementares)")
    print("   ✓ Etapa 2: Processamento e estruturação")
    print("   ✓ Etapa 3: Análise e indicadores")
    print("   ✓ Etapa 4: Geração de relatório")
    print("   ✓ Etapa 5: Entrega e validação")
    print("   ✓ Cronograma de execução (5 dias)")
    print("   ✓ Responsabilidades e papéis")
    print("   ✓ Indicadores de qualidade")
    print("\n👤 Autoria:")
    print("   Diogo Rego - Estagiário em Estatística (UFPB)")
    print("   Email: diogo.silva.rego@academico.ufpb.br")
    print("   Telefone: (83) 99955-6330")
    print("\n" + "=" * 70)
