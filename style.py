/* ======================================
   RESET E CONFIGURAÇÕES GERAIS
   ====================================== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --cor-primaria: #2563eb;
    --cor-secundaria: #1e40af;
    --cor-destaque: #f59e0b;
    --cor-fundo: #f0f4f8;
    --cor-texto: #374151;
    --cor-branca: #ffffff;
    --sombra: 0 4px 6px rgba(0, 0, 0, 0.1);
    --sombra-forte: 0 10px 25px rgba(0, 0, 0, 0.15);
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: var(--cor-fundo);
    color: var(--cor-texto);
    line-height: 1.6;
}

a {
    text-decoration: none;
    color: inherit;
}

ul {
    list-style: none;
}

img {
    max-width: 100%;
    height: auto;
}

/* ======================================
   BARRA DE NAVEGAÇÃO
   ====================================== */
.navbar {
    background-color: var(--cor-branca);
    box-shadow: var(--sombra);
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 100;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 5%;
}

.logo-texto {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--cor-primaria);
}

.nav-links {
    display: flex;
    gap: 30px;
}

.nav-links a {
    font-weight: 500;
    color: var(--cor-texto);
    transition: color 0.3s;
}

.nav-links a:hover {
    color: var(--cor-primaria);
}

/* ======================================
   HERO / CABEÇALHO
   ====================================== */
