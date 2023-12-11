import os
import shutil
import subprocess
import traceback


class Process:

    @staticmethod
    def run(programm: str, param: str =  "", shell: bool = True) -> bool:
        """
        Запуск сторонней программы

        :param programm: путь до программы
        :param param: параметры запуска
        :param shell: использовать ядро
        :return: True | False
        """

        try:
            if param:
                command = f'{programm} "{param}"'
            else:
                command = f'{programm}'
            print(command)
            subprocess.Popen(command, shell=shell)
            return True
        except Exception:
            traceback.print_exc()
            return False

    @staticmethod
    def kill(proc_name: str) -> bool:
        """
        Закрытие всех процессов по шаблону proc_name

        :param proc_name: название процесса
        :return: True | False
        """

        try:
            os.system(f'taskkill /f /im {proc_name}')
            return True
        except Exception:
            traceback.print_exc()
            return False


class Folder:

    @staticmethod
    def open(folder_name: str) -> bool:
        """
        Открытие папки

        :param folder_name: путь до папки
        :return: True | False
        """

        try:
            folder = os.path.abspath(folder_name)
            if not os.path.exists(folder):
                Folder.create(folder)
            Process.run('explorer.exe', os.path.abspath(folder_name))
            return True
        except Exception:
            traceback.print_exc()
            return False

    @staticmethod
    def create(output_folder: str) -> bool:
        """
        Создание выходной папки по полному пути

        :param output_folder: путь до папки
        :return: True | False
        """

        try:
            if os.path.exists(output_folder):
                return True

            os.makedirs(os.path.abspath(output_folder))
            return True
        except Exception:
            traceback.print_exc()
            return False

    @staticmethod
    def size(folder: str) -> dict:
        """
        Получение размера папки

        :param folder: путь к папке
        :return: словарь {размер папки, кол-во подпапок}
        """

        try:
            if not os.path.isdir(folder):
                raise NotADirectoryError("Указанный путь не является директорией")

            total_size = 0
            total_count = 0
            for dirpath, dirnames, filenames in os.walk(folder):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)
                        total_count += 1

            return {'size': total_size, 'count': total_count}

        except Exception:
            traceback.print_exc()
            return {}

    @staticmethod
    def delete_empty_folders(dir_path: str) -> bool:
        """
        Функция удаляет пустые папки

        :param dir_path: путь корневой папки
        :return: True | False
        """

        try:
            for dir_ in os.listdir(dir_path):
                subdir = os.path.join(dir_path, dir_)
                if os.path.isdir(subdir):
                    Folder.delete_empty_folders(subdir)
                    if not os.listdir(subdir):
                        os.rmdir(subdir)
            return True

        except Exception:
            traceback.print_exc()
            return False

    @staticmethod
    def clear(dir_path: str) -> bool:
        """
        Очистка папки

        :param dir_path: путь к папке
        :return: True | False
        """

        # TODO Можно уйти в бесконечность
        count = 0
        while len(os.listdir(dir_path)):
            for elem in os.listdir(dir_path):
                fullPath = os.path.join(dir_path, elem)

                if os.path.isfile(fullPath):
                    try:
                        os.remove(fullPath)
                    except Exception:
                        traceback.print_exc()
                        raise Exception
                else:
                    try:
                        shutil.rmtree(fullPath, ignore_errors=True)
                    except Exception:
                        traceback.print_exc()
                        raise Exception
            count += 1
            if count > 10:
                break
        return True

    @staticmethod
    def delete(dir_path: str) -> bool:
        """

        :param dir_path:
        :return:
        """

        try:
            shutil.rmtree(dir_path, ignore_errors=True)
            return True
        except Exception:
            traceback.print_exc()
            return False

    @staticmethod
    def is_empty(dir_path: str) -> bool:
        """

        :param dir_path:
        :return:
        """

        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            if not os.listdir(dir_path):
                return True
            else:
                for root, dirs, files in os.walk(dir_path):
                    if files:
                        return False
                return True
        else:
            return False


class File:

    @staticmethod
    def open(file_name: str) -> bool:
        """
        Запуск файла

        :param file_name: путь до папки
        :return: True | False
        """

        try:
            file = os.path.abspath(file_name)
            if not os.path.exists(file):
                raise FileNotFoundError
            print(file)
            Process.run(file, "")
            return True
        except Exception:
            traceback.print_exc()
            return False

    @staticmethod
    def delete(file_path: str) -> bool:
        """
        Удаление файла

        :param file_path: путь к файлу
        :return: True | False
        """

        try:
            os.remove(file_path)
            return True
        except Exception:
            traceback.print_exc()
            return False

    @staticmethod
    def move(old_path: str, new_path: str) -> bool:
        """
        Перемещение файла

        :param old_path: старый путь к файлу
        :param new_path: новый путь к файлу
        :return: True | False
        """

        try:
            if old_path == new_path:
                return True

            shutil.copy(old_path, new_path)
            os.remove(old_path)

            return True

        except Exception:
            traceback.print_exc()
            return False

    @staticmethod
    def copy(src_path: str, dst_path: str) -> bool:
        """
        Копирование файла

        :param src_path: путь к файлу, который нужно скопировать
        :param dst_path: путь к файлу, куда нужно скопировать
        :return: True | False
        """

        try:
            shutil.copy(src_path, dst_path)
            return True
        except Exception:
            traceback.print_exc()
            return False

    @staticmethod
    def to_bytes(file_path: str, count: int = 64) -> str:
        """
        Чтение 'count' символов файла

        :param file_path: путь к файлу
        :param count: кол-во символов для чтения
        :return: файл в байтовом представлении
        """

        try:
            with open(file_path, "r", errors='replace') as file_path:
                data = file_path.read(count)

            return ''.join(x for x in data if x.isprintable())

        except Exception:
            traceback.print_exc()
            return ""

    @staticmethod
    def to_hex(file_path: str, count: int = 64) -> str:
        """
        Получение файла в hex коде

        :param file_path: путь к файлу
        :param count: кол-во символов для чтения
        :return: файл в hex представлении
        """

        try:
            with open(file_path, "r", errors='replace') as file:
                data = file.read(count)

            return ' '.join("{:02x}".format(ord(char)) for char in data)

        except Exception:
            traceback.print_exc()
            return ""
