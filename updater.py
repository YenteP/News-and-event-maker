import sys, os, shutil, subprocess, time

def main():
    if len(sys.argv) < 3:
        return

    target_path = sys.argv[1]
    new_exe_path = sys.argv[2]

    time.sleep(2)

    try:
        os.remove(target_path)
        shutil.move(new_exe_path, target_path)
        update_dir = os.path.dirname(new_exe_path)
        shutil.rmtree(update_dir, ignore_errors=True)
        subprocess.Popen([target_path])
    except Exception as e:
        print(f"Update mislukt: {e}")

if __name__ == "__main__":
    main()