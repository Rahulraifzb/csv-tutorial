# from csv import reader

# with open("members.csv","r") as f:
#     csv_reader = reader(f)
#     next(csv_reader)
#     for row in csv_reader:
#         print(row)


# from csv import DictReader

# with open("members.csv","r") as f:
#     csv_reader = DictReader(f)
#     for key in csv_reader:
#         print(key["product"])

# from csv import writer

# with open("new_members.csv","w",newline="") as r:
#     csv_writer = writer(r)
    # csv_writer.writerow(["name","country"])
    # csv_writer.writerow(["rahul","india"])
    # csv_writer.writerow(["mohit","USA"])

    # csv_writer.writerows([["name","country"],["rahul","india"],["mohit","USA"]])

# from csv import DictWriter

# with open("new_members.csv","w",newline="") as w:
#     csv_writer = DictWriter(w,fieldnames=["firstname","lastname","age"])
    # csv_writer.writeheader()
    # csv_writer.writerow({
    #     "firstname":"Rahul",
    #     "lastname":"rai",
    #     "age":20
    # })
    # csv_writer.writerow({
    #     "firstname":"king",
    #     "lastname":"khan",
    #     "age":19
    # })
    # csv_writer.writerows([
    #     {"firstname":"Rahul","lastname":"rai","age":20},
    #     {"firstname":"king","lastname":"khan","age":19},
    #     {"firstname":"raj","lastname":"rani","age":19},
    # ])

# from csv import reader,writer


# with open("members.csv","r") as r:
#     with open("new_members.csv","w") as w:
#         csv_reader = reader(r)
#         csv_writer = writer(w)
#         csv_writer.writerow(next(csv_reader))
#         for value in csv_reader:
#             csv_writer.writerow(value)


# from csv import DictWriter,DictReader

# with open("members.csv","r") as r:
#     with open("new_members.csv","w",newline="") as w:
#         csv_reader = DictReader(r)
#         csv_writer = DictWriter(w,fieldnames=["product","salesman","quantity","total","created"])
#         csv_writer.writeheader()
#         for value in csv_reader:
#             csv_writer.writerow(value)
