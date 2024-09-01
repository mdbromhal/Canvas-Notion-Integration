# Canvas-Notion Integration (without my tokens)
# NOTE TO USER: you must add your own canvas token, notion token, database ID, and class names and course ID's

import requests

# Entering in API tokens & identifiers we will be using 
canvas_token = '' # Canvas API token
notion_token = '' # Notion API token
database_id = '' # Notion Database Identifier
# NOTE: You must have the database prepped in Notion with all the required properties you use below

# Entering url for school's canvas (after https:// and including the .com). For example, 'unvsty.instructure.com'
url = ''

# Defining a dictionary with each class with its respective HTML ID
class_dict = {
    "Class name 1": "course ID 1",
    "Class name 2": "course ID 2"
}

# Defining the headers (the tokens) for Canvas & Notion
canvas_headers = {'Authorization': f'Bearer {canvas_token}'}
notion_headers = {
    'Authorization': f'Bearer {notion_token}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}
    
# For each class, we'll get the assignments from Canvas and enter them into the Notion Database we've specified
for item in class_dict.items():
    class_name = item[0] # Getting the class name from the dictionary
    course_id = item[1] # Getting the course ID from the dictionary
    
    print(f"Entering {class_name} with ID {course_id} now...")

    # Getting the course assignments from the Canvas API
    canvas_response = requests.get(f'https://{url}/api/v1/courses/{course_id}/assignments', headers=canvas_headers)
    assignments = canvas_response.json() # Putting them into json format

    # For each assignment in the course, enter it into the Notion database with the specified properties
    for assignment in assignments: 
        
        data = {
            "parent": {"database_id": database_id},
            "properties": {

                # Name of the assignment
                "Name": {
                    "title": [{
                        "text": {
                            "content": assignment['name']
                        }
                    }]
                },

                # Due Date of the assignment
                "Due Date": {
                    "date": {
                        "start": assignment['due_at']
                    }
                },

                # Class name of the assignment
                "Class":{
                    "select": {
                        "name": class_name
                    }
                }
            }
            # 'children': [
            #     {
            #         'object': 'block',
            #         'type': 'paragraph',
            #         'paragraph': {
            #             'rich_text': [{
            #                 'text': 
            #                     {'content': assignment['description']}
            #             }]
            #         }
            #     }
            # ]
        }

        # Post the assignment database entry as a separate page in the Notion database
        response = requests.post(f'https://api.notion.com/v1/pages', headers=notion_headers, json=data) # databases/{database_id}

        # If everything went well, let us know
        if response.status_code == 200:
            print(f"Added assignment: {assignment['name']}")

        # # If the assignment doesn't have a description, don't add one and add to Notion
        # elif response.json()['message'] == "body failed validation: body.children[0].paragraph.rich_text[0].text.content should be a string, instead was `null`.":
        #     # Data without description
        #     data = {
        #         "parent": {"database_id": database_id},
        #         "properties": {

        #             # Name of the assignment
        #             "Name": {
        #                 "title": [{
        #                     "text": {
        #                         "content": assignment['name']
        #                     }
        #                 }]
        #             },

        #             # Due Date of the assignment
        #             "Due Date": {
        #                 "date": {
        #                     "start": assignment['due_at']
        #                 }
        #             },

        #             # Class name of the assignment
        #             "Class":{
        #                 "select": {
        #                     "name": class_name
        #                 }
        #             }
        #         }
        #     }
        #     # Post the assignment database entry as a separate page in the Notion database
        #     response = requests.post(f'https://api.notion.com/v1/pages', headers=notion_headers, json=data) # databases/{database_id}
        
        # If there was an issue, print issue
        else:
            print(f"Failed to add assignment {assignment['name']}")
            print(response.json())
