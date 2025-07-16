import streamlit as st
from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field
import json

# Define the email schema
class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )

# Define the root agent
root_agent = LlmAgent(
    name="email_generator_agent",
    model="gemini-2.5-flash",
    description="Professional email generator that creates structured email content",
    instruction="""
    You are a professional email writing assistant. 
    
    IMPORTANT: Your response must be a JSON object with exactly these fields:
    - "subject": A concise, relevant subject line
    - "body": Well-formatted email content with greeting, main content, and closing
    
    Format your response as valid JSON only.
    """,
    output_schema=EmailContent,
    output_key="generated_email",
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)

# Streamlit UI
st.set_page_config(page_title="📧 Professional Email Generator", layout="centered")
st.title("📧 Professional Email Generator")

with st.form("email_form"):
    prompt = st.text_area("Enter a brief prompt or context for the email", height=150, placeholder="E.g. Follow-up after a product demo...")
    submitted = st.form_submit_button("Generate Email")

if submitted and prompt:
    with st.spinner("Generating email..."):
        try:
            # Run the agent using run_step
            result = root_agent.run_step(input=prompt)

            # Get structured response from agent
            email = result.output["generated_email"]

            st.subheader("✉️ Generated Email")
            st.markdown(f"**Subject:** {email['subject']}")
            st.markdown("---")
            st.markdown(email["body"])

            with st.expander("View JSON response"):
                st.code(json.dumps(email, indent=2), language="json")

        except Exception as e:
            st.error(f"Failed to generate email: {e}")
