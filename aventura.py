import streamlit as st

st.set_page_config(page_title="Minha Aventura Visual", page_icon="🌈")

# --- PASSO NOVO: Criar o Personagem ---
if 'nome_jogador' not in st.session_state:
    st.markdown("<h1 style='text-align: center;'>Oi! Vamos Jogar?</h1>", unsafe_allow_html=True)
    st.write("### Primeiro, como você se chama?")
    nome = st.text_input("Digite seu nome aqui:")
    
    st.write("### Escolha seu personagem:")
    avatar = st.radio("Quem você quer ser?", ["Explorador 🤠", "Exploradora 👩‍🌾", "Astronauta 🚀", "Fada ✨"])
    
    if st.button("Começar Aventura! 🚀"):
        if nome:
            st.session_state.nome_jogador = nome
            st.session_state.avatar = avatar
            st.session_state.x = 1
            st.session_state.y = 1
            st.session_state.mochila = []
            st.rerun()
        else:
            st.warning("Por favor, digite seu nome para começar!")
    st.stop() # Para o código aqui até a criança clicar no botão

# --- DAQUI PARA BAIXO É O JOGO (Só aparece após escolher o nome) ---

st.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>🌈 Vila de {st.session_state.nome_jogador}</h1>", unsafe_allow_html=True)

# Imagens dos lugares (as mesmas de antes)
lugares = {
    (1, 1): {"nome": "Praça Central", "emoji": "⛲", "item": "Moeda de Ouro 🪙", "img": "https://freepik.com"},
    (1, 0): {"nome": "Floresta Encantada", "emoji": "🌲", "item": "Graveto Mágico ✨", "img": "https://freepik.com"},
    (1, 2): {"nome": "Parquinho Kids", "emoji": "🎡", "item": "Bola Colorida ⚽", "img": "https://freepik.com"},
    (0, 1): {"nome": "Sua Casinha", "emoji": "🏠", "item": "Lanche 🍎", "img": "https://freepik.com"},
    (2, 1): {"nome": "Loja de Brinquedos", "emoji": "🛍️", "item": "Brinquedo 🧸", "img": "https://freepik.com"},
}

local_atual = lugares.get((st.session_state.x, st.session_state.y), {"nome": "Estrada", "emoji": "🛤️", "item": None, "img": "https://freepik.com"})

st.image(local_atual['img'], use_container_width=True)
st.subheader(f"{local_atual['emoji']} {local_atual['nome']}")

# Botão de pegar item
item_daqui = local_atual.get("item")
if item_daqui and item_daqui not in st.session_state.mochila:
    if st.button(f"🎁 Pegar {item_daqui}", use_container_width=True):
        st.session_state.mochila.append(item_daqui)
        st.balloons()
        st.rerun()

st.divider()

# Controles
c1, c2, c3 = st.columns(3)
with c2: 
    if st.button("⬆️", key="up"): st.session_state.y -= 1; st.rerun()
c1, c2, c3 = st.columns(3)
with c1: 
    if st.button("⬅️", key="left"): st.session_state.x -= 1; st.rerun()
with c3: 
    if st.button("➡️", key="right"): st.session_state.x += 1; st.rerun()
with c2: 
    if st.button("⬇️", key="down"): st.session_state.y += 1; st.rerun()

# Barra lateral personalizada
with st.sidebar:
    st.header(f"{st.session_state.avatar}")
    st.write(f"**Jogador:** {st.session_state.nome_jogador}")
    st.divider()
    st.write("### 🎒 Mochila")
    for objeto in st.session_state.mochila:
        st.write(f"✅ {objeto}")
    
    if st.button("Sair do Jogo ❌"):
        st.session_state.clear()
        st.rerun()
