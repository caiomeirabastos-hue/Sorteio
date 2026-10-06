import streamlit as st
import random
import json
import os

# ==========================================
# CONFIGURAÇÕES
# ==========================================

ARQUIVO = "comunidades.json"
SENHA_ADMIN = "123456"

st.set_page_config(
    page_title="Sorteio de Comunidades",
    page_icon="🙏",
    layout="centered"
)

# ==========================================
# FUNÇÕES
# ==========================================

def carregar_comunidades():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_comunidades(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)


# Inicialização
if "historico" not in st.session_state:
    st.session_state.historico = []

# Carrega comunidades
comunidades = carregar_comunidades()

# ==========================================
# TÍTULO
# ==========================================

st.title("🙏 Sorteio de Comunidades")
st.caption("Clique no botão e receba uma comunidade para sua oração.")

aba1, aba2 = st.tabs(
    ["🎁 Sorteio", "⚙️ Administração"]
)

# ==========================================
# ABA SORTEIO
# ==========================================

with aba1:

    st.markdown("### Faça seu sorteio")

    st.metric(
        "Comunidades cadastradas",
        len(comunidades)
    )

    st.write("")

    if st.button(
        "🙏 Sortear Comunidade",
        use_container_width=True
    ):

        if not comunidades:

            st.error(
                "Nenhuma comunidade cadastrada."
            )

        else:

            sorteada = random.choice(
                comunidades
            )

            st.balloons()

            st.success(
                "Comunidade Sorteada"
            )

            st.markdown(
                f"""
                <div style="
                    background-color:#f2f2f2;
                    padding:30px;
                    border-radius:15px;
                    text-align:center;
                    border:2px solid #4CAF50;
                ">
                    <h1 style="
                        color:#2E8B57;
                        margin:0;
                    ">
                        {sorteada}
                    </h1>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.session_state.historico.append(
                sorteada
            )

# ==========================================
# ABA ADMIN
# ==========================================

with aba2:

    st.subheader("Área Administrativa")

    senha = st.text_input(
        "Senha do administrador",
        type="password"
    )

    if senha == SENHA_ADMIN:

        st.success("Acesso autorizado")

        st.divider()

        nomes = st.text_area(
            "Digite uma comunidade por linha",
            height=200,
            placeholder="""
Comunidade São José
Comunidade Santa Luzia
Comunidade Santo Antônio
"""
        )

        if st.button(
            "💾 Salvar Comunidades",
            use_container_width=True
        ):

            lista = [
                nome.strip()
                for nome in nomes.split("\n")
                if nome.strip()
            ]

            salvar_comunidades(lista)

            st.success(
                f"{len(lista)} comunidades salvas com sucesso."
            )

            st.rerun()

        st.divider()

        st.subheader("📋 Comunidades Cadastradas")

        if comunidades:

            for i, comunidade in enumerate(comunidades):

                col1, col2 = st.columns([8, 2])

                with col1:
                    st.write(comunidade)

                with col2:

                    if st.button(
                        "🗑️",
                        key=f"del_{i}"
                    ):

                        comunidades.remove(comunidade)
                        salvar_comunidades(comunidades)
                        st.rerun()

        else:
            st.info(
                "Nenhuma comunidade cadastrada."
            )

        st.divider()

        st.subheader("📊 Estatísticas")

        st.metric(
            "Total de Comunidades",
            len(comunidades)
        )

        st.metric(
            "Total de Sorteios",
            len(st.session_state.historico)
        )

        st.divider()

        if st.button(
            "🧹 Limpar Todas as Comunidades",
            use_container_width=True
        ):

            salvar_comunidades([])

            st.success(
                "Todas as comunidades foram removidas."
            )

            st.rerun()

    elif senha:
        st.error("Senha incorreta.")
            

    elif senha:
        st.error("Senha incorreta.")
