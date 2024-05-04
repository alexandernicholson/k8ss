import argparse
from kubernetes import client, config
from kubernetes.watch import Watch
import simpleaudio as sa
import datetime
import pytz
from rich.console import Console

# Load kube config
config.load_kube_config()

# Create Kubernetes API client
v1 = client.CoreV1Api()

# Create a Rich console
console = Console()

def watch_events(namespace=None, wait=False):
    # Get the current time in UTC timezone
    utc_timezone = pytz.timezone('UTC')
    current_time = datetime.datetime.now(utc_timezone)

    # Watch events indefinitely, starting from now
    w = Watch()
    api_function = v1.list_namespaced_event if namespace else v1.list_event_for_all_namespaces
    api_args = [namespace] if namespace else []
    for event in w.stream(api_function, *api_args, _request_timeout=60):
        event_time = event['object'].metadata.creation_timestamp
        # Check if the event occurred after the current time
        if event_time and event_time > current_time:
            # Check if the event type is Pod creation
            if event['type'] == 'ADDED' and event['object'].involved_object.kind == 'Pod':
                # Play a WAV file
                wave_obj = sa.WaveObject.from_wave_file("pod_creation.wav")
                play_obj = wave_obj.play()
                if wait:
                    play_obj.wait_done()
                print("-", end="", flush=True)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Listen to Kubernetes events and play a sound for pod creations.")
parser.add_argument("--namespace", "-n", default="", help="Namespace to listen to. If not provided, listen to all namespaces.")
parser.add_argument("--wait", "-w", default=False, help="Wait for each sound to finish completely. If not provided, sounds can overlap.")
args = parser.parse_args()

# Watch events based on the command-line argument
watch_events(args.namespace, args.wait)

