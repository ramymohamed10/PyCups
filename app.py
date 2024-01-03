import cups
conn = cups.Connection()
printers = conn.getPrinters()

print("Listing all Cups Printer...")
# For demonstration: List printers
for printer in printers:
    print(printer, printers[printer]["device-uri"])
