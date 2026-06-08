import streamlit as st
from extraction.extractor_manager import extract_text
from nlp.entity_extraction import extract_certifications, extract_education, extract_email, extract_experience, extract_languages, extract_phone, extract_skills, extract_candidate_name
from nlp.semantic_matching import compute_similarity
from scoring.matching import compute_skill_match
from scoring.ranking import calculate_global_score
from scoring.advanced_matching import compute_domain_match, compute_language_match, compute_certification_match, compute_education_match
from summary.summarizer import generate_summary




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

        required_skills = [s.strip() for s in skills.split(",") if s.strip()]

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

            # st.text_area(
            #     "Texte extrait",
            #     cv["text"][:3000],
            #     height=300
            # )

            text = cv["text"]
            results = []

            email = extract_email(text)
            phone = extract_phone(text)
            skills_found = extract_skills(text)
            languages_found = extract_languages(text)
            certifications_found = extract_certifications(text)
            education_found = extract_education(text)
            experience_found = extract_experience(text)
            candidate_name = extract_candidate_name(text)
            
            # calcul des scores
            semantic_score = compute_similarity(
                job_description,
                text
            )

            skills_score = compute_skill_match(
                required_skills,
                skills_found
            )

            experience_score = min(
                (experience_found / max(min_experience, 1)) * 100,
                100
            )

            # education_score = 100
            # language_score = 100
            # certification_score = 100

            language_score = compute_language_match(
                languages,
                languages_found
            )

            certification_score = compute_certification_match(
                certifications,
                certifications_found
            )

            education_score = compute_education_match(
                education,
                education_found
            )

            domain_score = compute_domain_match(
                domain,
                text
            )

            

            global_score = calculate_global_score(
                semantic_score,
                skills_score,
                experience_score,
                education_score,
                language_score,
                certification_score,
                domain_score
            )

            results.append({
                "filename": cv["filename"],
                "score": global_score,
                "email": email,
                "phone": phone,
                "skills": skills_found,
                "languages": languages_found,
                "experience": experience_found,
                "education": education_found,
                "certifications": certifications_found,
                "candidate_name": candidate_name

            })


            st.text_area(
                "Texte extrait",
                text[:2000],
                height=250
            )

            st.markdown("### 🔍 Informations détectées")

            col1, col2 = st.columns(2)

            with col1:

                st.write(f"📧 Email : {email}")
                st.write(f"📱 Téléphone : {phone}")
                st.write(f"🎓 Niveau : {education_found}")
                st.write(f"💼 Expérience : {experience_found} ans")

            with col2:

                st.write(f"🛠️ Compétences : {', '.join(skills_found)}")
                st.write(f"🌍 Langues : {', '.join(languages_found)}")
                st.write(f"📜 Certifications : {', '.join(certifications_found)}")


                
        
        # Tri des résultats par score
        results = sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )[:max_cv]

        # results = results[:max_cv]

        st.markdown("🏆 Classement des candidats")
        for rank,  candidate in enumerate(results, start=1):
            # st.markdown(
            #     f"**{rank}. {candidate['filename']}"
            # )
            # st.metric(
            #     "Score de pertinence",
            #     f"{candidate['score']}%100"
            # )

            summary = generate_summary(candidate)

            # st.progress(candidate['score'] / 100)
            # # st.write(
            # #     f"📧 Email : {candidate['email']}"
            # # )
            # # st.write(
            # #     f"📱 Téléphone : {candidate['phone']}"
            # # )
            # st.write(
            #     f"🎓 Éducation : {candidate['education']}"
            # )
            # st.write(
            #     f"💼 Expérience : {candidate['experience']} ans"
            # )
            # st.write(
            #     f"🛠️ Compétences : {', '.join(candidate['skills'])}"
            # )
            # st.write(
            #     f"🌍 Langues : {', '.join(candidate['languages'])}"
            # )
            # st.write(
            #     f"📜 Certifications : {', '.join(candidate['certifications'])}"
            # )

            # st.markdown("---")


            st.markdown(
                f"## 🏆 {rank}. {candidate['filename']}"
            )

            st.metric(
                "Score de Pertinence",
                f"{candidate['score']}/100"
            )

            st.progress(candidate["score"] / 100)

            st.markdown(f"🏆 {candidate['candidate_name']}")

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"🎓 Niveau d'études : {candidate['education']}"
                )

                st.write(
                    f"💼 Expérience : {candidate['experience']} ans"
                )

                st.write(
                    f"🛠️ Compétences : {', '.join(candidate['skills'])}"
                )

            with col2:
                
                st.write(
                    f"🌍 Langues : {', '.join(candidate['languages'])}"
                )

                st.write(
                    f"📜 Certifications : {', '.join(candidate['certifications'])}"
                )

            st.markdown("### ✅ Points forts")

            for item in summary["strengths"]:
                st.success(item)

            st.markdown("### ⚠️ Points de vigilance")

            for item in summary["warnings"]:
                st.warning(item)

            st.markdown("---")
            


            

            
