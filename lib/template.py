import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.title("Nick's app")
st.sidebar.markdown("## Home page 🎈")
st.subheader("Here is a subheader")

text = '''
#### This is my app template.
'''
text

# switch page
go_home = st.button("Home")
if go_home:
    switch_page("home")

#
x = st.slider('My slider')
st.write(x, 'squared is', x * x)

#
with st.form('form_text'):
    input_txt = st.text_area(label="", value="")
    submit = st.form_submit_button('Submit this')

response = ""
if submit:
    st.session_state.language = "my_function(input_txt)"

if st.session_state.language:
    st.markdown("##### The language is:")
    st.markdown(f"### {st.session_state.language}")

#
if st.checkbox('Show Me'):
    test_data = "Some text hidden that can be shown"
    test_data

option = st.selectbox('Which letter do you prefer?', options=['a', 'b', 'c', 'd'])
st.write('You selected: ', option)

select_box = st.sidebar.selectbox('How would you like to be contacted?',
                                  options=('Email', 'Home phone', 'Mobile phone'))

#
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio('Sorting hat', options=("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

