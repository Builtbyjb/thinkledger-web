if __name__ == "__main__":
  import platform
  import subprocess

  os_name = platform.system()
  print("Operating System: ", os_name)
  # Install npm packages
  result = subprocess.run(["npm", "install"], capture_output=True, text=True)
  print(result)
  # Install uv
  result = subprocess.run(["pip", "install", "uv"], capture_output=True, text=True)
  print(result)
  # Install python packages
  result = subprocess.run(["uv", "sync"], capture_output=True, text=True)
  print(result)
  if os_name == "Darwin" or os_name == "Linux":
    # install tide
    result = subprocess.run(
      ["curl", "-L" "-o", "tide", "https://github.com/Builtbyjb/tide/releases/tag/v0.1.0"],
      capture_output=True,
      text=True
      )
    print(result)
    # TODO: Add tide to path
  elif os_name == "Windows":
    result = subprocess.run(["pip", "install", "uv"], capture_output=True, text=True)
    print(result)
  else: print("Unable to determine operating system.")

  print("Setting up complete.")