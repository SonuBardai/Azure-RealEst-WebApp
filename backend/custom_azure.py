from storages.backends.azure_storage import AzureStorage
from decouple import config

class AzureMediaStorage(AzureStorage):
    account_name = config('STORAGE_ACC_NAME')
    account_key = config('STORAGE_ACC_KEY')
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = config('STORAGE_ACC_NAME')
    account_key = config('STORAGE_ACC_KEY')
    azure_container = 'static'
    expiration_secs = None