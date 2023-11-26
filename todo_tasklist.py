tasks_dict = {
	"tasks": [
	{
		"id":"1",
		"name":"Task 1",
		"status":"To Do",
		"createdDateTime":"05-11-2023T02:59:00",
		"modifiedDateTime":"05-11-2023T03:20:00",
		"category":"Personal",
		"detail":"This is task 1"
	},
	{
		"id":"2",
		"name":"Task 2",
		"status":"To Do",
		"createdDateTime":"05-11-2023T02:59:00",
		"modifiedDateTime":"05-11-2023T03:20:00",
		"category":"Personal",
		"detail":"This is task 2"
	}
	,
	{
		"id":"3",
		"name":"Task 3",
		"status":"To Do",
		"createdDateTime":"05-11-2023T02:59:00",
		"modifiedDateTime":"05-11-2023T03:20:00",
		"category":"Personal",
		"detail":"This is task 3"
	}
	]
}


tasks_list = []


print("=====Tasks List=====")

for i,_ in enumerate(tasks_dict["tasks"]):
    print(tasks_dict["tasks"][i]["id"]+". "+tasks_dict["tasks"][i]["name"])

print("4. Add New")


select_task = input ("Select Task: ")

tasks = tasks_dict["tasks"]

selected_tasks = [task for task in tasks_dict["tasks"] if task['id'] == select_task]
# tasks_list.append(task)
print("===Task===")
print(selected_tasks[0])
print("Task Detail: "+str(selected_tasks[0]["detail"])+"\nStatus: "+str(selected_tasks[0]["status"]))
print("1. Edit 2. Remove 3. Mark Completed 0. Back")
select_option = input("Select: ")

if select_option == "3":
	selected_tasks[0].update({"status":"Done"})
elif select_option == "1":
	current_detail = selected_tasks[0]["detail"]
	print("Current Task Detail: " + current_detail)
	new_detail = input("Enter the new task detail (or press Enter to keep the current detail): ")
	if new_detail:
		selected_tasks[0]["detail"] = new_detail
		print("Task detail updated.")
	else:
		print("Task detail remains unchanged.")
elif select_option == '2':
	#print(selected_tasks[0]["id"])
	#del tasks[int(selected_tasks[0]["id"])]
	#tasks.pop(int(selected_tasks[0]["id"]))
	tasks = [task for task in tasks_dict["tasks"] if task['id'] != select_task]
	tasks_dict["tasks"] = tasks
	print(tasks_dict)

#print(selected_tasks[0])
#print(tasks_dict["tasks"])