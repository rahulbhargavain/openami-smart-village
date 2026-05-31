#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Configuration variables
PROJECT_ID="sattal-a27f2"
SERVICE_ACCOUNT="github-ci-deployer@${PROJECT_ID}.iam.gserviceaccount.com"
POOL_NAME="github-actions-pool" # Using the clean pool name from our last step
PROVIDER_NAME="github-provider"

echo "==== 1. Fetching GCP Project Number ===="
# Automatically grab the numeric project ID required for the workflow file
PROJECT_NUMBER="993111087069" #$(gcloud projects describe "$PROJECT_ID" --format="value(projectNumber)")
echo "Found Project Number: $PROJECT_NUMBER"

# Define the full Workload Identity Provider resource string
PROVIDER_STRING="projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${POOL_NAME}/providers/${PROVIDER_NAME}"

echo "==== 2. Creating GitHub Workflow Directory ===="
mkdir -p .github/workflows

echo "==== 3. Generating deploy.yml ===="
cat << EOF > .github/workflows/deploy.yml
name: Deploy to Firebase

on:
  push:
    branches:
      - main

# Required permissions for requesting the OIDC JWT token from Google
permissions:
  contents: read
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v4

      - name: Authenticate to Google Cloud
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: '${PROVIDER_STRING}'
          service_account: '${SERVICE_ACCOUNT}'

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install Dependencies
        run: npm ci

      - name: Build Project
        run: npm run build --if-present

      - name: Deploy to Firebase
        uses: w9jds/firebase-action@v2
        with:
          args: deploy --project=${PROJECT_ID}
EOF

echo "File built successfully at .github/workflows/deploy.yml"

echo "==== 4. Pushing Changes to GitHub ===="
# Stage the brand new file structure
git add .github/workflows/deploy.yml

# Commit the configuration change
git commit -m "ci: implement workload identity federation token deployment for Firebase"

# Push the modifications directly up to main
git push origin main

echo "==== Done! Your CI/CD Pipeline is live ===="
