## 🧰 Projects & Contributions


*last updated: 28.1.2026*

<!-- Grafana Dashboard Integration -->
<details>
<summary><span style="font-size:1.5em;"> <b>Grafana Dashboard Integration</b></span></summary> 

&#32;

Developed a lightweight client that fetched bug ticket data via REST API, stored it in PostgreSQL, and visualized it using Grafana dashboards.

**Tech:** Python, PostgreSQL, Grafana
</details>

---

<!-- Worklog -->
<details>
<summary><span style="font-size:1.5em;"> <b>Worklog</b> </span></summary>

&#32;

Created a module to automatically retrieve and process work-hour data through API integration.

**Tech:** Python, PostgreSQL, Django
</details>

---

<!-- Custom Django Admin Extensions -->
<details>
<summary><span style="font-size:1.5em;"> <b>Custom Django Admin Extensions</b></span></summary>

&#32;

Built an advanced Django Admin interface with pagination, complex filters, and optimized data queries to improve usability and performance.

**Tech:** Python, Django

</details>

---

<!-- Rapid FastAPI Web Apps -->
<details>
<summary><span style="font-size:1.5em;"><b>Rapid FastAPI Web Apps</b></span></summary>

&#32;

Developed multiple small-scale FastAPI web applications (typically completed within a day).
These included CRUD interfaces, batch file uploads/downloads, and DB integration layers.

**Tech:** Python, FastAPI, SQL Drivers, Docker

</details>

---

<!-- Deployment & Infrastructure -->
<details>
<summary><span style="font-size:1.5em;"><b>Deployment & Infrastructure</b></span></summary>

&#32;

Hands-on experience deploying services using Portainer, Docker Stacks, Kubernetes, Rancher and little bit of AWS. 

**Tech:** Docker, Portainer, Kubernetes, Rancher

</details>

---

<!-- Adoption System -->
<details>
<summary><span style="font-size:1.5em;"><b>Adoption System</b></span></summary>

&#32;

Maintained and extended a Django-based adoption platform integrating GoPay and UPay payment gateways. Worked with a legacy dual-database architecture (MySQL + MariaDB), implementing backend patches, payment reconciliation fixes, and frontend improvements.

**Tech:** Python, Django, Payment APIs, MySQL, MariaDB, Docker, Kubernetes
</details>

---

<!-- TrackParse -->
<details>
<summary><span style="font-size:1.5em;"><b>TrackParse</b></span></summary>

&#32;

Architected and implemented a modular PDF parsing engine for railway timetable data. Represented table structures as object hierarchies, applying design patterns for flexible parsing, transformation, and validation logic.

**Tech:** Python
</details>

---

<!-- PDF Annotation Plugin For Nextcloud -->
<details>
<summary><span style="font-size:1.5em;"><b> PDF Annotation Plugin for Nextcloud</b></span></summary>

&#32;

Developed a Nextcloud extension allowing users to upload, annotate, and save drawings on PDFs directly in-browser. Designed to store annotations as external metadata to preserve original documents.

**Tech:** PHP, Nextcloud , JavaScript

</details>

---

<!-- Zammad Ticket Management Portal -->
<details>
<summary><span style="font-size:1.5em;"><b>Zammad Ticket Management Portal</b></span></summary>

&#32;

Designed and implemented a full-stack system integrating with Zammad to help agents efficiently manage organizations, products, and related ticket workflows. The application supports CRUD operations, ticket tracking and analytics, and enforces per-organization, product-specific ticket templates for faster and more consistent issue reporting.

The project is structured for long-term scalability and maintainability, with a modular architecture that cleanly separates application layers and responsibilities. It employs factory methods and a fallback process to ensure reliable API communication and smooth recovery from transient Zammad API errors. Architecture was also extended with dynamic background task registration, enabling new synchronization and processing jobs to be added without redeploying the core service.

The system is actively used in production and has scaled beyond its original scope. It now serves as a stable integration layer for other in-house reporting tools, which consume its API instead of querying Zammad directly (adapter pattern). This decoupling allowed independent evolution of reporting use cases without increasing load or complexity in Zammad itself.


**Tech:** Python (Flask), Bootstrap, Zammad API, PostgreSQL, Docker
</details>

&#32;


---
<!-- GitLab CI/CD Components-->

<details>
<summary><span style="font-size:1.5em;"><b>CI/CD Pipeline Architecture & DevSecOps</b></span></summary>

&#32;

Developed and maintained a library of reusable GitLab CI/CD components to enforce security gates and code quality standards. Key implementations include:

* **Gated Container Delivery:** Orchestrated a secure, rootless image build pipeline using Kaniko. Implemented an image promotion workflow where artifacts are scanned for vulnerabilities immediately after build; images are only promoted to the primary registry upon passing security checks, while failed builds are automatically purged.
* **Advanced Secret Detection:** Hardened repository security by combining GitLeaks with TruffleHog for verified credential checking. Engineered custom rulesets to detect semantic patterns (e.g., DB_PASSWORD) alongside standard entropy checks.
* **Python Quality & Security Suite:** Created a high-performance Python compliance track utilizing uv and Ruff. Enforces strict formatting, docstring standards, and class method ordering, combined with deep SAST analysis using Bandit and Semgrep.

**Tech:** GitLab CI/CD, Docker, Kaniko, GitLeaks, Trufflehog, Ruff, uv, Bandit, Semgrep

</details>

---
<!-- WireGuard RustDesk-->

<details>
<summary><span style="font-size:1.5em;"><b>WireGuard RustDesk</b></span></summary>

&#32;

Deployed internal access and support tooling, including a WireGuard-based VPN with web-based administration and a self-hosted RustDesk instance for secure out-of-office remote usage. These services standardized internal access and reduced reliance on external third-party tools.

**Tech:** WireGuard, RustDesk, Docker, Nginx

</details>

---

<details>
<summary><span style="font-size:1.5em;"><b>Zammad Metrics Exporter</b></span></summary>

&#32;

Built a lightweight FastAPI service exposing curated Zammad ticket metrics via HTTP JSON endpoints for use in dashboards and reporting tools (e.g. Grafana). Metrics are defined declaratively in a YAML file, with endpoints generated dynamically from configuration.

The service supports hot-reloading of metric definitions and is secured using Bearer token authentication. By exposing read-only analytical endpoints instead of direct database access, it simplifies reporting workflows and avoids placing additional load or complexity on the Zammad application.

Used in production as part of the Zammad reporting and monitoring stack.

**Tech:** Python(FastAPI), PostgreSQL, YAML, Docker, Grafana

</details>

[Back to main README](README.md)
