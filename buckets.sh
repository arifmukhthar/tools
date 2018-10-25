#!/bin/bash
for bucket in $(aws s3api list-buckets --query 'Buckets[*].{Name:Name}' --output text)
do 
    region=$(aws s3api get-bucket-location --bucket $bucket --query 'LocationConstraint' --output text | awk '{sub(/None/,"us-east-1")}; 1')
    parts=$(aws s3api list-multipart-uploads --bucket $bucket --region $region --query 'Uploads[*].{Key:Key,Initiated:Initiated}' --output text)
    echo "$bucket : $parts"
done
