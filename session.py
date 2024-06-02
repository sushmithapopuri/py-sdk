
# def create_session(provider):
#     if 

# def azure_session():
# Acquire a credential object
    # credential = DefaultAzureCredential()

    # blob_service_client = BlobServiceClient(account_url="https://<my_account_name>.blob.core.windows.net",credential=credential)


a = ['a','c','b','d']

bench = ['a','b','c']

c = [ae for ae in bench if ae not in a]
print(bench in a)
print(c == [])
print(all(x in a for x in bench))