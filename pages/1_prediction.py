##2nd page

import pickle  #to load a saved model
import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="prediction", page_icon="📈")
st.write('''# Moment of Truth 🕠
            You know nothing, Jon snow! 🤨'''    
)

app_mode=st.selectbox('Select mode ',['prediction using grades till sophomore','prediction using grades till junior'])

##prediction using grades till sophomore
if app_mode=='prediction using grades till sophomore':
    st.markdown("#Enter your GPs in the following fields :")

    f1=st.number_input("GP in PH-121 :",min_value=0.0,max_value=4.0)
    f2=st.number_input("GP in HS-101 :",min_value=0.0,max_value=4.0)
    f3=st.number_input("GP in CY-105 :",min_value=0.0,max_value=4.0)
    f4=st.number_input("GP in HS-105/12 :",min_value=0.0,max_value=4.0)
    f5=st.number_input("GP in MT-111 :",min_value=0.0,max_value=4.0)
    f6=st.number_input("GP in CS-105 :",min_value=0.0,max_value=4.0)
    f7=st.number_input("GP in CS-106 :",min_value=0.0,max_value=4.0)
    f8=st.number_input("GP in EL-102 :",min_value=0.0,max_value=4.0)
    f9=st.number_input("GP in EE-119 :",min_value=0.0,max_value=4.0)
    f10=st.number_input("GP in ME-107 :",min_value=0.0,max_value=4.0)
    f11=st.number_input("GP in CS-107 :",min_value=0.0,max_value=4.0)
    f12=st.number_input("GP in HS-205/20 :",min_value=0.0,max_value=4.0)
    f13=st.number_input("GP in MT-222 :",min_value=0.0,max_value=4.0)
    f14=st.number_input("GP in EE-222 :",min_value=0.0,max_value=4.0)
    f15=st.number_input("GP in MT-224 :",min_value=0.0,max_value=4.0)
    f16=st.number_input("GP in CS-210 :",min_value=0.0,max_value=4.0)
    f17=st.number_input("GP in CS-211 :",min_value=0.0,max_value=4.0)
    f18=st.number_input("GP in CS-203 :",min_value=0.0,max_value=4.0)
    f19=st.number_input("GP in CS-214 :",min_value=0.0,max_value=4.0)
    f20=st.number_input("GP in EE-217 :",min_value=0.0,max_value=4.0)
    f21=st.number_input("GP in CS-212 :",min_value=0.0,max_value=4.0)
    f22=st.number_input("GP in CS-215 :",min_value=0.0,max_value=4.0)

    test1=[[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22]]

    loaded_model2 = pickle.load(open('2nd_model.pkl', 'rb'))


    st.sidebar.header("Predicting your CGPA :")
    st.write(
        """Hope you get a good CGPA. Enjoy!"""
    )

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    # chart = st.line_chart()


    if st.sidebar.button("Predict"):
        for i in range(100):
            time.sleep(0.1)
            progress_bar.progress(i + 1)
            # last_rows = np.append(last_rows, np.random.randn(1, 1), axis=0)
            # chart.add_rows(last_rows)
            status_text.text("Status: %d%%" % (i + 1))
        st.write('''
        ## Prediction : ''')
        st.write(loaded_model2.predict(test1))



    progress_bar.empty()


##prediction using grades till junior
elif app_mode=='prediction using grades till junior':
    st.markdown("#Enter your GPs in the following fields :")

    g1=st.number_input("GP in PH-121 :",min_value=0.0,max_value=4.0)
    g2=st.number_input("GP in HS-101 :",min_value=0.0,max_value=4.0)
    g3=st.number_input("GP in CY-105 :",min_value=0.0,max_value=4.0)
    g4=st.number_input("GP in HS-105/12 :",min_value=0.0,max_value=4.0)
    g5=st.number_input("GP in MT-111 :",min_value=0.0,max_value=4.0)
    g6=st.number_input("GP in CS-105 :",min_value=0.0,max_value=4.0)
    g7=st.number_input("GP in CS-106 :",min_value=0.0,max_value=4.0)
    g8=st.number_input("GP in EL-102 :",min_value=0.0,max_value=4.0)
    g9=st.number_input("GP in EE-119 :",min_value=0.0,max_value=4.0)
    g10=st.number_input("GP in ME-107 :",min_value=0.0,max_value=4.0)
    g11=st.number_input("GP in CS-107 :",min_value=0.0,max_value=4.0)
    g12=st.number_input("GP in HS-205/20 :",min_value=0.0,max_value=4.0)
    g13=st.number_input("GP in MT-222 :",min_value=0.0,max_value=4.0)
    g14=st.number_input("GP in EE-222 :",min_value=0.0,max_value=4.0)
    g15=st.number_input("GP in MT-224 :",min_value=0.0,max_value=4.0)
    g16=st.number_input("GP in CS-210 :",min_value=0.0,max_value=4.0)
    g17=st.number_input("GP in CS-211 :",min_value=0.0,max_value=4.0)
    g18=st.number_input("GP in CS-203 :",min_value=0.0,max_value=4.0)
    g19=st.number_input("GP in CS-214 :",min_value=0.0,max_value=4.0)
    g20=st.number_input("GP in EE-217 :",min_value=0.0,max_value=4.0)
    g21=st.number_input("GP in CS-212 :",min_value=0.0,max_value=4.0)
    g22=st.number_input("GP in CS-215 :",min_value=0.0,max_value=4.0)
    g23=st.number_input("GP in MT-331 :",min_value=0.0,max_value=4.0)
    g24=st.number_input("GP in EF-303 :",min_value=0.0,max_value=4.0)
    g25=st.number_input("GP in HS-304 :",min_value=0.0,max_value=4.0)
    g26=st.number_input("GP in CS-301 :",min_value=0.0,max_value=4.0)
    g27=st.number_input("GP in CS-302 :",min_value=0.0,max_value=4.0)
    g28=st.number_input("GP in TC-383 :",min_value=0.0,max_value=4.0)
    g29=st.number_input("GP in EL-332 :",min_value=0.0,max_value=4.0)
    g30=st.number_input("GP in CS-318 :",min_value=0.0,max_value=4.0)
    g31=st.number_input("GP in CS-306 :",min_value=0.0,max_value=4.0)
    g32=st.number_input("GP in CS-312 :",min_value=0.0,max_value=4.0)
    g33=st.number_input("GP in CS-317 :",min_value=0.0,max_value=4.0)

    test2=[[g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14,g15,g16,g17,g18,g19,g20,g21,g22,g23,g24,g25,g26,g27,g28,g29,g30,g31,g32,g33]]

    loaded_model1 = pickle.load(open('1st_model.pkl', 'rb'))


    st.sidebar.header("Predicting your CGPA :")
    st.write(
        """Hope you get a good CGPA. Enjoy!"""
    )

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    # chart = st.line_chart()


    if st.sidebar.button("Predict"):
        for i in range(100):
            time.sleep(0.1)
            progress_bar.progress(i + 1)
            # last_rows = np.append(last_rows, np.random.randn(1, 1), axis=0)
            # chart.add_rows(last_rows)
            status_text.text("Status: %d%%" % (i + 1))
        st.write('''
        ## Prediction : ''')
        st.write(loaded_model1.predict(test2))



    progress_bar.empty()


