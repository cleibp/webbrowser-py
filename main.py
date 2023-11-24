def main():
  import webbrowser
  import time
  import random
  websites = random.choice(["youtube.com", "spotify.com", "uber.com", "google.com"])
  formatted = "https://{}".format(websites)
  while 1:
    webbrowser.open(formatted)
    time.sleep(3)


if __name__ == "__main__":
  main()
