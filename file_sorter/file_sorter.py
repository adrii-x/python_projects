import os
import shutil


keeper = []
stringer = ''
def create_folder(path: str, extension: str) -> str:

    # folder Creator
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)
    print(folder_name)
    print(folder_path)
    print(os.path.exists(folder_path))

    if not os.path.exists(folder_path) and len(keeper) == 0:
        print(folder_path + '********')
        keeper.append(folder_name)

        os.makedirs(folder_path)

        return folder_path

    elif len(keeper)>0 :
        print(keeper)

        print(''.join(keeper))
        if folder_name in ''.join(keeper):
            print(folder_name in ''.join(keeper))

            for file in keeper:
                print(file)

                if file == folder_name:
                    print('h1')
                    return folder_path

            for file in keeper:
                print(file)

                if file != folder_name and os.path.exists(folder_path):
                    print(file)
                    keeper.append(folder_name)
                    print(keeper)
                    return folder_path

                elif file != folder_name:
                    print(file)
                    keeper.append(folder_name)
                    print(keeper)
                    os.makedirs(folder_path)
                    return folder_path






        else:
            print(keeper)
            print(folder_path + '/////////')
            keeper.append(folder_name)
            print(keeper)
            os.makedirs(folder_path)
            return folder_path

    else:
        keeper.append(folder_name)

        return folder_path


def sort_files(source_path: str):

    for root_dir, sub_dir, filenames in os.walk(source_path):
        print(root_dir+"---------")
        print(filenames)

        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            print(file_path)
            extension: str = os.path.splitext(filename)[1]
            print(extension)

            if extension:
                print(extension + 'eeeeeeeeeee')
                target_folder: str = create_folder(source_path, extension)
                print(target_folder,'ttttttttttt')
                target_path: str = os.path.join(target_folder, filename)

                shutil.move(file_path, target_path)



def delete_empty_folders(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir, current_dir)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)

def main():

    user_input: str = input('enter file path to sort')

    if os.path.exists(path=user_input):
        sort_files(user_input)
        delete_empty_folders(user_input)
        print('Files sorted successfully')

    else:
        print('Invalid path')

if __name__ == '__main__':
    main()


    


