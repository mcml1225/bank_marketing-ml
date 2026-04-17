
---

### **Document 5: `docs/05_Deployment_Guide.md`**

```markdown
# Deployment Guide
## Bank Marketing Prediction API

### 1. Deployment Options

#### Option 1: Hugging Face Spaces (Recommended)

Create a `Dockerfile` (already exists) and configure Space:

```yaml
# Space metadata (create in Hugging Face)
title: Bank Marketing Prediction
emoji: 📊
colorFrom: blue
colorTo: green
sdk: docker
app_port: 8000