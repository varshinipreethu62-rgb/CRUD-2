import requests
import json

base_url = 'http://127.0.0.1:5000/api/students'

# 1. Create a student to delete
payload = {'name': 'To Be Deleted', 'email': 'delete_me@example.com'}
res_add = requests.post(base_url, json=payload)
data_add = res_add.json()
print("Add Response:", data_add)

if data_add.get('success'):
    student_id = data_add['data'][0]['id']
    print(f"Added student with ID: {student_id}")

    # 2. Delete the student via API
    res_del = requests.delete(f"{base_url}/{student_id}")
    print("Delete Status:", res_del.status_code)
    print("Delete Response:", res_del.json())
else:
    print("Failed to add student")
