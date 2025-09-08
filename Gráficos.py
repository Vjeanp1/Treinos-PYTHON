import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


# ---------- Funções auxiliares ----------

def _format_milhar(x, _pos):
    """Formata valores grandes com ponto (ex: 1.290)."""
    return f"{int(x):,}".replace(",", ".")


def _annotate_bars(ax):
    """Mostra valores acima de cada barra."""
    for p in ax.patches:
        valor = p.get_height()
        ax.annotate(
            f"{int(valor):,}".replace(",", "."),
            (p.get_x() + p.get_width() / 2, valor),
            xytext=(0, 5),
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


def _annotate_points(ax, xs, ys):
    """Mostra valores acima de cada ponto no gráfico de linha."""
    for x, y in zip(xs, ys):
        ax.annotate(
            f"{int(y):,}".replace(",", "."),
            (x, y),
            xytext=(0, 5),
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


# ---------- Funções de plotagem ----------

def plot_bar(df, title="Vendas da Semana", save_path=None):
    """Cria gráfico de barras das vendas."""
    plt.figure(figsize=(10, 7))
    ax = plt.gca()
    ax.bar(df["Dias"], df["Venda"])
    ax.set_title(title)
    ax.set_xlabel("Dias")
    ax.set_ylabel("Vendas")
    ax.yaxis.set_major_formatter(FuncFormatter(_format_milhar))

    _annotate_bars(ax)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_line(df, title="Vendas da Semana", save_path=None):
    """Cria gráfico de linha das vendas."""
    plt.figure(figsize=(10, 7))
    ax = plt.gca()
    ax.plot(df["Dias"], df["Venda"], marker="o", linestyle="--")
    ax.set_title(title)
    ax.set_xlabel("Dias")
    ax.set_ylabel("Vendas")
    ax.grid(True)
    ax.yaxis.set_major_formatter(FuncFormatter(_format_milhar))

    _annotate_points(ax, df["Dias"], df["Venda"])
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


# ---------- Carregamento de dados ----------

def carregar_de_excel(caminho_excel: str, sheet_name=0):
    """
    Carrega os dados a partir de um Excel (.xlsx).
    O arquivo precisa ter colunas chamadas 'Dias' e 'Venda'.
    """
    df = pd.read_excel(caminho_excel, sheet_name=sheet_name)
    if not {"Dias", "Venda"}.issubset(df.columns):
        raise ValueError("O Excel precisa ter colunas chamadas 'Dias' e 'Venda'.")
    return df


def carregar_de_csv(caminho_csv: str):
    """
    Carrega os dados a partir de um CSV (.csv).
    O arquivo precisa ter colunas chamadas 'Dias' e 'Venda'.
    """
    df = pd.read_csv(caminho_csv)
    if not {"Dias", "Venda"}.issubset(df.columns):
        raise ValueError("O CSV precisa ter colunas chamadas 'Dias' e 'Venda'.")
    return df


# ---------- Execução principal ----------

if __name__ == "__main__":
    # Escolha UMA das opções abaixo:

    # === OPÇÃO 1: LER DE EXCEL ===
    # df = carregar_de_excel("vendas_semana.xlsx")

    # === OPÇÃO 2: LER DE CSV ===
    df = carregar_de_csv("vendas_semana.csv")

    # Exibe tabela no terminal
    print(df)

    # Gera gráficos
    plot_bar(df, title="Vendas da Semana (Barras)", save_path="vendas_semana_barras.png")
    plot_line(df, title="Vendas da Semana (Linha)", save_path="vendas_semana_linha.png")
