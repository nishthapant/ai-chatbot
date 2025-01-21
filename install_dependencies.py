import subprocess

print("Installing dependencies...")

try:    
    subprocess.check_call(['pip3', 'install', '-r', 'requirements.txt'])
    print("Installation complete.")

except subprocess.CalledProcessError as e:
    print(f"Error installing packages: {e}")