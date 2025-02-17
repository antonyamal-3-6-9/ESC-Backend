import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
JWT = os.getenv("PINATA_JWT")  # Store your Pinata JWT in a .env file

# File path to upload
FILE_PATH = "sw.png"

# Function to upload an image to Pinata
def pin_file_to_ipfs(file_path):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    
    with open(file_path, "rb") as file:
        files = {"file": file}
        headers = {"Authorization": f"Bearer {JWT}"}
        
        response = requests.post(url, files=files, headers=headers)
        
        if response.status_code == 200:
            cid = response.json()["IpfsHash"]
            print(f"✅ Image uploaded successfully! CID: {cid}")
            print(f"🔗 View the image at: https://gateway.pinata.cloud/ipfs/{cid}")
            return cid
        else:
            print(f"❌ Error uploading image: {response.text}")
            return None

# Function to upload metadata to Pinata
def pin_metadata_to_ipfs(image_cid):
    if not image_cid:
        print("❌ Image CID is missing. Metadata upload aborted.")
        return

    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    metadata = {
        "name": "SwapCoin",
        "symbol": "SWAP",
        "description": "SwapCoin is a decentralized token on the Solana blockchain.",
        "image": f"https://gateway.pinata.cloud/ipfs/{image_cid}",
        "properties": {
            "files": [{"uri": f"https://gateway.pinata.cloud/ipfs/{image_cid}", "type": "image/png"}],
            "creators": [{"address": "YOUR_WALLET_ADDRESS", "share": 100}],
        },
    }

    headers = {
        "Authorization": f"Bearer {JWT}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, json=metadata)

    if response.status_code == 200:
        metadata_cid = response.json()["IpfsHash"]
        print(f"✅ Metadata uploaded successfully! CID: {metadata_cid}")
        print(f"🔗 View metadata at: https://gateway.pinata.cloud/ipfs/{metadata_cid}")
    else:
        print(f"❌ Error uploading metadata: {response.text}")

# Run the upload process
def get_uri(meta_data):
    
    image_cid = pin_file_to_ipfs(FILE_PATH)
    pin_metadata_to_ipfs(image_cid)

    return {
        "name": meta_data['name'],
        "symbol": meta_data['symbol'],
        'uri' : f"https://gateway.pinata.cloud/ipfs/{metadata_cid}"
    }
