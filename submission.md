# CSP451 Milestone 3 — Submission 
**Student Name:** Teena Therese 
**Student ID:** 2053476 
**GitHub Repo:** https://github.com/teenatherese/CSP451-milestone3 
**Live URL:** http://cloudmart-2053476.canadaeast.azurecontainer.io --- 
## 1. Azure Login and Resource Verification 
az group show --name Student-RG-2053476 -o table az resource list --resource-group Student-RG-2053476 -o table 
Screenshot: Resource group overview showing ACI + Cosmos DB + ACR 
## 2. Cosmos DB Setup az cosmosdb show --name cloudmart-db-2053476 ... Screenshot: Data Explorer with products, cart, and orders containers 
## 3. Application Development Key files: main.py, database.py, models.py, seed_data.py Local curl test output: (paste your curl output for /health, /api/v1/products, /api/v1/categories) 
## 4. Docker Build and Test Screenshot: docker build output 
Screenshot: App running locally at http://localhost:8080 
## 5. Azure Deployment Screenshot: ACI details (running, IP, FQDN) 
Screenshot: curl /health and /api/v1/products 
Screenshot: CloudMart homepage via public URL 
Screenshot: Container logs 
## 6. CI/CD Pipeline Screenshot: GitHub Secrets settings page (9 secrets configured) 
Screenshot: GitHub Actions CI + CD passing Screenshot: ACR repository with image tags 
## 7. End-to-End Testing All 11 curl test outputs: (paste your full test session output) 5 browser screenshots: Homepage, category filter, cart, order, /health ## 8. Reflection 
1. How does the security model of a publicly exposed ACI container differ from the NSG-protected VMs in Milestone 1? What additional protections would you add in production? 
In Milestone 1, VMs were protected by Network Security Groups and VNets that controlled inbound/outbound traffic at the network level. ACI containers in this milestone have a direct public IP with no NSG or VNet by default, making them more exposed. In production I would add Azure Application Gateway with a Web Application Firewall in front of the container, and place the ACI inside a VNet with private endpoints for Cosmos DB.
2. How could you apply the monitoring techniques from Milestone 2 (flow logs, IDS alerts) to this containerized deployment? 
In Milestone 2 we used NSG flow logs and IDS alerts to monitor network traffic on VMs. For this containerized deployment I would use Azure Monitor with Container Insights to track CPU, memory, and request logs. The /health endpoint acts as an application-layer health probe similar to how flow logs monitored network-layer activity in Milestone 2.


3. What is one thing you would change about this architecture if CloudMart had 10,000 concurrent users? 
For 10,000 concurrent users I would move from ACI to Azure Kubernetes Service (AKS) which supports horizontal pod autoscaling based on CPU and request load. I would also add a Redis cache in front of Cosmos DB to reduce database calls for frequently accessed data like the product catalog and put Azure Front Door in front for global load balancing and CDN caching.

              