import streamlit as st
import datetime
import pandas as pd
import random
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
# from funciones.funciones import *
from streamlit_extras.metric_cards import style_metric_cards
# pip install streamlit-aggrid
# from st_aggrid import AgGrid
# from streamlit_card import card

# streamlit run app.py
st.set_page_config(
  page_title="Dashboard Banplus",
  page_icon="💳",
  layout="wide"
)

# set margin top
st.markdown("<style> div[class^='block-container'] { padding-top: 2.8rem; } </style>", 
            unsafe_allow_html=True)
            
# some functions
def style_dataframe(df):
  return df.style.set_table_styles( [{'selector': 'th', 'props': [('background-color', '#f0f2f6'),
                                                                  ('color', '#00204e'),
                                                                  ('font-family', 'KaTeX_SansSerif'),
                                                                  ('font-size', '0.85em'),
                                                                  ('text-align','center')]
                                      }, 
                                      {'selector': 'td, th',
                                      'props': [('border', '0.5px solid #c3c8c8'),
                                                ('font-family', 'KaTeX_SansSerif'),
                                                ('font-size', '0.85em'),
                                                ('text-align','center')]
                                      }])
def display_dataframe(df):
  styled_df = style_dataframe(df)
  st.write(styled_df.hide(axis="index").to_html(),unsafe_allow_html=True)

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

# cliente a consultar
col1, col2 = st.columns([0.15, 0.85], vertical_alignment="center")
with col1:
  RIF = st.text_input(r"$\textsf{\Large Ingrese un RIF}$", placeholder='Número de RIF')
  RIF.strip()
  # components.html(
  #     """
  # <script>
  # const elements = window.parent.document.querySelectorAll('.stTextInput div[data-baseweb="input"] > div')
  # console.log(elements)
  # elements[0].style.backgroundColor = '#fafafa'
  # </script>
  # """,
  #     height=0,
  #     width=0,
  #     )
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

if reset:
  for key in st.session_state.keys():
    del st.session_state[key]
    
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
if not 'RIF' in st.session_state:
  if menu == 'Inicio':
    # Datos del cliente sin informacion aun
    with col2:  
      datos_cliente = """
      <style>.center_text {
          font-family:KaTeX_SansSerif;
          position:absolute;
          left:27%;
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
    # fila 2 cards con datos del cliente
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric(label=r"$\textsf{\large \textbf{Razón Social}}$",value=None)
    c2.metric(label=r"$\textsf{\large \textbf{Región}}$",value=None)
    c3.metric(label=r"$\textsf{\large \textbf{Gerente Ejecutivo}}$",value=None)
    c4.metric(label=r"$\textsf{\large \textbf{Oficina}}$",value=None)
    c5.metric(label=r"$\textsf{\large \textbf{Grupo Económico}}$",value=None)
    style_metric_cards(background_color="#ffffff", border_left_color='#00204e')
    css_metric = """ 
    <style>
    .st-emotion-cache-1wivap2 {
        font-size:1.2rem;
        font-family:KaTeX_SansSerif;
    }
    </style>"""
    st.markdown(css_metric, unsafe_allow_html=True)
    # fila tres datos telefono, email, email accionistas
    # color de fondo de la fila
    custom_css = """
    <style>
    .my-header {
        background-color: #f0f2f6;
        text-align:center;
        font-size:1.2em;
        font-family:KaTeX_SansSerif;
        font-weight:bold;
    }
    .values {
        font-family:KaTeX_SansSerif;
        line-height: normal;
        text-align:center;
        vertical-align: middle;
        font-size: 1.2rem;
        text-size-adjust: 100%;
    }
    </style>"""
    st.markdown(custom_css, unsafe_allow_html=True)
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
      custom_css = """
      <style>
      .st-b7 {
          background-color: #fafafa;
        }
      .st-bc {
          color:rgb(139,141,142);
      }
      </style>"""
      st.markdown(custom_css, unsafe_allow_html=True)
      # seleccion del usuario de temporalidad a observar de saldos promedio
      period = st.radio(r"$\textsf{\large Mostrar saldos prom.}$",
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
          # saldos_df[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']] = saldos_df[['Cuenta Bs','Cuenta M1','Cuenta Div. Plus']].round(0).astype(int)
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
        title = 'Saldo Promedio {period} Divisas'.format(period=period)
        legend=dict(orientation='h',yanchor='bottom',y=1,xanchor="right",x=0.4)
        fig = px.bar(div_df, x="meses", y="Saldo", color="Cuenta", text_auto='.2s', 
                     color_discrete_sequence=['rgb(105,190,40)', 'rgb(0,152,219)'])
        fig.update_layout(title_text=title, title_x=0.5, title_xanchor='center', 
                          title_font_style='normal', title_font_weight='bold', 
                          legend=legend, xaxis_title="Meses", 
                          yaxis_title="Saldo prom. Divisas", height=height)
        st.plotly_chart(fig)
else:
  if menu == 'Inicio':
    # Datos del cliente sin informacion aun
    with col2:  
      datos_cliente = """
      <style>.center_text {
          position:absolute;
          left:27%;
          margin:auto;
      }
      .center_section {
        text-align:center;
        margin:auto;
      }
      </style>
      <h3 class="center_text"> Información del Cliente </h3>
      """
      st.markdown(datos_cliente, unsafe_allow_html=True)
    # fila 2 cards con datos del cliente
    c1, c2, c3, c4, c5 = st.columns(5)
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
    # fila tres datos telefono, email, email accionistas
    # color de fondo de la fila
    custom_css = """
    <style>
    .my-header {
        background-color: #f0f2f6;
        text-align:center;
        font-size:1.2em;
        font-family:KaTeX_SansSerif;
        font-weight:bold;
    }
    .values {
        font-family: "Source Sans Pro", sans-serif;
        line-height: normal;
        text-align:center;
        vertical-align: middle;
        font-size: 1.2rem;
        text-size-adjust: 100%;
    }
    </style>"""
    st.markdown(custom_css, unsafe_allow_html=True)
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
      custom_css = """
      <style>
      .st-b7 {
          background-color: #fafafa;
        }
      .st-bc {
          color:rgb(139,141,142);
      }
      </style>"""
      st.markdown(custom_css, unsafe_allow_html=True)
      # seleccion del usuario de temporalidad a observar de saldos promedio
      period = st.radio(r"$\textsf{\large Mostrar saldos prom.}$",
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
      val1 = [f'{int(random.choice(range(1000,2000))):,}' for i in f]
      val2 = [random.choice(range(3000,6000)) for i in f]
      val3 = [random.choice(range(800,10000)) for i in f]
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
        fig = px.bar(saldos_df, x='meses', y='Cuenta Bs', text_auto='.2s')
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
                     color_discrete_sequence=['rgb(105,190,40)', 'rgb(0,152,219)'])
        fig.update_layout(title_text=title, title_x=0.5, title_xanchor='center', 
                          title_font_style='normal', title_font_weight='bold', 
                          legend=legend, xaxis_title="Meses", 
                          yaxis_title="Saldo prom. Divisas", height=height)
        st.plotly_chart(fig)
# st.write(st.session_state)
# if RIF == '':
#   st.write('ES VACIO')
