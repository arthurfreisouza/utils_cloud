# Azure Storage Pipeline

This project provides scripts and Azure pipelines to create an Azure Storage Account and assign roles to it.

## Project Structure

```
azure-storage-pipeline
├── scripts
│   ├── create_storage_account.sh  # Script to create an Azure storage account
│   └── assign_role.sh             # Script to assign a role to the storage account
├── pipelines
│   ├── create-storage-account.yml   # Pipeline to create a storage account
│   └── assign-role.yml              # Pipeline to assign a role to the storage account
└── README.md                        # Project documentation
```

## Prerequisites

- Azure CLI installed and configured
- Access to an Azure subscription
- Appropriate permissions to create resources and assign roles

## Scripts

### create_storage_account.sh

This script creates an Azure Storage Account. It requires the following parameters:
- `storage_account_name`: The name of the storage account to create.
- `resource_group`: The resource group in which to create the storage account.
- `location`: The Azure region where the storage account will be created.

### assign_role.sh

This script assigns a specified role to an Azure Storage Account. It requires the following parameters:
- `storage_account_name`: The name of the storage account.
- `resource_group`: The resource group of the storage account.
- `role`: The role to assign to the storage account.

## Pipelines

### create-storage-account.yml

This pipeline defines the steps to execute the `create_storage_account.sh` script to create a storage account.

### assign-role.yml

This pipeline defines the steps to execute the `assign_role.sh` script to assign a role to the storage account.

## Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Run the desired pipeline using Azure DevOps or Azure CLI.

For example, to run the create storage account pipeline, use the following command:

```bash
az pipelines run --name create-storage-account
```

To assign a role, run:

```bash
az pipelines run --name assign-role
```

## License

This project is licensed under the MIT License.