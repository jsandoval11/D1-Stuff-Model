from pathlib import Path
import pandas as pd

data_folder = Path("Pitch Data/Test Data")  


TARGET_COLUMNS = [
    "uniqPitchId", "batterHand", "pitcherHand", "date", "pitchResult", 
    "pitchingTeam", "pitcher", "pitcherId", "extension", "HorzApprAngle", "VertApprAngle",
    "ExitVel", "IndVertBrk", "HorzBrk", "type", "RelX", "RelZ", "Vel", "Spin", "SpinDir"
]

current_dir = Path(__file__).resolve().parent
data_folder = current_dir / "Test Data"

# Case-insensitive recursive match for .csv and .CSV
csv_files = list(data_folder.glob("**/*.[cC][sS][vV]"))
print(f"Looking in: {data_folder}")
print(f"Found {len(csv_files)} CSV files.")

df_list = []

for file_path in csv_files:
    try:
        sample = pd.read_csv(file_path, nrows=0)
        existing_cols = [c for c in TARGET_COLUMNS if c in sample.columns]
        
        df = pd.read_csv(file_path, usecols=existing_cols, low_memory=False)
        
        df["source_file"] = file_path.stem
        
        df_list.append(df)
    except Exception as e:
        print(f"Error reading {file_path.name}: {e}")

if df_list:
    combined_df = pd.concat(df_list, axis=0, ignore_index=True)
    print(f"Successfully combined {len(combined_df):,} total pitches.")
    print("Shape:", combined_df.shape)
    
    combined_df.to_csv("combined_test_data.csv", index=False)
else:
    print("No CSV files could be loaded.")


    data_folder = current_dir / "Test Data"


data_folder = Path("Pitch Data/Training Data")  

# Case-insensitive recursive match for .csv and .CSV
csv_files = list(data_folder.glob("**/*.[cC][sS][vV]"))
print(f"Looking in: {data_folder}")
print(f"Found {len(csv_files)} CSV files.")

df_list = []

for file_path in csv_files:
    try:
        sample = pd.read_csv(file_path, nrows=0)
        existing_cols = [c for c in TARGET_COLUMNS if c in sample.columns]
        
        df = pd.read_csv(file_path, usecols=existing_cols, low_memory=False)
        
        df["source_file"] = file_path.stem
        
        df_list.append(df)
    except Exception as e:
        print(f"Error reading {file_path.name}: {e}")

if df_list:
    combined_df = pd.concat(df_list, axis=0, ignore_index=True)
    print(f"Successfully combined {len(combined_df):,} total pitches.")
    print("Shape:", combined_df.shape)
    
    combined_df.to_csv("combined_train_data.csv", index=False)
else:
    print("No CSV files could be loaded.")