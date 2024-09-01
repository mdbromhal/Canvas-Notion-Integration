# Canvas-Notion-Integration
Integrating Canvas with Notion with Python. References are in Wiki.

# Step 1: Canvas token
1. Go to Canvas
2. Click your profile picture & go to Settings
3. Scroll down to "Approved Integrations" and generate a new token
4. Add token to python script


# Step 2: Notion token
1. Go to your Notion
2. In the sidebar, click Settings and Members
3. Choose Connections in sidebar
4. At bottom of screen, click Develop or Manage Integrations
5. Create a new integration
6. Add token to python script


# Step 3: Database ID
1. In Notion, make or choose the database you want your assignments to go into
2. Open the database in fullscreen and click Share
3. Copy the link and paste it somewhere you can see it better
4. Notion's databases have the following link format: https://www.notion.so/{workspace_name}/{database_id}?v={view_id}
5. Copy the database_id and put it into the python script


# Step 3.5: Link your Notion Integration to this Database
1. In the fullscreen of your Notion database, click the 3 dots (...) at the top right of the screen
2. Scroll down to "Connections" and click "Connect to"
3. Choose your integration that you made in Step 2 (you may have to search for it)


# Step 4: University's Canvas URL
1. Go to your Canvas website (Dashboard works)
2. Copy what's after "https://", which should be something like "university.instructure.com"
3. Paste this into the url in the python script


# Step 5: Course ID's
When you click on each course, the URL in your browser will change and end in a 5-digit number. For example, in "https://university.instructure.com/courses/xxxxx", you want "xxxxx".
1. Go to each course and note the Course Name and the Course ID (the 5-digit number in the URL)
2. Enter the data into the class_dict dictionary in the python file
