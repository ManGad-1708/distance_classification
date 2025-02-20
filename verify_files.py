import os

# List of essential files
required_files = [
    "distance_classification.py",
    "test_script.py",
    "verify_files.py",
    ".github/workflows/main.yml",
    "MananGadesha-Lab5.ipynb",  # Add the Jupyter Notebook
]

# List of required images
image_folder = "images"
required_images = ["Dr_Shashi_Tharoor.jpg", "Plaksha_Faculty.jpg"]

# Check for missing files
missing_files = [f for f in required_files if not os.path.exists(f)]
missing_images = [img for img in required_images if not os.path.exists(os.path.join(image_folder, img))]

# Print results
if not missing_files and not missing_images:
    print("✅ All files and images are present.")
else:
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
    if missing_images:
        print(f"❌ Missing images: {missing_images}")
    exit(1)  # Exit with error if files are missing
