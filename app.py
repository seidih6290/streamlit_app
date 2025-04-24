import streamlit as st
import os


    # Navigation handler
def go_to_page(page_name):
    st.session_state.page = page_name

# Function to get grade
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# Function to shut down the app
def shutdown():
    st.write("Exiting the application...")
    os._exit(0)  # Forcefully terminate the app (and the executable if running)

def main():
    # Safely initialize session state keys
    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "name" not in st.session_state:
        st.session_state.name = ""
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "grade" not in st.session_state:
        st.session_state.grade = ""

    # Page logic
    if st.session_state.page == "home":
        st.title("🏠 Home Page")
        st.subheader("Student Grade App!")
        st.write("Fill out the fields below")
        name = st.text_input("Student Name: ")
        score = st.number_input("Student Score: ", min_value=0, step=1, max_value=100)

        if st.button("Show Results"):
            st.session_state.name = name
            st.session_state.score = score
            st.session_state.grade = get_grade(score)
            st.session_state.page = "results"
            
            try:
                st.rerun()
            except AttributeError:

                st.experimental_rerun()
        # Add an exit button
        if st.button('Exit'):
            shutdown()

    elif st.session_state.page == "results":
        st.title("📊 Results Page")
        st.write(f"Name: {st.session_state.name}")
        st.write(f"Score: {st.session_state.score}")
        st.write(f"Grade: {st.session_state.grade}")
        
        # link back to home page
        st.button("Go Back", on_click=go_to_page('home'))
        
        # Add an exit button
        if st.button('Exit'):
            shutdown()

# Run the app
if __name__ == "__main__":
    main()

