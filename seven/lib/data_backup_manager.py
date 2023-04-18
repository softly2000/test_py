import os

class DataBackupManager:
    
    def __init__(self):
        self.backup_dir = 'backups'
        self.backup_num = 1
        
    def backup_data(self, data):
        # Создаем директорию для хранения резервных копий, если ее еще нет
        if not os.path.exists(self.backup_dir):
            os.mkdir(self.backup_dir)

        # Формируем имя файла для резервной копии данных
        backup_filename = os.path.join(self.backup_dir, f'backup_{self.backup_num}.txt')

        # Создаем и записываем данные в файл резервной копии
        with open(backup_filename, 'w') as backup_file:
            backup_file.write(data)

        # Увеличиваем номер резервной копии для следующего раза
        self.backup_num += 1

        # Выводим сообщение об успешном выполнении операции
        print(f'Data backup successful. Backup file: {backup_filename}')

    def restore_data(self):
        # Получаем список доступных резервных копий
        backup_files = os.listdir(self.backup_dir)

        if not backup_files:
            print('No backups found.')
            return

        # Выводим список доступных резервных копий
        print('Available backup files:')
        for i, backup_file in enumerate(backup_files):
            print(f'{i + 1}. {backup_file}')

        # Запрашиваем у пользователя идентификатор нужной резервной копии
        backup_id = int(input('Enter backup file number to restore: '))

        # Проверяем, что идентификатор находится в диапазоне номеров резервных копий
        if backup_id < 1 or backup_id > len(backup_files):
            print('Invalid backup file number.')
            return

        # Получаем имя выбранного файла резервной копии
        backup_filename = os.path.join(self.backup_dir, backup_files[backup_id - 1])

        # Загружаем данные из файла резервной копии
        with open(backup_filename, 'r') as backup_file:
            data = backup_file.read()

        # Восстанавливаем данные из резервной копии
        # ...

        # Выводим сообщение об успешном выполнении операции
        print(f'Data restore successful from backup file: {backup_filename}')
