import streamlit as st
from extraction.extractor_manager import extract_text

def render_ui():


    st.title("📄 AI CV Filtering & Analysis System")

    st.markdown("### Upload Candidate CVs")

    uploaded_files = st.file_uploader(
        "Upload CVs",
        type=["pdf", "docx", "doc", "png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    st.markdown("---")

    st.markdown("## Filtering Criteria")

    col1, col2 = st.columns(2)

    # LEFT COLUMN
    with col1:

        domain = st.selectbox(
            "Speciality / Domain",
            [
                "Software Engineering",
                "Finance",
                "Marketing",
                "Medicine",
                "Data Science",
                "Cybersecurity",
                "Civil Engineering",
                "Business Administration"
            ]
        )

        education = st.selectbox(
            "Education Level",
            [
                "Bac",
                "Licence",
                "Master",
                "Doctorat",
                "Ingénieur"
            ]
        )

        min_experience = st.slider(
            "Minimum Years of Experience",
            0,
            20,
            1
        )

        languages = st.multiselect(
            "Languages",
            [
                "English",
                "French",
                "Arabic",
                "Spanish",
                "German",
                "Italian"
            ]
        )

        contract_type = st.selectbox(
            "Contract Type",
            [
                "CDI",
                "CDD",
                "Stage",
                "Freelance",
                "Part-time"
            ]
        )

    # RIGHT COLUMN
    with col2:

        skills = st.text_input(
            "Required Technical Skills",
            placeholder="Python, React, SQL..."
        )

        certifications = st.multiselect(
            "Required Certifications",
            [
                "AWS",
                "PMP",
                "CISCO",
                "TOEFL",
                "IELTS",
                "Azure",
                "Google Cloud",
                "Scrum Master"
            ]
        )

        location = st.text_input(
            "Candidate Location",
            placeholder="Casablanca, Rabat, Paris..."
        )

        availability = st.selectbox(
            "Availability",
            [
                "Immediate",
                "1 Month Notice",
                "3 Months Notice"
            ]
        )

        previous_sector = st.selectbox(
            "Previous Activity Sector",
            [
                "IT",
                "Banking",
                "Healthcare",
                "Industry",
                "Education",
                "Telecommunications",
                "Marketing"
            ]
        )

        max_cv = st.number_input(
            "Maximum CVs to Select",
            min_value=1,
            max_value=50,
            value=10
        )

    st.markdown("---")

    st.markdown("## Job Description")

    job_description = st.text_area(
        "Paste Job Description Here (Optional)",
        height=250,
        placeholder="Describe the ideal candidate profile..."
    )

    st.markdown("---")

    st.markdown("## AI Relevance Score")

    st.info(
        """
        The system calculates a global relevance score based on:

        • Semantic similarity with the job description  
        • Technical skills match  
        • Experience level  
        • Education level  
        • Certifications  
        • Languages  
        • Candidate availability  
        """
    )

    analyze_button = st.button("🚀 Analyze CVs")

    if analyze_button:

        if not uploaded_files:
            st.warning("Please upload at least one CV.")
            return

        st.success(f"{len(uploaded_files)} CV(s) uploaded successfully.")

        # st.info("AI analysis pipeline will start here.")

        st.info("Extraction du texte des CV en cours...")

        all_cv_texts = []

        for file in uploaded_files:

            extracted_text = extract_text(file)

            all_cv_texts.append({
                "filename": file.name,
                "text": extracted_text
            })

        st.success("Extraction terminée.")

        for cv in all_cv_texts:

            st.markdown(f"### 📄 {cv['filename']}")

            st.text_area(
                "Texte extrait",
                cv["text"][:3000],
                height=300
            )