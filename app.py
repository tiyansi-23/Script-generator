import streamlit as st
from graph.ad_graph import create_ad_graph

st.set_page_config(page_title="AI Advertisement Script Generator")

st.title("📢 AI Advertisement Script Generator")

product_info = st.text_area(
    "Enter product details",
    placeholder="Example: Winter skin care cream for dry skin with natural oils..."
)

if st.button("Generate Advertisement"):
    if not product_info.strip():
        st.warning("Please enter product details.")
    else:
        with st.spinner("Generating high-quality advertisement..."):
            graph = create_ad_graph()
            result = graph.invoke({"product_info": product_info})

        st.subheader("📄 Final Advertisement Script")
        st.write(result["final_ad"])
 