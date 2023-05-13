import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
      with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("/Users/shreyas/Documents/Streamlit/styles/style.css")

lottie_profile = load_lottie("https://assets9.lottiefiles.com/packages/lf20_h5wdcgrm.json")
lottie_contact = load_lottie("https://assets2.lottiefiles.com/packages/lf20_px0ntw70.json")
ams = Image.open("/Users/shreyas/Documents/Streamlit/Images/Technologies-used-in-the-Attendance-management.jpg")

with st.container():
        
    st.write("##")
    st.subheader("Hey Fellas :wave:")
    st.title("Welcome to Streamlit Demo")
    st.write("""I am gonna explain briefly about how Streamlit can be used to build 
    interactive and responsive websites to deploy any machine learning model """)
    st.write("[Read more on Streamlit](https://streamlit.io/)")
    st.write("---")

with st.container():
        selected = option_menu(
             menu_title= None,
            options= ['About','Projects','Contact'],
            orientation='horizontal',
            icons=['person','code-slash','chat-left-text-fill']
        )
if selected == "About":
        with st.container():
             col1, col2 = st.columns(2)
             with col1:
                  st.write("##")
                  st.subheader("I am Shreyas KV")
                  st.title("Undergraduate at BIT")
                  st.write("""I am a diligent and enthusiastic developer with a good background in 
                           Python, AWS & Machine Learning
                           """)
             with col2:
                    st_lottie(lottie_profile, height=230)
            
        
        st.write("---")
        with st.container():
              col3, col4 = st.columns(2)
              with col3:
                    st.subheader("""
                    Education
                    - ***Bangalore Institute of Technology***
                        - Bachelor of Engineering - Computer Science
                        - Grade: xyz
                    - ***Vidya Mandir Ind. Pre-University College***
                        - PCMB
                        - Grade: abc
                    - ***Sri Vidya Mandir High School***
                        - Xth
                        - Grade: def
                    """)
              with col4:
                    st.subheader("Experience")
                    st.write("**Technical Intern**")
                    st.write("""
                    **Ellucian ~ Internship**
                    - Feb 2023 - Present ~ 4 mos
                    - Bangalore ~ On-site
                    """)

if selected == "Projects":
      with st.container():
            st.subheader("My Projects")
            st.write("##")
            col_l, col_r = st.columns((1,2))
            with col_l:
                  st.image(ams)
            with col_r:
                  st.subheader("Student Attendance Management System")
                  st.write("""

                  A student attendance management system is a software solution designed to streamline the process of recording, tracking, and 
                  managing student attendance in educational institutions. It replaces the traditional paper-based attendance registers and manual 
                  record-keeping methods with an automated digital system.
                  """)
                  st.markdown("[Visit Github Repo >](https://github.com/shreyas-helix/StudentAttendance)")

if selected == "Contact":
      st.header("Get In Touch With Me!")
      st.write("##")
      st.write("##")

      contact_form = """
      <form action="https://formsubmit.co/shreyaskv18@gmail.com" method="POST">
      <input type = "hidden" name ="_captcha" value = "false">
      <input type="text" name="name" placeholder = "Your name" required>
      <input type="email" name="email" placeholder = "Your email" required>
      <textarea name = "message" placeholder = "Your message" required></textarea>
      <button type="submit">Send</button>
      </form>
    """
      left_col, right_col = st.columns((2,1))
      with left_col:
            st.markdown(contact_form, unsafe_allow_html= True)
      with right_col:
            st_lottie(lottie_contact,height=245,width=450)


                  
                  
            
                    