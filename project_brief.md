## **Project Brief: PowerPoint Automation to Text-Based Content Generation Platform**

### **Project Title:**

PowerPoint Automation

### **Engineers Involved:**

* **Nachiket Kapure**
* **Gaurav Prakash**

### **Duration:**

April 15, 2025 – June 25, 2025

---

### **1. Objective**

The goal of the project was to automate the generation of professional-quality PowerPoint presentations using AI-driven content generation, incorporating a pre-defined slide template, text summaries, and relevant visuals. As the client’s requirements evolved, the scope was extended to support structured content generation in text/Word document format instead of PPT, with enhanced formatting and deployment flexibility, including AWS hosting.

---

### **2. Tools & Technologies Used**

* **Programming Language**: Python
* **Frameworks**: Streamlit
* **APIs**: OpenAI API, Perplexity API
* **Deployment**: Render, AWS EC2, Docker, AWS ECR
* **Version Control**: GitHub

---

### **3. Key Deliverables**

* AI-based PowerPoint generation with templated slides.
* Image generation and embedding in slides.
* Shifted to document-style output based on client feedback.
* UI enhancements with tab-based logic for dual output options.
* Full Dockerized deployment for AWS.
* Final hosting on AWS EC2, with container pushed to ECR.
* Well-documented GitHub repository with architectural diagram.

---

### **4. Timeline & Milestones**

#### **Phase 1: PPT Automation and Initial Deployment (Apr 15 – Apr 22)**

* Requirements gathered, initial research done.
* Template-based PPT generation logic implemented.
* Deployed working prototype on Render.
* Image generation and prompt tuning integrated.

#### **Phase 2: Client Feedback and Shift to Document Output (Apr 22 – May 6)**

* Client preferred structured text over PPT.
* Shifted app logic to generate document-style outputs.
* Iteratively improved content, formatting, and presentation.
* Final round of content updates with OpenAI integration.

#### **Phase 3: Finalization, Documentation & Dual Deployment (May 10 – May 17)**

* Created architecture diagram and GitHub documentation.
* Dual deployment (Render) with tab-based UI.
* Final GitHub push and Render deployment.
* Internal and senior reviews conducted.

#### **Phase 4: AWS Deployment Planning & Execution (May 20 – Jun 25)**

* Explored multiple AWS deployment strategies (EC2, App Runner).
* Overcame build issues and ECR limitations.
* Successful deployment on personal AWS account (t2.micro).
* Coordinated with client for production environment setup.

---

### **5. Challenges Faced**

* Build and configuration errors with AWS App Runner.
* Limited capabilities of AWS free-tier instances.
* Webhook compatibility issues with App Runner.
* Need for containerization and ECR integration.

---

### **6. Current Status**

* Successfully deployed and demonstrated AWS-hosted version.
* Container image available on AWS ECR.
* Awaiting client confirmation on target AWS environment for final deployment.

---

### **7. Conclusion**

This project showcased a complete AI-powered automation pipeline—from dynamic content generation to user-specific UI rendering and multi-platform deployment. The adaptability to changing client requirements and seamless transition from PPT to document-based output reflect a strong agile delivery process.

---




## **Project Brief: AI Value Index – Lovable Platform Development**

### **Project Title:**

AI Value Index (under Lovable Platform)

### **Engineer:**

**Nachiket Kapure**

### **Duration:**

May 6, 2025 – June 22, 2025

---

### **1. Objective**

The **AI Value Index** project aimed to create a web-based reporting platform as part of the **Lovable Platform**. The core functionality included:

* Collecting data via frontend forms,
* Automatically generating professional PDF reports based on that data,
* Sending those reports to clients via email,
* Supporting markdown-based report formats for flexibility,
* Deploying a full-stack application to a production environment (Render).

This initiative provided a scalable way to assess and present AI value metrics to stakeholders in a structured, visual, and automated format.

---

### **2. Tools & Technologies Used**

* **Frontend**: ReactJS
* **Backend**: FastAPI (Python), PostgreSQL
* **PDF Generation**: ReportLab / WeasyPrint (or equivalent library)
* **Emailing**: SMTP, MailerLite Integration
* **Deployment**: Render (Frontend + Backend)
* **Version Control**: GitHub

---

### **3. Key Deliverables**

* React-based UI for form input and report generation.
* FastAPI backend with endpoints for:

  * Saving form data to PostgreSQL,
  * Generating PDF reports,
  * Sending reports via email (SMTP).
* Markdown-to-PDF rendering API.
* MailerLite setup for scalable campaign distribution.
* Full deployment on Render (frontend and backend).
* Technical documentation and walkthrough videos for client handoff.

---

### **4. Timeline & Milestones**

#### **Phase 1: Initial Setup & UI/Backend Development (May 6 – May 20)**

* Project brief received and requirements gathered.
* React frontend initialized and UI elements built.
* Bug fixes implemented for early usability.
* FastAPI backend created with database connectivity.
* PDF generation and email delivery features started.
* Received client feedback to create a generic report format.

#### **Phase 2: Reporting Logic & SMTP Integration (May 21 – May 30)**

* Designed and implemented a generic report format.
* API to generate and send reports via SMTP completed.
* Visual formatting and layout refinements made.
* MailerLite integration completed to support scalable outreach.
* Documentation prepared and shared with the client.

#### **Phase 3: Deployment & Client Feedback (June 2 – June 17)**

* Render deployment attempted; initial PDF issues identified and resolved.
* Backend and frontend deployed successfully.
* Full functionality tested on production environment.
* Client walkthrough and feedback received.

#### **Phase 4: Markdown-to-PDF Feature (June 19 – June 22)**

* Developed an API to convert markdown content into formatted PDFs.
* Finalized and tested output.
* Pushed to GitHub and deployed on Render.

---

### **5. Challenges Faced**

* Compatibility issues in PDF module during Render deployment.
* Delay in document format sharing caused initial report structure changes.
* Coordination required for multi-step deployment (frontend/backend separation).

---

### **6. Current Status**

* Fully deployed frontend and backend on Render.
* PDF generation (template and markdown-based) and emailing workflows functioning as expected.
* Codebase pushed to GitHub.
* Ready for client scaling and integration into broader Lovable Platform initiatives.

---

### **7. Conclusion**

The **AI Value Index** project for the **Lovable Platform** demonstrated the successful integration of frontend forms, backend logic, automated document generation, and outbound email communication in a production-ready application. With features like markdown-based report generation and campaign integrations, the project provides a robust foundation for further scalability and reuse across different reporting use cases.

---

