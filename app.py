
import os
import sys
import platform
import socket
from datetime import datetime
import time

def display_system_info():
    """Display system information"""
    print("=" * 60)
    print("🖥️  SYSTEM INFORMATION")
    print("=" * 60)
    
    # Statement 1: Current timestamp
    print(f"📅 Current Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Statement 2: Python version
    print(f"🐍 Python Version: {sys.version}")

def display_github_info():
    """Display GitHub Actions specific information if available"""
    github_vars = {
        'GITHUB_REPOSITORY': os.environ.get('GITHUB_REPOSITORY', 'Not in GitHub Actions'),
        'GITHUB_REF': os.environ.get('GITHUB_REF', 'Not in GitHub Actions'),
        'GITHUB_SHA': os.environ.get('GITHUB_SHA', 'Not in GitHub Actions'),
        'GITHUB_ACTOR': os.environ.get('GITHUB_ACTOR', 'Not in GitHub Actions'),
        'GITHUB_WORKFLOW': os.environ.get('GITHUB_WORKFLOW', 'Not in GitHub Actions')
    }
    
    print("\n🔧 GITHUB ACTIONS INFORMATION")
    print("-" * 40)
    for key, value in github_vars.items():
        print(f"{key}: {value}")
    print("-" * 40)

def main():
    """Main function"""
    print("🚀 Starting Python Application...")
    print(f"⏰ Start Time: {datetime.now().strftime('%H:%M:%S')}")
    
    # Display system information
    display_system_info()
    
    # Display GitHub Actions info if available
    display_github_info()
    
    # Simulate some work
    print("\n💼 Performing some work...")
    time.sleep(2)
    
    print(f"⏰ End Time: {datetime.now().strftime('%H:%M:%S')}")
    print("🎉 Python application completed successfully!")

if __name__ == '__main__':
    main()
