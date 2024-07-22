import streamlit as st
import datetime
import pandas as pd
import random
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
from plotly.subplots import make_subplots
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards

# streamlit run app.py
st.set_page_config(
  page_title="Dashboard Banplus",
  page_icon="💳",
  layout="wide"
)

# set margin top
st.markdown("<style> div[class^='block-container'] { padding-top: 0rem; } </style>",
            unsafe_allow_html=True)
            
# some functions
# formato de tablas
def style_dataframe(df):
  return df.style.set_table_styles( [{'selector': 'th', 'props': [('background-color', '#f0f2f6'),
                                                                  ('color', '#00204e'),
                                                                  ('font-family', 'KaTeX_SansSerif'),
                                                                  ('font-size', '0.8em'),
                                                                  ('text-align','center')]
                                      }, 
                                      {'selector': 'td, th',
                                      'props': [('border', '0.5px solid #c3c8c8'),
                                                ('font-family', 'KaTeX_SansSerif'),
                                                ('font-size', '0.8em'),
                                                ('text-align','center')]
                                      }])
def display_dataframe(df):
  styled_df = style_dataframe(df)
  st.write(styled_df.hide(axis="index").to_html(),unsafe_allow_html=True)

# cards informacion del cliente  
def Cards(rif=False):
  c1, c2, c3, c4, c5 = st.columns(5)
  if not rif:
    c1.metric(label=r"$\textsf{\large \textbf{Razón Social}}$",value=None)
    c2.metric(label=r"$\textsf{\large \textbf{Región}}$",value=None)
    c3.metric(label=r"$\textsf{\large \textbf{Gerente Ejecutivo}}$",value=None)
    c4.metric(label=r"$\textsf{\large \textbf{Oficina}}$",value=None)
    c5.metric(label=r"$\textsf{\large \textbf{Grupo Económico}}$",value=None)
  else:
    c1.metric(label=r"$\textsf{\large \textbf{Razón Social}}$",value=random.choice(['Forum','Farmatodo','Nestle']))
    c2.metric(label=r"$\textsf{\large \textbf{Región}}$",value=random.choice(['Central','Occidental','Oriental']))
    c3.metric(label=r"$\textsf{\large \textbf{Gerente Ejecutivo}}$",value=random.choice(['Armando Gomes','Jose Coello','Juan Pocaterra']))
    c4.metric(label=r"$\textsf{\large \textbf{Oficina}}$",value=random.choice(['La Noria','Las Mercedes','Los Palos Grandes']))
    c5.metric(label=r"$\textsf{\large \textbf{Grupo Económico}}$",value=random.choice(['Retail','Distribuidora','Productora']))
  style_metric_cards(background_color="#ffffff", border_left_color='#00204e')  
  css_metric = """
  <style>
  .st-emotion-cache-1wivap2 {
      font-size:1.2rem;
      font-family:KaTeX_SansSerif;
  }
  </style>"""
  st.markdown(css_metric, unsafe_allow_html=True)

# set logo sidebar
logo = """
  <style>.img {
    float:left;
    padding:5px;
    width:276px;
    height:96px;
  }</style>
  <img class = 'img' src="https://storage.googleapis.com/vikua-styles/banplus-styles/logo_banplus_white.png">"""
st.sidebar.markdown(logo, unsafe_allow_html=True)
st.sidebar.write('\n')
st.sidebar.write('\n')

# set main menu sidebar
with st.sidebar:
  menu = option_menu(None, ["Inicio", "Entradas y Salidas", "Accionistas", "Comportamiento"],
        icons=['file-play-fill', 'calculator-fill', "people-fill", 'clipboard-data-fill'], 
        menu_icon="cast", default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#00204e", "font-size": "16px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "font-color":"green"},
            "nav-link-selected": {"background-color": "rgb(105,190,40)"},
            }
          )
st.sidebar.write('\n')
st.sidebar.write('\n')
reset = st.sidebar.button("Reset", type="primary")
if reset:
  for key in st.session_state.keys():
    del st.session_state[key]

####################### CSS custom
# css_input = """
#     <style>
#     .st-bb {
#         background-color: #fafafa;
#     }
#     .st-b6 {
#       color:rgb(0,32,78);
#     }
#     </style>"""
# st.markdown(css_input, unsafe_allow_html=True)
# 
titles = """
      <style>.CenterText {
          font-family:KaTeX_SansSerif;
          position:absolute;
          left:24%;
          margin:auto;
      }
      .CenterSection {
        font-family:KaTeX_SansSerif;
        text-align:center;
        margin:auto;
      }
      </style>
      """
