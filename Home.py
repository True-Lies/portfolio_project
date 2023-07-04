import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/arun.gif")

with col2:
    st.title("Arun")
    content ="""
    Cras magna velit, maximus in tortor ut, scelerisque semper quam. Integer euismod quam vitae vehicula suscipit. Sed justo tellus, dignissim eget scelerisque vel, consectetur at metus. Vestibulum urna lacus, feugiat sit amet erat eu, pretium commodo sem. Sed pretium at dolor id placerat. Donec pulvinar lectus ut nisl vestibulum vestibulum. Morbi euismod felis eros, eu ultricies nunc pulvinar ut. Nam sagittis maximus aliquam. In hac habitasse platea dictumst. In ac nisi aliquam, egestas lorem a, pharetra lorem. Mauris a leo convallis, pellentesque sem et, feugiat erat. Duis blandit lobortis purus sit amet aliquam. Etiam mollis arcu eget nulla elementum, euismod laoreet augue hendrerit. Interdum et malesuada fames ac ante ipsum primis in faucibus.
    """
    st.info(content)

content2 = """
Suspendisse posuere orci vel varius egestas. Proin accumsan magna dictum dolor ullamcorper mattis. Proin tristique nisl massa
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.2, 0.5, 1.5])

df =pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")

