import kaggle

# Download latest version
kaggle.api.authenticate()

path = kaggle.api.dataset_download_files("ijayuv/onlineretail",path='./data',unzip=True)

print("Path to dataset files:", path)