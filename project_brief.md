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
