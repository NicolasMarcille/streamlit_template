import streamlit as st


st.title("Nick's app")
st.sidebar.markdown("## Home page 🎈")
st.subheader("Here is a subheader")

text = '''
#### This is my app template.
'''
text


x = st.slider('My slider')
st.write(x, 'squared is', x * x)
st.text_input("My text input", key="my_text_input")
st.session_state.my_text_input

if st.checkbox('Show Me'):
    test_data = "Some text hidden that can be shown"
    test_data

option = st.selectbox('Which letter do you prefer?', options=['a', 'b', 'c', 'd'])
'You selected: ', option

select_box = st.sidebar.selectbox('How would you like to be contacted?',
                                  options=('Email', 'Home phone', 'Mobile phone'))

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio('Sorting hat', options=("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

