#!/usr/bin/env bash
# Usage: ./deploy.sh <bucket-name>
set -e
if [ -z "$1" ]; then
  echo "Usage: $0 <bucket-name>"
  exit 1
fi
BUCKET="$1"
echo "Syncing website files to s3://$BUCKET ..."
aws s3 sync . s3://$BUCKET --exclude '*.tf' --exclude 'deploy.sh' --exclude '*.md' --acl public-read
echo "Files uploaded."
echo "You can open the website at: http://$BUCKET.s3-website-$(aws configure get region).amazonaws.com"
