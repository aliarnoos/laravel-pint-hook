#!/usr/bin/env python3
import subprocess
import sys
import os

def main():
    # Check if we're in a Laravel project
    if not os.path.exists('vendor/bin/pint'):
        print("Laravel Pint not found. Run 'composer install' first.")
        return 1
    
    # Run Laravel Pint
    result = subprocess.run(['./vendor/bin/pint'], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Laravel Pint found issues:")
        print(result.stdout)
        print(result.stderr)
        return 1
    
    print("Laravel Pint: All files are properly formatted!")
    return 0

if __name__ == '__main__':
    sys.exit(main())