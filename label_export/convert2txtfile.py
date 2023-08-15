import csv
import json

# Read the CSV file and create a text file for writing
csv_file_path = r"C:\Users\Admin\Downloads\label_export\Input_file\project-3-at-2023-08-15-21-31-4b09dbe1.csv"  # Replace with the actual path
txt_file_path = r"C:\Users\Admin\Downloads\label_export\Output_file\output_data.txt"

with open(csv_file_path, "r", newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Process the data and write it to the text file
with open(txt_file_path, "w", encoding="utf-8") as txt_file:
    for entry in data:
        txt_file.write(f"annotation_id: {entry['annotation_id']}\n")
        txt_file.write(f"annotator: {entry['annotator']}\n")
        txt_file.write(f"created_at: {entry['created_at']}\n")
        txt_file.write(f"id: {entry['id']}\n")
        txt_file.write(f"img: {entry['img']}\n")

        # Parse the JSON-like structure in kp-1
        keypoints = json.loads(entry['kp-1'])
        txt_file.write("kp-1:\n")
        for idx, keypoint in enumerate(keypoints):
            txt_file.write(f"  Keypoint {idx + 1}:\n")
            for key, value in keypoint.items():
                if key == "keypointlabels":
                    value_str = ", ".join(value)
                else:
                    value_str = value
                txt_file.write(f"    {key}: {value_str}\n")

        txt_file.write(f"lead_time: {entry['lead_time']}\n")
        txt_file.write(f"updated_at: {entry['updated_at']}\n")
        txt_file.write("\n")

print("Data has been written to the text file.")
