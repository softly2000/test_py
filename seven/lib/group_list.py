class Group:
    def __init__(self, name):
        self.name = name
        self.tests = []

class GroupList:
    def __init__(self):
        self.groups = []
    
    def add_group(self, group_name):
        for group in self.groups:
            if group.name == group_name:
                print(f"Группа {group_name} уже существует")
                return False
        
        new_group = Group(group_name)
        self.groups.append(new_group)
        print(f"Группа {group_name} успешно создана")
        return True
    
    def remove_group(self, group_name):
        for group in self.groups:
            if group.name == group_name:
                self.groups.remove(group)
                print(f"Группа {group_name} успешно удалена")
                return True
        
        print(f"Группа {group_name} не существует")
        return False
    
    def get_group(self, group_name):
        for group in self.groups:
            if group.name == group_name:
                return group
        
        print(f"Группа {group_name} не найдена")
        return None
    
    def get_all_groups(self):
        return self.groups
