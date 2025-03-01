import os
import subprocess
import random

def list_devices(device_type):
    devices = []
    device_classes = {
        'camera': 'Image',
        'microphone': 'AudioEndpoint',
        'audio': 'Media',
        'network': 'Net'
    }
    target_class = device_classes.get(device_type.lower(), "*")

    try:
        result = subprocess.run(
            ["powershell", "-Command", f"Get-PnpDevice | Where-Object {{ $_.Class -eq '{target_class}' }} | Select-Object Name,Status,InstanceId"],
            capture_output=True, text=True, shell=True
        )
        for line in result.stdout.splitlines()[3:]:
            parts = line.strip().split()
            if len(parts) >= 3:
                status = parts[1]
                device_id = parts[-1]
                device_name = " ".join(parts[:-2])
                if device_type == "disabled" and "DISABLED" in status.upper():
                    devices.append((device_id, device_name, status))
                elif device_type != "disabled":
                    devices.append((device_id, device_name, status))
    except Exception as e:
        print(f"Erro ao listar dispositivos ({device_type}): {e}")
    return devices

def disable_device(device_id):
    try:
        subprocess.run(
            ["powershell", "-Command", f"Disable-PnpDevice -InstanceId '{device_id}' -Confirm:$false"],
            capture_output=True, text=True, shell=True
        )
        return True
    except Exception as e:
        print(f"Erro ao desativar dispositivo ({device_id}): {e}")
        return False

def enable_device(device_id):
    try:
        subprocess.run(
            ["powershell", "-Command", f"Enable-PnpDevice -InstanceId '{device_id}' -Confirm:$false"],
            capture_output=True, text=True, shell=True
        )
        return True
    except Exception as e:
        print(f"Erro ao ativar dispositivo ({device_id}): {e}")
        return False

def list_files_in_use():
    files = []
    try:
        result = subprocess.run(["powershell", "-Command", "Get-Process | Select-Object Name, Id"], capture_output=True, text=True, shell=True)
        for line in result.stdout.splitlines()[3:]:
            if any(keyword in line.lower() for keyword in ["camera", "microphone", "audio", "record"]):
                parts = line.strip().split()
                if len(parts) >= 2:
                    files.append((parts[0], parts[-1]))
    except Exception as e:
        print(f"Erro ao listar processos: {e}")
    return files

def corrupt_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "wb") as file:
            file.write(os.urandom(random.randint(512, 4096)))
        return True
    return False