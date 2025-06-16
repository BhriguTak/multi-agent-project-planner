"""
YAML Loading Debug Script - Focuses only on YAML functionality
"""

import os
import sys

def print_section(title):
    print("\n" + "="*50)
    print(f" {title}")
    print("="*50)

def test_yaml_import():
    print_section("YAML IMPORT TEST")
    
    try:
        import yaml
        print("✓ yaml module imported successfully")
        print(f"✓ PyYAML version: {yaml.__version__}")
        return True
    except ImportError as e:
        print(f"✗ Cannot import yaml module: {e}")
        print("\nTo fix this, run:")
        print("  pip install PyYAML")
        return False

def check_yaml_files():
    print_section("YAML FILES CHECK")
    
    files_to_check = [
        "config/agents.yaml",
        "config/tasks.yaml"
    ]
    
    existing_files = []
    
    for file_path in files_to_check:
        print(f"\nChecking: {file_path}")
        
        if os.path.exists(file_path):
            try:
                size = os.path.getsize(file_path)
                abs_path = os.path.abspath(file_path)
                print(f"✓ File exists")
                print(f"  Size: {size} bytes")
                print(f"  Full path: {abs_path}")
                existing_files.append(file_path)
                
                # Read and show first few lines
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')[:5]  # First 5 lines
                    print(f"  Content preview (first 5 lines):")
                    for i, line in enumerate(lines, 1):
                        print(f"    {i}: {line}")
                        
            except Exception as e:
                print(f"✗ Error reading file: {e}")
        else:
            print(f"✗ File does not exist")
            print(f"  Looking for: {os.path.abspath(file_path)}")
    
    return existing_files

def test_yaml_parsing(files):
    print_section("YAML PARSING TEST")
    
    if not files:
        print("No YAML files found to test")
        return
    
    try:
        import yaml
    except ImportError:
        print("Cannot import yaml - skipping parsing test")
        return
    
    for file_path in files:
        print(f"\nTesting YAML parsing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                
                if data is None:
                    print("✗ YAML file is empty or contains only comments")
                elif isinstance(data, dict):
                    print(f"✓ YAML parsed successfully as dictionary")
                    print(f"✓ Found {len(data)} top-level keys: {list(data.keys())}")
                    
                    # Show structure
                    for key, value in data.items():
                        if isinstance(value, dict):
                            sub_keys = list(value.keys())[:3]  # First 3 sub-keys
                            print(f"  {key}: dict with keys {sub_keys}{'...' if len(value) > 3 else ''}")
                        else:
                            print(f"  {key}: {type(value).__name__}")
                else:
                    print(f"✓ YAML parsed as {type(data).__name__}")
                    print(f"✓ Content: {str(data)[:100]}{'...' if len(str(data)) > 100 else ''}")
                    
        except yaml.YAMLError as e:
            print(f"✗ YAML parsing error: {e}")
            
            # Try to give specific advice
            if "found character" in str(e):
                print("  Tip: Check for special characters or encoding issues")
            elif "mapping" in str(e):
                print("  Tip: Check indentation and structure")
            elif "found undefined alias" in str(e):
                print("  Tip: Check for duplicate keys or reference errors")
                
        except Exception as e:
            print(f"✗ General error: {e}")

def test_code_simulation():
    print_section("CODE SIMULATION TEST")
    
    print("Testing the exact code from your script...")
    
    # Simulate the exact code structure
    files = {
        'agents': 'config/agents.yaml',
        'tasks': 'config/tasks.yaml'
    }
    
    # Test each file loading approach
    configs = {}
    
    for config_type, file_path in files.items():
        print(f"\nTesting load of {config_type}: {file_path}")
        
        try:
            # Check if file exists first
            if not os.path.exists(file_path):
                print(f"✗ FileNotFoundError would occur - file doesn't exist")
                continue
                
            # Try to open and load
            with open(file_path, 'r') as file:
                import yaml
                configs[config_type] = yaml.safe_load(file)
                print(f"✓ Successfully loaded {config_type} configuration")
                print(f"  Type: {type(configs[config_type])}")
                if isinstance(configs[config_type], dict):
                    print(f"  Keys: {list(configs[config_type].keys())}")
                    
        except FileNotFoundError:
            print(f"✗ FileNotFoundError: File not found")
        except yaml.YAMLError as e:
            print(f"✗ YAML Error: {e}")
        except Exception as e:
            print(f"✗ Other Error: {e}")
    
    # Test assignment
    if configs:
        print(f"\nTesting variable assignment...")
        try:
            agents_config = configs.get('agents', {})
            tasks_config = configs.get('tasks', {})
            print(f"✓ agents_config type: {type(agents_config)}")
            print(f"✓ tasks_config type: {type(tasks_config)}")
        except Exception as e:
            print(f"✗ Assignment error: {e}")

if __name__ == "__main__":
    print("YAML LOADING FUNCTIONALITY TEST")
    print("Checking only YAML-related functionality")
    
    # Test 1: Can we import yaml?
    yaml_available = test_yaml_import()
    
    # Test 2: Do the YAML files exist?
    existing_files = check_yaml_files()
    
    # Test 3: Can we parse the YAML files?
    if yaml_available:
        test_yaml_parsing(existing_files)
    
    # Test 4: Simulate your exact code
    if yaml_available:
        test_code_simulation()
    
    print_section("YAML TEST COMPLETE")
    print("Review the results above to identify YAML-specific issues.")