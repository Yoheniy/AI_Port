import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os
from streamlit_option_menu import option_menu

api_key=st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')



st.set_page_config(layout='wide')
with st.container():
    selected=option_menu(
        menu_title=None,
        options=['Home','Education','Projects','Contact'],
        icons=['person','code-slash','code-slash','chat-left-text-fill'],
        orientation='horizontal'
    )
if  selected=='Home':
        
    st.write('##')

    col1,col2=st.columns(2)

    with col1:
        st.subheader('Hello :wave:')
        st.subheader('Yohannes Welel')
        st.write("I'm a Software Engineer")
        st.write("I am a 3rd-year software engineering student at ASTU (Adama Science and Technology University.")
        st.write("I am passionate about competitive programming and have experience as a junior mobile app developer.")
        st.write("Currently, I am developing my portfolio to showcase my skills and projects. Feel free to explore and")
        st.write("learn more about my work!")
        st.write("[Read More](https://streamlit.io/)")
    
    with col2:
        st.image("static/images/about.png",width=300)


    st.write('-------')
    st.title(" ")
    st.write("")
    st.write("")
    persona="""You are Yohannes Welel AI bot. You help people answer questions about your self (i.e Yohannes)
            Answer as if you are responding . dont answer in second or third person.
            If you don't know they answer you simply say "That's a secret"
            Here is more info about Yohannes:

            Yohannes Welel is a student at Adama Science and Technology University in the field of Software Engineering.
            I am a 3rd-year software engineering student at ASTU (Adama Science and Technology University.")
            I am passionate about competitive programming and have experience as a junior mobile app developer.
        

            my education 
            -Higher Education
                        -Bachelor of Engineering -Software Engineering 
                        -CGPA:3.8     
            -Secondary Education
                        -Galema Secondary school
                        -Grade:3.92
            -Elementary Education
                        -Catholic Elementary School
                        -percentile:99.9
            
                        
            my experince:
            I have 3 working exerience.here is the list:

                1.Python Developer
                        -SYNC INTERN'S
                        During my virtual internship at Sync Interns, I built an authentication system and chatbot using Python. This
                        experience sparked my curiosity in Python and motivated me to explore the language further. It inspired me to
                        delve into frameworks like Django to enhance my development skills and broaden my knowledge.

                2.Adama Science and Technology University
                        Volunteer Tutor November 2023 - present
                        I provided a volunteer tutoring service for freshman and second-year students in courses such 
                        as Python, C++, and Data Structures and Algorithms
                3.Flutter Developer
                        -A2sv INTERN'S
                        During my in person internship at A2SV Internship,I built an a chat bot that help study 
                        stay focus on there education.From this internship i got a lot of experience.
            my projects 
            I have developed more projects.the main are EthioMarket,weather app,AI chatbot and E-commerce website
            1.EthioMarket
                Developed a commercial mobile app using the php framework for the EthioMarket e-commerce platform.
                            Designed and implemented the user interface and user experience, adhering to php's best practices.
                            Integrated the app with backend APIs to enable features such as product browsing, shopping cart, and order
                            management.
                            Implemented state management using Provider and utilized various Flutter widgets and packages.
                            Optimized app performance and ensured seamless user experience across different device configurations.
                            Collaborated with the backend team to ensure data integrity web
                            application.
            2.weather app
                A weather app is a simple yet powerful tool that provides real-time weather information. 
                This app can display the current weather conditions, including temperature, humidity, wind speed, and a brief description of the weather (e.g., sunny, cloudy, rainy). 
                Users can enter the name of a city, and the app fetches and displays the relevant weather data using an API like OpenWeatherMap.
                    
            3.AI chatbot
                    Developed an AI chatbot with the following features:
                        - Chatbot Interactions: Engages in natural language conversations, offering assistance, answering queries, and providing information based on user inputs.
                        - Image Generation: Utilizes AI to create images based on user descriptions or prompts.
                        - Translation Services: Converts text from one language to another seamlessly, providing real-time language assistance.
                        Technologies Used:
                        - Flutter for cross-platform app development.
                        - AI and Machine Learning models for chatbot interactions and image generation.
                        - Language translation APIs for multilingual support.
                        Impact:
                        This project demonstrates the integration of multiple AI functionalities into a single application, highlighting the potential of AI to enhance user experiences in various domains such as customer service, creative industries, and multilingual communication.
            4.E-commerce website
            An E-commerce website built using HTML, CSS, and JavaScript to provide users with a seamless online shopping experience. 
                        The website features a modern, responsive design, allowing users to browse and purchase products across different categories. 
                        It includes essential functionalities such as product listings, product details, shopping cart management, user authentication, and order processing.
                
            

        """




    with st.container():
        
        colo, coli = st.columns(2)
        with colo:

            st.subheader("JOHN Bot")
            user_question = st.text_input('Ask anything about me')
            if st.button('ASK', use_container_width=True):
                prompt = persona + "Here is the question that the user asked: " + user_question
                response = model.generate_content(prompt)
                st.write(response.text)

                # Convert the response text to speech
                tts = gTTS(text=response.text, lang='en')
                tts.save('response.mp3')
                st.audio('response.mp3', format='audio/mp3')
        with coli:
            st.subheader(""" 
                Portofolio Assistant AI
                        -it have a functionality Assist on portofolio through
                        
                        
                        -Text 
                        
                        -Audio Record
                """)



    st.write("")
    st.write("")
    st.write("")
    st.write("")


    with st.container():
        st.header("About Me")

    with st.container():
            st.image("static/images/Screenshot 2024-07-19 093546.png")
            
    st.write("-----")
    st.write(" ")
    st.write("")
    st.write("")

    with st.container():

        st.subheader("""  
        Education 
                    
            -Higher Education
                    
                        -Bachelor of Engineering -Software Engineering 
                    
                        -CGPA:3.8
                    


            -Secondary Education
                    
                        -Galema Secondary school
                    
                        -Grade:3.92
                    

            -Elementary Education
                    
                        -Catholic Elementary School
                    
                        -percentile:99.9
                    
                        """)
    st.write(" ")
    st.write(" ")
    st.write("")
    st.write("")

    with st.container():
    
        st.subheader("""
        Experience
            -Python Developer
                    
                    -SYNC INTERN'S
                    During my virtual internship at Sync Interns, I built an authentication system and chatbot using Python. This
                    experience sparked my curiosity in Python and motivated me to explore the language further. It inspired me to
                    delve into frameworks like Django to enhance my development skills and broaden my knowledge.

                    
            -Adama Science and Technology University
                    
                    Volunteer Tutor November 2023 - present
                    I provided a volunteer tutoring service for freshman and second-year students in courses such 
                    as Python, C++, and Data Structures and Algorithms
                    

            -Flutter Developer
                    
                    -A2sv INTERN'S
                    During my in person internship at A2SV Internship,I built an a chat bot that help study 
                    stay focus on there education.From this internship i got a lot of experience.

                        """)
        


    st.write(" ")
    st.write(" ")
    st.write("")
    st.write("")
    st.write("")
    st.write("")


    with st.container():
        st.header("My Projects")

    if 'show_ethio_market_details' not in st.session_state:
        st.session_state.show_ethio_market_details = False

    if 'show_weather_app_details' not in st.session_state:
        st.session_state.show_weather_app_details = False

    if 'show_ai_chatbot_details' not in st.session_state:
        st.session_state.show_ai_chatbot_details = False

    if 'show_E_commerce_details' not in st.session_state:
        st.session_state.show_E_commerce_details = False

    def toggle_ethio_market_details():
        st.session_state.show_ethio_market_details = not st.session_state.show_ethio_market_details

    def toggle_weather_app_details():
        st.session_state.show_weather_app_details = not st.session_state.show_weather_app_details

    def toggle_ai_chatbot_details():
        st.session_state.show_ai_chatbot_details = not st.session_state.show_ai_chatbot_details

    def toggle_E_commerce_details():
        st.session_state.show_E_commerce_details = not st.session_state.show_E_commerce_details

    with st.container():
        col3, col4 = st.columns(2)
        # st.header("My Projects")

        with col3:
            st.write("##")
            st.image('static/images/port-2.jpg', width=300)
            st.subheader("EthioMarket")
            if st.button("Read More", key="ethio_market", on_click=toggle_ethio_market_details):
                if st.session_state.show_ethio_market_details:
                    st.write("""
                        Developed a commercial mobile app using the php framework for the EthioMarket e-commerce platform.
                        Designed and implemented the user interface and user experience, adhering to php's best practices.
                        Integrated the app with backend APIs to enable features such as product browsing, shopping cart, and order
                        management.
                        Implemented state management using Provider and utilized various Flutter widgets and packages.
                        Optimized app performance and ensured seamless user experience across different device configurations.
                        Collaborated with the backend team to ensure data integrity web
                        application.
                    """)
                    st.markdown("[Visit my GitHub Profile](https://github.com/Sura-T/E_commerce)")

            st.write("##")
            st.image('static/images/port-4.jpg', width=300)
            st.subheader("Weather App")
            if st.button("Read More", key="weather_app", on_click=toggle_weather_app_details):
                if st.session_state.show_weather_app_details:
                    st.write("""
                        A weather app is a simple yet powerful tool that provides real-time weather information. 
                            This app can display the current weather conditions, including temperature, humidity, wind speed, and a brief description of the weather (e.g., sunny, cloudy, rainy). 
                            Users can enter the name of a city, and the app fetches and displays the relevant weather data using an API like OpenWeatherMap.
                    """)

        with col4:
            st.write("##")
            st.image('static/images/port-5.jpg', width=300)
            st.subheader("AI Chatbot in Flutter")
            if st.button("Read More", key="ai_chatbot", on_click=toggle_ai_chatbot_details):
                if st.session_state.show_ai_chatbot_details:
                    st.write("""
                        Developed an AI chatbot with the following features:
                        - Chatbot Interactions: Engages in natural language conversations, offering assistance, answering queries, and providing information based on user inputs.
                        - Image Generation: Utilizes AI to create images based on user descriptions or prompts.
                        - Translation Services: Converts text from one language to another seamlessly, providing real-time language assistance.
                        Technologies Used:
                        - Flutter for cross-platform app development.
                        - AI and Machine Learning models for chatbot interactions and image generation.
                        - Language translation APIs for multilingual support.
                        Impact:
                        This project demonstrates the integration of multiple AI functionalities into a single application, highlighting the potential of AI to enhance user experiences in various domains such as customer service, creative industries, and multilingual communication.
                    """)



            st.write("##")
            st.image('static/images/port-6.jpg', width=300)
            st.subheader("E-commerce Website")
            if st.button("Read More", key="E-commerce", on_click=toggle_E_commerce_details):
                if st.session_state.show_E_commerce_details:
                    st.write("""
                        An E-commerce website built using HTML, CSS, and JavaScript to provide users with a seamless online shopping experience. 
                        The website features a modern, responsive design, allowing users to browse and purchase products across different categories. 
                        It includes essential functionalities such as product listings, product details, shopping cart management, user authentication, and order processing.
                    """)
                st.markdown("[Visit my GitHub Profile](https://github.com/yohnsdev/ecommerce_project)")
                







    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")




    def skill_bar(skill, level):
        """Display a skill bar with a given level."""
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between;">
            <span>{skill}</span>
            <span>{level}%</span>
        </div>
        <div style="background-color: #e0e0e0; border-radius: 5px;">
            <div style="background-color: #4caf50; width: {level}%; height: 10px; border-radius: 5px;"></div>
        </div>
        """, unsafe_allow_html=True)

    st.header("My Skills")


    skills = {
        "Python": 97,
        "HTML": 85,
        "CSS": 75,
        "C++": 80,
        "Flutter": 90,
        "MySQL": 80
    }

    for skill, level in skills.items():
        skill_bar(skill, level)



    st.write("")
    st.write("")
    st.write(" ")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.header(":mailbox: Get In Touch With Me!")


    contact_form = """
    <form action="https://formsubmit.co/yohayowe@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")

