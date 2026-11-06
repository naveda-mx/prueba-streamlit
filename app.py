import streamlit as st

st.title("Simulador de amortización")
st.caption("Ejemplo con abonos iguales a capital e intereses mensuales sobre el saldo pendiente. Sin comisiones.")
principal = st.number_input("Monto del préstamo", 1, 100000000, 12000)
rate = st.number_input("Tasa nominal anual (%)", 0.0, 100.0, 12.0)
months = st.slider("Plazo en meses", 1, 120, 12)
capital = principal / months
rows = []
total_interest = 0.0
for month in range(1, months + 1):
    balance = capital * (months - month + 1)
    interest = balance * rate / 1200
    total_interest += interest
    rows.append({"Mes": month, "Capital": round(capital, 2),
                 "Interés": round(interest, 2), "Pago": round(capital + interest, 2),
                 "Saldo final": round(capital * (months - month), 2)})
st.metric("Intereses totales", f"{total_interest:,.2f}")
st.dataframe(rows, hide_index=True) 
