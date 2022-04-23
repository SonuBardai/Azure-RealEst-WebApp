# RealEst - An Azure-based Real Estate Marketplace
- This is a project created for Microsoft's Future Ready Talent Internship Program. 

- RealEst is a real-estate marketplace project that uses Azure technologies to provide a medium for real estate sellers and buyers to exchange property listings and real estate information quickly and effectively. 

## Azure Services Used: 
- ### Azure Web App: ]
    - This Azure service is used to host the web application to the Internet. 
    - <a href="https://realest.azurewebsites.net/">Link</a>
- ### Azure Postgres Database Server: 
    - This Azure service is used to store the user data and the data related to the properties that are listed on the application dashboard. 
- ### Azure Blob Storage Account: 
    - This Azure service is used to store all the static files associated with the web application, and also to store the property images uploaded while listing the properties. 
- ### Azure Computer Vision: 
    - This Azure service is used to generate metadata tags associated with the property images. 
    - Everytime a seller lists a property, the images associated with the property are sent to the Azure Computer Vision resource in a REST API call. 
    - The API returns a set of tags that describe the images, which are then stored along with the property listing. 
    - These tags assist the buyers in filtering out properties and finding property listings with specific features. 

### Problem Statement: 
- The problem with the current state of the online real estate market is that it is frustrating for property buyers to find the perfect house that they desire, and for property sellers to give a concise and comprehensive description of their house that would make their listing visible to the appropriate customers. 

### Project Description: 
- RealEst attempts to solve this issue by making use of Azure's Computer Vision technology to help real estate sellers automatically create appropriate tags and filters for their listings, and for buyers to find houses with the exact characteristics that they desire. 

## Setup: 
- pip install -r requirements.txt
- Create a .env file and include the following environment variables inside it:  
    - SECRET_KEY
    - (Azure Resources Details: )
        - DB_NAME
        - DB_USER
        - DB_PASSWORD
        - DB_HOST_URL
        - DB_PORT
        - STORAGE_ACC_NAME
        - STORAGE_ACC_DOMAIN
        - STORAGE_ACC_STATIC_URL
        - STORAGE_ACC_MEDIA_URL
- Create a 'credentials.json' file inside generateVision/ folder. Inside this JSON file, store the following details about the Azure Computer Vision Resource: 
    - API_KEY 
    - ENDPOINT

- The Project is now set up and can be hosted onto an Azure Web App. 

## Technology Stack Used: 
- HTML, CSS, JS
- Python Django, Azure Computer Vision
- Azure Postgres Database Server, Azure Blob Storage Account
- Azure Web App for Hosting