if selected=='Education':
    with st.container():

        st.subheader("""  
        Education 
                    
            -Higher Education
                    
                        -Bachelor of Engineering -Software Engineering 
                    
                        -CGPA:3.8
                    


            -Secondary Education
                    
                        -Galema Secondary school
                    
                        -Grade:3.92
                    

            -Elementary Education
                    
                        -Catholic Elementary School
                    
                        -percentile:99.9
                    
                        """)
    def skill_bar(skill, level):
        """Display a skill bar with a given level."""
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between;">
            <span>{skill}</span>
            <span>{level}%</span>
        </div>
        <div style="background-color: #e0e0e0; border-radius: 5px;">
            <div style="background-color: #4caf50; width: {level}%; height: 10px; border-radius: 5px;"></div>
        </div>
        """, unsafe_allow_html=True)

    st.header("My Skills")


    skills = {
        "Python": 97,
        "HTML": 85,
        "CSS": 75,
        "C++": 80,
        "Flutter": 90,
        "MySQL": 80
    }

    for skill, level in skills.items():
        skill_bar(skill, level)



if selected=='Projects':
    with st.container():
        st.header("My Projects")

    if 'show_ethio_market_details' not in st.session_state:
        st.session_state.show_ethio_market_details = False

    if 'show_weather_app_details' not in st.session_state:
        st.session_state.show_weather_app_details = False

    if 'show_ai_chatbot_details' not in st.session_state:
        st.session_state.show_ai_chatbot_details = False

    if 'show_E_commerce_details' not in st.session_state:
        st.session_state.show_E_commerce_details = False

    def toggle_ethio_market_details():
        st.session_state.show_ethio_market_details = not st.session_state.show_ethio_market_details

    def toggle_weather_app_details():
        st.session_state.show_weather_app_details = not st.session_state.show_weather_app_details

    def toggle_ai_chatbot_details():
        st.session_state.show_ai_chatbot_details = not st.session_state.show_ai_chatbot_details

    def toggle_E_commerce_details():
        st.session_state.show_E_commerce_details = not st.session_state.show_E_commerce_details

    with st.container():
        col3, col4 = st.columns(2)
        # st.header("My Projects")

        with col3:
            st.write("##")
            st.image('static/images/port-2.jpg', width=300)
            st.subheader("EthioMarket")
            if st.button("Read More", key="ethio_market", on_click=toggle_ethio_market_details):
                if st.session_state.show_ethio_market_details:
                    st.write("""
                        Developed a commercial mobile app using the php framework for the EthioMarket e-commerce platform.
                        Designed and implemented the user interface and user experience, adhering to php's best practices.
                        Integrated the app with backend APIs to enable features such as product browsing, shopping cart, and order
                        management.
                        Implemented state management using Provider and utilized various Flutter widgets and packages.
                        Optimized app performance and ensured seamless user experience across different device configurations.
                        Collaborated with the backend team to ensure data integrity web
                        application.
                    """)
                    st.markdown("[Visit my GitHub Profile](https://github.com/Sura-T/E_commerce)")

            st.write("##")
            st.image('static/images/port-6.jpg', width=300)
            st.subheader("Weather App")
            if st.button("Read More", key="weather_app", on_click=toggle_weather_app_details):
                if st.session_state.show_weather_app_details:
                    st.write("""
                        A weather app is a simple yet powerful tool that provides real-time weather information. 
                            This app can display the current weather conditions, including temperature, humidity, wind speed, and a brief description of the weather (e.g., sunny, cloudy, rainy). 
                            Users can enter the name of a city, and the app fetches and displays the relevant weather data using an API like OpenWeatherMap.
                    """)

        with col4:
            st.write("##")
            st.image('static/images/port-6.jpg', width=300)
            st.subheader("AI Chatbot in Flutter")
            if st.button("Read More", key="ai_chatbot", on_click=toggle_ai_chatbot_details):
                if st.session_state.show_ai_chatbot_details:
                    st.write("""
                        Developed an AI chatbot with the following features:
                        - Chatbot Interactions: Engages in natural language conversations, offering assistance, answering queries, and providing information based on user inputs.
                        - Image Generation: Utilizes AI to create images based on user descriptions or prompts.
                        - Translation Services: Converts text from one language to another seamlessly, providing real-time language assistance.
                        Technologies Used:
                        - Flutter for cross-platform app development.
                        - AI and Machine Learning models for chatbot interactions and image generation.
                        - Language translation APIs for multilingual support.
                        Impact:
                        This project demonstrates the integration of multiple AI functionalities into a single application, highlighting the potential of AI to enhance user experiences in various domains such as customer service, creative industries, and multilingual communication.
                    """)



            st.write("##")
            st.image('static/images/port-6.jpg', width=300)
            st.subheader("E-commerce Website")
            if st.button("Read More", key="E-commerce", on_click=toggle_E_commerce_details):
                if st.session_state.show_E_commerce_details:
                    st.write("""
                        An E-commerce website built using HTML, CSS, and JavaScript to provide users with a seamless online shopping experience. 
                        The website features a modern, responsive design, allowing users to browse and purchase products across different categories. 
                        It includes essential functionalities such as product listings, product details, shopping cart management, user authentication, and order processing.
                    """)
                st.markdown("[Visit my GitHub Profile](https://github.com/yohnsdev/ecommerce_project)")
                
if selected=='Contact':
    st.header(":mailbox: Get In Touch With Me!")


    contact_form = """
    <form action="https://formsubmit.co/yohayowe@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")