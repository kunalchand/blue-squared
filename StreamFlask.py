import streamlit as st
import requests  # To make API calls to Flask backend


def fetch_single_id_data(id):
    # Make an API call to Flask to fetch the data for the single id.
    response = requests.get(f"http://127.0.0.1:5000//get_records/{id}")
    return response.json()  # Assuming Flask returns JSON


def fetch_dual_id_data(id1, id2):
    # Make an API call to Flask to fetch the data for dual ids.
    response = requests.get(f"http://127.0.0.1:5000//get_records/{id1}/{id2}")
    return response.json()  # Assuming Flask returns JSON


# Streamlit UI
st.title("Fetching Records from Database")

# Option selection (Single ID or Dual ID)
option = st.selectbox("Select Option", ("Single ID", "Dual ID"))

if option == "Single ID":
    # Fetch available IDs from the Flask API
    ids = [1, 2, 3, 4, 5, 6, 7]  # Replace with a dynamic API call to get IDs from table1
    id_choice = st.selectbox("Choose an ID", ids)

    if st.button("Submit"):
        # Fetch and display the record data for the chosen ID
        record_data = fetch_single_id_data(id_choice)
        st.write("Table 1 Record:")
        st.write(record_data["table1"])
        st.write("Table 2 Record:")
        st.write(record_data["table2"])

        # Display same and different fields
        st.write("Same Fields:")
        st.write(record_data["Comparison"]["same_fields"])
        st.write("Different Fields:")
        st.write(record_data["Comparison"]["different_fields"])

elif option == "Dual ID":
    # Fetch available IDs for both tables
    ids_table1 = [1, 2, 3, 4, 5, 6, 7]  # Replace with API call to get IDs for table1
    ids_table2 = [1, 2, 3, 4, 5, 6, 7]  # Replace with API call to get IDs for table2

    id1_choice = st.selectbox("Choose ID from Table 1", ids_table1)
    id2_choice = st.selectbox("Choose ID from Table 2", ids_table2)

    if st.button("Submit"):
        # Fetch and display the record data for dual IDs
        dual_record_data = fetch_dual_id_data(id1_choice, id2_choice)
        st.write("Table 1 Record (ID1):")
        st.write(dual_record_data["table1"])
        st.write("Table 2 Record (ID2):")
        st.write(dual_record_data["table2"])

        # Display same and different fields
        st.write(f"Same Fields: Between Two tables with ids")
        st.write(dual_record_data["Comparison"]["same_fields"])
        st.write("Different Fields:")
        st.write(dual_record_data["Comparison"]["different_fields"])