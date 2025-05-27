if __name__ == "__main__":
  import platform
  import subprocess

  os_name = platform.system()
  # Check is python3 and node is installed

  # Install npm packages
  result = subprocess.run(["npm", "install"], capture_output=True, text=True)
  print(result)

  # install tide
  if os_name == "Darwin" or os_name == "Linux":
  # Install uv
    result = subprocess.run(["pip3", "install", "uv"], capture_output=True, text=True)
    print(result)
  elif os_name == "Windows":
    result = subprocess.run(["pip", "install", "uv"], capture_output=True, text=True)
    print(result)
  else:
    print(" Unable to determine operating system.")

  print(os_name)
  print("Setting up complete")