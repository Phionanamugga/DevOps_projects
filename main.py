
# MENU __
#!/bin/bash
# Author: Phiona Namugga (GitHub: Phionanamugga)
# Description: Simple DevOps script to deploy a static website on AWS S3

set -e

# ====== CONFIG ======
BUCKET_NAME="phiona-static-website-$RANDOM"
REGION="us-east-1"
INDEX_FILE="index.html"
STYLE_FILE="style.css"
# ====================

echo "🚀 Creating S3 bucket: $BUCKET_NAME in region $REGION..."
aws s3api create-bucket \
    --bucket "$BUCKET_NAME" \
    --region "$REGION" \
    --create-bucket-configuration LocationConstraint="$REGION"

echo "📂 Uploading site files..."
aws s3 cp "$INDEX_FILE" "s3://$BUCKET_NAME/"
aws s3 cp "$STYLE_FILE" "s3://$BUCKET_NAME/"

echo "🔓 Setting public read policy..."
cat > bucket-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::$BUCKET_NAME/*"
    }
  ]
}
EOF

aws s3api put-bucket-policy --bucket "$BUCKET_NAME" --policy file://bucket-policy.json

echo "🌍 Enabling static website hosting..."
aws s3 website "s3://$BUCKET_NAME/" --index-document index.html --error-document index.html

echo "✅ Deployment complete!"
echo "Your website is available at:"
echo "http://$BUCKET_NAME.s3-website-$REGION.amazonaws.com"


