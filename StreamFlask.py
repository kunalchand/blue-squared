import streamlit as st
import requests
import pandas as pd
from log.log_config import setup_logger

logger = setup_logger("StreamLitUI")
def fetch_single_id_data(id):
    logger.info("Make an API call to Flask to fetch the data for the single id")
    response = requests.get(f"http://127.0.0.1:5000//get_records/{id}")
    return response.json()


def fetch_dual_id_data(id1, id2):
    logger.info("Make an API call to Flask to fetch the data for dual ids.")
    response = requests.get(f"http://127.0.0.1:5000//get_records/{id1}/{id2}")
    return response.json()


# Streamlit UI
st.title("Fetching Records from Database")

# Option selection (Single ID or Dual ID)
option = st.selectbox("Select Option", ("Single ID", "Dual ID"))

if option == "Single ID":
    ids = [1, 2, 3, 4, 5, 6, 7]
    logger.info("Replace with a dynamic API call to get IDs from table1")
    id_choice = st.selectbox("Choose an ID", ids)

    if st.button("Submit"):
        logger.info(" Fetch and display the record data for the chosen ID ")
        record_data = fetch_single_id_data(id_choice)
        table1_df = pd.DataFrame([record_data["table1"]], index = [1])
        table2_df = pd.DataFrame([record_data["table2"]],index = [1])
        st.write("Table 1 Record:")
        st.dataframe(table1_df)
        st.write("Table 2 Record:")
        st.dataframe(table2_df)

        logger.info(" Display same and different fields ")
        same_fields_df = pd.DataFrame([record_data["Comparison"]["same_fields"]],index = [1])
        diff = record_data["Comparison"]["different_fields"]
        # Separate the data into two lists

        table1_values = []
        table2_values = []
        field_names = []

        for field_name, values in diff.items():
            field_names.append(field_name)
            table1_values.append(values["Table1_value"])
            table2_values.append(values["Table2_Value"])

        logger.info(" Create a DataFrame with separate columns for Table 1 and Table 2")
        df = pd.DataFrame({
            "Field Name": field_names,
            "Table 1 Value": table1_values,
            "Table 2 Value": table2_values
        },index=range(1, len(field_names) + 1))

        st.write("Same Fields:")
        st.dataframe(same_fields_df)
        st.write("Different Fields:")
        st.dataframe(df)

elif option == "Dual ID":
    # Fetch available IDs for both tables
    ids_table1 = [1, 2, 3, 4, 5, 6, 7]
    ids_table2 = [1, 2, 3, 4, 5, 6, 7]

    id1_choice = st.selectbox("Choose ID from Table 1", ids_table1)
    id2_choice = st.selectbox("Choose ID from Table 2", ids_table2)

    if st.button("Submit"):
        logger.info(" Fetch and display the record data for the chosen dual ID ")
        dual_record_data = fetch_dual_id_data(id1_choice, id2_choice)
        table1_df = pd.DataFrame([dual_record_data["table1"]],index = [1])
        table2_df = pd.DataFrame([dual_record_data["table2"]],index = [1])
        st.write("Table 1 Record:")
        st.dataframe(table1_df)
        st.write("Table 2 Record:")
        st.dataframe(table2_df)

        logger.info(" Display same and different fields of dual IDs")
        same_fields_df = pd.DataFrame([dual_record_data["Comparison"]["same_fields"]],index = [1])
        diff = dual_record_data["Comparison"]["different_fields"]
        # Separate the data into two lists
        table1_values = []
        table2_values = []
        field_names = []

        for field_name, values in diff.items():
            field_names.append(field_name)
            table1_values.append(values["Table1_value"])
            table2_values.append(values["Table2_Value"])

        # Create a DataFrame with separate columns for Table 1 and Table 2
        df = pd.DataFrame({
            "Field Name": field_names,
            "Table 1 Value": table1_values,
            "Table 2 Value": table2_values
        },index=range(1, len(field_names) + 1))

        st.write("Same Fields:")
        st.dataframe(same_fields_df)
        st.write("Different Fields:")
        st.dataframe(df)
