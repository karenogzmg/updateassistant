import subprocess
import logging
import os
import sys
import time

# Configure logging
logging.basicConfig(filename='update_assistant.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_for_updates():
    """Check for available Windows updates."""
    logging.info("Checking for updates...")
    try:
        result = subprocess.run(['powershell', '-Command', 
                                 'Get-WindowsUpdate'], 
                                capture_output=True, text=True)
        logging.info(f"Check for updates result: {result.stdout}")
        return result.stdout
    except Exception as e:
        logging.error(f"Error checking for updates: {e}")
        return None

def download_updates():
    """Download available Windows updates."""
    logging.info("Downloading updates...")
    try:
        result = subprocess.run(['powershell', '-Command', 
                                 'Install-WindowsUpdate -AcceptAll -IgnoreReboot'], 
                                capture_output=True, text=True)
        logging.info(f"Download updates result: {result.stdout}")
        return result.stdout
    except Exception as e:
        logging.error(f"Error downloading updates: {e}")
        return None

def install_updates():
    """Install downloaded Windows updates."""
    logging.info("Installing updates...")
    try:
        result = subprocess.run(['powershell', '-Command', 
                                 'Install-WindowsUpdate -AcceptAll'], 
                                capture_output=True, text=True)
        logging.info(f"Install updates result: {result.stdout}")
        return result.stdout
    except Exception as e:
        logging.error(f"Error installing updates: {e}")
        return None

def reboot_system():
    """Reboot the system to complete the installation of updates."""
    logging.info("Rebooting system...")
    try:
        subprocess.run(['shutdown', '/r', '/t', '0'])
    except Exception as e:
        logging.error(f"Error rebooting system: {e}")

def main():
    """Main function to manage the update process."""
    logging.info("Starting Update Assistant...")
    updates = check_for_updates()
    if "No updates" in updates:
        logging.info("No updates available.")
    else:
        download_updates()
        install_updates()
        reboot_system()

if __name__ == '__main__':
    main()