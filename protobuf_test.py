
import person_pb2

# 创建一个Person对象
person = person_pb2.Person()
person.name = "Alice"
person.age = 25
person.hobbies.extend(["reading", "swimming"])

# 将Person对象序列化为二进制格式
serialized_person = person.SerializeToString()

# 将二进制数据写入文件
with open("person.bin", "wb") as f:
    f.write(serialized_person)



# 从文件中读取二进制数据
with open("person.bin", "rb") as f:
    serialized_person = f.read()

# 将二进制数据解析为Person对象
person = person_pb2.Person()
person.ParseFromString(serialized_person)

# 打印Person对象的属性
print("Name:", person.name)
print("Age:", person.age)
print("Hobbies:", person.hobbies)
