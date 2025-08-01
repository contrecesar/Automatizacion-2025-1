import os
import json

# Base route where the checkpoints are
base_dir = "models/results"
output_log_dir = "models/logs"
output_file = os.path.join(output_log_dir, "trainer_state.json")

combined_log_history = []

# Traverse the checkpoint-* directories and extract the trainer_state.json
for folder in sorted(os.listdir(base_dir)):
    checkpoint_path = os.path.join(base_dir, folder)
    trainer_state_path = os.path.join(checkpoint_path, "trainer_state.json")

    if os.path.isdir(checkpoint_path) and folder.startswith("checkpoint-") and os.path.exists(trainer_state_path):
        with open(trainer_state_path, "r") as f:
            try:
                trainer_data = json.load(f)
                log_entries = trainer_data.get("log_history", [])
                combined_log_history.extend(log_entries)
                print(f" Agregado log de {folder} con {len(log_entries)} entradas")
            except json.JSONDecodeError:
                print(f" Error al leer {trainer_state_path}, archivo corrupto")

# Save the combined file to models/logs/
os.makedirs(output_log_dir, exist_ok=True)
with open(output_file, "w") as f:
    json.dump({"log_history": combined_log_history}, f, indent=2)

print(f"\n Log combinado guardado exitosamente en: {output_file}")
print(f" Total de entradas en log_history: {len(combined_log_history)}")