st.markdown(titles, unsafe_allow_html=True)
# 
# css_metric = """
#     <style>
#     .st-emotion-cache-1wivap2 {
#         font-size:1.2rem;
#         font-family:KaTeX_SansSerif;
#     }
#     </style>"""
# st.markdown(css_metric, unsafe_allow_html=True)
# 
custom_css = """
    <style>
    .my-header {
        background-color: #f0f2f6;
        text-align:center;
        font-size:1.2em;
        font-family:KaTeX_SansSerif;
        font-weight:bold;
        border: 0.5px solid #c3c8c8;
        border-radius:5px;
    }
    .Header{
        background-color: #f0f2f6;
        text-align:left;
        font-size:1.2em;
        font-family:KaTeX_SansSerif;
        font-weight:bold;
    }
    .sub-header {
        background-color: #f0f2f6;
        text-align:center;
        font-size:1.2em;
        font-family:KaTeX_SansSerif;
        font-weight:bold;
        border: 0.5px solid #c3c8c8;
        border-top:none;
        border-radius:5px;
    }
    .values {
        font-family:KaTeX_SansSerif;
        text-align:center;
        font-size: 1.2rem;
    }
    </style>"""
st.markdown(custom_css, unsafe_allow_html=True)

custom_css2 = """
      <style>
      .st-b7 {
          background-color: #fafafa;
        }
      .st-bc {
          color:rgb(139,141,142);
      }
      </style>"""
st.markdown(custom_css2, unsafe_allow_html=True)

custom_ser = """
    <style>
    .header {
        text-align:left;
        font-size:1.02em;
        font-family:KaTeX_SansSerif;
        font-weight:bold;
    }
    .val {
        font-family:KaTeX_SansSerif;
        text-align:left;
        font-size: 1.02rem;
    }
    .red-val {
        font-family:KaTeX_SansSerif;
        text-align:left;
        font-size: 1.02rem;
        color:#ff0000;
    }
    .val-bold {
        font-family:KaTeX_SansSerif;
        text-align:left;
        font-size:1.2em;
        font-weight:bold;
    }
    .val-red-bold {
        font-family:KaTeX_SansSerif;
        text-align:left;
        font-size:1.2em;
        font-weight:bold;
        color:#ff0000;
    }
    .diff {
        border: 0.5px solid #c3c8c8;
        border-radius:5px;
        font-family:KaTeX_SansSerif;
        text-align:right;
        font-size:1.2em;
        font-weight:bold;
    }
    .negative-diff {
        border: 0.5px solid #c3c8c8;
        border-radius:5px;
        font-family:KaTeX_SansSerif;
        text-align:right;
        font-size:1.2em;
        font-weight:bold;
        color:#ff0000;
    }
    </style>"""
st.markdown(custom_ser, unsafe_allow_html=True)

# configuracion de valores para construir slider user input fecha
fecha = datetime.datetime.now()
mes = fecha.month
year = fecha.year

if mes == 1:
  meses = list(range(1,13))
  years = [year-1]*12
else:
  meses = list(range(mes,13))+list(range(1,mes))
  years = [year-1]*len(range(mes,13)) + [year]*len(range(1,mes))

meses_spanish = {'1':'Ene','2':'Feb','3':'Mar','4':'Abr','5':'May','6':'Jun','7':'Jul','8':'Ago',
                 '9':'Sep','10':'Oct','11':'Nov','12':'Dic'}
 
vector = ['{mes}-{year}'.format(mes=meses_spanish.get(str(meses[i]), 'N/A'), year=years[i]) for i in range(len(meses))]

