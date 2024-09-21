
try:
    # Kodi rezikshem
    n1 = int(input("Jep numrin e pare"))
    n2 = int(input("Jep numrin e dyte"))
    pjestimi = n1/n2
except ZeroDivisionError:
    # Error handling
    print("Error.", ZeroDivisionError)