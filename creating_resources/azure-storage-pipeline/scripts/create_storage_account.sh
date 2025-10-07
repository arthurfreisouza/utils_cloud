#!/bin/bash

# This script creates an Azure storage account.

# Exit on error
set -e

# Function to display usage
usage() {
    echo "Usage: $0 -n <storage_account_name> -g <resource_group> -l <location>"
    exit 1
}

# Parse command line arguments
while getopts ":n:g:l:" opt; do
    case ${opt} in
        n )
            storage_account_name=$OPTARG
            ;;
        g )
            resource_group=$OPTARG
            ;;
        l )
            location=$OPTARG
            ;;
        \? )
            usage
            ;;
    esac
done

# Check if all parameters are provided
if [ -z "$storage_account_name" ] || [ -z "$resource_group" ] || [ -z "$location" ]; then
    usage
fi

# Create the storage account
az storage account create --name "$storage_account_name" --resource-group "$resource_group" --location "$location" --sku Standard_LRS