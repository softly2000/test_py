class GroupManager:
    def __init__(self):
        self.groups = {}
    
    def create_group(self, group_name):
        if group_name in self.groups:
            print(f"Группа {group_name} уже существует")
        else:
            self.groups[group_name] = []
            print(f"Группа {group_name} успешно создана")
    
    def remove_group(self, group_name):
        if group_name in self.groups:
            del self.groups[group_name]
            print(f"Группа {group_name} успешно удалена")
        else:
            print(f"Группа {group_name} не существует")
    
    def assign_test_to_group(self, group_name, test_name):
        if group_name in self.groups:
            self.groups[group_name].append(test_name)
            print(f"Тест {test_name} успешно назначен на группу {group_name}")
        else:
            print(f"Группа {group_name} не существует")
