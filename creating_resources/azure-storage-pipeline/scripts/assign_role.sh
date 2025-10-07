#!/bin/bash

# This script assigns a specified role to an Azure storage account.

# Exit on error
set -e

# Function to display usage
usage() {
    echo "Usage: $0 -a <storage_account_name> -g <resource_group> -r <role>"
    exit 1
}

# Parse command line arguments
while getopts ":a:g:r:" opt; do
    case ${opt} in
        a )
            storage_account_name=$OPTARG
            ;;
        g )
            resource_group=$OPTARG
            ;;
        r )
            role=$OPTARG
            ;;
        \? )
            usage
            ;;
    esac
done

# Check if all parameters are provided
if [ -z "$storage_account_name" ] || [ -z "$resource_group" ] || [ -z "$role" ]; then
    usage
fi

# Assign the role to the storage account
az role assignment create --assignee <assignee> --role "$role" --scope "/subscriptions/<subscription_id>/resourceGroups/$resource_group/providers/Microsoft.Storage/storageAccounts/$storage_account_name"