# main screen en funcion del menu seleccionado
if menu == 'Inicio':
  col1, col2 = st.columns([0.15, 0.85], vertical_alignment="center")
  with col1:
    RIF = st.text_input(r"$\textsf{\Large Ingrese un RIF}$", placeholder='Número de RIF')
    RIF.strip()
    css_input = """
      <style>
      .st-bb {
          background-color: #fafafa;
      }
      .st-b6 {
        color:rgb(0,32,78);
      }
      </style>"""
    st.markdown(css_input, unsafe_allow_html=True)
  # condicion para guardar el rif en la sesion para demas consultas en otros modulos
  if RIF:
    if len(RIF) > 0 and RIF.isnumeric():
      st.session_state['RIF'] = RIF
    else:
      st.error('Número de RIF: "{}" inválido, Ingrese solo número'.format(RIF))
      for key in st.session_state.keys():
        del st.session_state[key]
  with col2:
    datos_cliente = """
      <style>.center_text {
          font-family:KaTeX_SansSerif;
          position:absolute;
          left:24%;
          margin:auto;
      }
      .center_section {
        font-family:KaTeX_SansSerif;
        text-align:center;
        margin:auto;
      }
      </style>
      <h3 class="center_text"> Información del Cliente </h3>
      """
    st.markdown(datos_cliente, unsafe_allow_html=True)
  # show screen without a rif save in the session 
  if not 'RIF' in st.session_state:
    # fila 2 cards con datos del cliente
    Cards()
    # fila tres datos telefono, email, email accionistas
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="my-header">Teléfono</div>', unsafe_allow_html=True)
    c1.markdown('<div class="values">-</div>', unsafe_allow_html=True)
    c2.markdown('<div class="my-header">E-mail</div>', unsafe_allow_html=True)
    c2.markdown('<div class="values">-</div>', unsafe_allow_html=True)
    c3.markdown('<div class="my-header">E-mail Accionista</div>', unsafe_allow_html=True)
    c3.markdown('<div class="values">-</div>', unsafe_allow_html=True)
    # seccion de productos
    st.write('\n')
    st.write('\n')    
    st.markdown('<h3 class="center_section"> Consulta de Saldos Promedios </h3>', unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    col1, col2 = st.columns([0.15, 0.85],vertical_alignment="top")
    with col1:
      # seleccion del usuario de meses a consultar
      mes_inicio = st.selectbox(r"$\textsf{\large Desde}$",vector,0)
      option_vector = vector[vector.index(mes_inicio):]
      mes_fin = st.selectbox(r"$\textsf{\large Hasta}$",option_vector,(len(option_vector)-1))
      period = st.radio(r"$\textsf{\large Gráficar saldos prom.}$",
                        ["Mensual", "Trimestral", "Cuatrimestral", "Semestral"])
      # configuracion de graficas
      if period:
        if period == 'Mensual':
          col = meses
        elif period == 'Trimestral':
          col = [4,3,2,1]*3
          col.sort(reverse=True)
        elif period == 'Cuatrimestral':
          col = [3,2,1]*4
          col.sort(reverse=True)
        else:
          col = [1,2]*6
          col.sort(reverse=True)
          period='Semestral'
    with col2:
      c1, c2, c3 = st.columns([0.03, 0.42, 0.55])
      # creacion del data frame con las fechas a consultar seleccionadas
      f= vector[vector.index(mes_inicio): (vector.index(mes_fin)+1)]
      # val = ['' for i in f]
      val1 = ['' for i in f]
      val2 = ['' for i in f]
      val3 = ['' for i in f]
      saldos = {'Fecha': f, 'Cuenta Bs': val1, 'Cuenta M1':val2,'Cuenta Div. Plus':val3}
      saldos_df = pd.DataFrame(saldos)
      with c2:
        display_dataframe(saldos_df)
      with c3:
        # data
        v1=[None for i in vector]
        v2=[None for i in vector]
        v3=[None for i in vector]
        saldos = {'Fecha':vector,'Cuenta Bs':v1,'Cuenta M1':v2,'Cuenta Div. Plus':v3}
        saldos_df = pd.DataFrame(saldos)
        # configuracion de periodo a graficar (mes, trimestre,...)
        new_cols = {'mes':meses, 'period':col, 'year':years}
        saldos_df = saldos_df.assign(**new_cols)
        if period == 'Mensual':
          saldos_df['meses'] = saldos_df.groupby('period')['mes'].transform(
          lambda x: '{Mes}'.format(Mes=meses_spanish.get(str(list(x)[0])))
          ) +' '+ saldos_df.year.astype(str)
          saldos_df = saldos_df.groupby(['period', 'meses'])[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']].mean()
          saldos_df = saldos_df.reset_index()
          saldos_df = saldos_df.set_index('period')
          saldos_df = saldos_df.loc[col]
          # saldos_df[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']] = saldos_df[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']].round(0).astype(int)
        else:
          saldos_df['meses'] = saldos_df.groupby('period')['mes'].transform(
            lambda x: '{Min}-{Max}'.format(Min=meses_spanish.get(str(list(x)[0])),Max=meses_spanish.get(str(list(x)[-1]))))
          saldos_df = saldos_df.groupby(['period', 'meses'])[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']].mean()
          saldos_df = saldos_df.reset_index()
          saldos_df = saldos_df.set_index('period')
          col2 = [col.index(i) for i in np.unique(col)]
          col2.reverse()
          col2 = np.array(col)[[col2]]
          saldos_df = saldos_df.loc[list(col2[0])]
        
        height=260
        # plot saldos bs
        title='Saldo Promedio {period} Cuenta Bs'.format(period=period)
        fig = px.bar(saldos_df, x='meses', y='Cuenta Bs', text_auto='.2s')
        fig.update_traces(marker_color='rgb(0,152,219)')
        fig.update_layout(title_text=title, title_x=0.5, title_xanchor='center', 
                          title_font_style='normal', title_font_weight='bold',
                          xaxis_title="Meses", yaxis_title="Saldo promedio en Bs",
                          height=height)
        st.plotly_chart(fig)
        # plot saldos divisas
        div_df = saldos_df[['meses','Cuenta M1', 'Cuenta Div. Plus']].melt(id_vars='meses', var_name='Cuenta', value_name='Saldo')
        title = 'Saldo Promedio {period} en Divisas'.format(period=period)
        legend=dict(orientation='h',yanchor='bottom',y=1,xanchor="right",x=0.4)
        fig = px.bar(div_df, x="meses", y="Saldo", color="Cuenta", text_auto='.2s', 
                     color_discrete_sequence=['rgb(105,190,40)', 'rgb(0,152,219)'])
        fig.update_layout(title_text=title, title_x=0.5, title_xanchor='center', 
                          title_font_style='normal', title_font_weight='bold', 
                          legend=legend, xaxis_title="Meses", 
                          yaxis_title="Saldo prom. Divisas", height=height)
        st.plotly_chart(fig)
    # puntos de venta
    st.markdown('<h3 class="center_section"> Facturación POS </h3>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([0.15,0.70,0.1,0.05], vertical_alignment="center")
    # POS activos e inactivos
    with col1:
      period2 = st.radio(r"$\textsf{\large Facturación Total.}$",
                        ["Mensual", "Trimestral", "Cuatrimestral", "Semestral"])
      # configuracion de graficas
      if period2:
        if period2 == 'Mensual':
          column = meses
        elif period2 == 'Trimestral':
          column = [4,3,2,1]*3
          column.sort(reverse=True)
        elif period2 == 'Cuatrimestral':
          column = [3,2,1]*4
          column.sort(reverse=True)
        else:
          column = [1,2]*6
          column.sort(reverse=True)
          period2='Semestral'
    # data frame POS   
    fac_pos = [None for i in vector]
    cant_trx = [None for i in vector]
    pos = {'Fecha':vector,'N_tx':cant_trx,'Fac_pos':fac_pos}
    pos_df = pd.DataFrame(pos)
    # configuracion de periodo a graficar (mes, trimestre,...)
    new_cols2 = {'mes':meses, 'period':column, 'year':years}
    pos_df = pos_df.assign(**new_cols2)
    if period2 == 'Mensual':
      pos_df['meses'] = pos_df.groupby('period')['mes'].transform(
      lambda x: '{Mes}'.format(Mes=meses_spanish.get(str(list(x)[0])))
      ) +' '+ pos_df.year.astype(str)
      pos_df = pos_df.groupby(['period', 'meses'])[['N_tx','Fac_pos']].sum()
      pos_df = pos_df.reset_index()
      pos_df = pos_df.set_index('period')
      pos_df = pos_df.loc[column]
    else:
      pos_df['meses'] = pos_df.groupby('period')['mes'].transform(
        lambda x: '{Min}-{Max}'.format(Min=meses_spanish.get(str(list(x)[0])),Max=meses_spanish.get(str(list(x)[-1]))))
      pos_df = pos_df.groupby(['period', 'meses'])[['N_tx','Fac_pos']].sum()
      pos_df = pos_df.reset_index()
      pos_df = pos_df.set_index('period')
      Col = [column.index(i) for i in np.unique(column)]
      Col.reverse()
      Col = np.array(column)[[Col]]
      pos_df = pos_df.loc[list(Col[0])]
    with col2:
      height=350
      fig = make_subplots(specs=[[{"secondary_y": True}]])
      fig.add_trace(go.Scatter(x=pos_df.meses, y=pos_df.N_tx, name="Nro de Transacciones",
                    mode="lines+markers+text",textposition="bottom right",
                    line=dict(color="#00204e",dash='dash'), text=[f'{int(i):,}'for i in pos_df.N_tx.to_list()],
                    textfont=dict(color="#00204e"), marker=dict(symbol="arrow-bar-down")),secondary_y=True)

      fig.add_trace(go.Bar(x=pos_df.meses, y=pos_df.Fac_pos, name="Monto en Bs", text = [f'Bs {round(i,0):,}' for i in pos_df.Fac_pos.to_list()],
                    marker_color='#0098db'),secondary_y=False)

      fig.update_xaxes(title_text="Mes", type='category')
      legend=dict(orientation='h',yanchor='bottom',y=1,xanchor="right",x=0.3)
      title = 'Facturación {period} POS'.format(period=period2)
      fig.update_layout(title_text=title, title_x=0.5, title_xanchor='center', 
                        title_font_style='normal', title_font_weight='bold',
                        legend=legend,height=height,
                        yaxis=dict(title=dict(text="Facturación en Bs"),side="left"),
                        yaxis2=dict(title=dict(text="Nro de Transacciones"),side="right"))
      st.plotly_chart(fig)
    # POS activos e inactivos
    col3.markdown('<div class="my-header">Activos</div>', unsafe_allow_html=True)
    col4.markdown('<div class="values">0</div>', unsafe_allow_html=True)
    col3.markdown('<div class="sub-header">Inactivos</div>', unsafe_allow_html=True)
    col4.markdown('<div class="values">0</div>', unsafe_allow_html=True)
    col3.markdown('<div class="sub-header">Total</div>', unsafe_allow_html=True)
    col4.markdown('<div class="values">0</div>', unsafe_allow_html=True)
    
    # servicios
    st.markdown('<h3 class="center_section"> Servicios </h3>', unsafe_allow_html=True)
    col1,col2 = st.columns([0.1,0.9],vertical_alignment="top")
    servicios=['BOL PM Divisas','Bolpriaven','Comisión','Depósito Bs','Depósito Divisas','Detalle de Consumo POS por cliente',
               'Domiciliación','Encargo de Confianza','Facturación Adquirencia','LBTR','Liquidaciones de Crédito',
               'Nómina','Pago Móvil','Pago por deudas','PAP Banplus','PAP Otros Bancos','Retiro Bs','Retiro Divisas',
               'Reverso','Servicios de Impuesto (ISLR, SAREN, SENIAT)','Servicios de Telefonía (Digitel, Movistar, CANTV)',
               'Servicios Otros (Corpoelec, Inter, Simple TV)','Tesoreria','Transferencias Internas','Transferencias Otros Bancos',
               'Otros']
    val=['-' for s in servicios]
    ser = {'servicios':servicios, 'montos':val}
    ser_df = pd.DataFrame(ser)
    with col2:
      c1,c2,c3,c4=st.columns([0.25,0.13,0.35,0.13])
      half=len(servicios)/2
      count=1
      for i in range(len(ser_df)):
        if count<=np.ceil(half):
          c1.markdown('<div class="header">{ser}</div>'.format(ser=ser_df.iloc[(i,0)]),unsafe_allow_html=True)
          c2.markdown('<div class="val">{val}</div>'.format(val=ser_df.iloc[(i,1)]),unsafe_allow_html=True)
        else:
          c3.markdown('<div class="header">{ser}</div>'.format(ser=ser_df.iloc[(i,0)]),unsafe_allow_html=True)
          c4.markdown('<div class="val">{val}</div>'.format(val=ser_df.iloc[(i,1)]),unsafe_allow_html=True)
        count+=1
  # show screen with a rif save in the session   
  else:
    # fila 2 cards con datos del cliente
    Cards(True)
    # fila tres datos telefono, email, email accionistas
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="my-header">Teléfono</div>', unsafe_allow_html=True)
    c1.markdown('<div class="values">0414-522-96-87</div>', unsafe_allow_html=True)
    c2.markdown('<div class="my-header">E-mail</div>', unsafe_allow_html=True)
    c2.markdown('<div class="values">my_email@gmail.com</div>', unsafe_allow_html=True)
    c3.markdown('<div class="my-header">E-mail Accionista</div>', unsafe_allow_html=True)
    c3.markdown('<div class="values">email1@gmail.com, email2@gmail.com</div>', unsafe_allow_html=True)
    # seccion de productos
    st.write('\n')
    st.write('\n')
    st.markdown('<h3 class="center_section"> Consulta de Saldos Promedios </h3>', unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    col1, col2 = st.columns([0.15, 0.85],vertical_alignment="top")
    with col1:
      # seleccion del usuario de meses a consultar
      mes_inicio = st.selectbox(r"$\textsf{\large Desde}$",vector,0)
      option_vector = vector[vector.index(mes_inicio):]
      mes_fin = st.selectbox(r"$\textsf{\large Hasta}$",option_vector,(len(option_vector)-1))
      # seleccion del usuario de temporalidad a observar de saldos promedio
      period = st.radio(r"$\textsf{\large Gráficar saldos prom.}$",
                        ["Mensual", "Trimestral", "Cuatrimestral", "Semestral"])
      # configuracion de graficas
      if period:
        if period == 'Mensual':
          col = meses
        elif period == 'Trimestral':
          col = [4,3,2,1]*3
          col.sort(reverse=True)
        elif period == 'Cuatrimestral':
          col = [3,2,1]*4
          col.sort(reverse=True)
        else:
          col = [1,2]*6
          col.sort(reverse=True)
          period='Semestral'
    with col2:
      c1, c2, c3 = st.columns([0.03, 0.42, 0.55])
      # creacion del data frame con las fechas a consultar seleccionadas
      f= vector[vector.index(mes_inicio): (vector.index(mes_fin)+1)]
      # val = ['' for i in f]
      val1 = [f'{int(random.choice(range(1000,2000))):,}'.replace(',','.') for i in f]
      val2 = [f'{int(random.choice(range(3000,6000))):,}'.replace(',','.') for i in f]
      val3 = [f'{int(random.choice(range(800,10000))):,}'.replace(',','.') for i in f]
      saldos = {'Fecha': f, 'Cuenta Bs': val1, 'Cuenta M1':val2,'Cuenta Div. Plus':val3}
      saldos_df = pd.DataFrame(saldos)
      with c2:
        display_dataframe(saldos_df)
      with c3:
        # data
        v1=[random.choice(range(1000,2000)) for i in vector]
        v2=[random.choice(range(3000,6000)) for i in vector]
        v3=[random.choice(range(800,10000)) for i in vector]
        saldos = {'Fecha':vector,'Cuenta Bs':v1,'Cuenta M1':v2,'Cuenta Div. Plus':v3}
        saldos_df = pd.DataFrame(saldos)
        # configuracion de periodo a graficar (mes, trimestre,...)
        new_cols = {'mes':meses, 'period':col, 'year':years}
        saldos_df = saldos_df.assign(**new_cols)
        if period == 'Mensual':
          saldos_df['meses'] = saldos_df.groupby('period')['mes'].transform(
          lambda x: '{Mes}'.format(Mes=meses_spanish.get(str(list(x)[0])))
          ) +' '+ saldos_df.year.astype(str)
          saldos_df = saldos_df.groupby(['period', 'meses'])[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']].mean()
          saldos_df = saldos_df.reset_index()
          saldos_df = saldos_df.set_index('period')
          saldos_df = saldos_df.loc[col]
          saldos_df[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']] = saldos_df[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']].round(0).astype(int)
        else:
          saldos_df['meses'] = saldos_df.groupby('period')['mes'].transform(
            lambda x: '{Min}-{Max}'.format(Min=meses_spanish.get(str(list(x)[0])),Max=meses_spanish.get(str(list(x)[-1]))))
          saldos_df = saldos_df.groupby(['period', 'meses'])[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']].mean()
          saldos_df = saldos_df.reset_index()
          saldos_df = saldos_df.set_index('period')
          col2 = [col.index(i) for i in np.unique(col)]
          col2.reverse()
          col2 = np.array(col)[[col2]]
          saldos_df = saldos_df.loc[list(col2[0])]
          saldos_df[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']] = saldos_df[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']].round(0).astype(int)
        height=260
        # plot saldos bs
        title='Saldo Promedio {period} Cuenta Bs'.format(period=period)
        fig = px.bar(saldos_df, x='meses', y='Cuenta Bs', text_auto='.2s',
                     text=['Bs '+f'{bs:,}'.replace(',','.') for bs in saldos_df['Cuenta Bs'].to_list()])
        fig.update_traces(marker_color='rgb(0,152,219)')
        fig.update_layout(title_text=title, title_x=0.5, title_xanchor='center',
                          title_font_style='normal', title_font_weight='bold',
                          xaxis_title="Meses", yaxis_title="Saldo promedio en Bs",
                          height=height)
        st.plotly_chart(fig)
        # plot saldos divisas
        div_df = saldos_df[['meses','Cuenta M1', 'Cuenta Div. Plus']].melt(id_vars='meses', var_name='Cuenta', value_name='Saldo')
        title = 'Saldo Promedio {period} Divisas'.format(period=period)
        legend=dict(orientation='h',yanchor='bottom',y=1,xanchor="right",x=0.4)
        fig = px.bar(div_df, x="meses", y="Saldo", color="Cuenta", text_auto='.2s',
                     text=['$ '+f'{d:,}'.replace(',','.') for d in div_df['Saldo'].to_list()],
                     color_discrete_sequence=['rgb(105,190,40)', 'rgb(0,152,219)'])
        fig.update_layout(title_text=title, title_x=0.5, title_xanchor='center',
                          title_font_style='normal', title_font_weight='bold',
                          legend=legend, xaxis_title="Meses",
                          yaxis_title="Saldo prom. Divisas", height=height)
        st.plotly_chart(fig)
    # puntos de venta
    st.markdown('<h3 class="center_section"> Facturación POS </h3>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([0.15,0.70,0.1,0.05], vertical_alignment="center")
    # POS activos e inactivos
    with col1:
      period2 = st.radio(r"$\textsf{\large Facturación Total.}$",
                        ["Mensual", "Trimestral", "Cuatrimestral", "Semestral"])
      # configuracion de graficas
      if period2:
        if period2 == 'Mensual':
          column = meses
        elif period2 == 'Trimestral':
          column = [4,3,2,1]*3
          column.sort(reverse=True)
        elif period2 == 'Cuatrimestral':
          column = [3,2,1]*4
          column.sort(reverse=True)
        else:
          column = [1,2]*6
          column.sort(reverse=True)
          period2='Semestral'
    # data frame POS
    fac_pos = [random.choice(range(1000,2000)) for i in vector]
    cant_trx = [random.choice(range(50,200)) for i in vector]
    pos = {'Fecha':vector,'N_tx':cant_trx,'Fac_pos':fac_pos}
    pos_df = pd.DataFrame(pos)
    # configuracion de periodo a graficar (mes, trimestre,...)
    new_cols2 = {'mes':meses, 'period':column, 'year':years}
    pos_df = pos_df.assign(**new_cols2)
    if period2 == 'Mensual':
      pos_df['meses'] = pos_df.groupby('period')['mes'].transform(
      lambda x: '{Mes}'.format(Mes=meses_spanish.get(str(list(x)[0])))
      ) +' '+ pos_df.year.astype(str)
      pos_df = pos_df.groupby(['period', 'meses'])[['N_tx','Fac_pos']].sum()
      pos_df = pos_df.reset_index()
      pos_df = pos_df.set_index('period')
      pos_df = pos_df.loc[column]
    else:
      pos_df['meses'] = pos_df.groupby('period')['mes'].transform(
        lambda x: '{Min}-{Max}'.format(Min=meses_spanish.get(str(list(x)[0])),Max=meses_spanish.get(str(list(x)[-1]))))
      pos_df = pos_df.groupby(['period', 'meses'])[['N_tx','Fac_pos']].sum()
      pos_df = pos_df.reset_index()
      pos_df = pos_df.set_index('period')
      Col = [column.index(i) for i in np.unique(column)]
      Col.reverse()
      Col = np.array(column)[[Col]]
      pos_df = pos_df.loc[list(Col[0])]
    with col2:
      height=350
      fig = make_subplots(specs=[[{"secondary_y": True}]])
      fig.add_trace(go.Scatter(x=pos_df.meses, y=pos_df.N_tx, name="Nro de Transacciones",
                    mode="lines+markers+text",textposition="bottom right",
                    line=dict(color="#00204e",dash='dash'), text=[f'{int(i):,}'for i in pos_df.N_tx.to_list()],
                    textfont=dict(color="#00204e"), marker=dict(symbol="arrow-bar-down")),secondary_y=True)

      fig.add_trace(go.Bar(x=pos_df.meses, y=pos_df.Fac_pos, name="Monto en Bs",
                    text = [f'Bs {round(i,0):,}'.replace(',','.') for i in pos_df.Fac_pos.to_list()],
                    marker_color='#0098db'),secondary_y=False)

      fig.update_xaxes(title_text="Mes", type='category')
      legend=dict(orientation='h',yanchor='bottom',y=1,xanchor="right",x=0.3)
      title = 'Facturación {period} POS'.format(period=period2)
      fig.update_layout(title_text=title, title_x=0.5, title_xanchor='center',
                        title_font_style='normal', title_font_weight='bold',
                        legend=legend,height=height,
                        yaxis=dict(title=dict(text="Facturación en Bs"),side="left"),
                        yaxis2=dict(title=dict(text="Nro de Transacciones"),side="right"))
      st.plotly_chart(fig)
    # POS activos e inactivos
    activo=f'{random.choice(range(20,100))}'
    inactivo=f'{random.choice(range(1,20))}'
    total=f'{sum([int(activo),int(inactivo)])}'
    col3.markdown('<div class="my-header">Activos</div>', unsafe_allow_html=True)
    col4.markdown('<div class="values">{activo}</div>'.format(activo=activo), unsafe_allow_html=True)
    col3.markdown('<div class="sub-header">Inactivos</div>', unsafe_allow_html=True)
    col4.markdown('<div class="values">{inactivo}</div>'.format(inactivo=inactivo), unsafe_allow_html=True)
    col3.markdown('<div class="sub-header">Total</div>', unsafe_allow_html=True)
    col4.markdown('<div class="values">{total}</div>'.format(total=total), unsafe_allow_html=True)
    # SERVICIOS
    st.markdown('<h3 class="center_section"> Servicios </h3>', unsafe_allow_html=True)
    col1,col2 = st.columns([0.05,0.95],vertical_alignment="top")
    servicios=['BOL PM Divisas','Bolpriaven','Comisión','Depósito Bs','Depósito Divisas','Detalle de Consumo POS por cliente',
               'Domiciliación','Encargo de Confianza','Facturación Adquirencia','LBTR','Liquidaciones de Crédito',
               'Nómina','Pago Móvil','Pago por deudas','PAP Banplus','PAP Otros Bancos','Retiro Bs','Retiro Divisas',
               'Reverso','Servicios de Impuesto (ISLR, SAREN, SENIAT)','Servicios de Telefonía (Digitel, Movistar, CANTV)',
               'Servicios Otros (Corpoelec, Inter, Simple TV)','Tesoreria','Transferencias Internas','Transferencias Otros Bancos',
               'Otros']
    val=[random.choice([1000000,2500000,50000,6000000,600000,0,0,8000000,0]) for s in servicios]
    ser = {'servicios':servicios, 'montos':val}
    ser_df = pd.DataFrame(ser)
    ser_df=ser_df.sort_values('montos', ascending=False)
    with col2:
      c1,c2,c3,c4=st.columns([0.37,0.13,0.37,0.13])
      half=len(servicios)/2
      count=1
      for i in range(len(ser_df)):
        if count<=np.ceil(half):
          c1.markdown('<div class="header">{ser}</div>'.format(ser=ser_df.iloc[(i,0)]),unsafe_allow_html=True)
          if ser_df.iloc[(i,1)] > 0:
            c2.markdown('<div class="val">{val}</div>'.format(val=f'{ser_df.iloc[(i,1)]:,}'.replace(',','.')),unsafe_allow_html=True)
          else:
            c2.markdown('<div class="val">-</div>',unsafe_allow_html=True)
        else:
          c3.markdown('<div class="header">{ser}</div>'.format(ser=ser_df.iloc[(i,0)]),unsafe_allow_html=True)
          if ser_df.iloc[(i,1)]>0:
            c4.markdown('<div class="val">{val}</div>'.format(val=f'{ser_df.iloc[(i,1)]:,}'.replace(',','.')),unsafe_allow_html=True)
          else:
            c4.markdown('<div class="val">-</div>',unsafe_allow_html=True)
        count+=1
# MENU: ENTRADAS Y SALIDAS
elif menu=='Entradas y Salidas':
  # set data frame de entradas y salidas
  entradas=['BOL PM Divisas','Bolpriaven','Comisión','Depósito Bs','Depósito Divisas','Domiciliación','Encargo de Confianza',
              'Facturación Adquirencia','LBTR','Liquidaciones de Crédito','Nómina','Otros','Pago Móvil','Pago por deudas','PAP Banplus',
              'PAP Otros Bancos','Reverso','Servicios de Impuesto (ISLR, SAREN, SENIAT)','Servicios de Telefonía (Digitel, Movistar, CANTV)',
              'Servicios Otros (Corpoelec, Inter, Simple TV)','Tesoreria','Transferencias Internas','Transferencias Otros Bancos','','']
  salidas=['BOL PM Divisas','Bolpriaven','Comisión','Depósito Bs','Depósito Divisas','Detalle de Consumo POS por cliente','Domiciliación','Encargo de Confianza',
           'Facturación Adquirencia','LBTR','Nómina','Otros','Pago Móvil','Pago por deudas','PAP Banplus','PAP Otros Bancos','Retiro Bs',
           'Retiro Divisas','Reverso','Servicios de Impuesto (ISLR, SAREN, SENIAT)','Servicios de Telefonía (Digitel, Movistar, CANTV)',
           'Servicios Otros (Corpoelec, Inter, Simple TV)','Tesoreria','Transferencias Internas','Transferencias Otros Bancos']
  ent_sal = {'entradas':entradas, 'salidas':salidas}
  ent_sal_df = pd.DataFrame(ent_sal)
  # check si rif ya fue consultado
  if not 'RIF' in st.session_state:
    # datos generales del cliente a mostrar 
    Cards()
    # show items entradas y salidas
    # ENTRADAS
    ent_sal_df['montos']='-'
    col1,col2,col3,col4,col5=st.columns([0.35,0.1,0.35,0.1,0.1])
    col1.markdown('<div class="Header">Total Entradas que Aplican</div>', unsafe_allow_html=True)
    col2.markdown('<div class="val">-</div>', unsafe_allow_html=True)
    for i in range(len(ent_sal_df)-2):
      col1.markdown('<div class="header">{item}</div>'.format(item=ent_sal_df.iloc[(i,0)]),unsafe_allow_html=True)
      col2.markdown('<div class="val">-</div>', unsafe_allow_html=True)
    # SALIDAS
    col3.markdown('<div class="Header">Total Salidas que Aplican</div>', unsafe_allow_html=True)
    col4.markdown('<div class="val">-</div>', unsafe_allow_html=True)
    for i in range(len(ent_sal_df)):
      col3.markdown('<div class="header">{item}</div>'.format(item=ent_sal_df.iloc[(i,1)]),unsafe_allow_html=True)
      col4.markdown('<div class="val">-</div>', unsafe_allow_html=True)
  else:
    # datos del cliente
    Cards(True)
    # ENTRADAS
    ent_sal_df['monto_entrada']=[random.choice([100000,250000,50000,6000000,600000,0,0,300000,0]) for k in range(len(ent_sal_df)-2)]+[0,0]
    ent_sal_df['monto_salida']=[random.choice([300000,150000,40000,5000000,800000,0,0,200000,0]) for k in range(len(ent_sal_df))]
    col1,col2,col3,col4,col5=st.columns([0.35,0.1,0.35,0.1,0.1])
    col1.markdown('<div class="Header">Total Entradas que Aplican</div>', unsafe_allow_html=True)
    col2.markdown('<div class="val-bold">{val}</div>'.format(val=f'{ent_sal_df.monto_entrada.sum():,}'.replace(',','.')), unsafe_allow_html=True)
    for i in range(len(ent_sal_df)):
      # skip blank services
      if ent_sal_df.sort_values('monto_entrada', ascending=False).iloc[(i,0)] == '':
        continue
      col1.markdown('<div class="header">{item}</div>'.format(item=ent_sal_df.sort_values('monto_entrada', ascending=False).iloc[(i,0)]),unsafe_allow_html=True)
      # print values 
      if ent_sal_df.sort_values("monto_entrada", ascending=False).iloc[(i,2)]>0:
        col2.markdown('<div class="val">{val}</div>'.format(val=f'{ent_sal_df.sort_values("monto_entrada", ascending=False).iloc[(i,2)]:,}'.replace(',','.')), unsafe_allow_html=True)
      else:
        col2.markdown('<div class="val">-</div>', unsafe_allow_html=True)
    # SALIDAS
    col3.markdown('<div class="Header">Total Salidas que Aplican</div>', unsafe_allow_html=True)
    col4.markdown('<div class="val-red-bold">{val}</div>'.format(val='-'+f'{ent_sal_df.monto_salida.sum():,}'.replace(',','.')), unsafe_allow_html=True)
    for i in range(len(ent_sal_df)):
      col3.markdown('<div class="header">{item}</div>'.format(item=ent_sal_df.sort_values('monto_salida', ascending=False).iloc[(i,1)]),unsafe_allow_html=True)
      if ent_sal_df.sort_values("monto_salida", ascending=False).iloc[(i,3)]>0:
        col4.markdown('<div class="red-val">{val}</div>'.format(val='-'+f'{ent_sal_df.sort_values("monto_salida", ascending=False).iloc[(i,3)]:,}'.replace(',','.')), unsafe_allow_html=True)
      else:
        col4.markdown('<div class="red-val">-</div>', unsafe_allow_html=True)
    value=ent_sal_df.monto_entrada.sum()-ent_sal_df.monto_salida.sum()
    value_format=f'{value:,}'.replace(',','.')
    if value >= 0:
      col5.markdown('<div class="diff">{val}</div>'.format(val=value_format), unsafe_allow_html=True)
    else:
      col5.markdown('<div class="negative-diff">{val}</div>'.format(val=value_format), unsafe_allow_html=True)



# st.write(st.session_state)
# if RIF == '':
#   st.write('ES VACIO')
