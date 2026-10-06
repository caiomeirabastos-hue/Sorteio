import streamlit as st
import random

# Senha do administrador
SENHA_ADMIN = "123456"

# Lista inicial de participantes
if "participantes" not in st.session_state:
    st.session_state.participantes = []

if "sorteados" not in st.session_state:
    st.session_state.sorteados = []

st.set_page_config(
    page_title="Sorteio de Nomes",
    page_icon="🎲",
    layout="centered"
)

st.title("🎲 Sorteio de Participantes")

aba1, aba2 = st.tabs(["🎁 Sorteio", "⚙️ Administração"])

# =====================================================
# ÁREA DE SORTEIO
# =====================================================
with aba1:

    st.subheader("Sorteio")

    restantes = [
        nome for nome in st.session_state.participantes
        if nome not in st.session_state.sorteados
    ]

    st.metric("Participantes restantes", len(restantes))

    if st.button("🎲 Sortear Nome", use_container_width=True):

        if not restantes:
            st.error("Não existem mais participantes disponíveis.")
        else:
            vencedor = random.choice(restantes)
            st.session_state.sorteados.append(vencedor)

            st.success("Nome sorteado:")
            st.markdown(
                f"<h1 style='text-align:center;color:green'>{vencedor}</h1>",
                unsafe_allow_html=True
            )

# =====================================================
# ADMIN
# =====================================================
with aba2:

    st.subheader("Administração")

    senha = st.text_input(
        "Senha",
        type="password"
    )

    if senha == SENHA_ADMIN:

        st.success("Acesso liberado")

        nomes = st.text_area(
            "Digite um nome por linha",
            height=200
        )

        if st.button("Salvar Participantes"):

            lista = [
                x.strip()
                for x in nomes.split("\n")
                if x.strip()
            ]

            st.session_state.participantes = lista
            st.session_state.sorteados = []

            st.success(
                f"{len(lista)} participantes cadastrados."
            )

        st.divider()

        st.write("### Participantes")

        st.write(st.session_state.participantes)

        st.divider()

        st.write("### Já sorteados")

        st.write(st.session_state.sorteados)

        if st.button("🔄 Reiniciar Sorteio"):

            st.session_state.sorteados = []

            st.success(
                "Sorteio reiniciado."
            )

    elif senha:
        st.error("Senha incorreta.")