.hero {
    margin-top: 70px;
    padding: 60px 5%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    min-height: 90vh;
    background: linear-gradient(135deg, #e0e7ff 0%, #dbeafe 100%);
}

.hero-conteudo {
    flex: 1;
    max-width: 600px;
}

.hero h1 {
    font-size: 3rem;
    color: var(--cor-secundaria);
    margin-bottom: 15px;
    line-height: 1.2;
}

.destaque {
    color: var(--cor-primaria);
}

.subtitulo {
    font-size: 1.3rem;
    color: var(--cor-primaria);
    font-weight: 600;
    margin-bottom: 10px;
}

.descricao {
    font-size: 1.1rem;
    margin-bottom: 30px;
    color: #4b5563;
}

.botoes {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

.btn {
    padding: 14px 30px;
    border-radius: 8px;
    font-weight: bold;
    transition: transform 0.3s, box-shadow 0.3s;
    display: inline-block;
}

.btn-principal {
    background-color: var(--cor-primaria);
    color: white;
}

.btn-principal:hover {
    background-color: var(--cor-secundaria);
    transform: translateY(-3px);
    box-shadow: var(--sombra-forte);
}

.btn-secundario {
    background-color: transparent;
    color: var(--cor-primaria);
    border: 2px solid var(--cor-primaria);
}

.btn-secundario:hover {
    background-color: var(--cor-primaria);
    color: white;
    transform: translateY(-3px);
}

.hero-imagem {
    flex: 1;
    display: flex;
    justify-content: center;
}

.hero-imagem img {
    max-width: 400px;
    animation: flutuar 3s ease-in-out infinite;
}

@keyframes flutuar {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
}

/* ======================================
   SEÇÕES GERAIS
   ====================================== */
.secao {
    padding: 80px 5%;
    max-width: 1200px;
    margin: 0 auto;
}

.titulo-secao {
    text-align: center;
    font-size: 2.2rem;
    color: var(--cor-secundaria);
    margin-bottom: 10px;
    position: relative;
}

.titulo-secao::after {
    content: '';
    display: block;
    width: 80px;
    height: 4px;
    background-color: var(--cor-destaque);
    margin: 10px auto 0;
    border-radius: 2px;
}

.subtitulo-secao {
    text-align: center;
    color: #6b7280;
    margin-bottom: 50px;
    font-size: 1.1rem;
}

/* ======================================
   SOBRE MIM
   ====================================== */
.sobre-conteudo {
    display: flex;
    gap: 50px;
    flex-wrap: wrap;
}

.sobre-texto {
    flex: 2;
    min-width: 300px;
}

.sobre-texto p {
    margin-bottom: 15px;
    font-size: 1.05rem;
}

.sobre-info {
    flex: 1;
    min-width: 250px;
    background-color: var(--cor-branca);
    padding: 25px;
    border-radius: 12px;
    box-shadow: var(--sombra);
}

.info-item {
    padding: 12px 0;
    border-bottom: 1px solid #e5e7eb;
}

.info-item:last-child {
    border-bottom: none;
}

/* ======================================
   HABILIDADES
   ====================================== */
.habilidades-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 25px;
}

.habilidade-card {
    background-color: var(--cor-branca);
    padding: 30px 25px;
    border-radius: 12px;
    box-shadow: var(--sombra);
    transition: transform 0.3s;
}

.habilidade-card:hover {
    transform: translateY(-8px);
}

.habilidade-card h3 {
    font-size: 1.3rem;
    margin-bottom: 10px;
    color: var(--cor-secundaria);
}

.habilidade-card p {
    margin-bottom: 15px;
    color: #6b7280;
}

.barra-progresso {
    height: 10px;
    background-color: #e5e7eb;
    border-radius: 5px;
    overflow: hidden;
}

.progresso {
    height: 100%;
    border-radius: 5px;
    transition: width 1s ease-in-out;
}

.html { width: 60%; background-color: #f97316; }
.css { width: 40%; background-color: #3b82f6; }
.logica { width: 50%; background-color: #10b981; }
.js { width: 10%; background-color: #eab308; }

/* ======================================
   PROJETOS
   ====================================== */
.projetos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
}

.projeto-card {
    background-color: var(--cor-branca);
    padding: 30px 25px;
    border-radius: 12px;
    box-shadow: var(--sombra);
    transition: transform 0.3s, box-shadow 0.3s;
}

.projeto-card:hover {
    transform: translateY(-10px);
    box-shadow: var(--sombra-forte);
}

.projeto-card h3 {
    font-size: 1.3rem;
    margin-bottom: 12px;
    color: var(--cor-secundaria);
}

.projeto-card p {
    margin-bottom: 15px;
    color: #6b7280;
}

.tag {
    display: inline-block;
    background-color: var(--cor-primaria);
    color: white;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 0.85rem;
}

/* ======================================
   CONTATO
   ====================================== */
.contato-form {
    max-width: 600px;
    margin: 0 auto 50px;
    background-color: var(--cor-branca);
    padding: 40px;
    border-radius: 12px;
    box-shadow: var(--sombra);
}

.contato-form label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: var(--cor-secundaria);
}

.contato-form input,
.contato-form textarea {
    width: 100%;
    padding: 14px;
    margin-bottom: 20px;
    border: 2px solid #e5e7eb;
    border-radius: 8px;
    font-size: 1rem;
    transition: border-color 0.3s;
}

.contato-form input:focus,
.contato-form textarea:focus {
    outline: none;
    border-color: var(--cor-primaria);
}

.contato-form textarea {
    min-height: 120px;
    resize: vertical;
}

.btn-enviar {
    background-color: var(--cor-primaria);
    color: white;
    padding: 14px 30px;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s;
    width: 100%;
}

.btn-enviar:hover {
    background-color: var(--cor-secundaria);
}

.contato-info {
    text-align: center;
    font-size: 1.1rem;
    line-height: 2;
}

/* ======================================
   RODAPÉ
   ====================================== */
.rodape {
    background-color: var(--cor-secundaria);
    color: white;
    text-align: center;
    padding: 40px 20px;
    margin-top: 50px;
}

.rodape p {
    margin-bottom: 10px;
}

/* ======================================
   RESPONSIVIDADE (CELULAR)
   ====================================== */
@media (max-width: 768px) {
    .navbar {
        flex-direction: column;
        gap: 10px;
        padding: 10px;
    }

    .nav-links {
        gap: 15px;
    }

    .hero {
        flex-direction: column;
        text-align: center;
        padding-top: 40px;
    }

    .hero h1 {
        font-size: 2rem;
    }

    .botoes {
        justify-content: center;
    }

    .sobre-conteudo {
        flex-direction: column;
    }
}