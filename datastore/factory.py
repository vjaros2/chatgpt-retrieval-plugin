from datastore.datastore import DataStore


async def get_datastore() -> DataStore:

    from datastore.providers.pinecone_datastore import PineconeDataStore

    return PineconeDataStore()
