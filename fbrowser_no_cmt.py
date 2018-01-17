import os    
import remove_comments
import tarb
import other_functions as other_f
H_DIR = os.path.expanduser('~') 
HMDIR = os.path.expanduser(os.path.join('~', '.hmdir'))
remove_comments.remove_cmts('fbrowser.py')
CMD_NOT_FOUND = "Command not recognized."
def run():
    other_f.print_start_info()
    command = None
    while command != 'exit':
        command = other_f.get_input()
        if command.startswith('cd'):
            other_f.command_cd_parse(command, HMDIR, H_DIR)
        elif command.startswith('bank'):
            other_f.command_bank()
        elif command.startswith('ls'):
            other_f.command_ls(command)
        elif command.startswith('mkdir'):
            other_f.command_mkdir_parse(command)
        elif command[0:4] == 'tar ':
            tarb.tarb(command[4:])
        elif command.startswith('info'):
            other_f.command_info(command)
        elif command.startswith('exit'):
            pass
        elif command.startswith('rm'):
            other_f.command_rm_all(command, CMD_NOT_FOUND)
        elif command.startswith('pwd'):
            other_f.command_pwd(command)
        elif command.startswith('help'):
            other_f.command_help_parse(command, __doc__)
        elif command == 'text editor' or command == 'joshpad':
            other_f.command_joshpad()
        elif command[0:3] == 'cp ':
            other_f.command_cp(command)
        elif command[0:3] == 'mv ':
            other_f.command_mv(command)
        elif command[0:6] == 'touch ':
            other_f.command_touch(command[6:])
        elif command[0:4] == 'run ':
            other_f.command_run(command)
        elif command[0:4] == 'cat ':
            other_f.command_cat(command[4:].strip())
        elif command[0:3] == 'dir':
            other_f.command_dir()
        elif command[0:5] == 'clear':
            other_f.command_clear()
        elif command == '':
            pass
        else:
            print(CMD_NOT_FOUND)
    print("Logging out.")
if __name__ == '__main__':
    try:
        run()
    except Exception as error:
        print("Exited by %s"%error)
        raise
