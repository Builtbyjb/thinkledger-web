if __name__ == "__main__":
  import platform
  import subprocess
  import sys

  os_name = platform.system()
  print("Operating System: ", os_name)
  try:
    # Install npm packages
    subprocess.run(["npm", "install"])
    if os_name == "Darwin" or os_name == "Linux":
      # Install uv
      subprocess.run(
        "curl -LsSf https://astral.sh/uv/install.sh | sh",
        shell=True,
        executable="/bin/bash"
        )
      subprocess.run("uv sync", shell=True, executable="/bin/bash", capture_output=True)
      # install tide
      subprocess.run(
        "curl -L -o tide https://github.com/Builtbyjb/tide/releases/tag/v0.1.0",
        shell=True,
        executable="/bin/bash"
        )
      # TODO: Add tide to path
      # run a install script
    elif os_name == "Windows":
      subprocess.run(["pip", "install", "uv"], capture_output=True, text=True)
    else: print("Unable to determine operating system.")
  except FileNotFoundError as f_err:
    print(f_err)
    sys.exit(1)
  except Exception as e:
    print(e)
    sys.exit(1)

  print("Setting up complete.")