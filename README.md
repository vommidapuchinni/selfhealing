# Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

## Introduction
This project demonstrates an automated self-healing infrastructure using **Prometheus**, **Alertmanager**, and **Ansible**. It monitors a sample NGINX service and automatically recovers it if it goes down.

---

## Abstract
The infrastructure continuously monitors the NGINX container. When Prometheus detects that the service is down, Alertmanager triggers a webhook, which calls an Ansible playbook to restart the container automatically. The system provides real-time monitoring and automated recovery.

---

## Tools Used
- **Prometheus**: Metrics collection and alerting rules  
- **Alertmanager**: Alert management and webhook integration  
- **Ansible**: Automating container restart tasks  
- **Docker**: Containerized services  
- **Flask (Python)**: Webhook server  
- **NGINX**: Sample service for monitoring  

---

## Infrastructure Diagram
![Infrastructure Diagram](infrastructure.png)

---

## Steps Involved in Building the Project

### 1. Deploy NGINX Service
NGINX container running as the monitored service:

![NGINX Service Running](screenshots/nginx-service.png)

Docker containers and images:

![Docker Containers](screenshots/dockercontainers.png)  
![Docker Images](screenshots/dockerimages.png)

NGINX configuration:

![NGINX Config](screenshots/nginxconfg.png)

---

### 2. Configure Prometheus
Prometheus config and rules for monitoring NGINX:

Prometheus main config:

![Prometheus Config](screenshots/prometheusfile.png)

NGINX alert rules:

![NGINX Rules File](screenshots/nginxrulesfile.png)

Prometheus metrics graph:

![NGINX Graph](screenshots/nginxgraph.png)

Rule health status:

![Rule Health](screenshots/rulehealth.png)

---

### 3. Configure Alertmanager
Alertmanager setup with webhook integration:

Alertmanager config file:

![Alertmanager Config File](screenshots/alertmanagerfile.png)

Alertmanager running:

![Alertmanager Running](screenshots/alertmanager.png)

Webhook configuration:

![Webhook File](screenshots/webhookfile.png)

---

### 4. Ansible Playbook
Ansible playbook to restart NGINX container:

![Ansible Playbook](screenshots/ansibleplaybook.png)  
![Restart NGINX Playbook](screenshots/restartnginxfile.png)

NGINX container restarted:

![NGINX Recovered](screenshots/nginxrestarted.png)

---

### 5. Triggering Alerts
When NGINX goes down, Prometheus fires an alert:

NGINX down alert firing:

![NGINX Down Firing](screenshots/nginxdownfiring.png)  
![NGINX Service Down](screenshots/nginx-service-down.png)

NGINX pending or inactive alerts:

![NGINX Down Pending](screenshots/nginxdownpending.png)  
![NGINX Inactive](screenshots/alertinactive.png)

NGINX recovered and back online:

![NGINX Up Job Table](screenshots/nginxupjob-table.png)

![NGINX RESTARTED](screenshots/nginxrestarted.png)

---
