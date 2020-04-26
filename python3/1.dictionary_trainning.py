target = {}
target = {"Damein": "Whiplash", "Speilberg": "Jaw"}
target2 = dict(eren="hangzhou", adina="shanghai")

element = target.get("eren", "default value when not found")

target["new key"] = "new value"
target["old key"] = "new value"

element = target.pop("name of the key, also remove this value pair")
del target["delete key value pair of this key"]

dict3 = dict(**dict1, **dict2)
dict4 = dict(x=5, z=8, **dict1)

"key" in dict4
"key" not in dict4

class_keys_object = target.keys()
keys_list = list(keys_object)

class_values_object = target.values()
values_list = list(values_object)

target.clear()

del target
