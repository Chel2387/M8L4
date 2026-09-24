import psutil
# Количество процессоров
cpy_count = psutil.cpu_count(logical=False)
# Загрузка процессоров
total_usage = psutil.cpu_percent(interval=1)
# Загрузка оперативной памяти
ram=psutil.virtual_memory()

disk_usage = psutil.disk_usage('/')

# Список запущенных процессов
for process in psutil.process_iter(['pid', 'name', 'username']):
    try:
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}, User: {process.info['username']}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
#
net = psutil.net_io_counters()
#print(f"CPU Count: {cpy_count}")
#print(f"Total CPU Usage: {total_usage}%")
#print(f"Total RAM: {ram.total / (1024 ** 3):.2f} GB")
#print(f"Available RAM: {ram.available / (1024 ** 3):.2f} GB")
#print(f"Used RAM: {ram.used / (1024 ** 3):.2f} GB")
#print(f"RAM Usage: {ram.percent}%")
#print(f"Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
#print(f"Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
#print(f"Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB")
#print(f"Disk Usage: {disk_usage.percent}%")
#print(f'Отправлено данных: {net.bytes_sent // (1024 ** 2)} МБ')
#print(f'Получено данных: {net.bytes_recv // (1024 ** 2)} МБ')

#time.time() - psutil.boot_time()