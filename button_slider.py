import time
import streamlit as st

st.title('Creating a Button')
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button!')
else:
    st.write('You have not clicked the Button.')

st.title('Creating a Radio Buttons')
gender = st.radio('Select Your Gender', ('Male', 'Female', 'Others'))
st.write(f'Selected gender is {gender}.')

st.title('Creating Checkboxes')
st.write('Select your Hobbies:')

options = ['Books', 'Movies', 'Sports']
checkboxes = [st.checkbox(option) for option in options]

st.title('Pre-Select')
check = st.checkbox('Accept all Terms and Conditions***', value=True)

st.title('Creating Dropdown')
hobby = st.selectbox('Choose your hobby: ', options, index=1)

st.title('Multi-Select')
options = ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking']
hobbies = st.multiselect('what are your hobbies', options, default=options[0:2])

st.title('Download Button')
down_btn = st.download_button(
    label='Download Animal Image',
    data=open('./animal.jpeg', 'rb'),
    file_name='animal.jpeg',
    mime='image/jpeg',
    disabled=True,
)

st.title('Progress Bar')


def pseudo_download():
    msg = 'Downloading'
    download_msg.text(msg)
    try:
        clicked = pseudo_download_button.button('Stop Download', key='downloading', on_click=pseudo_download)
        if clicked:
            raise InterruptedError
        for percentage in range(1, 101):
            time.sleep(0.02)
            # XXX: If sleep_time is small(<0.02), progress render speed is slow and
            # progress bar is set 0 before reaching near 100!
            download.progress(percentage)
    except InterruptedError:
        msg = 'Download Interrupted.'
    else:
        msg = 'Download Complete!'
    finally:
        st.session_state.download_msg = msg
        download_msg.text(msg)


pseudo_download_button = st.empty()
download = st.progress(0)
clicked = pseudo_download_button.button(
    'Pseudo Download',
    key='pre_download',
    on_click=pseudo_download
)
download_msg = st.text(st.session_state.get('download_msg', ''))


st.title('some other title')
