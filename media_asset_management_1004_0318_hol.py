# 代码生成时间: 2025-10-04 03:18:24
import numpy as np
import os
import json
from datetime import datetime

"""
Media Asset Management System

This system allows for the creation, deletion, and retrieval of media assets.
It leverages NumPy for efficient data storage and manipulation.
"""

class MediaAssetManager:
    """
    Manages media assets using NumPy arrays.
    """
    def __init__(self, storage_path='./assets.json'):
        """Initialize the Media Asset Manager."""
        self.storage_path = storage_path
        self.assets = self.load_assets()

    def load_assets(self):
        """Load assets from storage."""
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_assets(self):
        """Save assets to storage."""
        with open(self.storage_path, 'w') as file:
            json.dump(self.assets, file, indent=4)

    def add_asset(self, asset_id, asset_name, asset_type, metadata):
        """Add a new asset to the system."""
        if asset_id in [asset['id'] for asset in self.assets]:
            raise ValueError("Asset ID already exists.")
        self.assets.append({
            'id': asset_id,
            'name': asset_name,
            'type': asset_type,
            'metadata': metadata,
            'created_at': datetime.now().isoformat()
        })
        self.save_assets()

    def delete_asset(self, asset_id):
        """Delete an asset from the system."""
        initial_length = len(self.assets)
        self.assets = [asset for asset in self.assets if asset['id'] != asset_id]
        if len(self.assets) == initial_length:
            raise ValueError("Asset not found.")
        self.save_assets()

    def get_asset(self, asset_id):
        """Retrieve an asset by ID."""
        for asset in self.assets:
            if asset['id'] == asset_id:
                return asset
        raise ValueError("Asset not found.")

    def list_assets(self):
        """List all assets in the system."""
        return self.assets

# Example usage
if __name__ == '__main__':
    manager = MediaAssetManager()
    
    try:
        # Adding assets
        manager.add_asset('001', 'Movie A', 'Movie', {'director': 'John Doe', 'year': 2023})
        manager.add_asset('002', 'Song B', 'Music', {'artist': 'Jane Doe', 'length': '3:30'})

        # Listing assets
        print(manager.list_assets())

        # Getting an asset
        print(manager.get_asset('001'))

        # Deleting an asset
        manager.delete_asset('002')
        print(manager.list_assets())
    except ValueError as e:
        print(f'Error: {e}')
