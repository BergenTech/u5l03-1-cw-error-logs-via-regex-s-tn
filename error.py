import csv, json, re

logs_path = 'logs.json'
csv_path = 'error_logs.csv'

try:
    logs = json.load(open(logs_path, 'r'))

    errors = [log for log in logs if re.match(r'(?im).*ERROR.*', log['level'])]

    with open(csv_path, 'w') as f:
        fieldnames = ['timestamp', 'level', 'message']
        writer = csv.DictWriter(f, fieldnames=errors[0].keys())
        writer.writeheader()

        for error in errors:
            error['level'] = "ERROR"
            writer.writerow(error)
except FileNotFoundError as e:
    print(f'File not found: {e.filename}')
except Exception as e:
    print(f'Error: {e}')