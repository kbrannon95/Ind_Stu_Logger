import json

# JSON
json_data = open("./config/config.json").read()
data = json.loads(json_data)
settings_root = json.loads(json_data)

rabbitmq_settings = settings_root["rabbitmq_settings"]