import subprocess

########################################## WRITTEN BY STEVEN V. COGNATA ##########################################

def disable_ipv6_windows():
    try:
        subprocess.run(["powershell", "-Command", "Get-NetAdapterBinding -ComponentID 'ms_tcpip6' | Disable-NetAdapterBinding -ComponentID 'ms_tcpip6' -PassThru"], check=True)
        print("IPv6 disabled on Windows")
    except subprocess.CalledProcessError as e:
        print("Failed to disable IPv6 on Windows:", e)

if __name__ == "__main__":
    disable_ipv6_windows()
