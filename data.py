'''
{
	"name": "tom",
	"age": 0,
	"height": 100
}
'''
import json


with open("data.json") as f:
	database = json.load(f)

while True:
	print("选择你要进行的操作: ")
	print("\t1.录入数据")
	print("\t2.查找")
	print("\t3.显示所有学生信息")
	choice = input("输入编号:")
	
	if choice == "1":
		# 进行数据录入
		name = input("name: ")
		age = int(input("age: "))
		height = int(input("height: "))

		database.append({"name": name, "age": age, "height": height})
	elif choice == "2":
		name = input("输入你要查找的姓名: ")
		
		for item in database:
			if name == item.get("name"):
				print("找到啦! name: %s, age: %s" % (name, item.get("age")))
	elif choice == "3":
		print("+------+------+-----+")
		print("| name |  age |height|")
		print("+------+------+-----+")
		for item in database:
			print("|%6s|%6s|%6s|" % (item.get("name"), item.get("age"), item.get("height")))
		print("+------+------+-----+")
	
	with open("data.json", 'w', encoding="utf-8") as f:
		json.dump(database, f, indent=4)
	input("按任意键继续.......")