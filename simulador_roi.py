import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(page_title="LB DIGITAL - Simulador de ROI", layout="centered")

# Sidebar com instruções
st.sidebar.markdown("### 📘 Como usar o simulador")
st.sidebar.markdown("""
Preencha os campos abaixo com os dados da sua campanha de tráfego pago:

1. **Investimento total**: quanto será investido em anúncios  
2. **CPC médio**: custo médio por clique no anúncio  
3. **Taxa de conversão**: porcentagem estimada de pessoas que compram  
4. **Ticket médio**: valor do seu produto ou serviço  
                    
Após preencher, os resultados aparecem automaticamente.
""")

# Título principal
st.subheader("📈 Simulador de ROI - LB DIGITAL")

# Entradas
investimento = st.number_input("💰 Investimento total (R$)", min_value=0.0, step=10.0, format="%.2f")
cpc = st.number_input("🖱️ CPC médio (R$)", min_value=0.01, step=0.01, format="%.2f")
taxa_conversao = st.slider("🎯 Taxa de conversão (%)", min_value=0.1, max_value=100.0, value=2.0, step=0.1)
ticket_medio = st.number_input("🛒 Ticket médio por venda (R$)", min_value=1.0, step=1.0, format="%.2f")

# Cálculos e exibição de resultados
if investimento > 0 and cpc > 0 and ticket_medio > 0:
    cliques = investimento / cpc
    conversoes = cliques * (taxa_conversao / 100)
    faturamento = conversoes * ticket_medio
    roas = faturamento / investimento
    lucro = faturamento - investimento

    st.markdown("---")
    st.subheader("📊 Resultados Simulados")
    st.metric("📌 Cliques estimados", f"{cliques:.0f}")
    st.metric("📌 Conversões estimadas", f"{conversoes:.0f}")
    st.metric("📌 Faturamento estimado", f"R$ {faturamento:,.2f}")
    st.metric("📌 ROAS", f"{roas:.2f}x")
    st.metric("📌 Lucro estimado", f"R$ {lucro:,.2f}")

    # Gráfico com Altair
    df_grafico = pd.DataFrame({
        'Categoria': ['Investimento', 'Faturamento Estimado', 'Lucro Estimado'],
        'Valor': [investimento, faturamento, lucro]
    })

    grafico = alt.Chart(df_grafico).mark_bar().encode(
        x=alt.X('Categoria', sort=None),
        y='Valor',
        color=alt.Color('Categoria', legend=None)
    ).properties(
        title='📊 Comparativo Financeiro',
        width=600,
        height=400
    )

    st.altair_chart(grafico)

else:
    st.warning("Preencha todos os campos acima para ver os resultados.")
