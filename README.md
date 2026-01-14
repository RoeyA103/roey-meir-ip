# Roy & Meir – Joint Project

Welcome to Roy and Meir's joint project 👋

## Overview

This software is built as a distributed system composed of **three servers**:

1. **Database Server (Redis)**  
   Stores IP-related data.

2. **IP Coordinator Server (Server-B)**  
   - Pulls and inserts information into the Redis database.
   - Receives IP addresses along with waypoint/location data and saves them.

3. **IP Geo Server (Server-A)**  
   - Receives an IP address.
   - Finds the geographical location of the IP.
   - Sends the enriched data to the coordinator server for storage.

> The Hardis server is imported externally.

---

## Prerequisites

To run this project, make sure the following are installed:

- Docker  
- Docker Compose  
- Minikube  
- Kubernetes (`kubectl`)

---

## Project Structure

```
.
├── service-a
│   ├── yamls
│   └── app (IP Geo Server)
│
├── service-b
│   ├── yamls
│   ├── docker-compose.yml
│   └── app (Coordinator + Redis)
```

- **Server-A**: Receives IP addresses and resolves geolocation.
- **Server-B**: Receives IP + waypoint and saves the data to Redis.
- **Redis**: Database backend.

---

## Local Testing (Docker Compose)

For local testing, you can run **Server-B and the Redis database** to verify that the services work together.

### Steps

1. Navigate to the `service-b` directory:
   ```bash
   cd service-b
   ```

2. Start the services:
   ```bash
   docker compose up
   ```

3. Verify that both containers are running:
   ```bash
   docker ps
   ```

4. Send requests to:
   ```
   http://localhost:8080
   ```

---

## Running with Minikube (Kubernetes)

### Step 1: Start Minikube
```bash
minikube start
```

### Step 2: Deploy Service-B
```bash
cd service-b/yamls
kubectl apply -f .
```

### Step 3: Deploy Service-A
```bash
cd ../../service-a/yamls
kubectl apply -f .
```

---

## Accessing the API

1. Find the API service name:
   ```
   coordinator-api-svc
   ```

2. Expose the service using Minikube:
   ```bash
   minikube service coordinator-api-svc
   ```

---
# OpenShift Deployment Guide (oc CLI)

This guide shows how to:
- Create a user in OpenShift
- Log in with `oc`
- Apply Kubernetes YAMLs (like `kubectl`)
- Expose a Service using an OpenShift Route
- Retrieve the external URL

---

## 1. Login to OpenShift

after login copy the login token from openshift web-site

like this:
 "oc login --token=shajdksjdissfjishddasgdhasnmnsaacniasncascnakjsb --server=https://api.rm1.thpm.p1.openshiftapps.com:4444"
---

## 3. Apply YAML Files (kubectl-style)

Apply all YAML files in the directory:

```bash
oc apply -f .
```

Check resources:

```bash
oc get pods
oc get svc
```

---

## 4. Find the coordinates API Service

List services:

```bash
oc get svc
```

Verify the service exists:

```bash
oc get svc coordinates-api-svc
```

---

## 5. Create an OpenShift Route (Edge TLS)

Expose the service externally:

```bash
oc create route edge coordinates-api   --service=coordinates-api-svc
```

## 6. List Routes

```bash
oc get routes
```

---

## 7. Get the External URL

Get only the host:

```bash
oc get route coordinates-api -o jsonpath='{.spec.host}'
```

Copy this URL and use it to access the API.

---

## Summary

- Logged in with `oc`
- Deployed resources from YAML
- Verified Service
- Exposed Service using Route
- Retrieved external HTTPS URL

---

## Status

✅ The software is working and all components communicate successfully.
