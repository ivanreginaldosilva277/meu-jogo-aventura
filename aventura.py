import streamlit as st

st.set_page_config(page_title="Minha Aventura Kids", page_icon="🌈", layout="centered")

# --- 1. Tela de Início (Escolha do Personagem) ---
if 'nome_jogador' not in st.session_state:
    st.markdown("<h1 style='text-align: center;'>🌟 Hora da Aventura!</h1>", unsafe_allow_html=True)
    nome = st.text_input("Qual o seu nome?")
    avatar = st.radio("Escolha quem você quer ser:", ["🤠 Explorador", "👩‍🌾 Exploradora", "🚀 Astronauta", "✨ Fada"])
    
    if st.button("ENTRAR NO MUNDO! 🚀"):
        if nome:
            st.session_state.nome_jogador = nome
            st.session_state.avatar = avatar
            st.session_state.x, st.session_state.y = 1, 1
            st.session_state.mochila = []
            st.rerun()
        else:
            st.warning("Escreva seu nome primeiro! 😊")
    st.stop()

# --- 2. Dados do Mundo ---
lugares = {
    (1, 1): {"n": "Praça Central", "item": "Moeda 🪙", "img": "https://freepik.com"},
    (1, 0): {"n": "Floresta Encantada", "item": "Graveto ✨", "img": "https://freepik.com"},
    (1, 2): {"n": "Parquinho", "item": "Bola ⚽", "img": "https://freepik.com"},
    (0, 1): {"n": "Sua Casinha", "item": "Lanche 🍎", "img": "https://freepik.com"},
    (2, 1): {"n": "Loja de Brinquedos", "item": "Ursinho 🧸", "img": "https://freepik.com"},
}

local = lugares.get((st.session_state.x, st.session_state.y), {"n": "Estrada", "item": None, "img": "https://freepik.com"})

# --- 3. Visual do Personagem "Caminhando" ---
st.markdown(f"### 📍 {st.session_state.nome_jogador} está em: {local['n']}")

# Mostra a imagem do lugar
st.image(local['img'], use_container_width=True)

# Faz o bonequinho aparecer "em cima" de um palco
st.markdown(f"<div style='text-align: center; font-size: 80px; margin-top: -60px;'>{st.session_state.avatar.split()[-1]}</div>", unsafe_allow_html=True)

# --- 4. Interação e Movimento ---
if local['item'] and local['item'] not in st.session_state.mochila:
    if st.button(f"🎁 Pegar {local['item']}", use_container_width=True):
        st.session_state.mochila.append(local['item'])
        st.balloons()
        st.rerun()

st.write("---")
c1, c2, c3 = st.columns([1,1,1])
with c2:
    if st.button("⬆️ Subir"): st.session_state.y -= 1; st.rerun()
c1, c2, c3 = st.columns([1,1,1])
with c1:
    if st.button("⬅️ Esquerda"): st.session_state.x -= 1; st.rerun()
with c3:
    if st.button("Direita ➡️"): st.session_state.x += 1; st.rerun()
with c2:
    if st.button("⬇️ Descer"): st.session_state.y += 1; st.rerun()

# Mochila lateral
with st.sidebar:
    st.header(f"🎒 Mochila de {st.session_state.nome_jogador}")
    for i in st.session_state.mochila: st.write(f"✅ {i}")
    if st.button("Recomeçar Jogo"): st.session_state.clear(); st.rerun()
