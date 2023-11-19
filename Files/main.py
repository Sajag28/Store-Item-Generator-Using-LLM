import streamlit as st
import langchain_helper
st.title("Different Store Item Generator")
Store=st.sidebar.selectbox("Pick a Store",("Apple","OnePlus","Samsung","Lenovo","Dell","HP","Asus","Acer","MSI","IQOO","Sony"))

if Store:
  response=langchain_helper.generate_store_items(Store)
  st.header(response['Store_name'].strip())
  store_items=response['Item_name'].strip().split(",")
  st.write("Store Items")
  for item in store_items:
    st.write("-",item)
  